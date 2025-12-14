--Creamos la Base de Datos
CREATE DATABASE manufactura_db;
-- Tabla: CUSTOMER
CREATE TABLE CUSTOMER (
    CustomerID VARCHAR(10) PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerAddress VARCHAR(255),
    CustomerEmail VARCHAR(100) UNIQUE
);

-- Tabla: SUBCONTRACTOR
CREATE TABLE SUBCONTRACTOR (
    SubcontractorID VARCHAR(10) PRIMARY KEY,
    SubcontractorName VARCHAR(100) NOT NULL,
    ServiceType VARCHAR(50)
);

-- Tabla: MATERIAL
CREATE TABLE MATERIAL (
    MaterialID VARCHAR(10) PRIMARY KEY,
    MaterialName VARCHAR(100) NOT NULL UNIQUE,
    UnitCost NUMERIC(10, 2) NOT NULL
);
-- Tabla: PRODUCT (Relacionada con SUBCONTRACTOR)
CREATE TABLE PRODUCT (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    ProductCategory VARCHAR(50),
    ProductPrice NUMERIC(10, 2) NOT NULL,
    SubcontractorID VARCHAR(10),
    
    -- Definición de la relación 1:M (un subcontratista tiene muchos productos)
    FOREIGN KEY (SubcontractorID) REFERENCES SUBCONTRACTOR (SubcontractorID)
);

--Tablas Transaccionales
-- Tabla: ORDER_HEADER (Relacionada con CUSTOMER)
CREATE TABLE ORDER_HEADER (
    OrderID SERIAL PRIMARY KEY, -- Usamos SERIAL para IDs autoincrementables
    OrderDate DATE NOT NULL,
    OrderStatus VARCHAR(20) NOT NULL,
    CustomerID VARCHAR(10) NOT NULL,
    
    -- Definición de la relación 1:M (un cliente tiene muchas órdenes)
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER (CustomerID)
);

-- Tabla: ORDER_DETAIL (Resuelve M:N entre Orden y Producto)
-- Contiene la cantidad ordenada de cada producto en una orden.
CREATE TABLE ORDER_DETAIL (
    OrderID INTEGER NOT NULL,
    ProductID VARCHAR(10) NOT NULL,
    QuantityOrdered INTEGER NOT NULL CHECK (QuantityOrdered > 0), -- Asegura que la cantidad sea positiva
    
    -- La Clave Primaria Compuesta garantiza que un par (Orden, Producto) sea único
    PRIMARY KEY (OrderID, ProductID),
    
    -- Relaciones con ORDER_HEADER
    FOREIGN KEY (OrderID) REFERENCES ORDER_HEADER (OrderID),
    
    -- Relaciones con PRODUCT
    FOREIGN KEY (ProductID) REFERENCES PRODUCT (ProductID)
);
-- Tablas de Relación (Muchos a Muchos - M:N)
-- Tabla: PRODUCT_HAS_MATERIAL (Resuelve M:N entre Producto y Material)
-- Es la "Lista de Materiales" (Bill of Materials).
CREATE TABLE PRODUCT_HAS_MATERIAL (
    ProductID VARCHAR(10) NOT NULL,
    MaterialID VARCHAR(10) NOT NULL,
    QuantityRequired NUMERIC(10, 2) NOT NULL, -- Cantidad de material requerida por unidad de producto
    
    PRIMARY KEY (ProductID, MaterialID),
    
    FOREIGN KEY (ProductID) REFERENCES PRODUCT (ProductID),
    FOREIGN KEY (MaterialID) REFERENCES MATERIAL (MaterialID)
);