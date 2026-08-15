"""Manejo de ValidationError."""
from pydantic import BaseModel, ValidationError
class Num(BaseModel): val: int
try: Num(val='abc')
except ValidationError as e: print('Error capturado correctamente.')
