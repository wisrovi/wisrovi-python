"""Mini Vector Store en Memoria."""
class MiniStore:
    def __init__(self): self.db = []
    def add(self, t, v): self.db.append((t, v))
store = MiniStore(); store.add('Doc 1', [1, 2]); print('Store inicializado.')
