# ==============================================================================
# 🐍 CLASE 3 - Ejemplo 03: El Menú del Restaurante (elif múltiple)
# ==============================================================================

opcion = 2

if opcion == 1:
    print("👨‍🍳 Marchando una Pizza 🍕")
elif opcion == 2:
    print("👨‍🍳 Marchando una Hamburguesa 🍔")
elif opcion == 3:
    print("👨‍🍳 Marchando una Ensalada 🥗")
else:
    print("❓ Opción no válida. Servir plato del día.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'elif' (abreviatura de else-if) permite evaluar múltiples condiciones en cadena.")
print("2. Se evalúan en orden de arriba a abajo. Al encontrar la primera verdadera, se detiene.")
print("="*60)
