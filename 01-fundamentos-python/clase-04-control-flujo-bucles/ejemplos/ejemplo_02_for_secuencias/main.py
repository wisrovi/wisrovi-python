"""Ejemplo 02: Iteración sobre Colecciones y enumerate()."""
frameworks = ["FastAPI", "Streamlit", "Pydantic", "Pytest"]

for indice, nombre in enumerate(frameworks, start=1):
    print(f"[{indice}] Framework de IA/Web: {nombre}")
