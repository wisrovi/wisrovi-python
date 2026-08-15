"""División de Texto en Chunks."""
def chunk(t, sz=10, ov=2): return [t[i:i+sz] for i in range(0, len(t), sz-ov)]
print('Chunks:', chunk('ABCDEFGHIJKLMN', 5, 1))
