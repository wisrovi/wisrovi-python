"""
Ejemplo 05: Operadores Aritméticos, División Entera (//), Módulo (%) y Asignación Aumentada (+=).
Demostración de Funciones Modulares Tipadas (PEP 484).
"""

from typing import Dict, List


def calcular_estadisticas_division(dividendo: int, divisor: int) -> Dict[str, float]:
    """Calcula cociente exacto (/), cociente entero (//) y residuo (%) entre dos números."""
    if divisor == 0:
        raise ZeroDivisionError("El divisor no puede ser cero.")

    cociente_real: float = dividendo / divisor
    cociente_entero: int = dividendo // divisor
    residuo: int = dividendo % divisor
    potencia: int = dividendo ** 2

    return {
        "division_real": cociente_real,
        "division_entera": float(cociente_entero),
        "modulo_residuo": float(residuo),
        "cuadrado_dividendo": float(potencia),
    }


def calcular_interes_compuesto(
    capital_inicial: float, tasa_anual: float, anios: int
) -> float:
    """Calcula el capital final acumulado usando el operador de potenciación (**)."""
    # Fórmula: M = C * (1 + r)^t
    monto_final = capital_inicial * ((1.0 + (tasa_anual / 100.0)) ** anios)
    return round(monto_final, 2)


def simular_caja_registradora(saldo_inicial: float, compras: List[float]) -> float:
    """Demuestra el uso de operadores de asignación aumentada (+=, -=)."""
    saldo_acumulado: float = saldo_inicial
    print(f"Saldo Inicial en Caja: ${saldo_acumulado:.2f}")

    for monto in compras:
        saldo_acumulado += monto
        print(f"  + Cobro registrado: ${monto:>6.2f} | Nuevo Subtotal: ${saldo_acumulado:>8.2f}")

    return round(saldo_acumulado, 2)


if __name__ == "__main__":
    print("=" * 60)
    print("🧮 1. OPERADORES DE DIVISIÓN, MÓDULO Y POTENCIACIÓN")
    print("=" * 60)
    stats = calcular_estadisticas_division(dividendo=17, divisor=5)
    print(f"Dividiendo 17 entre 5:")
    print(f"  • División Real (/):      {stats['division_real']:.2f}")
    print(f"  • División Entera (//):   {int(stats['division_entera'])}")
    print(f"  • Módulo / Residuo (%):   {int(stats['modulo_residuo'])}")
    print(f"  • Cuadrado 17^2 (**):     {int(stats['cuadrado_dividendo'])}")

    print("\n" + "=" * 60)
    print("📈 2. CÁLCULO DE INTERÉS COMPUESTO (**)")
    print("=" * 60)
    capital = 1000.0
    tasa = 7.5
    tiempo = 5
    resultado_inversion = calcular_interes_compuesto(capital, tasa, tiempo)
    print(f"Inversión de ${capital:.2f} al {tasa}% a {tiempo} años: ${resultado_inversion:.2f}")

    print("\n" + "=" * 60)
    print("💳 3. ASIGNACIÓN AUMENTADA (+=)")
    print("=" * 60)
    ventas = [45.50, 120.00, 15.99, 89.40]
    total_caja = simular_caja_registradora(500.0, ventas)
    print(f"Balance Final de Caja: ${total_caja:.2f}")
