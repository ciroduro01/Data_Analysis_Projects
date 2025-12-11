--Cálculo de la Retención Mensual
--Esta es la consulta compleja que une la cohorte con cada actividad posterior.
--¿Cuántos meses han pasado desde la cohorte_mes hasta el rating_date?
--Aquí utilizaremos una consulta más avanzada con una CTE (Common Table Expression) y la función de PostgreSQL AGE() para medir el tiempo transcurrido.
--
WITH UsuarioCohorte AS (
    -- CTE: Determina el mes de adquisición (cohorte) para cada usuario
    SELECT
        userid,
        -- Obtenemos el primer día del mes de la fecha mínima de rating
        DATE_TRUNC('month', MIN(rating_date)) AS cohorte_mes
    FROM
        ratings
    GROUP BY
        userid
)
SELECT
    -- Paso 1: Identificadores
    rc.cohorte_mes,
    r.userid,
    r.rating,
    
    -- Paso 2: Calculamos el mes en que ocurrió este rating
    DATE_TRUNC('month', r.rating_date) AS mes_actividad,

    -- Paso 3: Calculamos la diferencia de meses entre la actividad actual y la cohorte (Meses Transcurridos)
(
        -- (Diferencia de años * 12) + (Diferencia de meses)
        (EXTRACT(YEAR FROM DATE_TRUNC('month', r.rating_date)) - EXTRACT(YEAR FROM rc.cohorte_mes)) * 12 +
        (EXTRACT(MONTH FROM DATE_TRUNC('month', r.rating_date)) - EXTRACT(MONTH FROM rc.cohorte_mes))
    ) AS desfase_meses -- Mes 0 = Mes de adquisición
FROM
    ratings r
JOIN
    UsuarioCohorte rc ON r.userid = rc.userid
ORDER BY
    rc.cohorte_mes,
    r.userid,
    desfase_meses;