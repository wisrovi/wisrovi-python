"""Ejemplo 03: Ámbito Local vs Global."""
tasa_global = 0.21

def calcular_impuesto(monto: float) -> float:
    # tasa_global se lee del ámbito global
    return monto * tasa_global

print(f"Impuesto de $100: ${calcular_impuesto(100.0)}")
