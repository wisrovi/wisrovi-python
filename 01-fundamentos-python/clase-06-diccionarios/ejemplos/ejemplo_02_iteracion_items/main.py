"""Ejemplo 02: Iteración sobre Diccionarios."""
precios = {"Laptop": 1200, "Monitor": 300, "Teclado": 80}

for producto, precio in precios.items():
    print(f"📦 {producto:<10}: ${precio:>4}")
