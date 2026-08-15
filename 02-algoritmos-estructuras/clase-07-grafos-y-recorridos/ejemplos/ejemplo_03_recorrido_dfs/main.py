"""Búsqueda en Profundidad (DFS Recursivo)."""
def dfs(g, n, vis=None):
    if vis is None: vis = set()
    vis.add(n)
    for v in g.get(n, []):
        if v not in vis: dfs(g, v, vis)
    return vis
print('DFS visitados:', dfs({'A':['B'], 'B':[]}, 'A'))
