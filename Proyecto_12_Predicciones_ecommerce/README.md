# Proyecto N°12 - Predicción de Cantidad de Ventas de E-commerce

## Objetivos y Resumen Ejecutivo

Este proyecto tiene como objetivo principal construir un *pipeline* de análisis predictivo completo, desde la ingesta de datos brutos hasta la visualización ejecutiva del error del modelo.

El corazón del proyecto es la implementación de un modelo de **Regresión Logarítmica** para predecir la variable crítica de negocio: la **Cantidad** de productos vendidos por transacción (`Quantity`).

### Conclusiones Ejecutivas

* **Modelo Final:** Se implementó un modelo de Regresión Lineal con transformación Logarítmica en la variable dependiente (`Quantity`).

* **Diagnóstico de Error (Heterocedasticidad):** El error de predicción es **diez veces mayor** para las transacciones de *Venta Grande* (>20 unidades) que para las *Ventas Pequeñas* (1-5 unidades). El modelo es inconsistente y solo es confiable para estimar volúmenes bajos.

* **Sesgo Geográfico:** El modelo es ineficiente y registra un Error Absoluto Medio (MAE) extremadamente alto en **Suecia (Sweden)**, sugiriendo un patrón de compra atípico en esa región que el modelo general no puede capturar.

---

## Tecnologías Utilizadas

| Categoría | Herramientas y Lenguajes | Propósito |
| :--- | :--- | :--- |
| **Ingesta y Procesamiento** | Python, Pandas, NumPy | Limpieza, *Feature Engineering* y transformación de datos. |
| **Machine Learning** | Scikit-learn (Linear Regression) | Creación y entrenamiento del modelo predictivo. |
| **Persistencia de Datos** | PostgreSQL, `psycopg2` | Almacenamiento seguro del dataset limpio y de las predicciones. |
| **Visualización Ejecutiva** | Power BI, DAX | Análisis de error post-predicción para conclusiones de negocio. |
| **Seguridad** | `.gitignore`, `config.py` | Gestión segura de credenciales de base de datos. |

---

## Resultados Clave y Visualizaciones

Las principales conclusiones provienen del análisis de los residuos del modelo de Regresión Logarítmica.

### Gráficos Matplotlib: Predicción y Distribución de Residuos

* **Archivos:** `assets/dispersion_cantidad.png` y `assets/residuos_cantidad.png`
* **Propósito:** Confirmar visualmente la alineación general de las predicciones y la distribución de los errores generados en Python.

![Gráfico de Dispersión Cantidad](assets/dispersion_cantidad.png)
![Gráfico de Residuos Cantidad](assets/residuos_cantidad.png)

### Gráfico Power BI 1: Diagnóstico del Modelo

**Título:** **MAE Promedio por Rango de Cantidad**

Este gráfico confirma la **Heterocedasticidad**. La barra de `Venta Grande` muestra que el error se dispara en las transacciones de alto valor, un punto débil crítico del modelo.

![MAE Promedio por Rango de Cantidad](assets/MAE_rango.png)

### Gráfico Power BI 2: Sesgo Geográfico

**Título:** **Desempeño del Error (MAE) por País**

Este gráfico de barras horizontales revela que el MAE en **Suecia** es anormalmente alto, sugiriendo que las características de venta en ese país no se ajustan al modelo global.

![Desempeño del Error (MAE) por País](assets/MAE_pais.png)

---

## Procedimiento y Metodología

El proyecto se ejecutó siguiendo un *pipeline* de **4 Fases**:

1.  **FASE 1: Limpieza y *Feature Engineering***: Carga del CSV, limpieza de valores nulos y atípicos, y creación de variables categóricas (ej. `DiaSemana`) y numéricas (ej. `ValorTotal`).
2.  **FASE 2: Persistencia Segura**: Uso de `config.py` y el método `copy_from` de `psycopg2` para realizar la carga masiva (CRUD) y segura del dataset limpio (`retail_clean`) en PostgreSQL.
3.  **FASE 3: Modelado (Regresión Logarítmica)**: Aplicación de la transformación logarítmica (`np.log1p`) a la variable dependiente `Quantity` para mitigar la asimetría, entrenamiento del modelo de Regresión Lineal y reversión de la transformación (`np.expm1`) para la predicción final.
4.  **FASE 4: Exportación y Visualización Ejecutiva**: Generación del archivo `ecommerce_predicciones_bi.csv` con las predicciones y los residuos, y análisis detallado en Power BI.

---

## Estructura del Proyecto

```
Proyecto_12_Predicciones_ecommerce/
├── assets/
│   ├── dispersion_cantidad.png    
│   ├── residuos_cantidad.png     
│   ├── MAE_rango.png             
│   └── MAE_pais.png              
├── config.py                     # Credenciales seguras para PostgreSQL (IGNORADO)
├── citacion.txt                  # Archivo de citación del dataset
├── .gitignore                    # Ignora archivos sensibles (config.py) y grandes (datasets)
├── online_retail.csv             # Dataset original (IGNORADO)
├── ecommerce_base.sql            # Definición de la base de datos (DB) y la tabla (DDL)
├── ecommerce.py                  # Script principal (Limpieza, ML, Persistencia, Exportación)
├── ecommerce_predicciones_bi.csv # Datos de salida con predicciones y residuos para BI (IGNORADO)
└── README.md                     # Documentación del proyecto
```

---

## Conclusiones

El proyecto demostró la capacidad de construir un *pipeline* predictivo completo. El uso de la **Regresión Logarítmica** mejoró la métrica global y el MAE para la mayoría de los datos, pero las visualizaciones en Power BI revelaron que el modelo sigue siendo vulnerable a la **Heterocedasticidad** (ventas grandes) y al **Sesgo Geográfico** (Suecia). Las futuras mejoras deberían enfocarse en modelos más robustos (ej. Random Forest) o en la segmentación del modelo por país.

---

## Citación del Dataset

El dataset utilizado en este proyecto es:

> UCI Machine Learning Repository. (2020). Online Retail II. Obtenido de https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

---

# Project N°12 - E-commerce Sales Quantity Prediction

## 1. Objectives and Summary

The main objective of this project is to build a complete predictive analytics pipeline, from raw data ingestion to executive visualization of model error.

The core of the project is the implementation of a Logarithmic Regression model to predict the critical business variable: the number of products sold per transaction (`Quantity`).

### Executive Conclusions

* **Final Model**: A Linear Regression model with Logarithmic transformation was implemented for the dependent variable (`Quantity`).

* **Error Diagnosis (Heteroscedasticity)**: The prediction error is ten times greater for Large Sales transactions (`>20 units`) than for Small Sales (1-5 units). The model is inconsistent and is only reliable for estimating low volumes.

* **Geographic Bias**: The model is inefficient and registers an extremely high Mean Absolute Error (MAE) in Sweden, suggesting an atypical purchasing pattern in that region that the overall model cannot capture.

---

## 2. Technologies Used

|Category | Tools and Languages | Purpose |
| :--- | :--- | :--- |
| **Data Ingestion and Processing** | Python, Pandas, NumPy | Data cleaning, feature engineering, and transformation. |
| **Machine Learning** | Scikit-learn (Linear Regression) | Predictive model creation and training. |
| **Data Persistence** | PostgreSQL, psycopg2 | Secure storage of the cleaned dataset and predictions. |
| **Executive Visualization** | Power BI, DAX | Post-prediction error analysis for business insights. |
| **Security** | `.gitignore`, `config.py` | Secure database credential management. |

---

## 3. Key Results and Visualizations:

The main findings come from the analysis of the residuals of the Logarithmic Regression model.

### Matplotlib Charts: Prediction and Residual Distribution

* **Files**: `assets/dispersion_cantidad.png` and `assets/residuos_cantidad.png`
* **Purpose**: To visually confirm the overall alignment of the predictions and the distribution of errors generated in Python.

![Quantity Dispersion](assets/dispersion_cantidad.png)
![Residual Quantity](assets/residuos_cantidad.png)

### Power BI Chart 1: Model Diagnostics

**Title: Average MAE by Quantity Range**

This chart confirms heteroscedasticity. The Large Sale bar (`Venta Grande`) shows that the error spikes in high-value transactions, a critical weakness of the model.

![Average MAE by Quantity Range](assets/MAE_rango.png)

### Power BI Chart 2: Geographic Bias

**Title: Average Error Performance (MAE) by Country**

This horizontal bar chart reveals that the MAE in Sweden (*Suecia*) is abnormally high, suggesting that the sales characteristics in that country do not fit the global model.

![MAE by Country](assets/MAE_pais.png)

---

## 4. Procedure and Methodology

The project was executed following a 4-phase pipeline:

1. **PHASE 1: Cleaning and Feature Engineering**: Loading the CSV file, cleaning null and outlier values, and creating categorical (e.g., `DiaSemana`) and numeric (e.g., `ValorTotal`) variables.
2. **PHASE 2: Secure Persistence**: Using `config.py` and the `copy_from` method of `psycopg2` to perform a secure bulk (CRUD) load of the cleaned dataset (`retail_clean`) into PostgreSQL.
3. **PHASE 3: Modeling (Logimic Regression)**: Applying the logarithmic transformation (`np.log1p`) to the dependent variable `Quantity` to mitigate skewness, training the linear regression model, and reversing the transformation (`np.expm1`) for the final prediction.
4. **PHASE 4: Export and Executive Visualization**: Generation of the `ecommerce_predicciones_bi.csv` file with predictions and residuals, and detailed analysis in Power BI.

---

## 5. Project Structure

```bash
Proyecto_12_Predicciones_ecommerce/
├── assets/
│   ├── dispersion_cantidad.png    
│   ├── residuos_cantidad.png     
│   ├── MAE_rango.png             
│   └── MAE_pais.png   
├── config.py # Secure credentials for PostgreSQL (IGNORED)
├── citacion.txt # Dataset citation file
├── .gitignore # Ignores sensitive (config.py) and large (datasets) files
├── online_retail.csv # Original dataset IGNORED
├── ecommerce_base.sql # Definition from the database (DB) and table (DDL)
├── ecommerce.py # Main script (Cleaning, ML, Persistence, Export)
├── ecommerce_predicciones_bi.csv # Output data with predictions and residuals for BI (IGNORED)
└── README.md # Project documentation
```

---

## 6. Conclusions

The project demonstrated the ability to build a complete predictive pipeline. The use of Logarithmic Regression improved the overall metric and MAE for most of the data, but the visualizations in Power BI revealed that the model remains vulnerable to Heteroscedasticity (large sales) and Geographic Bias (Sweden). Future improvements should focus on more robust models (e.g., Random Forest) or on segmenting the model by country.

---

## 7. Dataset Citation

The dataset used in this project is:

UCI Machine Learning Repository. (2020). Online Retail II. Retrieved from https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

---
