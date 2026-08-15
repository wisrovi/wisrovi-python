"""MergeSort Divide y Vencerás."""
def mergesort(a):
    if len(a) <= 1: return a
    m = len(a)//2
    l, r = mergesort(a[:m]), mergesort(a[m:])
    res = []
    while l and r: res.append(l.pop(0) if l[0] <= r[0] else r.pop(0))
    return res + l + r
print(mergesort([12, 11, 13, 5, 6]))
