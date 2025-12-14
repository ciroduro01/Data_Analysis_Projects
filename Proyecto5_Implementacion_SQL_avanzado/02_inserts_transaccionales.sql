-- PROYECTO N°5: Implementación y SQL Avanzado
-- FASE 1: INSERCIÓN DE DATOS TRANSACCIONALES

-- 1. Inserción en PRODUCT (ProductID, ProductName, ProductCategory, ProductPrice, SubcontractorID)
-- NOTA: Todos los SubcontractorID deben existir en SUBCONTRACTOR (Ej: SC001, SC002, etc.).
INSERT INTO PRODUCT (ProductID, ProductName, ProductCategory, ProductPrice, SubcontractorID) VALUES
-- Producto SC001 (Mecanizado y Soldadura)
('P101', 'Estructura Modular Acero', 'Maquinaria', 850.00, 'SC001'),
-- Producto SC002 (Inyección de Plástico)
('P102', 'Carcasa de Plástico Reforzado', 'Componente', 45.50, 'SC002'),
-- Producto SC003 (Ensamblaje Electrónico)
('P103', 'Placa de Control IoT', 'Electrónica', 120.00, 'SC003'),
-- Producto SC004 (Corte y Acabado de Madera)
('P104', 'Mesa de Trabajo Premium', 'Mobiliario', 320.00, 'SC004');


-- 2. Inserción en ORDER_HEADER (OrderID, OrderDate, OrderStatus, CustomerID)
-- NOTA: CustomerID debe existir en CUSTOMER (Ej: C100, C101, etc.).
-- El OrderID es SERIAL, pero lo insertamos explícitamente para asegurar la referencia en ORDER_DETAIL.
INSERT INTO ORDER_HEADER (OrderID, OrderDate, OrderStatus, CustomerID) VALUES
(1, '2025-10-01', 'Completada', 'C100'), -- Tech Solutions Corp.
(2, '2025-10-05', 'Pendiente', 'C101'), -- EcoHome Builders
(3, '2025-10-08', 'En Proceso', 'C102'), -- Fitness Gears Inc.
(4, '2025-10-15', 'Completada', 'C103'), -- Global Retail Chain
(5, '2025-10-20', 'Cancelada', 'C100');


-- 3. Inserción en PRODUCT_HAS_MATERIAL (ProductID, MaterialID, QuantityRequired)
-- Esta es la "Lista de Materiales" (BOM).
-- NOTA: ProductID debe existir en PRODUCT. MaterialID debe existir en MATERIAL.
INSERT INTO PRODUCT_HAS_MATERIAL (ProductID, MaterialID, QuantityRequired) VALUES
-- P101 (Estructura Modular Acero): Requiere Acero y Tornillos
('P101', 'M001', 15.5), -- 15.5 unidades de Acero
('P101', 'M005', 40.0), -- 40 Tornillos
-- P102 (Carcasa Plástico): Requiere Polipropileno
('P102', 'M002', 2.8), -- 2.8 unidades de Polipropileno
-- P103 (Placa de Control IoT): Requiere Cobre y Microcontrolador
('P103', 'M003', 1.0), -- 1.0 unidad de Cable de Cobre
('P103', 'M006', 1.0), -- 1.0 unidad de Chip Microcontrolador
-- P104 (Mesa de Trabajo Premium): Requiere Madera
('P104', 'M004', 5.0); -- 5.0 unidades de Madera de Haya


-- 4. Inserción en ORDER_DETAIL (OrderID, ProductID, QuantityOrdered)
-- NOTA: OrderID debe existir en ORDER_HEADER. ProductID debe existir en PRODUCT. QuantityOrdered > 0.
INSERT INTO ORDER_DETAIL (OrderID, ProductID, QuantityOrdered) VALUES
(1, 'P101', 5),    -- Orden 1: 5 Estructuras de Acero
(1, 'P103', 10),   -- Orden 1: 10 Placas IoT
(2, 'P104', 20),   -- Orden 2: 20 Mesas de Madera
(3, 'P102', 500),  -- Orden 3: 500 Carcasas de Plástico
(4, 'P103', 100);  -- Orden 4: 100 Placas IoT