"""Ejercicio: Extractor de datos de contacto estructurados con Pydantic."""
from pydantic import BaseModel, EmailStr, Field

class ContactoExtraido(BaseModel):
    nombre_completo: str
    email: str
    telefono: str | None = None
    empresa: str = "Independiente"

def validar_contacto(json_str: str) -> ContactoExtraido:
    return ContactoExtraido.model_validate_json(json_str)

if __name__ == "__main__":
    ejemplo = '{"nombre_completo": "Ana Gomez", "email": "ana@empresa.com", "empresa": "TechCorp"}'
    c = validar_contacto(ejemplo)
    print("Contacto procesado:", c)
