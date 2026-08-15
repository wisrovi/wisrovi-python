# ==============================================================================
# 🐍 CLASE 2 - Ejemplo 01: El Collar de Letras (Strings)
# ==============================================================================

saludo = "¡Hola a todos!"
nombre_curso = 'Fundamentos de Python'

mensaje_concatenado = saludo + " Bienvenido a " + nombre_curso
print("Unido con '+':", mensaje_concatenado)

mensaje_fstring = f"{saludo} Estás en el curso {nombre_curso}."
print("Usando f-string:", mensaje_fstring)

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Los STRINGS (str) son secuencias de texto encerradas en comillas.")
print("2. Podemos unir dos textos usando el operador '+'.")
print("3. Las f-strings f\"{variable}\" permiten insertar datos directamente dentro del texto.")
print("="*60)
