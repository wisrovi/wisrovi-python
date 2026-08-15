"""Tests de validación para Clase 03: Control de Flujo: Condicionales (if / elif / else)."""
def test_c1_clase_03():
    nota = 85
    resultado = "Aprobado" if nota >= 60 else "Reprobado"
    assert resultado == "Aprobado"

