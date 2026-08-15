"""Verificación de Fuentes y Citas."""
def validar_cita(res, ctx): return 'Horario' in res and 'Horario' in ctx
print('¿Cita válida?:', validar_cita('Horario 9-18h', 'Horario 9-18h'))
