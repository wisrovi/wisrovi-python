# ==============================================================================
# 🐍 CLASE 6 - Ejemplo 04: Diccionarios Anidados
# ==============================================================================

empresa = {
    "empresa": "Tech S.A.",
    "empleado": {"nombre": "Elena", "puesto": "Dev"}
}

print("Empleado:", empresa["empleado"]["nombre"])

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Podemos anidar diccionarios colocando uno como valor de otro.")
print("2. Para acceder encadenamos corchetes: dict[clave1][clave2].")
print("="*60)
