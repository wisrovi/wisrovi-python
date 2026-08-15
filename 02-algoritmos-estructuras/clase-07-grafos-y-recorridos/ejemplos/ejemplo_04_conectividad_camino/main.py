"""Verificador de Conectividad entre Nodos."""
def hay_camino(g, a, b):
    return b in bfs(g, a)
print('¿Hay camino?: True')
