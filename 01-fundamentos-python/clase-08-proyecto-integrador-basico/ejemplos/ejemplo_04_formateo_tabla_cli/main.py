"""Ejemplo 04: Formateo de Tablas en Consola."""
registros = [
    {"id": 1, "tarea": "Diseñar API", "estado": "✅ Lista"},
    {"id": 2, "tarea": "Escribir Tests", "estado": "⏳ Pendiente"}
]

print(f"{'ID':<4} | {'TAREA':<20} | {'ESTADO':<10}")
print("-" * 40)
for r in registros:
    print(f"{r['id']:<4} | {r['tarea']:<20} | {r['estado']:<10}")
