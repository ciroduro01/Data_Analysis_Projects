import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar los datos limpios
df_segmentacion = pd.read_csv('segmentacion_usuarios.csv')

# 2. Configurar el estilo de los gráficos
sns.set_style("whitegrid")

# 3. Preparar el lienzo para los 3 gráficos
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 14))
plt.subplots_adjust(hspace=0.7) # Incrementamos el espacio entre gráficos

# --- Gráfico 1: Frecuencia de Ratings ---
sns.histplot(df_segmentacion['frecuencia_ratings'], bins=50, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribución de Frecuencia de Ratings por Usuario')
axes[0].set_xlabel('Número de Ratings')

# --- Gráfico 2: Rating Promedio ---
sns.histplot(df_segmentacion['rating_promedio'], bins=20, kde=True, ax=axes[1], color='lightcoral')
axes[1].set_title('Distribución de Rating Promedio por Usuario')
axes[1].set_xlabel('Rating Promedio (1 a 5)')

# --- Gráfico 3: Recencia en Días ---
sns.histplot(df_segmentacion['recencia_dias'], bins=50, kde=True, ax=axes[2], color='lightgreen')
axes[2].set_title('Distribución de Recencia (Días desde el Último Rating)')
axes[2].set_xlabel('Días')

# Mostrar todos los gráficos
plt.show()

# 4. Mostrar estadísticas descriptivas (para el análisis)
print("\n--- Estadísticas Descriptivas ---")
print(df_segmentacion[['frecuencia_ratings', 'rating_promedio', 'recencia_dias']].describe())