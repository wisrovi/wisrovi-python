def test_c2_clase_06():
    class N:
        def __init__(self, v): self.v = v; self.izq = None; self.der = None
    raiz = N(10)
    raiz.izq = N(5)
    assert raiz.izq.v == 5
