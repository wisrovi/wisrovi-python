"""Tests de validación para Clase 06: Diccionarios y Conjuntos (Sets)."""
def test_c1_clase_06():
    persona = {"nombre": "Ana", "edad": 30}
    assert persona.get("nombre") == "Ana"
    assert persona.get("ciudad", "Madrid") == "Madrid"

