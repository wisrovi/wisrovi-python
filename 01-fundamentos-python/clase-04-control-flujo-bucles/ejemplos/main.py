"""Clase 04: Control de Flujo: Bucles (for / while) - Código de Demostración."""
ventas = [120.0, 45.5, 300.0, 89.9]
total = 0.0

for venta in ventas:
    if venta < 50.0:
        continue
    total += venta

print(f"Total de ventas > $50: ${total:.2f}")
