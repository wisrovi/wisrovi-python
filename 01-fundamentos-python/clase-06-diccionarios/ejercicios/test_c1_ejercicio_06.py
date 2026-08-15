import subprocess, sys

def test_ejercicio_06():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-06-diccionarios/ejercicios/ejercicio_06_agenda_contactos.py'],
        input="Carlos\n987654\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Carlos: 987654" in res.stdout
