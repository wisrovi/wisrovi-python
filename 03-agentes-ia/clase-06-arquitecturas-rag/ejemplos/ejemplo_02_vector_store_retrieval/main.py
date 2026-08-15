"""Recuperador Top-K."""
class Retriever:
    def get_top_k(self, q): return ['Chunk 1 relevante', 'Chunk 2 relevante']
print(Retriever().get_top_k('test'))
