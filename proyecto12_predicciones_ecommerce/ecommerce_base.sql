CREATE DATABASE ecommercefinal_db;
-- Tabla para almacenar los datos limpios de E-commerce
CREATE TABLE retail_clean (
    invoiceno VARCHAR(20),
    stockcode VARCHAR(20),
    description TEXT,
    quantity INTEGER,
    invoicedate TIMESTAMP,
    unitprice NUMERIC(10, 2),
    customerid INTEGER,
    country VARCHAR(50),
    valortotal NUMERIC(10, 2),
    fecha DATE,
    hora TIME,
    diasemana VARCHAR(10)
);