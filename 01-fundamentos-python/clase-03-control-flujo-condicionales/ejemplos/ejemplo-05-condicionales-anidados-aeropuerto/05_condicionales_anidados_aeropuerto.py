# ==============================================================================
# 🐍 CLASE 3 - Ejemplo 05: El Filtro del Aeropuerto (Anidados)
# ==============================================================================

pasaporte = True
peso_maleta = 22

if pasaporte:
    print("✅ Pasaporte válido. Verificando equipaje...")
    if peso_maleta <= 23:
        print("✅ Equipaje dentro del límite. ¡Buen viaje!")
    else:
        print("⚠️ Exceso de equipaje.")
else:
    print("❌ No puede ingresar sin pasaporte.")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Un 'if' anidado es una condición colocada dentro de otra condición previa.")
print("2. Permite verificar requisitos por etapas o niveles de profundidad.")
print("="*60)
