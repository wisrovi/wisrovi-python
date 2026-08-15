"""Tests de validación para Clase 04: Algoritmos de Búsqueda: Lineal vs Binaria O(log n)."""
def test_c2_clase_04():
    arr = [10, 20, 30, 40, 50]
    target = 30
    left, right = 0, len(arr) - 1
    found = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: found = mid; break
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    assert found == 2

