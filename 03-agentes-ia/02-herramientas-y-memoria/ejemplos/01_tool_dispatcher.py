"""Motor de despacho dinámico de herramientas (Tool Calling)."""
import math

def calcular_hipotenusa(a: float, b: float) -> float:
    """Calcula la hipotenusa de un triángulo rectángulo."""
    return math.sqrt(a**2 + b**2)

REGISTRO_HERRAMIENTAS = {
    "calcular_hipotenusa": calcular_hipotenusa
}

def ejecutar_tool_call(nombre_fn: str, kwargs: dict):
    if nombre_fn in REGISTRO_HERRAMIENTAS:
        return REGISTRO_HERRAMIENTAS[nombre_fn](**kwargs)
    raise ValueError(f"Herramienta '{nombre_fn}' no registrada.")

res = ejecutar_tool_call("calcular_hipotenusa", {"a": 3.0, "b": 4.0})
print("Resultado Tool Call:", res)
