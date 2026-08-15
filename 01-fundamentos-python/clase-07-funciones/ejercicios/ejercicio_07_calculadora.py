# ==============================================================================
# 🏋️ CLASE 7 - Ejercicio Práctico: Descuentos
# ==============================================================================

def descuento(precio, pct):
    return precio - (precio * (pct/100))

p = float(input("Precio: "))
d = float(input("Descuento %: "))
print(f"Final: ${descuento(p, d):.2f}")
