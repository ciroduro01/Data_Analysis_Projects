# Proyecto N°9: Predicción de Valor de Viviendas (Regresión)
---
## **Implementación y Validación de un Modelo de Regresión para Predecir el Valor Mediano de Viviendas en California.**

---

## Objetivos y Resumen Ejecutivo

### Objetivo del Proyecto
El objetivo central fue construir y validar un modelo de Regresión para el dataset de Viviendas de California, enfocándose en la obtención de un alto rendimiento (R² Score) y la generación de un output de datos limpio para el análisis de Business Intelligence.

### Resumen Ejecutivo
El proyecto ha finalizado con la implementación de un **Random Forest Regressor** en Python. El modelo alcanzó un **R² Score de 0.803**, demostrando una alta capacidad para predecir los valores inmobiliarios. La validación exhaustiva de los resultados mediante visualizaciones de BI confirma la solidez metodológica y estadística.

---

## Arquitectura de Data Science

La arquitectura se divide en tres fases principales: Adquisición y EDA, Modelado y Validación, y Generación de Output para BI.

### ETL, EDA y Feature Engineering
* **Adquisición:** El script `housing.py` se encarga de cargar el dataset nativo de Scikit-learn.
* **Análisis Exploratorio de Datos (EDA):** Se analizó la correlación de las variables y la distribución geográfica de los precios (`eda_regresion.py`).
* **Feature Engineering:** Se aplicó la división Train/Test y la **Estandarización** de las variables predictoras.

#### Visualizaciones Clave de EDA
* **Gráfico 1: Matriz de Correlación**
![Matriz de Correlación](assets/Heatmap_Correlacion.png)
    * **Análisis:** Confirma que el **Ingreso Mediano (`MedInc`)** es el predictor con mayor correlación positiva.
* **Gráfico 2: Dispersión Geográfica**
![Dispersión Geográfica](assets/Distribucion_Vivienda.png)
    * **Análisis:** Visualiza la concentración de precios altos cerca de la costa, crucial para la justificación del modelo.

### Machine Learning (modelado_regresion2.py)
* **Algoritmo:** **Random Forest Regressor**.
* **Métrica:** **R² Score** (80.3% de la varianza explicada).

### Generación de Output para Power BI
* El script `modelado_regresion2.py` exporta el archivo `predicciones_viviendas_bi_FINAL_CORREGIDO.csv`, listo para la ingesta en BI.

---

## Resultados de Validación y Visualizaciones

La validación se realizó sobre el conjunto de prueba, utilizando Power BI para una mejor interpretabilidad de los resultados.

### Métricas Finales
| Métrica | Valor | Interpretación |
| :--- | :--- | :--- |
| **R^2 Score** | 0.803 | La varianza en el valor de las viviendas se explica en un 80.3% por el modelo. |

### Visualizaciones de Validación (Power BI)

#### Gráfico 1: Mapa Geográfico de Errores
El mapa permite ver la identificación geográfica de las áreas de mayor imprecisión en la predicción.
![Mapa de Errores BI](assets/Mapa_California.png)


#### Gráfico 2: Curva de Predicción vs. Realidad
La curva confirma visualmente la alta alineación del modelo con la línea de *y=x*, validando el alto *R^2*.
![Curva Predicción vs Realidad BI](assets/Dispersion_Valores.png)

#### Gráfico 3: Histograma de Error Absoluto
El histograma muestra una **Distribución Sesgada a la Derecha**, con el pico concentrado en los valores más cercanos a cero. Esta forma confirma que la mayoría de los errores son mínimos y que el modelo es estadísticamente robusto.
![Histograma de Error Absoluto BI](assets/Distribucion_Frecuencia.png)

---

## Estructura del Repositorio

El repositorio sigue la siguiente estructura de directorios:

```

Proyecto9_Predicciones_viviendas_California
├── .gitignore                      # Archivo de configuración.
├── housing.py                      # Script de Adquisición de datos.
├── eda_regresion.py                # Script de EDA y Matplotlib.
├── modelado_regresion2.py          # Script de Modelado y exportación final.
├── predicciones_viviendas_bi_FINAL_CORREGIDO.csv  # Output de datos final. IGNORADO
├── assets/                         # Carpeta de recursos visuales
│   ├── Heatmap_Correlacion.png
│   ├── Distribucion_Vivienda.png
│   ├── Mapa_California.png
│   ├── Dispersion_Valores.png
│   └── Distribucion_Frecuencia.png
└── README.md                       # Documentación principal.

```

---

## Conclusiones

El Proyecto N°9 ha finalizado con éxito, entregando un modelo de regresión con alto rendimiento. El artefacto de datos es apto para su ingesta directa en el área de BI, y la validación visual confirma la calidad y la interpretabilidad de las predicciones del modelo.

---

# Project N°9: Home Value Prediction (Regression) 

## **Implementation and Validation of a Regression Model to Predict the Median Home Value in California.**

## 1. Objectives and Summary

**Project Objective**
The central objective was to build and validate a regression model for the California home dataset, focusing on achieving high performance (R² score) and generating clean data output for Business Intelligence analysis.

**Summary**
The project culminated in the implementation of a Random Forest Regressor in Python. The model achieved an R² score of 0.803, demonstrating a high capacity for predicting real estate values. Extensive validation of the results through BI visualizations confirms the methodological and statistical soundness.

---

## 2. Data Science Architecture

The architecture is divided into three main phases: Acquisition and Data Entry Analysis (DEA), Modeling and Validation, and Output Generation for BI.

### ETL, EDA, and Feature Engineering
* **Acquisition**: The `housing.py` script handles loading the native Scikit-learn dataset.
* **Exploratory Data Analysis (EDA)**: The correlation of variables and the geographic distribution of prices were analyzed (`eda_regresion.py`).
* **Feature Engineering**: The Train/Test split and standardization of predictor variables were applied.

#### Key EDA Visualizations
* **Chart 1: Correlation Matrix**

![Correlation Matrix](assets/Heatmap_Correlacion.png)

* **Analysis**: Confirms that Median Income (`MedInc`) is the predictor with the strongest positive correlation.

* **Chart 2: Geographic Dispersion**

![Geographic Dispersion](assets/Distribucion_Vivienda.png)

* **Analysis**: Visualizes the concentration of high prices near the coast, crucial for justifying the model.

### Machine Learning (`modelado_regression2.py`)
* **Algorithm**: Random Forest Regressor.
* **Metric**: R² Score (80.3% of the variance explained). 

### Generating Output for Power BI
* The `modelado_regresion2.py` script exports the `predicciones_viviendas_bi_FINAL_CORREGIDO.csv` file, ready for ingestion into BI.

---

## 3. Validation Results and Visualizations

Validation was performed on the test set, using Power BI for better interpretability of the results.

### Final Metrics
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **R^2 Score** | 0.803 | The variance in the housing value is explained by the model at 80.3%. |

### Validation Visualizations (Power BI)

#### Chart 1: Geographic Map of Errors
The map allows you to see the geographic identification of the areas with the greatest inaccuracy in the prediction.

![Geographic Map of Errors](assets/Mapa_California.png)

#### Chart 2: Prediction vs. Reality Curve
The curve visually confirms the high alignment of the model with the y=x line, validating the high R^2.

![Prediction vs Reality Curve BI](assets/Dispersion_Valores.png)

#### Chart 3: Absolute Error Histogram
The histogram shows a right-skewed distribution, with the peak concentrated at values ​​closest to zero. This shape confirms that most errors are minimal and that the model is statistically robust.

![Absolute Error Histogram BI](assets/Distribucion_Frecuencia.png)

---

## 4. Repository Structure

The repository follows the following directory structure:

```bash
Proyecto9_Predicciones_viviendas_California
├── .gitignore # Configuration file.
├── housing.py # Data acquisition script.
├── eda_regresion.py # EDA and Matplotlib script.
├── modelado_regresion2.py # Modeling and final export script.
├── predicciones_viviendas_bi_FINAL_CORREGIDO.csv # Final data output. IGNORED
├── assets/ # Visual Resources Folder
│   ├── Heatmap_Correlacion.png
│   ├── Distribucion_Vivienda.png
│   ├── Mapa_California.png
│   ├── Dispersion_Valores.png
│   └── Distribucion_Frecuencia.png
└── README.md # Main Documentation
```

---

## 5. Conclusions

Project 9 has been successfully completed, delivering a high-performance regression model. The data artifact is suitable for direct ingestion in the BI area, and visual validation confirms the quality and interpretability of the model's predictions.

---
