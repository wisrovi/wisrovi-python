"""Búsqueda Binaria O(log n)."""
def bb(arr, t):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == t: return m
        elif arr[m] < t: l = m+1
        else: r = m-1
    return -1
print(bb([1, 3, 5, 7, 9], 7))
