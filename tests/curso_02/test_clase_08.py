"""Tests de validación para Clase 08: Recursividad y Programación Dinámica con Memoización."""
from functools import lru_cache
def test_c2_clase_08():
    @lru_cache(None)
    def f(n): return n if n <= 1 else f(n-1) + f(n-2)
    assert f(10) == 55

