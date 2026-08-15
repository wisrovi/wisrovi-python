# ==============================================================================
# 🐍 CLASE 7 - Ejemplo 05: Scope (Alcance)
# ==============================================================================

global_var = "Pública"

def funcion():
    local_var = "Privada"
    print("Dentro:", global_var, local_var)

funcion()
print("Fuera:", global_var)

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Las variables creadas dentro de una función son LOCALES.")
print("="*60)
