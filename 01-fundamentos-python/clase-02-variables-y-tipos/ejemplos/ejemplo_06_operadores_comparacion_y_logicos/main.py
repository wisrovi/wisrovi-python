"""
Ejemplo 06: Operadores de Comparación (==, !=, <, >, <=, >=) y Operadores Lógicos (and, or, not).
Demostración de Evaluación en Cortocircuito y Validación de Accesos.
"""


def validar_acceso_plataforma(
    edad: int, tiene_membresia: bool, saldo_creditos: int, es_admin: bool = False
) -> bool:
    """Evalúa reglas de negocio combinando operadores relacionales y lógicos."""
    # Regla: Los administradores siempre acceden O los usuarios mayores de edad con membresía y créditos
    acceso_regular: bool = (edad >= 18) and tiene_membresia and (saldo_creditos > 0)
    acceso_concedido: bool = es_admin or acceso_regular

    return acceso_concedido


def clasificar_rango_temperatura(
    temp_celsius: float, min_confort: float = 20.0, max_confort: float = 25.0
) -> str:
    """Demuestra encadenamiento de comparaciones (min <= temp <= max) típico en Python."""
    es_temperatura_ideal: bool = min_confort <= temp_celsius <= max_confort
    esta_fuera_de_rango: bool = not es_temperatura_ideal

    if es_temperatura_ideal:
        return f"🌡️ {temp_celsius:.1f}°C: Rango de Confort Óptimo ({min_confort}°C - {max_confort}°C)"
    elif temp_celsius < min_confort:
        return f"❄️ {temp_celsius:.1f}°C: Ambiente Frío (Requiere Calefacción)"
    else:
        return f"🔥 {temp_celsius:.1f}°C: Ambiente Caluroso (Requiere Ventilación)"


def demostracion_cortocircuito_logico(numero: int) -> bool:
    """Muestra cómo 'and' evita evaluar la segunda condición si la primera es False (previene ZeroDivisionError)."""
    # Si numero == 0, 'numero != 0' es False, y Python NO ejecuta '(100 / numero) > 2'
    resultado_seguro: bool = (numero != 0) and ((100 / numero) > 2)
    return resultado_seguro


if __name__ == "__main__":
    print("=" * 60)
    print("🛡️ 1. VALIDACIÓN LÓGICA DE ACCESOS (and, or, not)")
    print("=" * 60)

    casos = [
        {"nombre": "Ana (Admin)", "edad": 17, "membresia": False, "creditos": 0, "admin": True},
        {"nombre": "Carlos (Cliente VIP)", "edad": 25, "membresia": True, "creditos": 10, "admin": False},
        {"nombre": "Sofía (Sin créditos)", "edad": 30, "membresia": True, "creditos": 0, "admin": False},
        {"nombre": "Mateo (Menor de edad)", "edad": 16, "membresia": True, "creditos": 50, "admin": False},
    ]

    for usuario in casos:
        permitido = validar_acceso_plataforma(
            edad=usuario["edad"],
            tiene_membresia=usuario["membresia"],
            saldo_creditos=usuario["creditos"],
            es_admin=usuario["admin"],
        )
        icono = "✅ PERMITIDO" if permitido else "❌ DENEGADO "
        print(f"{icono} | {usuario['nombre']:<25} -> Acceso: {permitido}")

    print("\n" + "=" * 60)
    print("🌡️ 2. COMPARACIONES ENCADENADAS (20.0 <= temp <= 25.0)")
    print("=" * 60)
    muestras = [16.5, 22.4, 29.8]
    for temp in muestras:
        print(clasificar_rango_temperatura(temp))

    print("\n" + "=" * 60)
    print("⚡ 3. CORTOCIRCUITO LÓGICO Y PREVENCIÓN DE ERRORES")
    print("=" * 60)
    print(f"Evaluando numero = 10 -> {demostracion_cortocircuito_logico(10)} (100/10 = 10 > 2)")
    print(f"Evaluando numero = 0  -> {demostracion_cortocircuito_logico(0)} (Cortocircuito previene división por 0)")
