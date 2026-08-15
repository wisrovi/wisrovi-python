# ==============================================================================
# 🐍 CLASE 8 - Ejemplo 01: Manejo de errores (try / except)
# ==============================================================================

try:
    num = int(input("Ingresa un número: "))
    print(f"Número válido: {num}")
except ValueError:
    print("⚠️ Error: No ingresaste un entero. Se usará 0.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. try/except evita que el programa colapse ante un error inesperado del usuario.")
print("="*60)
