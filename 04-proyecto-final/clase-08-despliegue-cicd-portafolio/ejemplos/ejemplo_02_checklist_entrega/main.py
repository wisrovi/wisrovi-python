"""Checklist de Verificación de Entrega."""
check = {'tests': True, 'docker': True, 'readme': True}
print('¿Listo para entrega?:', all(check.values()))
