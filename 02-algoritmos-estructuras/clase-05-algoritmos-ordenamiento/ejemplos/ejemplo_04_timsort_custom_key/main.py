"""Ordenamiento con Key Custom."""
estudiantes = [{'n': 'Ana', 'nota': 90}, {'n': 'Carlos', 'nota': 80}]
ordenados = sorted(estudiantes, key=lambda x: x['nota'], reverse=True)
print(ordenados)
