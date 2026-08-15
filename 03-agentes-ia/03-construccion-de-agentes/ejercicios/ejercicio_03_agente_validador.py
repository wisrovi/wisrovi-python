"""Ejercicio: Agente evaluador de presupuestos."""

class AgentePresupuesto:
    def __init__(self, limite_maximo: float):
        self.limite = limite_maximo

    def evaluar_gasto(self, items: list[dict[str, float]]) -> dict:
        total = sum(i["monto"] for i in items)
        aprobado = total <= self.limite
        return {
            "total_solicitado": total,
            "limite": self.limite,
            "aprobado": aprobado,
            "mensaje": "Aprobado" if aprobado else "Excede presupuesto"
        }

if __name__ == "__main__":
    ag = AgentePresupuesto(500.0)
    res = ag.evaluar_gasto([{"nombre": "Suscripción", "monto": 120.0}, {"nombre": "Hardware", "monto": 300.0}])
    print(res)
