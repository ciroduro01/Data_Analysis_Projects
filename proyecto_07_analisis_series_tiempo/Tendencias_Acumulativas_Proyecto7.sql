--Tendencias Acumulativas con Funciones de Ventana
--El objetivo es calcular el Total Acumulado de Ratings Históricos (Running Total). Esta métrica es vital para Power BI, ya que muestra la curva de crecimiento total de la plataforma a lo largo del tiempo.
--La consulta del archivo anterior se usará como una CTE (Common Table Expression) y aplicaremos la función de ventana SUM() sobre ella.
WITH AgregacionTemporal AS (
    SELECT
        DATE_TRUNC('month', rating_date) AS mes_rating,
        EXTRACT(WEEK FROM rating_date) AS num_semana,
        EXTRACT(DOW FROM rating_date) AS dia_semana_num,
        TO_CHAR(rating_date, 'Day') AS dia_semana_nombre,
        COUNT(rating_date) AS ratings_totales_mensuales,
        AVG(rating) AS rating_promedio_mensual
    FROM
        ratings
    GROUP BY
        mes_rating, num_semana, dia_semana_num, dia_semana_nombre
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
FROM
    AgregacionTemporal
ORDER BY
    mes_rating, num_semana;