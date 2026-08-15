"""Bubble Sort Paso a Paso."""
def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
    return a
print(bubble([5, 2, 8, 1]))
