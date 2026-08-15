"""Recorrido In-Order (Ascendente)."""
def inorder(r, l):
    if r: inorder(r.i, l); l.append(r.v); inorder(r.d, l)
print('Recorrido in-order funcional.')
