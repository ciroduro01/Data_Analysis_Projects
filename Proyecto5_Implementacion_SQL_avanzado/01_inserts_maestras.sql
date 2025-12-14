-- PROYECTO N°5: Implementación y SQL Avanzado
-- FASE 1: INSERCIÓN DE DATOS MAESTROS (DIMENSIONES)

-- 1. Inserción en SUBCONTRACTOR (SubcontractorID, SubcontractorName, ServiceType)
INSERT INTO SUBCONTRACTOR (SubcontractorID, SubcontractorName, ServiceType) VALUES
('SC001', 'Metalurgica Norte S.A.', 'Mecanizado y Soldadura'),
('SC002', 'Plásticos Modernos Ltda.', 'Inyección de Plástico'),
('SC003', 'Componentes Eléctricos Z', 'Ensamblaje Electrónico'),
('SC004', 'Maderas Finas Muebles', 'Corte y Acabado de Madera');

-- 2. Inserción en MATERIAL (MaterialID, MaterialName, UnitCost)
-- NOTA: El campo MaterialName debe ser UNIQUE y UnitCost NOT NULL, según el diseño.
INSERT INTO MATERIAL (MaterialID, MaterialName, UnitCost) VALUES
('M001', 'Acero Inoxidable 304', 5.50),
('M002', 'Polipropileno Grado A', 1.20),
('M003', 'Cable de Cobre AWG18', 0.85),
('M004', 'Madera de Haya', 15.00),
('M005', 'Tornillo M4 x 10mm', 0.05),
('M006', 'Chip Microcontrolador V2', 3.50);

-- 3. Inserción en CUSTOMER (CustomerID, CustomerName, CustomerAddress, CustomerEmail)
-- NOTA: El campo CustomerEmail debe ser UNIQUE.
INSERT INTO CUSTOMER (CustomerID, CustomerName, CustomerAddress, CustomerEmail) VALUES
('C100', 'Tech Solutions Corp.', 'Av. Principal 123, Ciudad A', 'contacto@techsol.com'),
('C101', 'EcoHome Builders', 'Calle Verde 45, Pueblo B', 'compras@ecohome.net'),
('C102', 'Fitness Gears Inc.', 'Ruta Industrial 77, Zona C', 'pedidos@fitnessgear.org'),
('C103', 'Global Retail Chain', 'Centro Comercial Mega, Ciudad D', 'ventas@globalretail.com');