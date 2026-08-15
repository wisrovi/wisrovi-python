# ==============================================================================
# 🐍 CLASE 6 - Ejemplo 02: Modificar claves
# ==============================================================================

producto = {"nombre": "Laptop", "precio": 899.99}
producto["precio"] = 799.99  # Modificar
producto["stock"] = 15       # Añadir nuevo

print("Producto actualizado:", producto)

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Si la clave existe, dict['clave'] = nuevo_valor actualiza su contenido.")
print("2. Si la clave no existe, la crea automáticamente.")
print("="*60)
