"""Ejemplo 04: Indentación y Jerarquía de Bloques."""
activo = True

if activo:
    # Bloque nivel 1 (4 espacios)
    print("Nivel 1: El sistema está activo.")
    if True:
        # Bloque nivel 2 (8 espacios)
        print("    Nivel 2: Verificación secundaria aprobada.")

print("Fuera del bloque condicional (Nivel 0).")
