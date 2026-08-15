"""Medición de Tiempo con perf_counter."""
import time
t0=time.perf_counter()
sum(range(100000))
print(f'Tiempo: {(time.perf_counter()-t0)*1000:.4f}ms')
