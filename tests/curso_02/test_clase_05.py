"""Tests de validación para Clase 05: Algoritmos de Ordenamiento: QuickSort y MergeSort."""
def test_c2_clase_05():
    def qs(a):
        if len(a) <= 1: return a
        p = a[len(a)//2]
        return qs([x for x in a if x < p]) + [x for x in a if x == p] + qs([x for x in a if x > p])
    assert qs([5, 2, 8, 1]) == [1, 2, 5, 8]

