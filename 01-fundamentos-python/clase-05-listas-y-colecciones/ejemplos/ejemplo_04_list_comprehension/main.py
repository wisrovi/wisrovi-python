"""Ejemplo 04: List Comprehension."""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cuadrados de números pares
pares_al_cuadrado = [n**2 for n in numeros if n % 2 == 0]
print("Pares al cuadrado:", pares_al_cuadrado)
