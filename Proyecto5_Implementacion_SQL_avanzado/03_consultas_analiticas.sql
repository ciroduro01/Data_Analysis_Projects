-- PROYECTO N°5: Implementación y SQL Avanzado
-- FASE 2: CONSULTAS ANALÍTICAS

-- Consulta 1: Cálculo del Costo Total de Materiales por Unidad de Producto (Roll-up Cost)
-- Objetivo: Determinar el costo total de materiales para fabricar una unidad de cada PRODUCTO.
-- Este cálculo es esencial para fijar precios de venta y márgenes de ganancia.

SELECT
    p.ProductID,
    p.ProductName,
    -- Sumamos el costo de cada material (Cantidad Requerida * Costo Unitario)
    ROUND(SUM(phm.QuantityRequired * m.UnitCost), 2) AS CostoTotalMateriales
FROM
    PRODUCT p
-- 1. Unimos el Producto con su Lista de Materiales (BOM)
JOIN
    PRODUCT_HAS_MATERIAL phm ON p.ProductID = phm.ProductID
-- 2. Unimos la Lista de Materiales con la tabla MATERIAL para obtener el Costo Unitario
JOIN
    MATERIAL m ON phm.MaterialID = m.MaterialID
-- Agrupamos por producto para sumar todos los costos de los componentes
GROUP BY
    p.ProductID, p.ProductName
ORDER BY
    CostoTotalMateriales DESC;

-- Consulta 2: Costo Total de Materiales Requeridos por Orden
-- Objetivo: Multiplicar el Costo Unitario de Materiales (de Consulta 1) por la Cantidad Ordenada.

WITH ProductoCosto AS (
    -- 1. Subconsulta CTE que calcula el costo total de materiales por UNIDAD de producto (Roll-up Cost)
    SELECT
        p.ProductID,
        ROUND(SUM(phm.QuantityRequired * m.UnitCost), 2) AS CostoUnitarioMaterial
    FROM
        PRODUCT p
    JOIN PRODUCT_HAS_MATERIAL phm ON p.ProductID = phm.ProductID
    JOIN MATERIAL m ON phm.MaterialID = m.MaterialID
    GROUP BY p.ProductID
)
SELECT
    oh.OrderID,
    oh.OrderDate,
    c.CustomerName,
    oh.OrderStatus,
    -- 2. Multiplicamos la cantidad ordenada (ORDER_DETAIL) por el Costo Unitario (CTE) y sumamos
    ROUND(SUM(od.QuantityOrdered * pc.CostoUnitarioMaterial), 2) AS CostoTotalMaterialesOrden
FROM
    ORDER_HEADER oh
JOIN
    CUSTOMER c ON oh.CustomerID = c.CustomerID
JOIN
    ORDER_DETAIL od ON oh.OrderID = od.OrderID
-- 3. Unimos el detalle de la orden con el costo pre-calculado por unidad
JOIN
    ProductoCosto pc ON od.ProductID = pc.ProductID
GROUP BY
    oh.OrderID, oh.OrderDate, c.CustomerName, oh.OrderStatus
ORDER BY
    oh.OrderDate;

-- Consulta 3: Análisis de la Dependencia y Volumen de Órdenes por Subcontratista
-- Objetivo: Contar el número total de Órdenes que incluyen al menos un producto asociado a cada subcontratista.

SELECT
    sc.SubcontractorName,
    sc.ServiceType,
    -- Contamos las Órdenes únicas asociadas a los productos de este subcontratista
    COUNT(DISTINCT od.OrderID) AS TotalOrdenesDependientes
FROM
    SUBCONTRACTOR sc
-- 1. Unimos Subcontratista con el PRODUCTO que fabrica
JOIN
    PRODUCT p ON sc.SubcontractorID = p.SubcontractorID
-- 2. Unimos el PRODUCTO con los detalles de las ÓRDENES donde fue pedido
JOIN
    ORDER_DETAIL od ON p.ProductID = od.ProductID
-- Agrupamos por subcontratista para obtener el conteo
GROUP BY
    sc.SubcontractorName, sc.ServiceType
ORDER BY
    TotalOrdenesDependientes DESC;