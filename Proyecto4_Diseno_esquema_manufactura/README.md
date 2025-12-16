# Proyecto N°4: Diseño y Normalización de Esquema para Manufactura

## Objetivo del Proyecto
El objetivo de este proyecto es diseñar y normalizar un esquema de base de datos relacional (Modelo Entidad-Relación) para gestionar los procesos centrales de una pequeña empresa de manufactura: **Pedidos (Órdenes), Clientes, Productos, Subcontratistas y Materiales de Producción**.

El diseño se enfoca en alcanzar la Tercera Forma Normal (3NF) para asegurar la integridad de los datos, minimizar la redundancia y facilitar el análisis transaccional.

---

## Estructura del Esquema (`manufactura_db`)

El esquema se divide en tres tipos de tablas, como se visualiza en el Diagrama Entidad-Relación (DER):

![Diagrama Entidad-Relación del Esquema Manufactura](assets/manufactura_db.png)

### Tablas Maestras (Dimensiones)
| Tabla | Propósito | Clave Primaria (PK) |
| :--- | :--- | :--- |
| **CUSTOMER** | Almacena la información de contacto de los clientes. | `CustomerID` |
| **SUBCONTRACTOR** | Almacena datos de las empresas externas que fabrican o procesan productos. | `SubcontractorID` |
| **MATERIAL** | Almacena todos los componentes necesarios para la producción, con su costo unitario. | `MaterialID` |

### Tabla de Hechos (Transaccional)
| Tabla | Propósito | Relaciones Clave |
| :--- | :--- | :--- |
| **ORDER_HEADER** | Encabezado de la orden (Fecha, estado). | Relacionada 1:M con **CUSTOMER**. |
| **ORDER_DETAIL** | Resuelve la relación M:N entre Órdenes y Productos. | Relacionada M:N con **ORDER_HEADER** y **PRODUCT**. |

### Tablas de Relación
| Tabla | Propósito | Clave Primaria Compuesta |
| :--- | :--- | :--- |
| **PRODUCT** | Almacena los bienes finales. Incluye una FK para el subcontratista asociado. | `ProductID` (FK a **SUBCONTRACTOR**). |
| **PRODUCT_HAS_MATERIAL** | **Lista de Materiales (BOM - Bill of Materials)**. Define qué materiales y qué cantidad se requieren para cada producto. | Compuesta: `(ProductID, MaterialID)` |

---

## Consideraciones de Normalización (3NF)

El diseño cumple con los requisitos de normalización para asegurar la integridad de las transacciones:

* **Integridad Referencial:** Todas las tablas transaccionales tienen claves foráneas (FK) que apuntan a las tablas maestras, garantizando que no se puedan ingresar órdenes, materiales o productos que no existan.
* **Resolución de M:N:** Las relaciones Muchos-a-Muchos se resuelven mediante tablas intermedias (o tablas de enlace):
    * `ORDER_DETAIL` une `ORDER_HEADER` y `PRODUCT`.
    * `PRODUCT_HAS_MATERIAL` une `PRODUCT` y `MATERIAL`.
* **Ausencia de Redundancia:** Datos como el `CustomerName` o `SubcontractorName` solo existen en sus respectivas tablas maestras, evitando la duplicación en miles de filas de órdenes.

---

## Archivos del Proyecto
```
Proyecto4_Diseno_esquema_manufactura/
├── assets/
│   └── manufactura_db.png      # Diagrama Entidad-Relación (DER)
├── Estructura_Proyecto N°4.sql   # Sentencias CREATE TABLE (Lógica del diseño)
└── README.md                            # Documentación del proyecto
```

---

# Project N°4: Design and Standardization of a Manufacturing Schema

## 1. Project Objective

The objective of this project is to design and standardize a relational database schema (Entity-Relationship Model) to manage the core processes of a small manufacturing company: Orders, Customers, Products, Subcontractors, and Production Materials.

The design focuses on achieving Third Normal Form (3NF) to ensure data integrity, minimize redundancy, and facilitate transactional analysis.

---

## 2. Schema Structure (`manufactura_db`)

The schema is divided into three types of tables, as shown in the Entity-Relationship Diagram (ERD):

![Manufactura schema ERD Diagram](assets/manufactura_db.png)

### Master Tables (Dimensions)
| Table | Purpose | Primary Key (PK) |
| :--- | :--- | :--- |
| **CUSTOMER** | Stores customer contact information. | `CustomerID` |
| **SUBCONTRACTOR** | Stores data for external companies that manufacture or process products. | `SubcontractorID` |
| **MATERIAL** | Stores all components necessary for production, with their unit cost. | `MaterialID` |

### Facts Table (Transactional)
| Table | Purpose | Key Relationships |
| :--- | :--- | :--- |
| **ORDER_HEADER** | Order header (Date, status). | 1:M related to **CUSTOMER**. |
| **ORDER_DETAIL** | Resolves the M:N relationship between Orders and Products. | M:N related to **ORDER_HEADER** and **PRODUCT**. |

### Relationship Tables
| Table | Purpose | Composite Primary Key |
| :--- | :--- | :--- |
| **PRODUCT** | Stores finished goods. | Includes a foreign key for the associated subcontractor. | `ProductID` (Foreign Key to SUBCONTRACTOR). |
| **PRODUCT_HAS_MATERIAL** | Bill of Materials (BOM). Defines which materials and quantities are required for each product. | Composite: (`ProductID`, `MaterialID`) |

---

## 3. Normalization Considerations (3NF)

The design complies with normalization requirements to ensure transaction integrity:

* **Referential Integrity**: All transaction tables have foreign keys (FK) that point to the master tables, guaranteeing that orders, materials, or products that do not exist cannot be entered.
* **Many-to-Many Resolution**: Many-to-many relationships are resolved using intermediate tables (or linking tables):
* `ORDER_DETAIL` links `ORDER_HEADER` and `PRODUCT`.
* `PRODUCT_HAS_MATERIAL` links `PRODUCT` and `MATERIAL`.
* **No Redundancy**: Data such as `CustomerName` or `SubcontractorName` only exists in their respective master tables, preventing duplication across thousands of order rows.

---

## 4. Project Files

```bash
Proyecto4_Diseno_esquema_manufactura/
├── assets/
│   └── manufactura_db.png  # Entity-Relationship Diagram (ERD)
├── Estructura_Proyecto N°4.sql # CREATE TABLE Statements (Design Logic)
└── README.md # Project Documentation
```
