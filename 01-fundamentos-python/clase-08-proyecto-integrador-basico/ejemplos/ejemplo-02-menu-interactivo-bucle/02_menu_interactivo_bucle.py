# ==============================================================================
# 🐍 CLASE 8 - Ejemplo 02: Menú interactivo
# ==============================================================================

saldo = 100

while True:
    print("\n1. Saldo | 2. Salir")
    op = input("Opción: ")
    if op == "1":
        print(f"Saldo: ${saldo}")
    elif op == "2":
        print("👋 ¡Hasta luego!")
        break

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'while True' crea un menú interactivo permanente que solo se cierra con 'break'.")
print("="*60)
