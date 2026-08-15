import subprocess, sys

def test_ejercicio_03():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-03-control-flujo-condicionales/ejercicios/ejercicio_03_evaluador_notas.py'],
        input="95\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Excelente (A)" in res.stdout
