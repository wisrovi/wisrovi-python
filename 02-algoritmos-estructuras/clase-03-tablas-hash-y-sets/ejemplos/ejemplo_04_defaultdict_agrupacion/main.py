"""Agrupación con collections.defaultdict."""
from collections import defaultdict
agrupados = defaultdict(list)
agrupados['frutas'].append('Manzana')
print(dict(agrupados))
