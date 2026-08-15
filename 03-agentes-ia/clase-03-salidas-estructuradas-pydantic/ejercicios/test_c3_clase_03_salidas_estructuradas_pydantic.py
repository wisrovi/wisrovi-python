from pydantic import BaseModel
def test_c3_clase_03():
    class Item(BaseModel): name: str; price: float
    i = Item(name="Test", price=10.0)
    assert i.price == 10.0
