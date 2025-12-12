import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import numpy as np

# Adquisición de Datos
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Gráfico 1: Mapa de Calor (Correlación)
# Calcular la matriz de correlación de todas las columnas
matriz_correlacion = df.corr()

# Configurar el gráfico
plt.figure(figsize=(10, 8))

# Crear el mapa de calor
sns.heatmap(
    matriz_correlacion,
    annot=True, # Mostrar los valores de correlación en las celdas
    cmap='coolwarm', # Elegir un esquema de color (rojo/azul para positivo/negativo)
    fmt=".2f", # Mostrar solo dos decimales
    linewidths=0.5, # Añadir líneas entre celdas
    cbar=True
)

plt.title('Mapa de Calor de la Matriz de Correlación')
plt.show()

# Extraer la correlación con la variable objetivo
print("\n--- Correlación con MedHouseVal ---")
print(matriz_correlacion['MedHouseVal'].sort_values(ascending=False))

# Gráfico 2: Dispersión Geográfica
plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    x=df['Longitude'],
    y=df['Latitude'],
    alpha=0.4,
    s=df['Population'] / 10,
    c=df['MedHouseVal'],
    cmap=plt.get_cmap("jet")
)
cbar = plt.colorbar(scatter)
cbar.set_label('Valor Mediano de la Vivienda (x$100k)')
plt.title('Distribución Geográfica del Valor de la Vivienda en California')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()