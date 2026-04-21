# =========================================
# PROYECTO: ANALISIS DE VENTAS RETAIL
# =========================================

import pandas as pd


# =========================
# 1. CARGA DE DATOS
# =========================

df_clientes = pd.read_csv("data/clientes.csv")
df_productos = pd.read_csv("data/productos.csv")
df_ventas = pd.read_csv("data/ventas.csv")


# =========================
# 2. LIMPIEZA CLIENTES
# =========================

# Convertir fechas
df_clientes["fecha_registro"] = pd.to_datetime(
    df_clientes["fecha_registro"], errors="coerce"
)

# Rellenar edad faltante con mediana
df_clientes["edad"] = df_clientes["edad"].fillna(df_clientes["edad"].median())

# Rellenar texto faltante
df_clientes["nombre"] = df_clientes["nombre"].fillna("Desconocido")
df_clientes["ciudad"] = df_clientes["ciudad"].fillna("Desconocido")
df_clientes["genero"] = df_clientes["genero"].fillna("N/A")


# =========================
# 3. LIMPIEZA PRODUCTOS
# =========================

df_productos["marca"] = df_productos["marca"].fillna("Desconocido")
df_productos["categoria"] = df_productos["categoria"].fillna("Desconocido")


# =========================
# 4. LIMPIEZA VENTAS
# =========================

# Convertir fechas
df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"], errors="coerce")

# Eliminar fechas inválidas
df_ventas = df_ventas.dropna(subset=["fecha"])

# Eliminar cantidades incorrectas
df_ventas = df_ventas[df_ventas["cantidad"] > 0]


# =========================
# 5. FEATURE ENGINEERING
# =========================

df_ventas["total"] = df_ventas["cantidad"] * df_ventas["precio_unitario"]


# =========================
# 6. INTEGRIDAD REFERENCIAL
# =========================

# Clientes faltantes en ventas
clientes_faltantes = set(df_ventas["cliente_id"]) - set(df_clientes["cliente_id"])

for cliente_id in clientes_faltantes:
    nuevo_cliente = pd.DataFrame([{
        "cliente_id": cliente_id,
        "nombre": "Desconocido",
        "genero": "N/A",
        "edad": None,
        "ciudad": "Desconocido",
        "fecha_registro": None
    }])
    df_clientes = pd.concat([df_clientes, nuevo_cliente], ignore_index=True)


# =========================
# 7. EXPORTACION FINAL
# =========================

df_clientes.to_csv("data/clientes_clean.csv", index=False)
df_productos.to_csv("data/productos_clean.csv", index=False)
df_ventas.to_csv("data/ventas_clean.csv", index=False)


# =========================
# 8. VERIFICACION
# =========================

print("Clientes:", df_clientes.shape)
print("Productos:", df_productos.shape)
print("Ventas:", df_ventas.shape)

print("Limpieza completada correctamente 🚀")
