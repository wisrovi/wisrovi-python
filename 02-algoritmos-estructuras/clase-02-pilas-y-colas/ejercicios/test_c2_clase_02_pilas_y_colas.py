from collections import deque
def test_c2_clase_02():
    q = deque([1, 2, 3])
    q.append(4)
    assert q.popleft() == 1
