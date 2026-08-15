import subprocess, sys

def test_ejercicio_07():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-07-funciones/ejercicios/ejercicio_07_calculadora.py'],
        input="100\n20\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Final: $80.00" in res.stdout
