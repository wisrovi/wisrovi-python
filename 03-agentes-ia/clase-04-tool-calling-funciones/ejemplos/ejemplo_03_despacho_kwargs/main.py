"""Ejecución Dinámica con kwargs."""
TOOLS = {'calc': lambda x: x*2}
res = TOOLS['calc'](**{'x': 21})
print('Resultado despachado:', res)
