"""Ejemplo 03: Validación Segura de Entradas."""
def leer_entero_seguro(mensaje: str, default: int = 1) -> int:
    try:
        return int(default)
    except ValueError:
        print("Entrada inválida. Usando valor por defecto.")
        return default

val = leer_entero_seguro("Opción: ", default=3)
print(f"Opción procesada: {val}")
