"""Servicio de Inferencia Desacoplado."""
class AgentService:
    def ask(self, q): return f'Respuesta a: {q}'
print(AgentService().ask('Hola'))
