"""Ejemplo 02: Escalera de Condiciones elif."""

# Opcion 1: Escalera de condiciones elif
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


# Opcion 2: Escalera de condiciones elif con rango de notas
nota = 62

if nota >= 90:
    rango = "Sobresaliente (A)"
else:
    if nota >= 80:
        rango = "Notable (B)"
    else:
        if nota >= 70:
            rango = "Aprobado (C)"
        else:
            rango = "Refuerzo (D)"

print(f"Puntaje {nota}/100 -> Clasificación: {rango}")
