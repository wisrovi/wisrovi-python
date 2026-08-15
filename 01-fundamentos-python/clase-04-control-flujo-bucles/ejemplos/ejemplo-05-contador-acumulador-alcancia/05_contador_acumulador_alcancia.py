# ==============================================================================
# 🐍 CLASE 4 - Ejemplo 05: La Alcancía (Contadores y Acumuladores)
# ==============================================================================

monedas = [5, 10, 2, 5, 20]
total_ahorrado = 0
cantidad_monedas = 0

for m in monedas:
    total_ahorrado += m
    cantidad_monedas += 1

print(f"Monedas ingresadas: {cantidad_monedas}")
print(f"Total ahorrado: ${total_ahorrado}")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Un CONTADOR se suma en 1 en cada vuelta (c += 1).")
print("2. Un ACUMULADOR suma valores variables en cada vuelta (a += valor).")
print("="*60)
