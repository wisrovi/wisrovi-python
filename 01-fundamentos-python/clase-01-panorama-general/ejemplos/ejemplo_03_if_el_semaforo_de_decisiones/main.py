"""Ejemplo 03: El Semáforo de Decisiones (if / else)."""
estatura_visitante = 1.55
estatura_minima = 1.40

print(f"Estatura del visitante: {estatura_visitante} m")

if estatura_visitante >= estatura_minima:
    print("🚦 SEMÁFORO VERDE: ¡Adelante! Puedes subir a la montaña rusa. 🎢")
else:
    print("🚦 SEMÁFORO ROJO: Aún eres un poco bajo para este juego. 🛑")

print("\n" + "="*50)
print("💡 Resumen: 'if' evalúa condiciones booleanas para decidir.")
print("="*50)
