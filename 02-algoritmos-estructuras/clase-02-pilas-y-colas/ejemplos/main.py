"""Clase 02: Pilas (Stacks) y Colas (Queues) con collections.deque - Código de Demostración."""
from collections import deque

# 1. Pila (Stack LIFO)
def balanceado(expr: str) -> bool:
    pila = []
    mapa = {")": "(", "}": "{", "]": "["}
    for char in expr:
        if char in mapa.values(): pila.append(char)
        elif char in mapa:
            if not pila or pila.pop() != mapa[char]: return False
    return len(pila) == 0

# 2. Cola (Queue FIFO)
cola = deque(["Ticket 1", "Ticket 2", "Ticket 3"])
cola.append("Ticket 4")
print("Atendido:", cola.popleft())  # Ticket 1
print("Es valido:", balanceado("{[()]}"))
