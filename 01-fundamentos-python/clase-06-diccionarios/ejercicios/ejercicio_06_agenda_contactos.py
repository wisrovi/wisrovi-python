# ==============================================================================
# 🏋️ CLASE 6 - Ejercicio Práctico: Agenda
# ==============================================================================

agenda = {"Mamá": "123456"}
nombre = input("Nombre: ")
tel = input("Teléfono: ")
agenda[nombre] = tel

for k, v in agenda.items():
    print(f"{k}: {v}")
