"""Buffer Circular con maxlen."""
from collections import deque
buf = deque(maxlen=3)
for i in range(5): buf.append(i)
print('Buffer (últimos 3):', list(buf))
