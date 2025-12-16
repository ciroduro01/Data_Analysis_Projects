# Proyecto N°2: ETL y Análisis de Datos de Películas (MovieLens)

## Objetivos y Resumen Ejecutivo

Este proyecto implementa un proceso de Extracción, Transformación y Carga (ETL) utilizando Python y Pandas para procesar un *dataset* de más de 100,000 *ratings* y 3,600 películas (MovieLens). El objetivo es normalizar estos datos y cargarlos en una base de datos relacional PostgreSQL.

**Resumen Ejecutivo:**
* **ETL:** Script de Python (`peliculas.py`) que lee múltiples CSV, normaliza la relación N:M de géneros, transforma los *timestamps*, y carga los datos en PostgreSQL.
* **Modelado:** Se crea un esquema relacional con tablas para **Películas**, **Géneros**, **Ratings** y **Tags**.
* **BI:** Se desarrolla un *dashboard* en Power BI conectado a la base de datos para analizar tendencias de calificación y popularidad.

---

## Tecnologías Utilizadas

| Categoría | Tecnología | Uso Específico |
| :--- | :--- | :--- |
| **Lenguaje Principal** | Python 3.x | Lógica de ETL, limpieza y conexión a la base de datos. |
| **Librerías Python** | Pandas, Psycopg2, io | Manipulación de datos, conexión y carga masiva a PostgreSQL. |
| **Base de Datos** | PostgreSQL (pgAdmin) | Almacenamiento final de los datos transformados. |
| **Visualización** | Power BI | Creación del *dashboard* analítico y ejecución de consultas SQL clave. |
| **Control de Versiones**| Git / GitHub | Gestión del código fuente y del historial de cambios. |

---

## Resultados Clave y Visualizaciones

Las siguientes visualizaciones clave fueron creadas en Power BI, conectadas directamente a las tablas y consultas optimizadas en PostgreSQL (pgAdmin):

### 1. Top 10 Películas Populares por Rating Promedio
**Descripción:** Muestra las películas más consistentes y mejor valoradas.
![Top 10 Películas Populares por Rating Promedio](assets/Proyecto2_Peliculas_Populares.png)

### 2. Distribución del Catálogo por Género
**Descripción:** Determina el peso de cada género en el catálogo total.
![Distribución del Catálogo por Género](assets/Proyecto2_Catalogo_Genero.png)

### 3. Ranking de Usuarios más Activos
**Descripción:** Identifica a los contribuyentes principales de la plataforma.
![Ranking de Usuarios más Activos](assets/Proyecto2_Usuarios_Activos.png)

### 4. Evolución del Rating Promedio Anual
**Descripción:** Analiza la tendencia histórica del promedio de calificaciones.
![Evolución del Rating Promedio Anual](assets/Proyecto2_Evolucion_Rating.png)

### 5. Película Más Etiquetada en 2015
**Descripción:** Muestra la película con mayor interacción por etiquetas o *tags* para un año específico.
![Película Más Etiquetada en 2015](assets/Proyecto2_Pelicula_Etiquetada.png)

---

## Metodología (Fases del Proyecto, Procedimiento)

El proyecto se dividió en tres fases principales:

### **Fase 1: Extracción y Transformación (Python)**

* **Extracción:** Carga de los archivos `movies.csv`, `ratings.csv` y `tags.csv`.
* **Limpieza/Transformación:**
    * Conversión de la columna `timestamp` en `ratings` y `tags` a formato `datetime`.
    * **Normalización de Géneros:** División de la columna `genres` en múltiples filas para crear las tablas `generos` y `peliculas_generos` (relación N:M).
    * Ajuste de nombres de columnas a minúsculas para compatibilidad con PostgreSQL.

### **Fase 2: Carga (PostgreSQL)**

* **Creación del Esquema:** Ejecución del script `Estructura_Proyecto2.sql` para crear la base de datos y las 5 tablas relacionales. 
* **Carga de Datos:** El script `peliculas.py` se conecta a PostgreSQL (usando `config.py` para credenciales) y utiliza `psycopg2` para la carga masiva (función `copy_from`) en el orden de dependencia de las tablas (Padres primero, Hijos después).

### **Fase 3: Análisis (Power BI)**

* Conexión directa a PostgreSQL y uso de las `Consultas_Proyecto2.sql` para generar las vistas necesarias para el *dashboard* (ej. Top 10 por Rating, Usuarios más Activos).

---

## Modelado de Datos (Esquema Relacional)

El esquema relacional fue diseñado con una estructura optimizada para análisis. A continuación, se muestra el diagrama del modelo:

![Diagrama modelado en DBeaver](assets/Proyecto2_Diagrama.png)

### Tablas Creadas:

| Tabla | Propósito | Clave Primaria (PK) | Claves Foráneas (FK) |
| :--- | :--- | :--- | :--- |
| **peliculas** | Catálogo de películas. | `movieid` | N/A |
| **generos** | Lista única de categorías de género. | `genero_id` | N/A |
| **peliculas_generos**| Normaliza la relación M:M. | `(movieid, genero_id)` | `peliculas(movieid)`, `generos(genero_id)` |
| **ratings** | Almacena las calificaciones de los usuarios. | `(userid, movieid)` | `peliculas(movieid)` |
| **tags** | Almacena las etiquetas (tags) dadas por los usuarios. | `tag_id` (Serial) | `peliculas(movieid)` |

---

## Estructura del Archivo

Se utiliza una estructura modular para separar los recursos visuales, los archivos fuente (CSV) y el código.

```

.
└── Proyecto2_Peliculas_ETL/
├── peliculas.py              # Script principal de ETL
├── Estructura_Proyecto2.sql # Creación del esquema DB
├── Consultas_Proyecto2.sql # Consultas para BI (SQL)
├── Código_Adicional_Proyecto2.sql # Comandos de limpieza (TRUNCATE)
├── README.md                 # Documentación del proyecto
├── Citación.txt # Citación del Dataset
├── assets/                   # Recursos visuales del proyecto
|   ├── Proyecto2_Peliculas_Populares.png
|   ├── Proyecto2_Catalogo_Genero.png
|   ├── Proyecto2_Usuarios_Activos.png
|   ├── Proyecto2_Evolucion_Rating.png
|   ├── Proyecto2_Pelicula_Etiquetada.png
|   └── Proyecto2_Diagrama.png         # Diagrama del modelo relacional
├── data/                     # (IGNORADO) Archivos fuente CSV
|   ├── movies.csv
|   ├── ratings.csv
|   └── tags.csv
└── config.py                 # (IGNORADO) Credenciales de conexión

```

---

## Conclusiones

* **Normalización Exitosa:** Se demostró la capacidad de normalizar datos no estructurados (géneros concatenados) en un modelo relacional de Tercera Forma Normal (3NF) para optimizar las consultas.
* **Rendimiento de Carga:** El uso de la función `copy_from` de `psycopg2` garantiza una carga eficiente de grandes volúmenes de datos en PostgreSQL.
* **Insights:** El *dashboard* reveló una gran concentración de la actividad de *ratings* en un Top 5 de usuarios y destacó las preferencias de los usuarios por los géneros `Drama` y `Comedy`.

---

## Citación del Dataset

El *dataset* utilizado para este proyecto es el conjunto de datos **MovieLens**.

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872.

Descargado de https://grouplens.org/datasets/movielens/latest/

---

# Project N°2: ETL and Data Analysis of Movies (MovieLens)

## 1. Objectives and Summary

**Objective**
This project implements an Extract, Transform, Load (ETL) process using Python and Pandas to process a dataset of over 100,000 ratings and 3,600 movies (MovieLens). The objective is to normalize this data and load it into a PostgreSQL relational database.

**Summary**:

* **ETL**: A Python script (`peliculas.py`) reads multiple CSV files, normalizes the N:M relationship of genres, transforms timestamps, and loads the data into PostgreSQL.
* **Modeling**: A relational schema is created with tables for Movies, Genres, Ratings, and Tags.
* **BI**: A dashboard is developed in Power BI connected to the database to analyze rating and popularity trends. 

---

## 2. Technologies Used

| Category | Technology | Specific Use |
| :--- | :--- | :--- |
| **Main Language** | Python 3.x | ETL logic, cleaning, and database connection. |
| **Python Libraries** | Pandas, Psycopg2, io | Data manipulation, connection, and bulk loading to PostgreSQL. |
| **Database** | PostgreSQL (pgAdmin) | Final storage of transformed data. |
| **Visualization** | Power BI | Creation of the analytical dashboard and execution of key SQL queries. |
| **Version Control** | Git / GitHub | Management of source code and change history. |

---

## 3. Key Results and Visualizations

The following key visualizations were created in Power BI, directly connected to the optimized tables and queries in PostgreSQL (pgAdmin):

### 1. Top 10 Popular Movies by Average Rating
**Description**: Shows the most consistent and highest-rated movies.
![Top 10 Popular Movies by Average Rating](assets/Proyecto2_Peliculas_Populares.png)

### 2. Catalog Distribution by Genre
Description: Determines the weight of each genre in the total catalog.
![Catalog Distribution by Genre](assets/Proyecto2_Catalogo_Genero.png)

### 3. Ranking of Most Active Users
Description: Identifies the platform's top contributors.
![Ranking of Most Active Users](assets/Proyecto2_Usuarios_Activos.png)

### 4. Evolution of the Average Annual Rating
Description: Analyzes the historical trend of the average rating.
![Evolution of the Average Annual Rating](assets/Proyecto2_Evolucion_Rating.png)

### 5. Most Tagged Movie in 2015
Description: Shows the movie with the most tag interaction for a specific year.
![Most Tagged Movie in 2015](assets/Proyecto2_Pelicula_Etiquetada.png)

---

## 4. Methodology (Project Phases, Procedure)

The project was divided into three main phases:

1. **Phase 1: Extraction and Transformation (Python)**
* **Extraction**: Loading the `movies.csv`, `ratings.csv`, and `tags.csv` files.
* **Cleaning/Transformation**:
* Converting the `timestamp` column in `ratings` and `tags` to `datetime` format.
* **Genre Normalization**: Splitting the `genres` column into multiple rows to create the `generos` and `peliculas_generos` tables (N:M relationship).
* Adjusting column names to lowercase for PostgreSQL compatibility.
2. **Phase 2: Loading (PostgreSQL)**
* **Schema Creation**: Execution of the `Estructura_Proyecto2.sql` script to create the database and the 5 relational tables.
* **Data Loading**: The `peliculas.py` script connects to PostgreSQL (using `config.py` for credentials) and uses `psycopg2` for bulk loading (`copy_from` function) in the order of table dependencies (Parents first, Children second).
3. **Phase 3: Analysis (Power BI)**
* Direct connection to PostgreSQL and use of `Consultas_Proyecto2.sql` to generate the necessary views for the dashboard (e.g., Top 10 by Rating, Most Active Users).

---

## 5. Data Modeling (Relational Schema)

The relational schema was designed with a structure optimized for analysis. The following diagram shows the model:

![ERD Diagram](assets/Proyecto2_Diagrama.png)

**Tables Created**

| Table | Purpose | Primary Key (PK) | Foreign Keys (FK) |
| :--- | :--- | :--- | :--- |
| **peliculas** | Movie catalog. | `movieid` | N/A |
| **generos** | Unique list of genre categories. | `genero_id` | N/A |
| **peliculas_generos** | Normalizes the M:M relationship. | (`movieid`, `genero_id`) | `peliculas(movieid)`, `generos(genero_id)` |
| **ratings** | Stores user ratings. | (`userid, movieid`) | `peliculas(movieid)` |
| **tags** | Stores user-defined tags. | `tag_id` (Serial) | `peliculas(movieid)` |

---

## 6. File Structure

A modular structure is used to separate visual resources, source files (CSV), and code.

```bash
└── Proyecto2_Peliculas_ETL/
├── peliculas.py       # Main ETL script
├── Estructura_Proyecto2.sql   # DB schema creation
├── Consultas_Proyecto2.sql    # BI queries (SQL)
├── Código_Adicional_Proyecto2.sql    # Cleanup commands (TRUNCATE)
├── README.md # Project documentation
├── Citación.txt # Dataset citation
├── assets/ # Project visual resources
     ├── Proyecto2_Peliculas_Populares.png
     ├── Proyecto2_Catalogo_Genero.png
     ├── Proyecto2_Usuarios_Activos.png
     ├── Proyecto2_Evolucion_Rating.png
     ├── Proyecto2_Pelicula_Etiquetada.png
     └── Proyecto2_Diagrama.png     # Relational model diagram
├── data/ # (IGNORED) CSV source files
    ├── movies.csv
    ├── ratings.csv
    └── tags.csv
└── config.py # (IGNORED) Connection credentials
```

---

## 7. Conclusions

1. **Successful Normalization**: The ability to normalize unstructured data (concatenated genres) in a Third Normal Form (3NF) relational model to optimize queries was demonstrated.
2. **Load Performance**: The use of the `copy_from` function in psycopg2 ensures efficient loading of large volumes of data into PostgreSQL.
3. **Insights**: The dashboard revealed a high concentration of rating activity among a top 5 users and highlighted user preferences for the **Drama** and **Comedy** genres.

---

## 8. Dataset Citation

The dataset used for this project is the MovieLens dataset.

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872.

Downloaded from https://grouplens.org/datasets/movielens/latest/
