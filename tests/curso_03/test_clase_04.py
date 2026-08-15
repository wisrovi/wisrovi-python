"""Tests de validación para Clase 04: Tool Calling y Function Calling en Python."""
def test_c3_clase_04():
    tools = {"sumar": lambda a, b: a + b}
    assert tools["sumar"](2, 3) == 5

