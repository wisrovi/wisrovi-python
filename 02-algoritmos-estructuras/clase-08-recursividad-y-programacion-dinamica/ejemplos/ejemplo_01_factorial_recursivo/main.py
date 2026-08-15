"""Caso Base y Paso Recursivo."""
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
print('Factorial(5):', factorial(5))
