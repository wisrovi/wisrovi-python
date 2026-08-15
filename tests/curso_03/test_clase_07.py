"""Tests de validación para Clase 07: Agentes Autónomos y el Ciclo Cognitivo ReAct."""
def test_c3_clase_07():
    class Agent:
        def act(self): return "Done"
    a = Agent()
    assert a.act() == "Done"

