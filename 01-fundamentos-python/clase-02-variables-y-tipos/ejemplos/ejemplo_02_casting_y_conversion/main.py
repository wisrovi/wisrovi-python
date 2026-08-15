"""Ejemplo 02: Casting y Conversión de Tipos."""
entrada_usuario = "45.90"

# Conversión a float y posterior a int
precio_float = float(entrada_usuario)
precio_int = int(precio_float)

print(f"Original (str): '{entrada_usuario}'")
print(f"Como Float: {precio_float:.2f}")
print(f"Como Int (truncado): {precio_int}")
