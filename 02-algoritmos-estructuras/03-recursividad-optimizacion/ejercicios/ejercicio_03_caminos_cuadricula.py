"""Ejercicio: Calcular caminos únicos en cuadrícula m x n con memoización."""
from functools import lru_cache

@lru_cache(maxsize=None)
def caminos_unicos(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    return caminos_unicos(m - 1, n) + caminos_unicos(m, n - 1)

if __name__ == "__main__":
    print("Caminos en 3x7:", caminos_unicos(3, 7))
