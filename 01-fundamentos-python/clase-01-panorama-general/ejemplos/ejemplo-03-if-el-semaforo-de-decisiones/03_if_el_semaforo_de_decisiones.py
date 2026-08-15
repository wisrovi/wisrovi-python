# ==============================================================================
# 🐍 CLASE 1 - Ejemplo 03: El Semáforo de Decisiones (if / else)
# ==============================================================================

estatura_visitante = 1.55
estatura_minima = 1.40

print("Estatura del visitante:", estatura_visitante, "m")

if estatura_visitante >= estatura_minima:
    print("🚦 SEMÁFORO VERDE: ¡Adelante! Puedes subir a la montaña rusa. 🎢")
else:
    print("🚦 SEMÁFORO ROJO: Aún eres un poco bajo para este juego. 🛑")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. El bloque 'if' permite tomar decisiones evaluando una condición.")
print("2. Si la condición es VERDADERA (True), se ejecuta el bloque sangrado debajo de 'if'.")
print("3. Si la condición es FALSA (False), se ejecuta el bloque debajo de 'else'.")
print("="*60)
