-- Consultas Clave para el Proyecto N°2
-- Consulta 1: Películas Populares con Mejor Puntuación
-- Objetivo: Encontrar las 10 películas más populares (con más de 50 ratings) y su calificación promedio. Demuestra el uso de JOIN, GROUP BY, y HAVING.
SELECT 
    p.title,
    COUNT(r.rating) AS num_ratings,
    ROUND(AVG(r.rating), 2) AS rating_promedio
FROM 
    ratings r
JOIN 
    peliculas p ON r.movieid = p.movieid
GROUP BY 
    p.title
HAVING 
    COUNT(r.rating) >= 50
ORDER BY 
    rating_promedio DESC, 
    num_ratings DESC
LIMIT 10;
-- Consulta 2: Distribución de Géneros
--Objetivo: Contar cuántas películas existen en cada género. Demuestra la unión de la tabla de hechos con la tabla de dimensiones.
SELECT
    g.nombre_genero,
    COUNT(pg.movieid) AS total_peliculas
FROM 
    generos g
JOIN 
    peliculas_generos pg ON g.genero_id = pg.genero_id
GROUP BY 
    g.nombre_genero
ORDER BY 
    total_peliculas DESC;
-- Consulta 3: Usuarios Más Activos
--Objetivo: Encontrar los 5 usuarios que han realizado la mayor cantidad de ratings.
SELECT
    r.userid,
    COUNT(r.movieid) AS total_ratings,
    MAX(r.rating_date) AS ultimo_rating
FROM
    ratings r
GROUP BY
    r.userid
ORDER BY
    total_ratings DESC
LIMIT 5;
-- Consulta 4: Análisis de Tags por Año
--Objetivo: Encontrar la película más etiquetada en un año específico (ej., 2015). Demuestra el uso de funciones de fecha de PostgreSQL (EXTRACT).
SELECT
    p.title,
    COUNT(t.tag) AS total_tags_2015
FROM
    tags t
JOIN
    peliculas p ON t.movieid = p.movieid
WHERE 
    EXTRACT(YEAR FROM t.tag_date) = 2015
GROUP BY
    p.title
ORDER BY
    total_tags_2015 DESC
LIMIT 1;