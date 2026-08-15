"""Calculador de Costos de Inferencia."""
def costo(tokens, precio_k=0.002): return (tokens/1000)*precio_k
print(f'Costo: ${costo(5000):.4f}')
