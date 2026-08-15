"""Supervisor de Tareas."""
class Supervisor:
    def coordinar(self, t): return f'Aprobado: {t}'
print(Supervisor().coordinar('Reporte'))
