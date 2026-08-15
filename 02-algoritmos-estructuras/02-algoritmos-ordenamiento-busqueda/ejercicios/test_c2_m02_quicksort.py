import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_02_quicksort import quicksort

def test_quicksort():
    assert quicksort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 3, 3]) == [3, 3, 3]
