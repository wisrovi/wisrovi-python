"""Demostración de Pilas (LIFO) y Colas (FIFO) con collections.deque."""
from collections import deque

# 1. Pila (LIFO)
pila = []
pila.append("Página 1")
pila.append("Página 2")
pila.append("Página 3")
print("Tope de la pila extraído:", pila.pop())  # Página 3

# 2. Cola (FIFO)
cola = deque()
cola.append("Cliente A")
cola.append("Cliente B")
cola.append("Cliente C")
print("Primer cliente atendido:", cola.popleft())  # Cliente A
