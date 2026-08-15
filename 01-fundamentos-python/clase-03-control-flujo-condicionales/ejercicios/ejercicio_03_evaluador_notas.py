# ==============================================================================
# 🏋️ CLASE 3 - Ejercicio Práctico: Evaluador de Notas
# ==============================================================================

nota = int(input("Ingresa tu nota (0-100): "))

if nota >= 90:
    print("🏆 Excelente (A)")
elif nota >= 80:
    print("🌟 Sobresaliente (B)")
elif nota >= 70:
    print("👍 Aprobado (C)")
else:
    print("📚 Necesita reforzar (D)")
