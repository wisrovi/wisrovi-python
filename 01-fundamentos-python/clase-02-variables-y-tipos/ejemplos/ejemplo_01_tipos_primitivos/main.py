"""Ejemplo 01: Tipos Primitivos y Anotaciones de Tipo (PEP 484)."""
edad: int = 30
altura: float = 1.78
nombre: str = "Wisrovi"
es_estudiante: bool = False

print(f"Nombre: {nombre} ({type(nombre).__name__})")
print(f"Edad: {edad} ({type(edad).__name__})")
print(f"Altura: {altura} m ({type(altura).__name__})")
print(f"¿Estudiante?: {es_estudiante} ({type(es_estudiante).__name__})")
