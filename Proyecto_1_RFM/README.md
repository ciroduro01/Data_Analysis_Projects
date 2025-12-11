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
└── Proyecto_1_RFM/
   ├── online_retail.py                  # Script principal de Python (Análisis RFM).
   ├── Matplotlib_Proyecto_1_Distribucion_RFM.jpg       # Visualización de la distribución de segmentos.
   ├── README.md                         # Descripción del proyecto (este archivo).
   ├── Citación_Proyecto_N°1_dataset.txt # Fuente de datos citada.
   └── online_retail.csv                 # Archivo de datos de entrada (no subido al repo por tamaño).

```

---

## Conclusiones

La alta proporción de clientes en el segmento **"Dormidos/Perdidos"** subraya la necesidad de implementar campañas de reactivación dirigidas a estos usuarios, quizás a través de descuentos por tiempo limitado o encuestas para entender la razón del abandono. Por otro lado, los segmentos **"Campeones/Leales"** deben ser recompensados con programas VIP o acceso anticipado a productos para asegurar su retención y maximizar su valor a largo plazo.

---
