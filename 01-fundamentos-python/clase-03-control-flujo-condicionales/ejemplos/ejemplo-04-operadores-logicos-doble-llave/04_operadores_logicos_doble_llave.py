# ==============================================================================
# 🐍 CLASE 3 - Ejemplo 04: La Cerradura de Doble Llave (and, or, not)
# ==============================================================================

usuario_valido = True
clave_correcta = True

if usuario_valido and clave_correcta:
    print("🔓 ACCESO CONCEDIDO: Usuario y contraseña correctos.")
else:
    print("🔒 ACCESO DENEGADO.")

es_feriado = True
es_fin_de_semana = False

if es_feriado or es_fin_de_semana:
    print("🎉 ¡Hoy no se trabaja!")

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. 'and' requiere que TODAS las condiciones sean verdaderas.")
print("2. 'or' requiere que AL MENOS UNA condición sea verdadera.")
print("3. 'not' invierte el valor de verdad (not True es False).")
print("="*60)
