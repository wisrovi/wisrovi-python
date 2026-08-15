"""Clase 04: Algoritmos de Búsqueda: Lineal vs Binaria O(log n) - Código de Demostración."""
import bisect

def busqueda_binaria(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

datos = [10, 20, 30, 40, 50, 60, 70, 80]
idx = busqueda_binaria(datos, 60)
print("Índice de 60:", idx)  # 5
print("Índice con bisect_left:", bisect.bisect_left(datos, 60))
