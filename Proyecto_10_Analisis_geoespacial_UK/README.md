# Proyecto N°10: Análisis Geoespacial de Accidentes de Tráfico en el Reino Unido

## Título del Proyecto
**Análisis Geoespacial y Temporal de Riesgo de Accidentes de Tráfico en el Reino Unido: Identificación de Zonas Calientes y Patrones Horarios.**

---

## Objetivos y Resumen Ejecutivo

### Objetivo del Proyecto
El objetivo principal fue realizar una limpieza robusta de un dataset geoespacial (Accidentes de Tráfico en UK), transformando las coordenadas y la severidad en información accionable para identificar los patrones de riesgo espacial y temporal.

### Resumen Ejecutivo
El proyecto ha concluido con la limpieza exitosa de **1,910,000** registros geoespaciales y la generación de un modelo de datos apto para Business Intelligence. El análisis reveló que el **máximo riesgo de incidentes graves se concentra entre las 15:00 y las 18:00**, y los puntos calientes de riesgo fatal se ubican en carreteras y cruces específicos fuera de las áreas de mayor densidad de tráfico.

---

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías Clave:**
    * **Pandas / NumPy:** Carga, limpieza, filtrado geoespacial y corrección de tipos.
    * **Folium / HeatMap:** Generación de mapas de calor estáticos (artefactos de código).
* **Plataforma de Visualización:** Microsoft Power BI.

---

## Resultados Clave y Visualizaciones

### Limpieza y Transformación de Datos
* **Registros Iniciales:** 2,000,000
* **Registros Finales Limpios:** 1,910,000 (Pérdida del 4.5% de registros no válidos o incompletos).
* **Transformaciones:** Mapeo de Severidad (Texto a Número), Creación de `Hour_of_Day`, y Filtrado de Coordenadas fuera de UK.

### Visualizaciones Clave

#### Mapa 1: Concentración Geográfica de Incidentes de Tráfico en UK
Muestra el volumen total de accidentes, confirmando que la densidad se concentra en las grandes áreas metropolitanas.
![Mapa de Densidad General](assets/incidentes_trafico_uk.png)

#### Mapa 2: Puntos Calientes de Máximo Riesgo (Accidentes Graves y Fatales)
Aísla solo los accidentes de Severidad Fatal y Grave (1 y 2). Este mapa revela los *hotspots* críticos de riesgo, que no siempre coinciden con la mayor densidad de tráfico.
![Mapa de Riesgo Máximo](assets/maximo_riesgo_uk.png)

#### Gráfico 3: Patrón Horario de Máximo Riesgo: Picos entre 15:00 y 18:00
Identifica el factor tiempo. La concentración de la mayoría de los incidentes en la hora pico vespertina es un hallazgo clave para la planificación de recursos de seguridad vial.
![Gráfico de Horas Pico](assets/hora_maximo_riesgo.png)

---

## Procedimiento y Ejecución

1.  **Carga y Selección:** Carga del dataset `Accidents.csv` seleccionando las columnas clave (`accidents2.py`).
2.  **Limpieza Crítica:** Corrección de tipos, eliminación de nulos y **filtrado geoespacial** estricto para coordenadas (`Latitude` y `Longitude`) fuera de los límites del Reino Unido.
3.  **Transformación:** Creación de la columna `Hour_of_Day` y mapeo numérico de `Accident_Severity`.
4.  **Generación de Artefactos:** Creación de los mapas estáticos de Folium (`01_accidents_heatmap_general.html` y `02_accidents_heatmap_graves.html`).
5.  **Exportación:** Generación de `accidentes_uk_limpio_para_bi_final.csv` para la ingesta en Power BI.
6.  **Análisis BI:** Creación de los visuales de validación (Gráficos 1, 2 y 3).

---

## Estructura de los Archivos

El repositorio sigue la siguiente estructura de directorios:

```

Proyecto_10_Analisis_geoespacial_UK
├── .gitignore                      # Ignora el CSV de salida.
├── accidents2.py                   # Script principal de Ingeniería de Datos y Folium.
├── Accidents.csv                   # Dataset original (entrada). IGNORED
├── accidentes_uk_limpio_para_bi_final.csv # Output de datos limpio para BI (salida). IGNORED
├── 01_accidents_heatmap_general.html # Mapa estático de Folium (General).
├── 02_accidents_heatmap_graves.html  # Mapa estático de Folium (Graves/Fatales).
├── assets/                         # Carpeta de recursos visuales de Power BI
│   ├── incidentes_trafico_uk.png   # Mapa 1 (Power BI)
│   ├── maximo_riesgo_uk.png        # Mapa 2 (Power BI)
│   └── hora_maximo_riesgo.png      # Gráfico 3 (Power BI)
├── Citacion.txt                    # Documento de citación del dataset.
├── folium_uk.png # Imagen del archivo HTML, creada para el README principal
└── README.md                       # Documentación principal.

```

---

## Conclusiones

El Proyecto N°10 ha proporcionado un análisis robusto y visualmente impactante, destacando que el riesgo de accidentes de tráfico es un problema tanto **espacial** como **temporal**. Los artefactos generados son aptos para ser utilizados por el área de Business Intelligence.

---

## Citación del Dataset

El dataset se basa en los Datos de Seguridad Vial del Departamento de Transporte (*Department for Transport's Road Safety Data*) para los años 2005-2017, disponibles a través del sitio web oficial del Gobierno del Reino Unido. El dataset original fue descargado de la página https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles

---

# Project N°10: Geospatial Analysis of Traffic Accidents in the United Kingdom

## **Geospatial and Temporal Analysis of Traffic Accident Risk in the United Kingdom: Identification of Hotspots and Time Patterns**

## 1. Objectives and Summary

**Objective**: The main objective was to perform a robust cleaning of a geospatial dataset (Traffic Accidents in the UK), transforming coordinates and severity into actionable information to identify spatial and temporal risk patterns.

**Summary**: The project concluded with the successful cleaning of 1,910,000 geospatial records and the generation of a data model suitable for Business Intelligence. The analysis revealed that the highest risk of serious incidents is concentrated between 3:00 PM and 6:00 PM, and fatal risk hotspots are located on specific roads and intersections outside of areas with the highest traffic density.

---

## 2. Technologies Used

* **Language**: Python 3.x
* **Key Libraries**:
  * **Pandas / NumPy**: Loading, cleaning, geospatial filtering and type correction.
  * **Folium / HeatMap**: Generation of static heat maps (code artifacts).
* **Visualization Platform**: Microsoft Power BI.

---

## 3. Key Results and Visualizations

### Data Cleaning and Transformation
* **Initial Records**: 2,000,000
* **Final Cleaned Records**: 1,910,000 (4.5% loss of invalid or incomplete records).
* **Transformations**: Severity Mapping (Text to Number), Creation of `Hour_of_Day`, and Filtering of Coordinates outside the UK.

### Key Visualizations

#### Map 1: Geographic Concentration of Traffic Incidents in the UK
Shows the total volume of accidents, confirming that the density is concentrated in large metropolitan areas.

![Traffic Incidents Concentration in the UK](assets/incidentes_trafico_uk.png)

#### Map 2: High-Risk Hotspots (Serious and Fatal Accidents)
Isolates only fatal and serious accidents (1 and 2 severity). This map reveals critical risk hotspots, which do not always coincide with the highest traffic density.
![High-Risk Hotspots in the UK](assets/maximo_riesgo_uk.png)

#### Chart 3: Peak Time Pattern: Peaks between 3:00 PM and 6:00 PM
Identifies the time factor. The concentration of most incidents during the evening rush hour is a key finding for road safety resource planning.
![Peak Time Pattern](assets/hora_maximo_riesgo.png)

---

## 4. Procedure and Execution

1. **Loading and Selection**: Loading the `Accidents.csv` dataset by selecting the key columns (`accidents2.py`).
2. **Critical Cleaning**: Type correction, null removal, and strict geospatial filtering for coordinates (`Latitude` and `Longitude`) outside the UK.
3. **Transformation**: Creation of the `Hour_of_Day` column and numerical mapping of `Accident_Severity`.
4. **Artifact Generation**: Creation of the static Folium heatmaps (`01_accidents_heatmap_general.html` and `02_accidents_heatmap_graves.html`).
5. **Export: Generation of the `accidentes_uk_limpio_para_bi_final.csv` file for ingestion into Power BI.
6. **BI Analysis**: Creation of the validation visuals (Charts 1, 2, and 3).

---

## 5. File Structure

The repository follows the following directory structure:

```bash
Proyecto_10_Analisis_geoespacial_UK
├── .gitignore # Ignores the output CSV.
├── accidents2.py # Main Data Engineering and Folium script.
├── Accidents.csv # Original dataset (input). IGNORED
├── accidentes_uk_limpio_para_bi_final.csv # Clean data output for BI. IGNORED
├── 01_accidents_heatmap_general.html # Static Folium heatmap (General).
├── 02_accidents_heatmap_graves.html # Static Folium heatmap (Severe/Fatal).
├── assets/ # Power BI visual resources folder
│   ├── incidentes_trafico_uk.png # Map 1 (Power BI)
│   ├── maximo_riesgo_uk.png # Map 2 (Power BI)
│   └── hora_maximo_riesgo.png # Chart 3 (Power BI)
├── Citacion.txt # Dataset citation document.
├── folium_uk.png # Imagen taken from the HTML file, created for the main README
└── README.md # Main documentation.
```

---

## 6. Conclusions
Project 10 has provided a robust and visually impactful analysis, highlighting that the risk of traffic accidents is both a spatial and temporal problem. The generated artifacts are suitable for use by the Business Intelligence area.

---

## 7. Dataset Citation
The dataset is based on the Department for Transport's Road Safety Data for the years 2005-2017, available through the official UK Government website. The original dataset was downloaded from https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles
