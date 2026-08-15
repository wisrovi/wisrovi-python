import sys, os, pytest
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_01_extractor_contacto import validar_contacto
from pydantic import ValidationError

def test_contacto_valido():
    json_data = '{"nombre_completo": "Carlos Ruiz", "email": "carlos@test.com"}'
    c = validar_contacto(json_data)
    assert c.nombre_completo == "Carlos Ruiz"
    assert c.empresa == "Independiente"

def test_contacto_invalido():
    with pytest.raises(ValidationError):
        validar_contacto('{"nombre_completo": 123}')
