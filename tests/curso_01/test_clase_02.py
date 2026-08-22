"""Tests de validación para Clase 02: Variables, Tipos de Datos y Funciones con Type Hints."""

import importlib.util
import os
import pytest

RETO_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../01-fundamentos-python/clase-02-variables-y-tipos/ejercicios/reto.py",
    )
)

spec = importlib.util.spec_from_file_location("reto_c1_c2", RETO_PATH)
reto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reto)


def test_c1_clase_02_tipado_basico():
    precio = 50.0
    total = precio * 1.21
    assert total == pytest.approx(60.5)


def test_c1_clase_02_calcular_propina():
    assert reto.calcular_propina(100.0, 15.0) == 15.0
    assert reto.calcular_propina(85.50, 10.0) == 8.55
    assert reto.calcular_propina(50.0, 0.0) == 0.0


def test_c1_clase_02_calcular_total_por_persona():
    # Cuenta $100 con 10% de propina = $110 / 2 personas = $55 cada una
    cuota = reto.calcular_total_por_persona(100.0, 10.0, 2)
    assert cuota == 55.0

    # Cuenta $60 con 20% propina = $72 / 3 personas = $24 cada una
    cuota_3 = reto.calcular_total_por_persona(60.0, 20.0, 3)
    assert cuota_3 == 24.0


def test_c1_clase_02_error_division_cero():
    with pytest.raises(ValueError, match="mayor a 0"):
        reto.calcular_total_por_persona(100.0, 10.0, 0)


def test_c1_clase_02_formatear_factura():
    resumen = reto.formatear_factura(100.0, 15.0, 57.50)
    assert "Subtotal:" in resumen
    assert "$100.00" in resumen
    assert "Propina:" in resumen
    assert "$15.00" in resumen
    assert "$115.00" in resumen


