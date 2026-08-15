"""Tokenizador Simulado."""
def tokenizar(t): return t.replace('.', ' .').split()
print(tokenizar('Python es potente.'))
