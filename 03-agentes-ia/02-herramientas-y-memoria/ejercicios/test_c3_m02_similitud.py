import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_02_similitud_coseno import similitud_coseno

def test_similitud_identica():
    assert round(similitud_coseno([1.0, 0.0], [1.0, 0.0]), 2) == 1.0

def test_similitud_ortogonal():
    assert round(similitud_coseno([1.0, 0.0], [0.0, 1.0]), 2) == 0.0
