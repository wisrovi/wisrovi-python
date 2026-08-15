import subprocess, sys

def test_ejercicio_04():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-04-control-flujo-bucles/ejercicios/ejercicio_04_tabla_multiplicar.py'],
        input="7\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "7 x 10 = 70" in res.stdout
