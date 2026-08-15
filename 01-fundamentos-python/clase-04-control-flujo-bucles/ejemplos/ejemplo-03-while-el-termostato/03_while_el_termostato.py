# ==============================================================================
# 🐍 CLASE 4 - Ejemplo 03: El Termostato Inteligente (while)
# ==============================================================================

temperatura = 25
meta = 22

while temperatura > meta:
    print(f"❄️ Aire encendido... Temp actual: {temperatura}°C")
    temperatura -= 1

print(f"✅ Temperatura meta alcanzada ({temperatura}°C).")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'while' se repite indefinidamente MIENTRAS la condición sea True.")
print("2. Debes modificar la variable adentro para evitar un 'bucle infinito'.")
print("="*60)
