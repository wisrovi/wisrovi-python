"""Ejemplo 01: Funciones Puras."""
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área geométrica de un rectángulo."""
    return base * altura

area = calcular_area_rectangulo(5.0, 3.0)
print(f"Área calculada: {area} m²")
