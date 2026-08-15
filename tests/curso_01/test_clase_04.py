"""Tests de validación para Clase 04: Control de Flujo: Bucles (for / while)."""
def test_c1_clase_04():
    suma = sum(i for i in range(1, 6))
    assert suma == 15

