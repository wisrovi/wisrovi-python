import subprocess, sys

def test_ejercicio_01():
    res = subprocess.run([sys.executable, '01-fundamentos-python/clase-01-panorama-general/ejercicios/ejercicio_01_mi_primer_vistazo.py'], capture_output=True, text=True)
    assert res.returncode == 0
    assert "¡Hola!" in res.stdout
