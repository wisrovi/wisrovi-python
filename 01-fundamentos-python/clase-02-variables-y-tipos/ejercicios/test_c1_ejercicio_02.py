import subprocess, sys

def test_ejercicio_02():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-02-variables-y-tipos/ejercicios/ejercicio_02_perfil_usuario.py'],
        input="Madrid\n4.50\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Ciudad: Madrid" in res.stdout
    assert "Total por 5 bebidas: $22.50" in res.stdout
