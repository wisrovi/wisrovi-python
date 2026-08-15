"""Búsqueda Binaria O(log n) vs Búsqueda Lineal O(n)."""

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

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Índice de 70:", busqueda_binaria(numeros, 70))
