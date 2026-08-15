"""Modelos de Dominio y DTOs."""
from pydantic import BaseModel
class UserDTO(BaseModel): name: str
print(UserDTO(name='Wisrovi'))
