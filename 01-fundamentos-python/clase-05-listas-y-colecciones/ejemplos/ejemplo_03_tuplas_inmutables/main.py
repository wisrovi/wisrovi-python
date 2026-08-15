"""Ejemplo 03: Tuplas e Inmutabilidad."""
coordenadas: tuple[float, float] = (38.8794, -6.9706)  # Badajoz, España

latitud, longitud = coordenadas  # Desempaquetado
print(f"Latitud: {latitud} | Longitud: {longitud}")
