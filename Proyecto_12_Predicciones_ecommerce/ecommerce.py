import pandas as pd
import numpy as np
import psycopg2
from psycopg2 import Error
from io import StringIO # Necesario para la inserción masiva
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import config
# Definición de nombres de columnas limpios para la lectura
column_names = [
    'InvoiceNo', 'StockCode', 'Description', 'Quantity', 
    'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'
]

# Cargar el dataset, ignorando el encabezado del archivo (header=None), y asignando los nombres de columna limpios
try:
    # Usamos low_memory=False y saltamos el encabezado
    df = pd.read_csv(
        'online_retail.csv', 
        encoding='latin1', 
        low_memory=False,
        header=None,  # Ignoramos la primera fila
        names=column_names, # Asigna nuestros nombres de columna limpios
        skiprows=1 # Salta la primera fila sucia
    )
    print(f"Dataset cargado. Registros iniciales: {len(df)}")
except FileNotFoundError:
    print("ERROR: Asegúrate de que el archivo 'online_retail.csv' esté en la carpeta.")
    exit()

print("Lectura forzada y nombres de columnas estandarizados.")

## Limpieza Inicial y Conversión de Tipos
# Eliminar filas con valores nulos en columnas críticas
df.dropna(subset=['CustomerID', 'Description'], inplace=True)

# Conversión de tipos
# La columna CustomerID se leerá como float debido a los NaN, la convertimos a int después de dropna
df['CustomerID'] = df['CustomerID'].astype(int)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Fechas: Convertimos y eliminamos nulos
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce') 
df.dropna(subset=['InvoiceDate'], inplace=True) 

## Feature Engineering
df['ValorTotal'] = df['Quantity'] * df['UnitPrice']
df['Fecha'] = df['InvoiceDate'].dt.date
df['Hora'] = df['InvoiceDate'].dt.time
df['DiaSemana'] = df['InvoiceDate'].dt.day_name()

print(f"Limpieza y Feature Engineering completado. Registros finales: {len(df)}")
print("\n--- Vista Previa del DataFrame Limpio ---")
print(df[['InvoiceDate', 'Quantity', 'UnitPrice', 'ValorTotal', 'Country']].head())

print("\n--- FASE 2: Carga Masiva a PostgreSQL (CRUD) ---")

def insertar_datos_en_bd(df, table_name):
    # Usamos las credenciales de config
    try:
        conn = psycopg2.connect(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Usamos StringIO para simular un archivo y usar el comando COPY (más rápido que muchos INSERTs)
        buffer = StringIO()
        
        columnas_db = ['invoiceno', 'stockcode', 'description', 'quantity', 
                       'invoicedate', 'unitprice', 'customerid', 'country', 
                       'valortotal', 'fecha', 'hora', 'diasemana']
        
        # Aseguramos que el DataFrame tenga los nombres de columna correctos para la carga
        df_final = df[['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                       'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country', 
                       'ValorTotal', 'Fecha', 'Hora', 'DiaSemana']].copy()
                       
        df_final.columns = columnas_db 
        
        # Usamos '|' como separador en to_csv
        df_final.to_csv(buffer, header=False, index=False, sep='|')
        buffer.seek(0)
        # Usamos '|' como separador en copy_from
        cursor.copy_from(buffer, 'retail_clean', sep="|", columns=columnas_db)
        
        conn.commit()
        print(f"Éxito: Se insertaron {len(df_final)} registros en la tabla 'retail_clean'.")
        
    except (Exception, Error) as error:
        print("Error al conectar o insertar datos en PostgreSQL:", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión a PostgreSQL cerrada.")

insertar_datos_en_bd(df, config.TABLE_NAME)
# ML - Regresión Logarítmica para Cantidad

print("\n--- FASE 3 (FINAL): Regresión Logarítmica para CANTIDAD ---")

# Definir variables y aplicar Log-Transformación a la CANTIDAD (Y)
# Queremos predecir la CANTIDAD (Quantity)
X = df[['UnitPrice', 'Country', 'DiaSemana']]
y_log_quantity = np.log1p(df['Quantity']) # Aplicamos Log a la Cantidad

# División de Datos
X_train, X_test, y_log_train, y_log_test = train_test_split(
    X, y_log_quantity, test_size=0.2, random_state=42
)

# Preprocesamiento
categorical_features = ['Country', 'DiaSemana']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# Pipeline y Entrenamiento
model_final = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model_final.fit(X_train, y_log_train)
print("Modelo de Regresión Logarítmica para Cantidad entrenado con éxito.")

# Predicción y Reversión
y_log_pred = model_final.predict(X_test)
y_pred_quantity = np.expm1(y_log_pred) # Revertir: Cantidad Predicha
y_test_quantity = np.expm1(y_log_test) # Revertir: Cantidad Real

# Evaluación (Usando valores reales revertidos)
mse = mean_squared_error(y_test_quantity, y_pred_quantity)
r2 = r2_score(y_test_quantity, y_pred_quantity)

print("\n--- Evaluación del Modelo de Regresión (FINAL) ---")
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
# Aquí deberíamos obtener un R^2 bajo (cercano a 0 o negativo), porque predecir la cantidad es muy difícil, pero mucho mejor que los miles que obtuvimos.
print(f"Coeficiente de Determinación (R²): {r2:.4f}")

# Preparación de Resultados para Visualización
df_test_results = X_test.copy()
df_test_results['CantidadReal'] = y_test_quantity
df_test_results['CantidadPredicha'] = y_pred_quantity

# Creamos ValorTotalReal
df_test_results['ValorTotalReal'] = df_test_results['CantidadReal'] * df_test_results['UnitPrice']
df_test_results['ValorTotalPredicho'] = df_test_results['CantidadPredicha'] * df_test_results['UnitPrice']

# Limpiamos resultados extremos para mejor visualización
df_test_results = df_test_results[df_test_results['ValorTotalReal'] < 200]
print(f"Resultados de predicción preparados para visualización.")

# Visualización del Rendimiento (Matplotlib)
# Gráfico de Dispersión: Cantidad Real vs. Cantidad Predicha (Ahora se verá mucho mejor)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='CantidadReal', 
    y='CantidadPredicha', 
    data=df_test_results, 
    alpha=0.6,
    s=10 
)
plt.plot([0, 50], [0, 50], color='red', linestyle='--', linewidth=2, label='Predicción Ideal (y=x)')
plt.title('Gráfico de Dispersión: Cantidad Real vs. Cantidad Predicha')
plt.xlabel('Cantidad Real')
plt.ylabel('Cantidad Predicha')
plt.legend()
plt.show()

# Histograma de Residuos (Errores del Modelo)
df_test_results['Residuos'] = df_test_results['CantidadReal'] - df_test_results['CantidadPredicha']
plt.figure(figsize=(10, 6))
sns.histplot(df_test_results['Residuos'], bins=50, kde=True, color='purple')
plt.title('Distribución de Residuos del Modelo de Cantidad')
plt.xlabel('Residuo (Error de Predicción)')
plt.ylabel('Frecuencia')
plt.show()

print("Visualización de dispersión y residuos generada.")

# FASE 5 (FINAL): Muestreo y Exportación para Power BI
# Tomamos una muestra aleatoria de 9,999 filas para cumplir con el límite de Power BI.
# Esto asegura que el Gráfico de Dispersión se pueda dibujar.
df_muestra_final = df_test_results.sample(
    n=9999, 
    random_state=42, # Asegura que la muestra sea reproducible
    replace=False
) 

# Exportación del CSV muestreado
df_muestra_final.to_csv('ecommerce_predicciones_bi.csv', index=False)
print("Exportación para Power BI lista: 'ecommerce_predicciones_bi.csv' (9,999 filas muestreadas).")