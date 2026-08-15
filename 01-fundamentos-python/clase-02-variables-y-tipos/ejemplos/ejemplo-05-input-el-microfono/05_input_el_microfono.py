# ==============================================================================
# 🐍 CLASE 2 - Ejemplo 05: El Micrófono Interactivo (input)
# ==============================================================================

nombre = input("🎤 Escribe tu nombre: ")
print(f"¡Hola {nombre}!")

anio_txt = input("🎤 ¿En qué año naciste?: ")
anio_num = int(anio_txt)

edad = 2026 - anio_num
print(f"En 2026 cumples o cumpliste {edad} años.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. input() pausa el programa y espera a que el usuario escriba algo por teclado.")
print("2. ATENCIÓN: input() SIEMPRE devuelve un dato de tipo String (texto).")
print("3. Para números, usa int() o float() sobre la respuesta.")
print("="*60)
