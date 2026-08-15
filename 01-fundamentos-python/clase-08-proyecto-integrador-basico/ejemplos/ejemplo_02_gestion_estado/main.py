"""Ejemplo 02: Clase de Estado TaskManager."""
class TaskManager:
    def __init__(self):
        self.tareas = []

    def agregar(self, titulo: str):
        self.tareas.append({"id": len(self.tareas) + 1, "titulo": titulo, "hecho": False})

    def listar(self):
        return self.tareas

tm = TaskManager()
tm.agregar("Aprender Python con Wisrovi")
print("Tareas actuales:", tm.listar())
