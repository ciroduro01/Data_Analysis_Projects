# Proyecto N°11: Análisis de Sentimientos en Reseñas de Películas (IMDB)

## Objetivos y Resumen Ejecutivo

Este proyecto implementa una solución completa de **Machine Learning (ML)** y **Procesamiento de Lenguaje Natural (NLP)** sobre 50,000 reseñas de películas. El objetivo fue construir un clasificador robusto (**Regresión Logística** con **Tf-idf**), asegurar la persistencia de los resultados en **PostgreSQL** y validar el rendimiento del modelo mediante la visualización de la distribución y la confianza de las predicciones en **Power BI**.

| Métrica | Valor Clave |
| :--- | :--- |
| **Dataset Base** | 50,000 Reseñas (IMDB) |
| **Modelo Principal**| Regresión Logística |
| **Balance de Salida** | 49,2% Positivo / 50,8% Negativo |
| **Persistencia** | PostgreSQL (Tabla `resultados_prediccion`) |

## Tecnologías Utilizadas

* **Lenguajes:** Python (versión 3.x), SQL (PostgreSQL).
* **Librerías ML/NLP:** Scikit-learn (Regresión Logística, Tf-idf), NLTK, Pandas, NumPy.
* **Base de Datos:** PostgreSQL (`psycopg2`).
* **Visualización:** Matplotlib, Seaborn, y **Power BI**.
* **Seguridad:** Uso de **`config.py`** para el manejo seguro de credenciales de BD.

## Resultados Clave y Visualizaciones

### Gráficos Ejecutivos (Power BI)

#### Distribución Final de Sentimientos Predichos

* **Hallazgo:** Muestra un balance perfecto, de aproximadamente **49,2% Positivo / 50,8% Negativo**, confirmando la solidez del modelo al mantener la distribución del dataset original.
![Sentimientos Predichos (Power BI)](assets/sentimientos_predichos.png)

#### Volumen de Reseñas por Rango de Confianza

* **Hallazgo Clave:** El volumen se concentra en los extremos (alta confianza), con una baja representación en el rango central (40-60%). Esto indica que el modelo es **altamente decisivo** y encuentra pocas reseñas ambiguas.
![Rango de Confianza (Power BI)](assets/rango_confianza.png)

### Gráficos de Validación (Matplotlib)

* **Matriz de Confusión:** Valida la precisión del modelo al comparar aciertos (True Positives, True Negatives) y errores (False Positives, False Negatives).
![Matriz de Confusión](assets/Matriz_Confusion.png)

* **Distribución de Sentimientos:** Muestra el conteo de predicciones 0 (Negativo) y 1 (Positivo).
![Distribución de Sentimientos](assets/Distribucion_Sentimientos.png)

## Procedimiento y Metodología

1.  **Limpieza (NLP):** El script `sentimientos.py` utiliza la función `limpiar_texto` para la remoción de etiquetas HTML, *stopwords* y puntuación, esencial para la calidad del análisis de texto.
2.  **Vectorización:** El texto limpio se transforma en características numéricas mediante el **Tf-idf Vectorizer**.
3.  **Modelado:** Se utiliza la **Regresión Logística** para la clasificación binaria de sentimientos.
4.  **Persistencia:** La función `insertar_resultados()` guarda el `Texto_Original`, el `Sentimiento_Predicho` y la `Probabilidad_Positiva` en la tabla **`resultados_prediccion`** de PostgreSQL, utilizando los parámetros de **`config.py`** de forma segura.

## Estructura del Proyecto

La carpeta `Proyecto_11_Sentimientos_peliculas` contiene los siguientes archivos:

| Archivo/Carpeta | Propósito | Notas de Ingeniería de Datos |
| :--- | :--- | :--- |
| `sentimientos.py` | Código fuente principal. | Implementa el flujo ETL y el entrenamiento del modelo. |
| `config.py` | Configuración de la BD. | **EXCLUIDO** en `.gitignore` por seguridad. |
| `IMDB_Dataset.csv` | Dataset Original. | **EXCLUIDO**. |
| `sentimientos_predichos_bi.csv`| Datos de Salida. | **EXCLUIDO**. |
| `assets/` | Gráficos y Esquemas. | Contiene todos los archivos `.png` (Matplotlib, DBeaver, Power BI). |
| `.gitignore` | Control de Versiones. | **Excluye** `config.py` y archivos de formato .csv. |

## Conclusiones

El Proyecto N°11 fue un éxito en la implementación completa de un flujo de trabajo de Ciencia de Datos:

1.  **Seguridad:** Se garantiza la seguridad de las credenciales de PostgreSQL mediante el uso de `config.py`.
2.  **Rendimiento del Modelo:** Los gráficos de confianza en Power BI confirman que el modelo es altamente predictivo y decisivo.
3.  **Integración:** Se demostró la capacidad de llevar los resultados del Machine Learning a una base de datos relacional y, posteriormente, a una herramienta de Business Intelligence para el análisis ejecutivo.

## Citación

**Citación del Proyecto N°11 (Sentimientos de Reseñas de Películas)**

* **Dataset:** IMDB Movie Reviews
* **Fuente:** El dataset fue descargado de: [https://www.kaggle.com/datasets/vishakhdapat/imdb-movie-reviews](https://www.kaggle.com/datasets/vishakhdapat/imdb-movie-reviews)
* **Licencia:** MIT.

---

# Project N°11: Sentiment Analysis of Movie Reviews (IMDB)

## 1. Objectives and Summary

This project implements a complete Machine Learning (ML) and Natural Language Processing (NLP) solution on 50,000 movie reviews. The objective was to build a robust classifier (Logistic Regression with Tf-idf), ensure the persistence of results in PostgreSQL, and validate the model's performance by visualizing the distribution and confidence of the predictions in Power BI.

| Metric | Key Value |
| :--- | :--- |
| **Original Dataset** | 50,000 Reviews (IMDB) |
| **Main Model** | Logistic Regression |
| **Output Balance** | 49.2% Positive / 50.8% Negative |
| **Persistence** | PostgreSQL (`resultados_prediccion` Table) |

---

## 2. Technologies Used

* **Languages**: Python (version 3.x), SQL (PostgreSQL).
* **ML/NLP Libraries**: Scikit-learn (Logistic Regression, TF-IDF), NLTK, Pandas, NumPy.
* **Database**: PostgreSQL (psycopg2).
* **Visualization**: Matplotlib, Seaborn, and Power BI.
* **Security**: Use of `config.py` for secure handling of database credentials.

---

## 3. Key Results and Visualizations

### Executive Charts (Power BI)

#### Final Distribution of Predicted Sentiment

* **Key Finding**: Shows a perfect balance, approximately 49.2% Positive / 50.8% Negative, confirming the robustness of the model by maintaining the distribution of the original dataset.

![Predicted Sentiment](assets/sentimientos_predichos.png)

#### Review Volume by Confidence Range

* **Key Finding**: The volume is concentrated at the extremes (high confidence), with low representation in the central range (40-60%). This indicates that the model is highly decisive and finds few ambiguous reviews.

![Confidence Range (Power BI)](assets/rango_confianza.png)

### Validation Plots (Matplotlib)

* **Confusion Matrix**: Validates the model's accuracy by comparing hits (True Positives, True Negatives) and errors (False Positives, False Negatives).

![Confusion Matrix](assets/Matriz_Confusion.png)

* **Sentiment Distribution**: Shows the count of 0 (Negative) and 1 (Positive) predictions.

![Sentiment Distribution](assets/Distribucion_Sentimientos.png)

---

## 4. Procedure and Methodology

1. **Cleaning (NLP)**: The `sentimientos.py` script uses the `limpiar_texto` function to remove HTML tags, stopwords, and punctuation, which is essential for the quality of the text analysis.
2. **Vectorization**: The cleaned text is transformed into numerical features using the Tf-idf Vectorizer.
3. **Modeling**: Logistic Regression is used for binary sentiment classification.
4. **Persistence**: The `insertar_resultados()` function securely saves the `Texto_Original`, `Sentimiento_Predicho`, and `Probabilidad_Positiva` to the `resultados_prediccion` table in PostgreSQL, using the parameters from `config.py`.

---

## 5. Project Structure

The `Proyecto_11_Sentimientos_peliculas` folder contains the following files:

| File/Folder | Purpose | Data Engineering Notes |
| :--- | :--- | :--- |
| `sentimientos.py` | Main source code. | Implements the ETL flow and model training. |
| `config.py` | Database configuration. | EXCLUDED in `.gitignore` for security. |
| `IMDB_Dataset.csv` | Original dataset. | EXCLUDED. |
| `sentimientos_predichos_bi.csv` | Output data. | EXCLUDED. |
| `assets/` | Graphs and Schemas. | Contains all `.png` files (Matplotlib, Power BI). |
| `.gitignore` | Version Control. | Excludes `config.py` and `.csv` files. |

---

## 6. Conclusions

Project 11 was a success in the complete implementation of a Data Science workflow:

1. **Security**: The security of PostgreSQL credentials is ensured through the use of `config.py`.
2. **Model Performance**: Confidence charts in Power BI confirm that the model is highly predictive and decisive.
3. **Integration**: The ability to bring Machine Learning results to a relational database and subsequently to a Business Intelligence tool for executive analysis was demonstrated.

---

## 7. Citation

Citation of Project 11 (Movie Review Sentiments)

Dataset: IMDB Movie Reviews
Source: The dataset was downloaded from: https://www.kaggle.com/datasets/vishakhdapat/imdb-movie-reviews
License: MIT.

---
