"""Preservación de Estado con session_state."""
state = {'counter': 1}
state['counter'] += 1
print('Contador de sesión:', state['counter'])
