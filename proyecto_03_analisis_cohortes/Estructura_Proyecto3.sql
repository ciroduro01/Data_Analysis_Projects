-- Determinando la Cohorte
--Usaremos el concepto de una función de ventana de SQL para encontrar el valor mínimo de rating_date por cada userid.

-- Obtener la Fecha del Primer Rating (Fecha de Adquisición)
--Utilizaremos una Common Table Expression (CTE) llamada Adquisicion y la función de ventana MIN() para encontrar el primer rating de cada usuario.

WITH Adquisicion AS (
    -- Paso 1: Usamos una función de ventana para encontrar la fecha mínima por usuario
    SELECT
        userid,
        rating_date,
        -- MIN() OVER (PARTITION BY userid) calcula la fecha mínima (primera vez) para cada usuario
        MIN(rating_date) OVER (PARTITION BY userid) AS fecha_adquisicion_completa
    FROM
        ratings
)
-- Paso 2: Seleccionamos solo el primer registro único por usuario (la fecha de la cohorte)
SELECT DISTINCT
    userid,
    -- Utilizamos DATE_TRUNC para obtener solo el primer día del mes (la cohorte)
    DATE_TRUNC('month', fecha_adquisicion_completa)::date AS cohorte_mes
FROM
    Adquisicion
ORDER BY
    cohorte_mes, userid;