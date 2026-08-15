"""Tests de validación para Clase 02: Desarrollo del Backend: APIs RESTful con FastAPI."""
from pydantic import BaseModel
def test_c4_clase_02():
    class Item(BaseModel): id: int; name: str
    it = Item(id=1, name="Laptop")
    assert it.id == 1

