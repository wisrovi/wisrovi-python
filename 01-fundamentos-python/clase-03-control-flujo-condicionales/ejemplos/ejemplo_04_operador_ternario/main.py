"""Ejemplo 04: Expresión Condicional Ternaria."""
estado_servidor = 200

if estado_servidor == 200:
    mensaje = "OK - Operativo"
else:
    mensaje = "ERROR - Fallo"
print(f"Estado HTTP {estado_servidor}: {mensaje}")


# Sintaxis: valor_si_true if condicion else valor_si_false
mensaje = "OK - Operativo" if estado_servidor == 200 else "ERROR - Fallo"

print(f"Estado HTTP {estado_servidor}: {mensaje}")
