"""Búsqueda en Arreglo Rotado."""
def buscar_rotado(arr, t):
    return arr.index(t) if t in arr else -1
print(buscar_rotado([4, 5, 6, 1, 2], 1))
