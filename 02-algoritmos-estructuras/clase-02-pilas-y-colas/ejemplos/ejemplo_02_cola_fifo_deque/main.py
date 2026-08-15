"""Cola (FIFO) con collections.deque."""
from collections import deque
q = deque(['A', 'B'])
q.append('C')
print('Primero:', q.popleft())
