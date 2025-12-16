# Proyecto N°6: Dashboard de Business Intelligence con Power BI

## Objetivo del Proyecto
El objetivo de este proyecto es llevar las conclusiones de las consultas analíticas de SQL (Proyecto N°5) a un **dashboard visual y ejecutivo** utilizando Power BI. Este proyecto valida la capacidad de transformar datos brutos de la base de datos `manufactura_db` en información estratégica para la toma de decisiones gerenciales.

---

## Metodología y Conexión

La visualización se construyó conectando Power BI directamente al servidor de base de datos **PostgreSQL** para consumir los resultados de las consultas.

### Estructura del Esquema
El análisis se basa en el esquema relacional normalizado de la base de datos `manufactura_db`:

![Diagrama Entidad-Relación del Esquema Manufactura](assets/manufactura_db_esquema.png)

---

## Visualizaciones Clave

Las tres visualizaciones principales responden directamente a las necesidades de la gerencia de manufactura y demuestran el valor de un esquema normalizado:

### Costo Base de Materiales por Unidad de Producto (Roll-up)
Este gráfico de barras visualiza la métrica de costeo de materiales, un insumo clave para la fijación de precios:

![Costo Base de Materiales por Unidad de Producto (Roll-up)](assets/costo_producto.png)

* **Conclusión Clave:** La `Estructura Modular Acero` es, por mucho, el producto con el costo de material más alto, lo que dirige la atención a la optimización de la compra de su principal componente.

### Total de Costos de Materiales Comprometidos por Orden
Este gráfico de columnas muestra el costo total de materiales que la empresa debe invertir para cumplir con los pedidos:

![Total de Costos de Materiales Comprometidos por Orden](assets/costo_orden.png)

* **Conclusión Clave:** La orden con el costo de materiales comprometido más alto corresponde a **EcoHome Builders** y **Fitness Gears Inc.**, identificando los pedidos que requieren la mayor inversión de capital.

### Volumen de Órdenes que Dependen de Cada Subcontratista
Este gráfico de anillo evalúa el riesgo en la cadena de suministro al cuantificar cuántas órdenes dependen de cada proveedor externo:

![Volumen de Órdenes que Dependen de Cada Subcontratista](assets/dependencia_sc.png)

* **Conclusión Clave:** El análisis revela una dependencia crítica del proveedor **Componentes Eléctricos Z** (40% de las órdenes), un hallazgo vital para la gestión de riesgos y la negociación con proveedores.

---

## Estructura del Repositorio

```

Proyecto6_Visualizacion_PowerBI/
├── assets/
│   ├── manufactura_db_esquema.png      # Esquema de la Base de Datos manufactura_db
│   ├── costo_producto.png              # Gráfico 1: Costo Unitario
│   ├── costo_orden.png                 # Gráfico 2: Costo por Orden
│   └── dependencia_sc.png              # Gráfico 3: Dependencia de Subcontratistas
└── README.md                           # Documentación del proyecto

````

---

# Project N°6: Business Intelligence Dashboard with Power BI

## 1. Project Objective

The objective of this project is to translate the findings from the SQL analytical queries (Project 5) into a visual and executive-level dashboard using Power BI. This project validates the ability to transform raw data from the `manufactura_db` database into strategic information for managerial decision-making.

---

## 2. Methodology and Connection

The visualization was built by connecting Power BI directly to the PostgreSQL database server to consume the query results.

### Schema Structure

The analysis is based on the normalized relational schema of the `manufactura_db` database:

![Manufactura schema ERD Diagram](assets/manufactura_db_esquema.png)

---

## 3. Key Visualizations

The three main visualizations directly address the needs of manufacturing management and demonstrate the value of a normalized schema:

### Base Material Cost per Unit of Product (Roll-up)
This bar chart visualizes the material costing metric, a key input for pricing:

![Base Material Cost per Unit of Product (Roll-up)](assets/costo_producto.png)

* **Key Conclusion**: The `Estructura Modular Acero` (*Modular Steel Structure*) is by far the product with the highest material cost, directing attention to optimizing the purchase of its main component.

### Total Committed Material Costs per Order
This column chart shows the total material cost the company must invest to fulfill orders:

![Total Committed Material Costs per Order](assets/costo_orden.png)

* **Key Conclusion**: The order with the highest committed material cost corresponds to **EcoHome Builders** and **Fitness Gears Inc.**, identifying the orders that require the greatest capital investment.

### Volume of Orders Dependent on Each Subcontractor
This pie chart assesses supply chain risk by quantifying how many orders depend on each external supplier:

![Volume of Orders Dependent on Each Subcontractor](assets/dependencia_sc.png)

* **Key Finding**: The analysis reveals a critical dependence on the supplier **Electrical Components Z** (40% of orders), a vital finding for risk management and supplier negotiations.

---

## 4. Repository Structure

```bash
Proyecto6_Visualizacion_PowerBI/
├── assets/
│ ├── manufactura_db_esquema.png # Database Schema for manufactura_db
│ ├── costo_producto.png # Chart 1: Unit Cost
│ ├── costo_orden.png # Chart 2: Cost per Order
│ └── dependencia_sc.png # Chart 3: Subcontractor Dependencies
└── README.md # Project Documentation
```

---
