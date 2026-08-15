# ==============================================================================
# 🏋️ CLASE 2 - Ejercicio Práctico: Perfil de Usuario
# ==============================================================================

ciudad = input("1. ¿En qué ciudad vives?: ")
precio_str = input("2. Precio de tu bebida favorita ($): ")

precio_num = float(precio_str)
total = precio_num * 5

print("\n--- PERFIL GENERADO ---")
print(f"Ciudad: {ciudad}")
print(f"Precio por bebida: ${precio_num:.2f}")
print(f"Total por 5 bebidas: ${total:.2f}")
