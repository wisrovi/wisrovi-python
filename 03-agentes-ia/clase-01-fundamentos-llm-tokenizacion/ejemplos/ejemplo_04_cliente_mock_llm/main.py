"""Cliente de Inferencia Simulado."""
class MockLLM:
    def generar(self, p): return f'Respuesta a: {p}'
print(MockLLM().generar('Hola'))
