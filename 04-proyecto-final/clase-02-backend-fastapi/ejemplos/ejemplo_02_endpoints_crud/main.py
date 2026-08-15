"""Endpoints GET y POST con DTO."""
from pydantic import BaseModel
class Item(BaseModel): name: str
print('DTO listo para validación.')
