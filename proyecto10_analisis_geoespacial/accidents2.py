import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap

# FASES 1 & 2: Carga, Limpieza Geoespacial y Corrección de Tipo

print("--- FASE 1 & 2: Carga y Limpieza de Datos ---")
nombre_archivo = 'Accidents.csv' 

# COLUMNAS NECESARIAS
columnas_clave = [
    'Accident_Index', 
    'Latitude', 
    'Longitude', 
    'Accident_Severity',
    'Date', 
    'Time',
    'Light_Conditions'
]

try:
    df = pd.read_csv(nombre_archivo, usecols=columnas_clave, low_memory=False) 
    print(f"Datos de Accidentes del Reino Unido cargados con éxito.")
except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{nombre_archivo}'.")
    exit()

registros_iniciales = len(df)

# INICIO DE LA SECCIÓN DE LIMPIEZA CRÍTICA

# Mapeo de Severidad (Texto a Número)
severity_map = {
    'Fatal': 1, 
    'Serious': 2, 
    'Slight': 3
}
df['Accident_Severity'] = df['Accident_Severity'].map(severity_map)

# CONVERSIÓN FORZADA Y LIMPIEZA DE COORDENADAS
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

# CREAR COLUMNA DE HORA DEL DÍA
# Unir Date y Time y extraer la hora
try:
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors='coerce', dayfirst=True)
    df['Hour_of_Day'] = df['Datetime'].dt.hour
except Exception:
    # Manejo de error si los formatos de fecha son inconsistentes
    df['Hour_of_Day'] = pd.to_numeric(df['Time'].str[:2], errors='coerce') # Intentamos tomar las primeras 2 cifras de la hora

# ELIMINAR FILAS CON VALORES NULOS EN LOS CAMPOS CLAVE
# Limpieza en coordenadas, severidad y la nueva Hour_of_Day
df_limpio = df.dropna(subset=['Latitude', 'Longitude', 'Accident_Severity', 'Hour_of_Day']).copy()

# FILTRAR COORDENADAS FUERA DE LÍMITES
df_limpio = df_limpio[
    (df_limpio['Latitude'] > 49) & (df_limpio['Latitude'] < 61) &
    (df_limpio['Longitude'] > -11) & (df_limpio['Longitude'] < 3)
].copy()

# Renombrar las columnas para Folium y exportación
df_limpio.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

# FIN DE LA SECCIÓN DE LIMPIEZA CRÍTICA FINAL

registros_finales = len(df_limpio)
print(f"Total de registros geoespaciales limpios: {registros_finales} (de {registros_iniciales} iniciales)")
print(f"Limpieza y corrección de tipos completada.")


# FASES 3 y 4: Generación de Mapas
if registros_finales > 0:
    print("\n--- Generando Mapas... ---")
    #Mapa 1
    df_muestra_general = df_limpio.sample(n=100000, random_state=42)
    datos_heatmap_general = df_muestra_general[['lat', 'lon']].values.tolist()
    mapa_acc_general = folium.Map(location=[52.48, -1.89], zoom_start=6, tiles="CartoDB positron")
    HeatMap(datos_heatmap_general).add_to(mapa_acc_general)
    nombre_mapa_general = '01_accidents_heatmap_general.html'
    mapa_acc_general.save(nombre_mapa_general)
    print(f"Mapa General guardado como '{nombre_mapa_general}'.")
    #Mapa 2
    df_graves = df_limpio[df_limpio['Accident_Severity'] <= 2].copy()
    datos_heatmap_graves = df_graves[['lat', 'lon']].values.tolist()
    mapa_graves = folium.Map(location=[52.48, -1.89], zoom_start=6, tiles="CartoDB positron") # Usamos el tile que sí muestra ciudades
    HeatMap(datos_heatmap_graves, radius=8, max_zoom=13).add_to(mapa_graves)
    nombre_mapa_graves = '02_accidents_heatmap_graves.html'
    mapa_graves.save(nombre_mapa_graves)
    print(f"Mapa de Accidentes Graves guardado como '{nombre_mapa_graves}'.")

# EXPORTACIÓN FINAL PARA POWER BI
if registros_finales > 0:
    df_limpio.to_csv('accidentes_uk_limpio_para_bi_final.csv', index=False)
    print("\n DataFrame limpio exportado a 'accidentes_uk_limpio_para_bi_final.csv'.")
    print("PROYECTO FINALIZADO.")
else:
    print("\n No hay datos limpios para exportar.")