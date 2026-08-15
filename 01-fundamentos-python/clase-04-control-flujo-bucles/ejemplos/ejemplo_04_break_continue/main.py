"""Ejemplo 04: break y continue en Bucles."""
numeros = [12, -4, 0, 45, 999, 88]

for n in numeros:
    if n < 0:
        print(f"Saltando número negativo: {n}")
        continue  # Salta a la siguiente iteración
    if n == 999:
        print("🚨 Código de parada 999 detectado. Deteniendo bucle.")
        break  # Rompe el bucle por completo
    print(f"Procesando dato válido: {n}")
