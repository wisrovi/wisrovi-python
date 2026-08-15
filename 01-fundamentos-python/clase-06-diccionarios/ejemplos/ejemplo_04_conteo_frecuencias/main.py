"""Ejemplo 04: Contador de Frecuencias."""
texto = "python es genial y python es muy rapido"
frecuencias = {}

for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencias)
