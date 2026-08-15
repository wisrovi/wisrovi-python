"""QuickSort Recursivo."""
def qs(a):
    if len(a) <= 1: return a
    p = a[len(a)//2]
    return qs([x for x in a if x < p]) + [x for x in a if x == p] + qs([x for x in a if x > p])
print(qs([38, 27, 43, 3, 9]))
