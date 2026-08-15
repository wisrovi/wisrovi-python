"""Resolución de Two-Sum en O(n)."""
def two_sum(nums, target):
    m = {}
    for i, n in enumerate(nums):
        if target - n in m: return (m[target - n], i)
        m[n] = i
print(two_sum([2, 7, 11], 9))
