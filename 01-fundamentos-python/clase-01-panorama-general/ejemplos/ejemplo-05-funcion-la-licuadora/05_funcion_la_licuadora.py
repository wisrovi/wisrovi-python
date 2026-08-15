# ==============================================================================
# 🐍 CLASE 1 - Ejemplo 05: La Licuadora (Funciones def y return)
# ==============================================================================

def preparar_jugo(fruta_1, fruta_2):
    print(f"⚙️ Mezclando {fruta_1} con {fruta_2}...")
    jugo_listo = f"🍹 Delicioso Jugo de {fruta_1} y {fruta_2}"
    return jugo_listo

# Usamos la función 2 veces con diferentes ingredientes
resultado_1 = preparar_jugo("Fresa", "Plátano")
print("Resultado 1:", resultado_1)

resultado_2 = preparar_jugo("Naranja", "Zanahoria")
print("Resultado 2:", resultado_2)

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Una FUNCIÓN ('def') es un bloque de código reutilizable con un nombre.")
print("2. Los PARÁMETROS son los datos que le pasamos a la función entre paréntesis.")
print("3. La palabra 'return' devuelve el resultado de la función para usarlo fuera de ella.")
print("="*60)
