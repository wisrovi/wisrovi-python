"""Ejemplo 03: F-Strings Avanzados."""
producto = "Teclado Mecánico"
precio = 89.9543
descuento = 0.15

total = precio * (1 - descuento)

print(f"Producto: {producto:<20} | Precio Base: ${precio:.2f}")
print(f"Descuento: {descuento * 100:.0f}% | Total a Pagar: ${total:.2f}")
