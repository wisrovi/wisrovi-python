"""Clase 03: Tablas Hash y Conjuntos (Sets) para Búsqueda O(1) - Código de Demostración."""
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    vistos = {}  # mapa: valor -> indice
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in vistos:
            return (vistos[complemento], i)
        vistos[num] = i
    return (-1, -1)

indices = two_sum([2, 7, 11, 15], 9)
print("Índices que suman 9:", indices)  # (0, 1)
