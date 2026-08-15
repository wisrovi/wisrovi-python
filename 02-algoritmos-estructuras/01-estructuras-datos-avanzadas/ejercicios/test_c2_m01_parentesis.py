import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_01_validador_parentesis import son_parentesis_validos

def test_parentesis_validos():
    assert son_parentesis_validos("()") is True
    assert son_parentesis_validos("()[]{}") is True
    assert son_parentesis_validos("{[()]}") is True
    assert son_parentesis_validos("(]") is False
    assert son_parentesis_validos("([)]") is False
