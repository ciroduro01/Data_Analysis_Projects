import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos limpios
df_segmentacion = pd.read_csv('segmentacion_usuarios.csv')

# Seleccionar las columnas que usaremos para el clustering
df_clustering = df_segmentacion[['frecuencia_ratings', 'rating_promedio', 'recencia_dias']]

# Transformación Logarítmica (Para reducir el sesgo)
# Aplicamos np.log1p (log(1+x)) para manejar el valor mínimo de 0 sin error.
df_clustering['log_frecuencia'] = np.log1p(df_clustering['frecuencia_ratings'])
df_clustering['log_recencia'] = np.log1p(df_clustering['recencia_dias'])
# El rating_promedio se deja sin transformar (ya está bien distribuido)

# Estandarización (Scaling)
# Creamos el objeto StandardScaler
scaler = StandardScaler()

# Seleccionamos las columnas transformadas y el promedio
datos_a_escalar = df_clustering[['log_frecuencia', 'rating_promedio', 'log_recencia']]

# Aplicamos la estandarización
df_escalado = scaler.fit_transform(datos_a_escalar)

# Convertimos el array de nuevo a DataFrame para el clustering
df_escalado = pd.DataFrame(df_escalado, columns=datos_a_escalar.columns)

print("Datos transformados y escalados listos para el clustering.")
print("\n--- Vista previa de los datos escalados (Media ~0, Std ~1) ---")
print(df_escalado.head())

# Lista para almacenar la inercia (Suma de Cuadrados Intra-Cluster)
inercia = []

# Rango de K a probar (Generalmente de 1 a 10)
rango_k = range(1, 11)

# Ejecutar K-Means para cada valor de K
for k in rango_k:
    # Inicializamos K-Means (usamos n_init='auto' para versiones recientes de sklearn)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    
    # Entrenamos el modelo con los datos escalados
    kmeans.fit(df_escalado)
    
    # Almacenamos la inercia (suma de los cuadrados de las distancias)
    inercia.append(kmeans.inertia_)

# Graficar los resultados (Método del Codo)
plt.figure(figsize=(10, 6))
plt.plot(rango_k, inercia, marker='o', linestyle='--', color='blue')
plt.title('Método del Codo para Encontrar K Óptimo')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inercia (Suma de Cuadrados Intra-Cluster)')
plt.xticks(rango_k)
plt.grid(True)
plt.show()

print("Gráfico del Método del Codo generado.")
# Aplicar K-Means con K=4 (Nuestro valor óptimo)
K_OPTIMO = 4
kmeans_final = KMeans(n_clusters=K_OPTIMO, random_state=42, n_init='auto')
kmeans_final.fit(df_escalado)

# Asignar las etiquetas de cluster al DataFrame original (df_segmentacion): Esto es crucial, ya que necesitamos los valores originales para el análisis final.
df_segmentacion['Cluster'] = kmeans_final.labels_

# Analizar los Centros de Cluster (La 'firma' de cada segmento): Hacemos el análisis sobre los datos ESCALADOS (para ver cómo se separan)
centros_escalados = pd.DataFrame(kmeans_final.cluster_centers_, columns=df_escalado.columns)

# Invertir la transformación logarítmica y el escalado: Para interpretar los centros, los convertiremos de nuevo a sus valores originales (ej. días, conteo)

# Primero, invertimos el escalado (usamos el mismo objeto scaler que entrenamos)
centros_originales_escalados = scaler.inverse_transform(centros_escalados)
centros_originales_df = pd.DataFrame(centros_originales_escalados, columns=df_escalado.columns)

# Segundo, invertimos la transformación logarítmica (np.expm1 es el inverso de np.log1p)
centros_originales_df['frecuencia_ratings'] = np.expm1(centros_originales_df['log_frecuencia'])
centros_originales_df['recencia_dias'] = np.expm1(centros_originales_df['log_recencia'])

# Exportar el DataFrame segmentado para Power BI
df_segmentacion.to_csv('segmentacion_final_para_bi.csv', index=False)

print("K-Means aplicado con K=4.")
print("\n--- Centros de Cluster (Valores originales) ---")
# Mostramos la tabla de centros para entender los segmentos
print(centros_originales_df[['frecuencia_ratings', 'rating_promedio', 'recencia_dias']])