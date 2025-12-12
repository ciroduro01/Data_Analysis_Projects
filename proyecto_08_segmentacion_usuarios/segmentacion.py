import psycopg2
import pandas as pd
from config import DB_CREDENTIALS
# pandas y psycopg2 deben estar instalados

def exportar_segmentacion_csv():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_CREDENTIALS["db_name"],
            user=DB_CREDENTIALS["user"],
            password=DB_CREDENTIALS["password"],
            host=DB_CREDENTIALS["host"]
        )
        cursor = conn.cursor()

        consulta_segmentacion = """
            WITH FechaMaxima AS (
                SELECT MAX(rating_date) AS fecha_max FROM ratings
            )
            SELECT
                r.userid,
                COUNT(r.rating) AS frecuencia_ratings,
                AVG(r.rating) AS rating_promedio,
                EXTRACT(DAY FROM (fm.fecha_max - MAX(r.rating_date))) AS recencia_dias
            FROM
                ratings r
            CROSS JOIN 
                FechaMaxima fm 
            GROUP BY
                r.userid, fm.fecha_max
            ORDER BY
                recencia_dias DESC;
        """
        
        cursor.execute(consulta_segmentacion)
        column_names = [desc[0] for desc in cursor.description] 
        data = cursor.fetchall()
        
        df = pd.DataFrame(data, columns=column_names)
        
        # Eliminar filas con valores nulos (NaN): Esto es vital para el clustering, ya que K-Means no acepta nulos.
        df.dropna(inplace=True) 
        
        # Guardamos el archivo ya limpio para el EDA y el Clustering
        df.to_csv('segmentacion_usuarios.csv', index=False)
        
        print("Exportación y limpieza de 'segmentacion_usuarios.csv' completada.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error al exportar datos: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# El usuario debe insertar sus credenciales
if __name__ == "__main__":
    exportar_segmentacion_csv()