import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from database import BaseDeDatos

def test_database_crud():
    db = BaseDeDatos(":memory:")
    prod_id = db.insertar("Monitor", 10, 199.99)
    assert prod_id == 1
    items = db.listar()
    assert len(items) == 1
    assert items[0][1] == "Monitor"
