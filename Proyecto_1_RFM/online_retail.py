import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carga del archivo CSV
try:
    df = pd.read_csv('online_retail.csv', encoding='latin1')
except Exception as e:
    print(f"Error Crítico de Carga: {e}")
    exit()

# Definición del nombre de la columna
columna_cliente_correcta = 'Customer ID' 

# Convertir la columna de fecha
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Eliminar filas con nulos en 'Customer ID' y crear una copia
df_limpio = df.dropna(subset=[columna_cliente_correcta]).copy()

# Conversión de ID a entero (usamos el .astype(str) para manejar los '.0' y luego a int)
df_limpio[columna_cliente_correcta] = (
    df_limpio[columna_cliente_correcta]
    .astype(str)
    .str.replace(r'\.0$', '', regex=True)
    .astype(int)
)

print(f"Limpieza y conversión de la columna '{columna_cliente_correcta}' completada.")
print(f"Filas limpias listas para el siguiente paso: {len(df_limpio)}")
#df_limpio ya está cargado y la columna 'Customer ID' está limpia.
# Las columnas de Quantity, Price y InvoiceDate existen y 'InvoiceDate' es tipo datetime.
# Las columnas se llaman 'Quantity' y 'Price'.

#Crear la columna de Ingresos (Sales)
df_limpio.loc[:, 'Sales'] = df_limpio['Quantity'] * df_limpio['Price']

#Filtrado de Compras Válidas para Análisis RFM
#Las transacciones deben tener Cantidad > 0 y Precio > 0
df_compras = df_limpio[(df_limpio['Quantity'] > 0) & (df_limpio['Price'] > 0)].copy()

print("Columna 'Sales' creada y transacciones negativas/nulas filtradas.")
print(f"Total de Compras Válidas para Análisis RFM: {len(df_compras)}")
#Calcular la Fecha de Referencia
fecha_maxima = df_compras['InvoiceDate'].max()
fecha_referencia = fecha_maxima + pd.Timedelta(days=1)

print(f"Fecha de Referencia para Recencia: {fecha_referencia.date()}")

#Calcular RFM usando groupby y agg
df_rfm = df_compras.groupby('Customer ID').agg(
    #Recencia: Días transcurridos desde la última compra
    Recency=('InvoiceDate', lambda x: (fecha_referencia - x.max()).days),
    
    #Frecuencia: Número de facturas únicas (Usamos 'Invoice' en lugar de 'InvoiceNo')
    Frequency=('Invoice', 'nunique'), 
    
    #Monetario: Suma total de los ingresos (columna 'Sales')
    Monetary=('Sales', 'sum')
).reset_index()

#Vista Previa del resultado
print("\n--- Vista Previa del DataFrame RFM Final ---")
print(df_rfm.head())
print(f"\nTotal de Clientes Únicos: {len(df_rfm)}")
#df_rfm ya está creado.

#ASIGNACIÓN DE PUNTUACIONES (SCORING)

# R: Recencia. Menor Recencia es mejor (Score 5).
df_rfm.loc[:, 'R_Score'] = pd.qcut(df_rfm['Recency'], q=5, labels=[5, 4, 3, 2, 1])

# F y M: Mayor valor es mejor (Score 5).
# Usamos 'duplicates="drop"' para manejar los valores repetidos.
df_rfm.loc[:, 'F_Score'] = pd.qcut(
    df_rfm['Frequency'], 
    q=5, 
    labels=False, # -- Le decimos a Pandas que use el número de grupo como etiqueta
    duplicates='drop'
) + 1 # Sumamos 1 para que los scores vayan de 1 a N (donde N <= 5)

df_rfm.loc[:, 'M_Score'] = pd.qcut(
    df_rfm['Monetary'], 
    q=5, 
    labels=False, # -- Le decimos a Pandas que use el número de grupo como etiqueta
    duplicates='drop'
) + 1 # Sumamos 1 para que los scores vayan de 1 a N (donde N <= 5)


# ASEGURAR TIPOS Y CREAR SCORES COMPUESTOS

# Convertimos a entero para las sumas
df_rfm['R_Score'] = df_rfm['R_Score'].astype(int)
df_rfm['F_Score'] = df_rfm['F_Score'].astype(int)
df_rfm['M_Score'] = df_rfm['M_Score'].astype(int)

# RFM_Segment (Concatenación de R y F, ej: '55')
df_rfm.loc[:, 'RFM_Segment'] = df_rfm['R_Score'].astype(str) + df_rfm['F_Score'].astype(str)

# RFM_Score (Suma simple de los scores)
df_rfm.loc[:, 'RFM_Score'] = df_rfm['R_Score'] + df_rfm['F_Score'] + df_rfm['M_Score']


# DEFINICIÓN DE SEGMENTOS DE NEGOCIO (Función y Aplicación)

def asignar_segmento(df):
    if df['RFM_Segment'] in ['55', '54', '45', '44']:
        return '01 - Campeones/Leales'
    elif df['RFM_Segment'] in ['51', '41']:
        return '02 - Nuevos Clientes/Promesas'
    elif df['RFM_Segment'] in ['34', '33', '43']:
        return '03 - Clientes Potenciales'
    elif df['RFM_Segment'] in ['15', '25', '24', '14', '13']:
        return '04 - En Riesgo/No se Irán'
    else:
        return '05 - Dormidos/Perdidos'

df_rfm.loc[:, 'Segmento'] = df_rfm.apply(asignar_segmento, axis=1)


# RESULTADOS FINALES
print("\n--- Conteo de Clientes por Segmento ---")
print(df_rfm['Segmento'].value_counts())
print("\n Puntuación y Segmentación RFM completadas con éxito.")

#df_rfm está cargado con la columna 'Segmento'

#Preparar los datos para la visualización
# Contar el número de clientes en cada segmento.
# La ordenación por índice (que comienza con 01, 02...) asegura el orden lógico en el gráfico.
segmento_counts = df_rfm['Segmento'].value_counts().sort_index()

#Configuración del gráfico
plt.figure(figsize=(12, 6))
plt.title('Distribución de Clientes por Segmento RFM')
plt.xlabel('Segmento RFM')
plt.ylabel('Número de Clientes')
sns.set_palette("viridis") # Paleta de colores profesional

#Crear el gráfico de barras
barras = sns.barplot(
    x=segmento_counts.index, 
    y=segmento_counts.values,
    order=segmento_counts.index # Usar el orden lógico 01, 02, etc.
)

#Añadir etiquetas de valor (el número exacto de clientes) encima de cada barra
for p in barras.patches:
    barras.annotate(
        format(p.get_height(), ',.0f'), # Formato de número (ej: 3,630)
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', 
        va = 'center', 
        xytext = (0, 9), # Desplazamiento de la etiqueta
        textcoords = 'offset points'
    )

#Ajustar el diseño para una mejor lectura
plt.xticks(rotation=45, ha='right') # Rotar las etiquetas del eje X para que no se superpongan
plt.tight_layout() # Asegura que nada se corte

#Mostrar el gráfico
plt.show()

print("\n Visualización de la distribución de clientes generada.")