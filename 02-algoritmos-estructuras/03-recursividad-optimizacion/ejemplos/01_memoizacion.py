"""Optimización con Memoización @lru_cache."""
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

t0 = time.perf_counter()
res = fib(50)
t1 = time.perf_counter()
print(f"Fib(50) = {res} en {(t1-t0)*1000:.4f} ms")
