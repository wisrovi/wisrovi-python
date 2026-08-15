import subprocess, sys

def test_ejercicio_05():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-05-listas-y-colecciones/ejercicios/ejercicio_05_gestion_inventario.py'],
        input="Zapatos\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Zapatos" in res.stdout
