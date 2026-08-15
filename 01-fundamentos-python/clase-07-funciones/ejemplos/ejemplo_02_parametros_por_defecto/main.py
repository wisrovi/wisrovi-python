"""Ejemplo 02: Argumentos por Defecto."""
def formatear_precio(monto: float, moneda: str = "EUR", decimales: int = 2) -> str:
    return f"{monto:.{decimales}f} {moneda}"

print(formatear_precio(45.5))
print(formatear_precio(100.0, moneda="USD", decimales=0))
