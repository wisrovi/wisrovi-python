# ==============================================================================
# 🐍 CLASE 6 - Ejemplo 03: Métodos (.keys, .values, .get)
# ==============================================================================

pais = {"nombre": "España", "capital": "Madrid"}

print("Claves:", list(pais.keys()))
print("Valores:", list(pais.values()))
print("Búsqueda segura:", pais.get("idioma", "No especificado"))

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. .keys() obtiene todas las claves del diccionario.")
print("2. .get('clave', por_defecto) evita que el programa se rompa si la clave no existe.")
print("="*60)
