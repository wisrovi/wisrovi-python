"""Ejercicio: Implementar QuickSort recursivo."""

def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izq = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    der = [x for x in arr if x > pivote]
    return quicksort(izq) + centro + quicksort(der)

if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Ordenado:", quicksort(datos))
