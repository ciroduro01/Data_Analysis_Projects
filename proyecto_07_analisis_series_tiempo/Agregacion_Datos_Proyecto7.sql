-- Agregación de Datos por Tiempo
--El objetivo de esta consulta es transformar la tabla de transacciones (ratings) en una tabla resumida que muestre la actividad a lo largo del tiempo.

-- Agregación Mensual (Tendencia a Largo Plazo)
-- La clave es usar la función DATE_TRUNC('month', ...) para agrupar todas las filas por el primer día del mes, permitiéndonos contar el total de ratings por mes.
SELECT
    -- 1. Truncar la fecha al inicio del mes (nuestra unidad de tiempo)
    DATE_TRUNC('month', rating_date) AS mes_rating,
    
    -- 2. Identificar el número de la semana y el día de la semana para estacionalidad
    EXTRACT(WEEK FROM rating_date) AS num_semana, -- Semana dentro del año
    EXTRACT(DOW FROM rating_date) AS dia_semana_num, -- Día de la semana
    TO_CHAR(rating_date, 'Day') AS dia_semana_nombre, -- Nombre del día para Power BI
    
    -- 3. Contar los ratings en ese intervalo de tiempo
    COUNT(rating_date) AS ratings_totales_mensuales,
    
    -- 4. Calcular el rating promedio en ese mes (métrico secundario)
    AVG(rating) AS rating_promedio_mensual

FROM
    ratings
    
GROUP BY
    mes_rating, num_semana, dia_semana_num, dia_semana_nombre
ORDER BY
    mes_rating;