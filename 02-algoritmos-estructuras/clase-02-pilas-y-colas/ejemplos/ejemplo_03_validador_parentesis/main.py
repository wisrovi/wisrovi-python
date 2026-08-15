"""Validador de Paréntesis Balanceados."""
def val(s):
    p = []
    m = {')':'('}
    for c in s:
        if c in m.values(): p.append(c)
        elif c in m and (not p or p.pop() != m[c]): return False
    return len(p) == 0
print(val('()'))
