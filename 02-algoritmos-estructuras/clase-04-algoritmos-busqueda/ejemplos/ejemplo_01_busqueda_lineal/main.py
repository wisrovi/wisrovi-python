"""Búsqueda Lineal Clásica."""
def buscar_lineal(arr, x):
    for i, v in enumerate(arr):
        if v == x: return i
    return -1
print(buscar_lineal([10, 20, 30], 20))
