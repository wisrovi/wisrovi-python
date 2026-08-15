"""Configuración Tipada con Pydantic."""
from pydantic import BaseModel
class Config(BaseModel): env: str = 'prod'
print(Config())
