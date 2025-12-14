# Proyecto N°3: Análisis de Retención y Valor de Usuario (MovieLens)

## Objetivo del Proyecto
Este proyecto de Data Engineering y Business Intelligence tiene como objetivo principal medir la **Retención de Usuarios por Cohortes** y el comportamiento asociado a la satisfacción (Rating Promedio) utilizando la base de datos de calificaciones de películas.

El análisis de cohortes permite entender cómo el comportamiento de los usuarios (su permanencia y su calidad de calificación) evoluciona con el tiempo, comparando a los usuarios según su mes de adquisición.

---

## Tecnologías y Herramientas

| Categoría | Herramienta | Uso |
| :--- | :--- | :--- |
| **Base de Datos** | PostgreSQL | Almacenamiento y procesamiento de datos relacionales (`ratings`, `peliculas`). |
| **ETL y Lógica** | Python (`pandas`, `psycopg2`) | Extracción de datos de PostgreSQL (Querying) y transformación del resultado a formato CSV. |
| **Análisis de Lógica** | SQL (PostgreSQL) | Lógica de negocio principal para calcular la cohorte y el desfase de meses. |
| **Visualización** | Power BI | Creación de dashboards interactivos y medidas DAX. |

---

## Metodología ETL (Extract, Transform, Load)

### 1. Extracción y Transformación (SQL y Python)
La lógica principal reside en una consulta SQL compleja diseñada para "alargar" los datos, transformando la tabla de hechos (`ratings`) en un formato adecuado para el análisis de cohortes.

* **Paso Clave: Determinación de Cohorte:** Se utiliza una Common Table Expression (CTE) para identificar el mes del *primer* rating de cada usuario (`cohorte_mes`).
* **Cálculo de Desfase:** Se calcula el número de meses transcurridos (`desfase_meses`) entre la fecha de cada actividad (`rating_date`) y la fecha de adquisición (`cohorte_mes`). Este cálculo es esencial para el eje de tiempo relativo.
* **Exportación:** El script `peliculasbases.py` ejecuta la consulta final, garantiza la correcta codificación (`encoding='ISO-8859-1'`) y exporta el resultado al archivo **`retencion_datos_largos.csv`**.

### 2. Carga y Modelado (Power BI)
1.  El CSV se carga en Power BI.
2.  Se crean las medidas DAX clave para el análisis:
    * **`[Usuarios Iniciales]`**: Utiliza `CALCULATE` y `ALLEXCEPT` para fijar el total de usuarios de la cohorte en el Mes 0 (el denominador).
    * **`[Usuarios Retenidos]`**: Cuenta los usuarios únicos activos en el mes (`DISTINCTCOUNT`).
    * **`[Porcentaje de Retención]`**: `DIVIDE([Usuarios Retenidos], [Usuarios Iniciales])`.
    * **`[Promedio Rating]`**: `AVERAGE()` de la columna `rating`.

---

## Visualizaciones Clave

El proyecto genera tres gráficos esenciales para entender el valor y la permanencia del usuario:

### 1. Matriz de Retención (Heatmap)
* **Tipo:** Matriz con Formato Condicional.
* **Uso:** Muestra visualmente el **`[Porcentaje de Retención]`** por `cohorte_mes` (Filas) a lo largo del `desfase_meses` (Columnas).

![Heatmap de Retención por Cohorte](assets/heatmap_retencion.png)

### 2. Gráfico de Columnas de Cohortes
* **Tipo:** Gráfico de Columnas Agrupadas.
* **Uso:** Muestra el **`[Usuarios Iniciales]`** de cada cohorte. Indica qué cohortes tienen un tamaño muestral significativo.

![Volumen de Usuarios Iniciales por Cohorte](assets/volumen_cohortes.png)

### 3. Promedio de Rating por Cohorte
* **Tipo:** Gráfico de Líneas.
* **Uso:** Muestra cómo evoluciona el **`[Promedio Rating]`** de cada cohorte a medida que pasa el tiempo (`desfase_meses`). Permite analizar si los usuarios que se quedan más tiempo están más o menos satisfechos.

![Promedio de Rating por Desfase de Meses](assets/promedio_rating.png)

---

## Estructura del Repositorio

El proyecto mantiene una estructura clara para la reproducibilidad:

```

Data_Analysis_Projects
└── Proyecto3_analisis_cohortes/  #Carpeta raíz del Proyecto N°3
    ├── assets/
    │   ├── heatmap_retencion.png
    │   ├── promedio_rating.png
    │   └── volumen_cohortes.png
    ├── config.py
    ├── Consultas_Proyecto3.sql
    ├── peliculasbases.py
    ├── README.md
    ├── Retencion_Proyecto3.sql
    ├── Estructura_Proyecto3.sql
    ├── schema_definition.sql
    └── .gitignore

```

**Archivos Excluidos (Vía `.gitignore`)**

Para mantener el repositorio limpio y seguro, se excluyen los siguientes archivos:

* `config.py` (Contiene credenciales sensibles)
* `retencion_datos_largos.csv` (Archivo generado por el script y potencialmente grande)
* `__pycache__/`


---

## **Conclusiones Clave y Recomendaciones**

Las siguientes conclusiones se derivan del análisis de las tendencias observadas en las visualizaciones:

* **Alto Desfase Inicial:** Existe una caída de retención significativa entre el Mes 0 y el Mes 1 en todas las cohortes, lo que sugiere una **fuga de usuarios de baja fricción**. Se requiere optimizar la experiencia de "Onboarding" para aumentar el valor percibido rápidamente.
* **Estabilización de Usuarios Leales:** La tasa de retención tiende a estabilizarse a partir del Mes 4. Los usuarios que permanecen más allá de este punto representan la **base de usuarios leales (Core Users)** del servicio.
* **Efecto del Volumen en la Calidad:** Las cohortes con el mayor volumen de adquisición (Gráfico de Columnas) no siempre presentan la mejor retención o el rating promedio más alto (Gráfico de Líneas). **Recomendación:** Concentrar los esfuerzos de marketing en canales que atraigan usuarios con alta propensión a la retención, no solo alto volumen.
* **Deterioro del Rating:** Se observa que el promedio de calificación de las películas (Rating) puede disminuir ligeramente a medida que el usuario permanece más tiempo. Esto indica una posible necesidad de mejorar el **algoritmo de recomendación** para usuarios con mayor antigüedad.

---

## Citación del Dataset

El *dataset* utilizado para este proyecto es el conjunto de datos **MovieLens**.

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872.

Descargado de https://grouplens.org/datasets/movielens/latest/

-----
