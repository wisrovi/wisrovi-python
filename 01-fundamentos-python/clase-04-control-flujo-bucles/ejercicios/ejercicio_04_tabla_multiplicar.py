# ==============================================================================
# 🏋️ CLASE 4 - Ejercicio Práctico: Tabla de Multiplicar
# ==============================================================================

numero = int(input("¿De qué número deseas ver la tabla?: "))

print(f"--- TABLA DEL {numero} ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
