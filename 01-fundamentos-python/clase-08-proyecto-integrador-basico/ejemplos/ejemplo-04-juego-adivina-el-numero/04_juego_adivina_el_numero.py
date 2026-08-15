# ==============================================================================
# 🐍 CLASE 8 - Ejemplo 04: Adivina el Número
# ==============================================================================

import random

secreto = random.randint(1, 10)

while True:
    try:
        intento = int(input("Adivina (1-10): "))
        if intento == secreto:
            print("🎉 ¡Adivinaste!")
            break
        elif intento < secreto:
            print("📈 Es Mayor")
        else:
            print("📉 Es Menor")
    except ValueError:
        print("⚠️ Número inválido")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Uso de módulos integrados de Python (random) para lógica de juegos.")
print("="*60)
