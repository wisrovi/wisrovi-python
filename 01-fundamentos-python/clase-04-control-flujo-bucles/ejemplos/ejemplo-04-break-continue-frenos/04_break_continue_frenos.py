# ==============================================================================
# 🐍 CLASE 4 - Ejemplo 04: Frenos de Emergencia (break)
# ==============================================================================

piezas = ["Pieza 1", "Pieza 2", "Pieza Defectuosa ❌", "Pieza 4"]

for pieza in piezas:
    if "Defectuosa" in pieza:
        print("🚨 SE DETECTÓ DEFECTO. ¡Deteniendo cinta con break!")
        break
    print("📦 Empacando:", pieza)

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'break' destruye el bucle y sale de él inmediatamente.")
print("2. 'continue' salta la iteración actual y pasa a la siguiente.")
print("="*60)
