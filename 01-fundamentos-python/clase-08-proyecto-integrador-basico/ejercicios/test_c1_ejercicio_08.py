import subprocess, sys

def test_ejercicio_08():
    res = subprocess.run([sys.executable, '01-fundamentos-python/clase-08-proyecto-integrador-basico/ejercicios/ejercicio_08_reto_final.py'], capture_output=True, text=True)
    assert res.returncode == 0
    assert "FELICIDADES" in res.stdout
