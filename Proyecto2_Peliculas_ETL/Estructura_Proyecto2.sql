-- Primero creamos la Base de Datos
CREATE DATABASE movielens_db;
-- Después creamos las Tablas
-- TABLA 1: GENEROS
-- Almacena una lista única de nombres de género.
CREATE TABLE generos (
    genero_id INTEGER PRIMARY KEY,
    nombre_genero VARCHAR(50) UNIQUE NOT NULL
);
-- TABLA 2: PELICULAS
-- Almacena el ID principal de la película y el título.
CREATE TABLE peliculas (
    movieid INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);
-- TABLA 3: PELICULAS_GENEROS
-- Tabla de unión que normaliza la relación M:M entre Películas y Géneros.
CREATE TABLE peliculas_generos (
    movieid INTEGER REFERENCES peliculas(movieid),
    genero_id INTEGER REFERENCES generos(genero_id),
    PRIMARY KEY (movieid, genero_id) -- Clave primaria compuesta
);
-- TABLA 4: RATINGS
-- Almacena las calificaciones de los usuarios.
CREATE TABLE ratings (
    userid INTEGER NOT NULL,
    movieid INTEGER REFERENCES peliculas(movieid),
    rating NUMERIC(2, 1) NOT NULL,
    rating_date TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (userid, movieid) -- Asumiendo que un usuario califica una película solo una vez
);
-- TABLA 5: TAGS
-- Almacena las etiquetas (tags) dadas por los usuarios.
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY, -- Usamos SERIAL para una clave auto-incrementable
    userid INTEGER NOT NULL,
    movieid INTEGER REFERENCES peliculas(movieid),
    tag VARCHAR(255) NOT NULL,
    tag_date TIMESTAMP WITHOUT TIME ZONE
);
