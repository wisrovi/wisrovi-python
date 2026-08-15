"""Clase Repositorio de Base de Datos."""
class Repo:
    def __init__(self): self.db = []
    def add(self, x): self.db.append(x)
r = Repo(); r.add(1); print('Items:', r.db)
