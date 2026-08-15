# ==============================================================================
# 🐍 CLASE 3 - Ejemplo 02: La Moneda al Aire (if / else)
# ==============================================================================

saldo_cuenta = 150
precio_articulo = 200

if saldo_cuenta >= precio_articulo:
    print("✅ COMPRA EXITOSA: Transacción aprobada.")
else:
    saldo_faltante = precio_articulo - saldo_cuenta
    print(f"❌ COMPRA RECHAZADA: Te faltan ${saldo_faltante}.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'else' define la acción de respaldo cuando el 'if' es FALSO.")
print("2. Garantiza que uno de los dos caminos SIEMPRE se ejecute.")
print("="*60)
