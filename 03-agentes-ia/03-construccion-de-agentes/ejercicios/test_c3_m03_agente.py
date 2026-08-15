import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_03_agente_validador import AgentePresupuesto

def test_agente_aprobado():
    ag = AgentePresupuesto(1000.0)
    res = ag.evaluar_gasto([{"nombre": "A", "monto": 200.0}])
    assert res["aprobado"] is True

def test_agente_rechazado():
    ag = AgentePresupuesto(500.0)
    res = ag.evaluar_gasto([{"nombre": "A", "monto": 600.0}])
    assert res["aprobado"] is False
