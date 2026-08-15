# ==============================================================================
# 🐍 CLASE 8 - Ejemplo 05: Gestor de Tareas To-Do Completo
# ==============================================================================

tareas = []

def agregar(desc):
    tareas.append({"desc": desc, "done": False})
    print("✅ Tarea agregada.")

def listar():
    for i, t in enumerate(tareas, 1):
        st = "☑️" if t["done"] else "🔲"
        print(f"{i}. [{st}] {t['desc']}")

while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar | 2. Ver | 3. Salir")
    op = input("Opción: ")
    if op == "1":
        agregar(input("Tarea: "))
    elif op == "2":
        listar()
    elif op == "3":
        print("🚀 ¡Felicidades por completar el Curso 1!")
        break

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Un programa completo combina estructura, interacción, funciones y colecciones.")
print("="*60)
