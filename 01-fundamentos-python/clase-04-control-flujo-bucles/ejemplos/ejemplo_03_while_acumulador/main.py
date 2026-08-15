"""Ejemplo 03: Bucle while con Acumulador."""
ahorro_actual = 0
meta = 100
deposito_semanal = 25
semanas = 0

while ahorro_actual < meta:
    ahorro_actual += deposito_semanal
    semanas += 1
    print(f"Semana {semanas}: Total ahorrado = ${ahorro_actual}")

print(f"🎯 Meta alcanzada en {semanas} semanas.")
