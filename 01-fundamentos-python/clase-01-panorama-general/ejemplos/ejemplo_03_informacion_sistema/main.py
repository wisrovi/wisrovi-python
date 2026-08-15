"""Ejemplo 03: Inspección del Entorno del Intérprete."""
import sys
import platform

print(f"Versión de Python: {platform.python_version()}")
print(f"Sistema Operativo: {platform.system()} ({platform.machine()})")
print(f"Ruta del ejecutable: {sys.executable}")
