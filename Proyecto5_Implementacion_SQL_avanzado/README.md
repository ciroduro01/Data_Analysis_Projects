# Proyecto N°5: Implementación y Consultas Analíticas Avanzadas (SQL)

## Objetivo del Proyecto
El objetivo principal de este proyecto es validar la funcionalidad y demostrar el valor analítico del esquema de base de datos **`manufactura_db`** (diseñado en el Proyecto N°4) a través de la implementación de datos coherentes y la creación de consultas SQL avanzadas.

El proyecto se enfoca en responder preguntas de negocio cruciales para un gerente de manufactura, como el costeo de productos y la evaluación de la cadena de suministro.

---

## Metodología y Fases

El proyecto se dividió en dos fases puramente SQL para la validación del esquema:

### Fase 1: Implementación de Datos

Se crearon sentencias `INSERT INTO` para poblar todas las tablas del esquema, asegurando la **integridad referencial** que fue diseñada con las claves foráneas (FK).

* **`01_inserts_maestras.sql`**: Inserta datos iniciales en las tablas `SUBCONTRACTOR`, `MATERIAL` y `CUSTOMER`.
* **`02_inserts_transaccionales.sql`**: Inserta datos en las tablas de hechos (`ORDER_HEADER`, `ORDER_DETAIL`, `PRODUCT`) y la tabla de relación `PRODUCT_HAS_MATERIAL` (Lista de Materiales - BOM).

### Fase 2: Consultas Analíticas Avanzadas

Se desarrollaron tres consultas clave para extraer información de negocio, utilizando `JOIN`s múltiples, agregaciones (`SUM`, `COUNT`) y Common Table Expressions (CTE).

---

## Consultas Analíticas Clave

El archivo `03_consultas_analiticas.sql` contiene las siguientes consultas:

### Consulta 1: Cálculo del Costo Total de Materiales por Unidad de Producto
* **Propósito:** Determinar el costo base de materiales de cada producto (el *Roll-up Cost*).
* **Lógica SQL:** Utiliza `JOIN`s entre `PRODUCT`, `PRODUCT_HAS_MATERIAL` y `MATERIAL` para multiplicar la `QuantityRequired` por el `UnitCost` y agregarlo (`SUM`) por `ProductID`.
* **Valor de Negocio:** Permite establecer el margen de ganancia y optimizar la compra de materiales.

### Consulta 2: Costo Total de Materiales Requeridos por Orden
* **Propósito:** Calcular el costo total de materiales que se debe invertir para cumplir una orden de cliente completa.
* **Lógica SQL:** Emplea una **CTE** (`ProductoCosto`) para reutilizar el costo por unidad (de la Consulta 1) y luego lo multiplica por la `QuantityOrdered` en la tabla `ORDER_DETAIL`, uniendo el resultado a `ORDER_HEADER` y `CUSTOMER`.
* **Valor de Negocio:** Permite una cotización rápida y precisa de los costos de producción por pedido.

### Consulta 3: Análisis de la Dependencia de Subcontratistas
* **Propósito:** Identificar el volumen de órdenes que dependen de cada subcontratista, evaluando el riesgo en la cadena de suministro.
* **Lógica SQL:** Utiliza `JOIN`s complejos entre `SUBCONTRACTOR`, `PRODUCT` y `ORDER_DETAIL`, empleando `COUNT(DISTINCT od.OrderID)` para contar las órdenes únicas asociadas a los productos de cada subcontratista.
* **Valor de Negocio:** Informa decisiones sobre negociaciones con proveedores y planes de mitigación de riesgos.

---

## Estructura del Repositorio

La siguiente estructura garantiza la ejecución ordenada de la base de datos:

```

Proyecto5_Implementacion_SQL_avanzado/
├── 01_inserts_maestras.sql           # Datos iniciales para tablas dimensionales
├── 02_inserts_transaccionales.sql    # Datos para órdenes, productos y listas de materiales
└── 03_consultas_analiticas.sql       # Consultas SQL analíticas de alto valor (Fase 2)
└── README.md                         # Documentación del proyecto

```

---
