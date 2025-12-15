## **Portafolio Profesional de Data Science y Análisis Avanzado**

### **Introducción**

Este repositorio es un portafolio de proyectos de Data Science que demuestra experiencia *end-to-end* en el ciclo de vida de los datos: **Ingeniería de Datos (SQL/PostgreSQL)**, **Análisis de Negocio (BI/Power BI)** y **Machine Learning (Modelado Supervisado/No Supervisado, NLP)**. Los proyectos se centran en la traducción de datos brutos a inteligencia de negocio y en la implementación de soluciones predictivas robustas, con un fuerte enfoque en el **diagnóstico de error** y el **valor ejecutivo**.

---

### **1. Resumen Ejecutivo**

| Dominio | Habilidades Clave y Demostración | Proyectos de Referencia |
| --- | --- | --- |
| **Ingeniería de Datos y DB** | Diseño de esquemas en Tercera Forma Normal (3NF), ETL con Python (`psycopg2` y carga masiva), Aplicación de Funciones de Ventana SQL y CTEs. | Proyectos de Manufactura y ETL |
| **Machine Learning** | Modelado de Regresión (Random Forest, Logarítmica), Clustering (K-Means), Clasificación y Vectorización NLP (Tf-idf). | Proyectos de Segmentación, Predicciones y Sentimientos |
| **Análisis de Negocio (BI)** | Análisis de Cohortes, Segmentación RFM, Creación de *Dashboards* Ejecutivos y Diagnóstico avanzado de Error de Modelos (Heterocedasticidad, Sesgo Geográfico). | Proyectos de RFM, Cohortes y E-commerce |
| **Análisis Especializado** | Series de Tiempo (Tendencia y Estacionalidad) y Análisis Geoespacial (Folium/Mapas de Calor, Riesgo Temporal). | Proyectos de Series de Tiempo y Geoespacial |

---

### **2. Tecnologías Utilizadas**

El *stack* tecnológico demuestra familiaridad con herramientas esenciales para la producción y el análisis avanzado:

* **Lenguajes:** **Python** (Dominio), **SQL** (PostgreSQL/MySQL).
* **Bibliotecas Centrales:** Pandas, NumPy, Scikit-learn, NLTK, Psycopg2.
* **Bases de Datos:** PostgreSQL.
* **Visualización y BI:** Power BI, Matplotlib, Seaborn, Folium.
* **Metodología:** Gestión segura de credenciales (`config.py`), Normalización 3NF, Modelado de Relación M:N.

---

### **3. Proyectos Agrupados por Dominio (12 Proyectos)**

#### **A. Ingeniería de Datos y Bases de Datos (SQL/ETL)**

* **Proyecto N°4:** Diseño y Normalización de Esquema para Manufactura (3NF, Modelado BOM).
* **Proyecto N°5:** Implementación y Consultas Analíticas Avanzadas (SQL) para costeo y riesgo de suministro.
* **Proyecto N°2:** ETL y Análisis de Datos de Películas (Carga Masiva con `psycopg2`).

#### **B. Machine Learning y Modelado Predictivo**

* **Proyecto N°12:** Predicción de Cantidad de Ventas de E-commerce con diagnóstico de **Heterocedasticidad y Sesgo Geográfico**.
* **Proyecto N°9:** Predicción de Valor de Viviendas (Regresión con Random Forest), alto R^2 Score.
* **Proyecto N°8:** Análisis de Segmentación y Clustering (K-Means) sobre métricas RFM.
* **Proyecto N°11:** Análisis de Sentimientos en Reseñas (NLP) usando Tf-idf y Clasificación.

#### **C. Business Intelligence y Análisis de Negocio**

* **Proyecto N°6:** Dashboard de Business Intelligence con Power BI para decisiones ejecutivas de Manufactura.
* **Proyecto N°3:** Análisis de Retención y Valor de Usuario por Cohortes.
* **Proyecto N°1:** Análisis de Segmentación de Clientes (RFM clásico).

#### **D. Análisis Especializado (Series de Tiempo y Geoespacial)**

* **Proyecto N°7:** Análisis de Series de Tiempo y Tendencias (Funciones de Ventana SQL y Curva de Crecimiento).
* **Proyecto N°10:** Análisis Geoespacial de Accidentes de Tráfico (Folium/HeatMaps) e identificación de riesgo horario.

---

### **4. Cómo Usar el Repositorio**

1. **Clonar el Repositorio:** Utiliza el comando `git clone` estándar y la URL del repositorio.
2. **Archivos de Datos y Configuración:** Debido al uso de archivos `.gitignore` en cada subdirectorio, el repositorio NO contiene los datasets originales (CSV) ni el archivo de credenciales `config.py`.
**Acción Requerida**: Para ejecutar los scripts, el usuario debe obtener los datasets citados en el `README.md` de cada proyecto y crear un archivo `config.py` con sus propias credenciales de PostgreSQL.
3. **Ejecución de Scripts:** Instala las dependencias de Python (listadas en el `README.md` de cada proyecto). Ejecuta el script principal de cada proyecto (ej. el script del Proyecto 12 es `python ecommerce.py`).
4. **Visualización y Análisis (Power BI):** El resultado de los scripts (archivos `.csv` de salida o la tabla final de PostgreSQL) se usa como fuente de datos para la generación de los *dashboards* de Power BI.

---

### **5. Licencia**

Este proyecto está bajo la licencia **MIT**. Eres libre de usar, modificar y distribuir el código con la atribución adecuada, **siempre y cuando se cite al autor original del repositorio.**

---
