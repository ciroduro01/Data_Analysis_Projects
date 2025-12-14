-- Ejecutar esta consulta para obtener el ID de un usuario activo
SELECT
    userid,
    DATE_TRUNC('month', MIN(rating_date)) AS mes_adquisicion,
    DATE_TRUNC('month', MAX(rating_date)) AS mes_ultima_actividad
FROM
    ratings
GROUP BY
    userid
HAVING
    DATE_TRUNC('month', MAX(rating_date)) > DATE_TRUNC('month', MIN(rating_date))
ORDER BY
    mes_ultima_actividad DESC
LIMIT 1;