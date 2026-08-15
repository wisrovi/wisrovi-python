# ==============================================================================
# 🐍 CLASE 2 - Ejemplo 04: Adaptadores de Enchufe (Casting)
# ==============================================================================

edad_texto = "25"
print("Tipo inicial de edad_texto:", type(edad_texto).__name__)

edad_numero = int(edad_texto)
print("Tipo después de int():", type(edad_numero).__name__)

edad_siguiente = edad_numero + 1
print(f"El próximo año tendrás {edad_siguiente} años.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'Casting' es convertir un dato de un tipo a otro.")
print("2. int('25') convierte el texto '25' al número 25.")
print("3. Indispensable cuando recibimos datos como texto y queremos operar numéricamente.")
print("="*60)
