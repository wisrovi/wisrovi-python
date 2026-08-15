"""Ejemplo 02: Escalera de Condiciones elif."""
nota = 87

if nota >= 90:
    rango = "Sobresaliente (A)"
elif nota >= 80:
    rango = "Notable (B)"
elif nota >= 70:
    rango = "Aprobado (C)"
else:
    rango = "Refuerzo (D)"

print(f"Puntaje {nota}/100 -> Clasificación: {rango}")
