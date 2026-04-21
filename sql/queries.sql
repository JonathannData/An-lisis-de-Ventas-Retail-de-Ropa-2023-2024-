-- =========================================
-- PROYECTO: ANALISIS DE VENTAS RETAIL
-- =========================================

-- =========================
-- 1. EXPLORACION INICIAL
-- =========================

SELECT * FROM clientes;
SELECT * FROM productos;
SELECT * FROM ventas;


-- =========================
-- 2. VALIDACION DE DATOS
-- =========================

-- Clientes que aparecen en ventas pero no existen en clientes
SELECT DISTINCT v.cliente_id
FROM ventas v
LEFT JOIN clientes c ON v.cliente_id = c.cliente_id
WHERE c.cliente_id IS NULL;


-- Productos que aparecen en ventas pero no existen en productos
SELECT DISTINCT v.producto_id
FROM ventas v
LEFT JOIN productos p ON v.producto_id = p.producto_id
WHERE p.producto_id IS NULL;


-- Productos que nunca se vendieron
SELECT p.producto_id, p.nombre_producto
FROM productos p
LEFT JOIN ventas v ON p.producto_id = v.producto_id
WHERE v.producto_id IS NULL;


-- =========================
-- 3. ANALISIS BASICO
-- =========================

-- Ventas totales
SELECT SUM(cantidad * precio_unitario) AS ventas_totales
FROM ventas;


-- Ventas por categoria
SELECT 
    p.categoria,
    SUM(v.cantidad * v.precio_unitario) AS ventas_totales
FROM ventas v
JOIN productos p ON v.producto_id = p.producto_id
GROUP BY p.categoria
ORDER BY ventas_totales DESC;


-- Top productos
SELECT 
    p.nombre_producto,
    SUM(v.cantidad * v.precio_unitario) AS ventas_totales
FROM ventas v
JOIN productos p ON v.producto_id = p.producto_id
GROUP BY p.nombre_producto
ORDER BY ventas_totales DESC
LIMIT 10;


-- Ventas por cliente
SELECT 
    c.nombre,
    SUM(v.cantidad * v.precio_unitario) AS ventas_totales
FROM ventas v
JOIN clientes c ON v.cliente_id = c.cliente_id
GROUP BY c.nombre
ORDER BY ventas_totales DESC;


-- =========================
-- 4. JOIN COMPLETO (REFERENCIA)
-- =========================

SELECT 
    v.venta_id,
    v.fecha,
    c.nombre AS cliente,
    c.genero,
    c.edad,
    c.ciudad,
    p.nombre_producto,
    p.categoria,
    p.marca,
    v.cantidad,
    v.precio_unitario,
    (v.cantidad * v.precio_unitario) AS total
FROM ventas v
LEFT JOIN clientes c ON v.cliente_id = c.cliente_id
LEFT JOIN productos p ON v.producto_id = p.producto_id;
