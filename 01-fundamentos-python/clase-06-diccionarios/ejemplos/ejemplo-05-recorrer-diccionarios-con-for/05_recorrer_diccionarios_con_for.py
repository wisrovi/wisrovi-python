# ==============================================================================
# 🐍 CLASE 6 - Ejemplo 05: Recorrer con .items()
# ==============================================================================

precios = {"Manzana": 1.5, "Plátano": 0.8}

for producto, precio in precios.items():
    print(f"🍎 {producto}: ${precio:.2f}")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. .items() devuelve parejas (clave, valor) en cada ciclo del bucle for.")
print("="*60)
