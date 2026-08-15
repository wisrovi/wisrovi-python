"""Ejemplo 03: Conjuntos (Sets)."""
skills_dev_a = {"Python", "Docker", "FastAPI", "Git"}
skills_dev_b = {"FastAPI", "React", "PostgreSQL", "Git"}

print("Habilidades comunes (Intersección):", skills_dev_a & skills_dev_b)
print("Todas las habilidades (Unión):", skills_dev_a | skills_dev_b)
print("Solo de Dev A (Diferencia):", skills_dev_a - skills_dev_b)
