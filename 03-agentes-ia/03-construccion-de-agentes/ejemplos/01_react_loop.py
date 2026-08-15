"""Bucle autónomo ReAct (Reasoning + Acting)."""

class SimpleReActAgent:
    def __init__(self, tools: dict):
        self.tools = tools
        self.history = []

    def step(self, thought: str, action: str, action_input: dict):
        self.history.append({"thought": thought, "action": action})
        if action in self.tools:
            obs = self.tools[action](**action_input)
            self.history.append({"observation": obs})
            return obs
        return "Error: Acción desconocida"

tools = {"sumar": lambda a, b: a + b}
agente = SimpleReActAgent(tools)
res = agente.step("Necesito sumar dos montos", "sumar", {"a": 25, "b": 75})
print("Observación final:", res)
