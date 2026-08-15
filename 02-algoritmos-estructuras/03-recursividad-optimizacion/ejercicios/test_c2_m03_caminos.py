import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_03_caminos_cuadricula import caminos_unicos

def test_caminos_unicos():
    assert caminos_unicos(3, 7) == 28
    assert caminos_unicos(3, 2) == 3
    assert caminos_unicos(1, 1) == 1
