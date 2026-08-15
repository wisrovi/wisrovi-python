"""Carga Segura de API Keys."""
import os
key = os.environ.get('API_KEY', 'default_key')
print('Key cargada:', key)
