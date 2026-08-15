"""Tests de validación para Clase 01: Primer Vistazo Práctico (print, variables, if, for)."""
def test_c1_clase_01():
    usuario = "Wisrovi"
    edad = 25
    es_mayor = edad >= 18
    herramientas = ["VS Code", "Terminal", "Git", "Python"]
    assert usuario == "Wisrovi"
    assert es_mayor is True
    assert len(herramientas) == 4

