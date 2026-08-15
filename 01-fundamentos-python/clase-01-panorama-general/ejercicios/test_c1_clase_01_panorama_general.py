import subprocess, sys
def test_c1_clase_01():
    res = subprocess.run([sys.executable, "-c", "print('Hola Python!')"], capture_output=True, text=True)
    assert res.returncode == 0
