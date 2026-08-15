"""Cálculo de Altura del Árbol."""
def altura(n):
    return 0 if not n else 1 + max(altura(getattr(n, 'i', None)), altura(getattr(n, 'd', None)))
print('Cálculo de altura listo.')
