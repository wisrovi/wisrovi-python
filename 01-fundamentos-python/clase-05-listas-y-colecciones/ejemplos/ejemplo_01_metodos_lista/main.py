"""Ejemplo 01: Métodos Principales de Listas."""
stack = ["Python", "FastAPI"]
stack.append("Docker")       # Agrega al final
stack.insert(1, "Pydantic")  # Inserta en posición 1
stack.sort()                 # Ordena in-place

print("Stack tecnológico:", stack)
eliminado = stack.pop()      # Extrae el último
print(f"Elemento extraído con pop(): {eliminado}")
