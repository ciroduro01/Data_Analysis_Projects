# Proyecto N°1: Análisis de Segmentación de Clientes ~ Online Retail de E-Commerce (RFM)

---

## Objetivos y Resumen

* **Objetivos:**
    1.  Implementar el modelo de segmentación de clientes RFM (Recency, Frequency, Monetary) para un negocio de venta minorista en línea.
    2.  Clasificar a los clientes en segmentos de negocio accionables (Campeones, En Riesgo, Perdidos, etc.).
    3.  Obtener *insights* clave sobre el comportamiento de compra para optimizar futuras estrategias de marketing y retención.

* **Resumen:**
    Este proyecto se centró en el preprocesamiento de un gran *dataset* transaccional de *Online Retail* y la aplicación del análisis RFM para la segmentación. El análisis reveló que la **mayoría de los clientes (3,630)** se encuentran en el segmento **"Dormidos/Perdidos"**, lo que indica una alta tasa de abandono o clientes de compra única, mientras que los clientes más valiosos (Campeones/Leales) representan una minoría que requiere estrategias de retención específicas.

---

## Tecnologías Utilizadas

Las herramientas y librerías clave utilizadas en este análisis son:

* **Lenguaje de Programación:** Python
* **Librerías de Análisis:** Pandas (para manipulación y cálculo de RFM), NumPy
* **Visualización:** Matplotlib, Seaborn (para el gráfico de distribución de segmentos)

---

## Resultados Clave y Visualizaciones

La segmentación RFM se realizó utilizando el método de cuantiles (quintiles) para asignar puntuaciones de 1 a 5, generando un score compuesto para clasificar a los clientes.

| Segmento RFM | R-Score (Recencia) | F-Score (Frecuencia) | M-Score (Monetario) | Conteo de Clientes |
| :--- | :---: | :---: | :---: | :---: |
| **05 - Dormidos/Perdidos** | Bajo (1, 2) | Bajo (1, 2) | Bajo/Medio | **3,630** |
| **01 - Campeones/Leales** | Alto (4, 5) | Alto (4, 5) | Alto/Medio | 879 |
| **03 - Clientes Potenciales** | Medio (3) | Alto (3, 4) | Alto/Medio | 746 |

## Distribución de Clientes por Segmento RFM

La siguiente visualización, generada por Matplotlib/Seaborn, muestra la distribución de los 5,878 clientes únicos totales:

![Distribución de Clientes por Segmento RFM](Matplotlib_Proyecto_1_Distribucion_RFM.jpg)

Fuente de Datos: UCI Machine Learning Repository. (2020). Online Retail II. Obtenido de https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

---

## Metodología (Procedimiento y Fases)

Este análisis se llevó a cabo siguiendo las siguientes fases:

1.  **Fase 1: Adquisición y Limpieza de Datos:**
    * Carga del dataset `online_retail.csv`. **(Fuente: UCI Machine Learning Repository. (2020). Online Retail II)**
    * Eliminación de valores nulos en la columna `Customer ID`.
    * Conversión de `InvoiceDate` a formato `datetime` y `Customer ID` a formato `int`.
    * Cálculo de la columna de ingresos (`Sales = Quantity * Price`).
    * Filtrado de transacciones no válidas (donde `Quantity <= 0` o `Price <= 0`).
2.  **Fase 2: Cálculo de Métricas RFM:**
    * Se estableció la **Fecha de Referencia** un día después de la última fecha de compra registrada (`InvoiceDate.max() + 1 día`).
    * **Recencia (R):** Días transcurridos desde la última compra hasta la Fecha de Referencia.
    * **Frecuencia (F):** Número de facturas únicas por cliente.
    * **Monetario (M):** Suma total de los ingresos (`Sales`) por cliente.
3.  **Fase 3: Asignación de Puntuaciones y Segmentación:**
    * Se aplicó la función `pd.qcut` (quintiles) para asignar puntuaciones de 1 a 5 a R, F y M. **(Nota: R se invirtió, 5 es la menor recencia).**
    * Se creó el **Segmento RFM** concatenando R y F (ej. '55').
    * Se definió una función `asignar_segmento` para mapear los valores de `RFM_Segment` a los 5 segmentos de negocio finales.

---

## Estructura de los Archivos

La estructura del directorio para este proyecto es la siguiente:

```

Data_Analysis_Projects/
└── Proyecto1_RFM/
   ├── online_retail.py                  # Script principal de Python (Análisis RFM).
   ├── Matplotlib_Proyecto_1_Distribucion_RFM.jpg       # Visualización de la distribución de segmentos.
   ├── README.md                         # Descripción del proyecto (este archivo).
   ├── Citación_Proyecto_N°1_dataset.txt # Fuente de datos citada.
   └── online_retail.csv                 # Archivo de datos de entrada (no subido al repo por tamaño). IGNORADO

```

---

## Conclusiones

La alta proporción de clientes en el segmento **"Dormidos/Perdidos"** subraya la necesidad de implementar campañas de reactivación dirigidas a estos usuarios, quizás a través de descuentos por tiempo limitado o encuestas para entender la razón del abandono. Por otro lado, los segmentos **"Campeones/Leales"** deben ser recompensados con programas VIP o acceso anticipado a productos para asegurar su retención y maximizar su valor a largo plazo.

---

# Project N°1: Customer Segmentation Analysis ~ Online Retail E-Commerce (RFM)

---

## 1. Objectives and Summary

**Objectives**:

1. Implement the RFM (Recency, Frequency, Monetary) customer segmentation model for an online retail business.
2. Classify customers into actionable business segments (Champions, At Risk, Lost, etc.).
3. Gain key insights into purchasing behavior to optimize future marketing and retention strategies.

**Summary**: This project focused on preprocessing a large transactional dataset from Online Retail and applying RFM analysis for segmentation. The analysis revealed that the majority of customers (3,630) are in the "Dormant/Lost" segment, indicating a high churn rate or one-time purchase customers, while the most valuable customers (Champions/Loyal) represent a minority requiring specific retention strategies.

---

## 2. Technologies and Tools Used

The key tools and libraries used in this analysis are:

* **Programming Language**: Python
* **Analysis Libraries**: Pandas (for RFM manipulation and calculation), NumPy
* **Visualization**: Matplotlib, Seaborn (for the segment distribution graph)

---

## 3. Key Results and Visualizations

RFM segmentation was performed using the quantile (quintile) method to assign scores from 1 to 5, generating a composite score to classify customers.

| RFM Segment | R-Score (Recency) | F-Score (Frequency) | M-Score (Monetary) | Customer Count |
| :--- | :--- | :--- | :--- | :--- |
| **05 - Dormant/Lost** | Low (1, 2) | Low (1, 2) | Low/Medium | 3,630 |
| **01 - Champions/Loyal** | High (4, 5) | High (4, 5) | High/Medium | 879 |
| **03 - Potential Customers** | Medium (3) | High (3, 4) |High/Medium | 746 |

## 4. Customer Distribution by RFM Segment

The following visualization, generated by Matplotlib/Seaborn, shows the distribution of the 5,878 total unique customers:

![Customer Distribution by RFM Segment](Matplotlib_Proyecto_1_Distribucion_RFM.jpg)

Data Source: UCI Machine Learning Repository. (2020). Online Retail II. Retrieved from https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

---

## 5. Methodology (Procedure and Phases)

This analysis was carried out following these phases:

1. **Phase 1: Data Acquisition and Cleaning**:
* Loading the `online_retail.csv` dataset. (Source: UCI Machine Learning Repository. (2020). Online Retail II)
* Removal of null values ​​in the `Customer ID` column.
* Conversion of `InvoiceDate` to `datetime` format and `Customer ID` to `int` format.
* Calculation of the revenue column (`Sales = Quantity * Price`).
* Filtering of invalid transactions (where `Quantity <= 0` or `Price <= 0`).
2. **Phase 2: Calculation of RFM Metrics**:
* The Reference Date was set to one day after the last recorded purchase date (`InvoiceDate.max() + 1 día`).
* Recency (R): Days elapsed since the last purchase to the Reference Date.
* Frequency (F): Number of unique invoices per customer.
* Monetary (M): Total revenue (`Sales`) per customer.
3. **Phase 3: Scoring and Segmentation**:
* The `pd.qcut` (quintiles) function was applied to assign scores from 1 to 5 to R, F, and M. (Note: R was inverted; 5 is the lowest recency.)
* The RFM Segment was created by concatenating R and F (e.g., '55').
* An `asignar_segmento` function was defined to map the `RFM_Segment` values ​​to the final 5 business segments.

---

## 6. File Structure

The directory structure for this project is as follows:

```bash
Data_Analysis_Projects/
└── Proyecto1_RFM/
   ├── online_retail.py # Main Python script (RFM Analysis).
   ├── Matplotlib_Proyecto_1_Distribucion_RFM.jpg  # Visualization of the segment distribution.
   ├── README.md       # Project description (this file).
   ├── Citación_Proyecto_N°1_dataset.txt # Cited data source.
   └── online_retail.csv         # Input data file (not uploaded to the repository due to size). IGNORED
```

---

## 7. Conclusions
The high proportion of customers in the **"Dormant/Lost"** segment underscores the need to implement reactivation campaigns targeting these users, perhaps through limited-time discounts or surveys to understand the reasons for abandonment. On the other hand, the **"Champion/Loyal"** segments should be rewarded with VIP programs or early access to products to ensure their retention and maximize their long-term value.
