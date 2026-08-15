"""Ejemplo 04: Identidad en Memoria (id() y operador 'is')."""
a = "Python"
b = a

print(f"Dirección de 'a': {id(a)}")
print(f"Dirección de 'b': {id(b)}")
print(f"¿Apuntan al mismo objeto?: {a is b}")

# Reasignación crea un nuevo objeto
a = a + " 3.12"
print(f"Nueva dirección de 'a': {id(a)}")
print(f"¿Siguen siendo iguales?: {a is b}")
