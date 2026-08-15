"""Módulo Estándar bisect."""
import bisect
datos = [10, 20, 30, 40]
idx = bisect.bisect_left(datos, 25)
print('Punto de inserción para 25:', idx)
