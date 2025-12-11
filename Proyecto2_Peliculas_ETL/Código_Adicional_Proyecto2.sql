--En caso de saturación:
-- Ejecuta estos comandos en el cliente de PostgreSQL.
-- TRUNCATE vacía completamente la tabla. CASCADE asegura que se vacíen también las tablas dependientes (ej. si ratings depende de peliculas).

TRUNCATE TABLE generos CASCADE;
TRUNCATE TABLE peliculas CASCADE;
TRUNCATE TABLE ratings CASCADE;
TRUNCATE TABLE peliculas_generos CASCADE;
TRUNCATE TABLE tags CASCADE;

-- Confirma que la base de datos vació las tablas.
-- Volver a ejecutar el script de Python (peliculas.py).