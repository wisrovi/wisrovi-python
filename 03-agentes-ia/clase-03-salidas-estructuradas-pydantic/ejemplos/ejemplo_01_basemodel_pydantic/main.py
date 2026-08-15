"""Modelo BaseModel de Pydantic."""
from pydantic import BaseModel
class User(BaseModel): id: int; name: str
u = User(id=1, name='Ana')
print(u.model_dump())
