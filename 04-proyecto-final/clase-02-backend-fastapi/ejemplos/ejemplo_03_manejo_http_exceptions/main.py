"""Manejo de HTTPException (404, 400)."""
from fastapi import HTTPException
def validar(x):
    if x < 0: raise HTTPException(400, 'Inválido')
print('Validación lista.')
