import psycopg2
import pandas as pd
from config import DB_CREDENTIALS
# pandas y psycopg2 debe estar instalados

def exportar_tendencias_csv(db_name, user, password, host):
    conn = None
    try:
        conn = psycopg2.connect(f"dbname={db_name} user={user} password={password} host={host}")
        cursor = conn.cursor()

        consulta_tendencias = """
        WITH AgregacionTemporal AS (
            SELECT
              DATE_TRUNC('month', rating_date) AS mes_rating,
              EXTRACT(WEEK FROM rating_date) AS num_semana,
              EXTRACT(DOW FROM rating_date) AS dia_semana_num,
              TO_CHAR(rating_date, 'Day') AS dia_semana_nombre,
              COUNT(rating_date) AS ratings_totales_mensuales,
              AVG(rating) AS rating_promedio_mensual
              FROM ratings
              GROUP BY mes_rating, num_semana, dia_semana_num, dia_semana_nombre
        )
        SELECT
          *, -- Seleccionamos todas las columnas de la CTE
          -- Calculamos el Total Acumulado (Running Total)
          SUM(ratings_totales_mensuales) OVER (
              -- Ordenamos por mes para sumar progresivamente
              ORDER BY mes_rating
              -- La ventana va desde el inicio (UNBOUNDED PRECEDING) hasta la fila actual (CURRENT ROW)
              ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
          ) AS ratings_acumulados_historicos
        FROM AgregacionTemporal
        ORDER BY mes_rating, num_semana;
        """

        cursor.execute(consulta_tendencias)
        column_names = [desc[0] for desc in cursor.description] 
        data = cursor.fetchall()
        
        df = pd.DataFrame(data, columns=column_names)
        # Reemplazamos valores nulos (NaN) por 0, específicamente en las columnas que causan problemas
        df['rating_promedio_mensual'] = df['rating_promedio_mensual'].fillna(0)
        df['ratings_totales_mensuales'] = df['ratings_totales_mensuales'].fillna(0)
        df['ratings_acumulados_historicos'] = df['ratings_acumulados_historicos'].fillna(0)
        
        # 2. Forzar el tipo a float (número de punto flotante)
        df['rating_promedio_mensual'] = df['rating_promedio_mensual'].astype(float)
        df.to_csv(
            'tendencias_series_tiempo.csv',
            index=False,
            sep=',', 
            decimal='.'
        )
        print("Exportación de 'tendencias_series_tiempo.csv' completada con éxito.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error al exportar datos: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    try:
        exportar_tendencias_csv(
            db_name=DB_CREDENTIALS["db_name"], 
            user=DB_CREDENTIALS["user"], 
            password=DB_CREDENTIALS["password"], 
            host=DB_CREDENTIALS["host"]
        )
    except ImportError:
        print("ERROR: Debes tener el archivo 'config.py' en la misma carpeta.")
    except Exception as e:
        print(f"Error al ejecutar: {e}")
