"""Optimización con @lru_cache."""
from functools import lru_cache
@lru_cache(None)
def fib_fast(n):
    return n if n <= 1 else fib_fast(n-1) + fib_fast(n-2)
print('Fib(50):', fib_fast(50))
