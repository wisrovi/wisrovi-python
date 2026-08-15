"""Inserción Recursiva en BST."""
class N:
    def __init__(self, v): self.v = v; self.i = self.d = None
def ins(r, v):
    if not r: return N(v)
    if v < r.v: r.i = ins(r.i, v)
    else: r.d = ins(r.d, v)
    return r
r = ins(None, 10); r = ins(r, 5)
print('Árbol raíz:', r.v)
