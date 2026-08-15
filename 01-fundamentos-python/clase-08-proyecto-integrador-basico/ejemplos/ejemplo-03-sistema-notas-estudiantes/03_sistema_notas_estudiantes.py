# ==============================================================================
# 🐍 CLASE 8 - Ejemplo 03: Sistema de Notas
# ==============================================================================

estudiantes = [{"nombre": "Ana", "nota": 90}, {"nombre": "Carlos", "nota": 80}]

def promedio(lista):
    return sum(e["nota"] for e in lista) / len(lista)

print("Promedio de la clase:", promedio(estudiantes))

# ==============================================================================
# 📘 ACLARACIÓN DEL CONCEPTO APRENDIDO EN ESTE EJEMPLO:
# ==============================================================================
print("\n" + "="*60)
print("💡 RESUMEN DEL CONCEPTO (¿Qué aprendimos en este ejemplo?):")
print("1. Combinar estructuras de datos y funciones permite crear sistemas reales complejos.")
print("="*60)
