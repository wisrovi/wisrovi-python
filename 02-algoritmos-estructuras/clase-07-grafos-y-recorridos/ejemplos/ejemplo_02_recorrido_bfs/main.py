"""Búsqueda en Amplitud (BFS con deque)."""
from collections import deque
def bfs(g, start):
    vis = {start}; q = deque([start]); res = []
    while q:
        n = q.popleft(); res.append(n)
        for v in g.get(n, []):
            if v not in vis: vis.add(v); q.append(v)
    return res
print(bfs({'A':['B'], 'B':['C'], 'C':[]}, 'A'))
