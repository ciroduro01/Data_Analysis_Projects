import pandas as pd
import numpy as np
import psycopg2 
import io
import csv
from config import DB_PARAMS # Importamos las credenciales
# --- CONFIGURACIÓN DE RUTAS ---
PATH_MOVIES = 'movies.csv'
PATH_RATINGS = 'ratings.csv'
PATH_TAGS = 'tags.csv'

# EXTRACCIÓN Y TRANSFORMACIÓN (E & T)

# 1. CARGA DE DATASETS Y CORRECCIÓN DE NOMBRES DE COLUMNA
try:
    df_movies = pd.read_csv(PATH_MOVIES)
    df_ratings = pd.read_csv(PATH_RATINGS)
    df_tags = pd.read_csv(PATH_TAGS)
    
    print("Archivos cargados exitosamente.")
    
    # NOTA: Normalizar nombres de columna a minúsculas  para coincidir con el esquema de PostgreSQL (que es caso-insensible)
    df_movies.columns = df_movies.columns.str.lower()
    df_ratings.columns = df_ratings.columns.str.lower()
    df_tags.columns = df_tags.columns.str.lower()
    
    print("Nombres de columnas normalizados a minúsculas.")
    
except FileNotFoundError as e:
    print(f"Error: Archivo no encontrado. Asegúrate de que {e.filename} está en la carpeta correcta.")
    exit()

# 2. TRANSFORMACIÓN DE TIMESTAMPS Y RENOMBRAMIENTO
df_ratings['timestamp'] = pd.to_datetime(df_ratings['timestamp'], unit='s')
df_tags['timestamp'] = pd.to_datetime(df_tags['timestamp'], unit='s')

df_ratings.rename(columns={'timestamp': 'rating_date'}, inplace=True)
df_tags.rename(columns={'timestamp': 'tag_date'}, inplace=True)

print("Timestamps convertidos a formato de fecha/hora.")

# 3. EXTRACCIÓN Y NORMALIZACIÓN DE GÉNEROS
# Esto crea las tablas df_generos y df_peliculas_generos

df_genres_temp = df_movies.copy()
df_genres_temp['genres'] = df_genres_temp['genres'].str.split('|')
df_genres_temp = df_genres_temp.explode('genres')

# Crear el DataFrame de Géneros Únicos
df_generos = pd.DataFrame(df_genres_temp['genres'].unique(), columns=['nombre_genero'])
df_generos.reset_index(inplace=True)
df_generos.rename(columns={'index': 'genero_id'}, inplace=True)
df_generos['genero_id'] = df_generos['genero_id'] + 1 

# Crear la tabla de Unión (peliculas_generos)
df_peliculas_generos = df_genres_temp.merge(
    df_generos, 
    left_on='genres', 
    right_on='nombre_genero', 
    how='left'
)
# Usamos 'movieid' en minúsculas
df_peliculas_generos = df_peliculas_generos[['movieid', 'genero_id']].drop_duplicates() 

print("Géneros separados y listos para la Normalización.")

# CONEXIÓN Y CARGA (LOAD)

def conectar_db():
    """Establece y retorna la conexión a PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        print("Conexión a PostgreSQL establecida.")
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a PostgreSQL. ¿Están bien las credenciales? {e}")
        return None

def cargar_df_a_pg(conn, df, table):
    """Carga un DataFrame de Pandas a una tabla de PostgreSQL usando copy_from."""
    if df.empty:
        print(f"Advertencia: DataFrame para la tabla '{table}' está vacío.")
        return

    buffer = io.StringIO()
    # NOTA: Usamos quoting=csv.QUOTE_NONE para evitar el problema de las comillas en el título
    df.to_csv(buffer, header=False, index=False, quoting=csv.QUOTE_NONE, escapechar='\\')
    buffer.seek(0)
    
    cursor = conn.cursor()
    try:
        # Nota: El comando COPY usará el formato CSV sin comillas de texto
        cursor.copy_from(buffer, table, sep=",", columns=df.columns)
        conn.commit()
        print(f" Datos cargados en la tabla '{table}': {len(df)} filas.")
    except (Exception, psycopg2.Error) as error:
        # El error anterior puede ser un problema de integridad, no necesariamente de formato
        print(f"Error en la carga de la tabla '{table}'. El error anterior fue probablemente: {error}")
        conn.rollback()
    finally:
        cursor.close()
# --- EJECUCIÓN DEL BLOQUE DE CARGA ---

conn = conectar_db()
if conn is None:
    exit()

print("\n--- Iniciando Carga de Datos (LOAD) ---")

# A. Cargar Generos (Padre)
cargar_df_a_pg(conn, df_generos[['genero_id', 'nombre_genero']], 'generos')

# B. Cargar Peliculas (Padre) 
df_peliculas_limpio = df_movies[['movieid', 'title']].copy() # Usa 'movieid' en minúsculas
cargar_df_a_pg(conn, df_peliculas_limpio, 'peliculas')


# C. Cargar Relación Peliculas-Generos (Hijo)
cargar_df_a_pg(conn, df_peliculas_generos[['movieid', 'genero_id']], 'peliculas_generos')

# D. Cargar Ratings (Hijo)
cargar_df_a_pg(conn, df_ratings[['userid', 'movieid', 'rating', 'rating_date']], 'ratings')

# E. Cargar Tags (Hijo)
cargar_df_a_pg(conn, df_tags[['userid', 'movieid', 'tag', 'tag_date']], 'tags')


# Cerrar la conexión
conn.close()
print("\n Proceso de ETL (LOAD) finalizado y conexión cerrada.")
