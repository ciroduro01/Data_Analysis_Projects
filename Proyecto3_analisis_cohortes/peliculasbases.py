import psycopg2
import pandas as pd
from config import DB_PARAMS
# pandas y psycopg2 tienen que estar instalados: pip install pandas psycopg2-binary

def exportar_retencion_csv(db_name, user, password, host):
    conn = None
    try:
        # 1. Conexión a la base de datos
        conn = psycopg2.connect(f"dbname={db_name} user={user} password={password} host={host}")
        cursor = conn.cursor()

        # 2. La consulta SQL de Cohorte y Retención
        consulta_retencion = """
            WITH UsuarioCohorte AS (
                SELECT userid, DATE_TRUNC('month', MIN(rating_date)) AS cohorte_mes
                FROM ratings GROUP BY userid
            )
            SELECT
                rc.cohorte_mes,
                r.userid,
                r.rating,  -- OK: Incluido para el Gráfico 3
                DATE_TRUNC('month', r.rating_date) AS mes_actividad,
                (  -- INICIO DEL CÁLCULO
                    (EXTRACT(YEAR FROM DATE_TRUNC('month', r.rating_date)) - EXTRACT(YEAR FROM rc.cohorte_mes)) * 12 + 
                    (EXTRACT(MONTH FROM DATE_TRUNC('month', r.rating_date)) - EXTRACT(MONTH FROM rc.cohorte_mes))
                ) AS desfase_meses -- Mes 0 = Mes de adquisición
            FROM
                ratings r
            JOIN
                UsuarioCohorte rc ON r.userid = rc.userid
            -- WHERE r.userid = 272  -- OK: Filtro de usuario único ELIMINADO
            ORDER BY rc.cohorte_mes, r.userid, desfase_meses;
        """
        
        # 3. Ejecutar la consulta y obtener los datos
        cursor.execute(consulta_retencion)
        column_names = [desc[0] for desc in cursor.description] 
        data = cursor.fetchall()
        
        # 4. Crear un DataFrame de Pandas
        df = pd.DataFrame(data, columns=column_names)
        
        # 5. Exportar a CSV de forma limpia
        df.to_csv('retencion_datos_largos.csv', index=False, encoding='ISO-8859-1')
        
        print("Exportación de 'retencion_datos_largos.csv' completada con éxito. ¡Listo para Power BI!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error al exportar datos: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    # Usamos los parámetros importados directamente
    exportar_retencion_csv(
        DB_PARAMS['database'],
        DB_PARAMS['user'],
        DB_PARAMS['password'],
        DB_PARAMS['host']
    )