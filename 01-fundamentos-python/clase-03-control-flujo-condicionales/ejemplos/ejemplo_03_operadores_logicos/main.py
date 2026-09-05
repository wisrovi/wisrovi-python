"""Ejemplo 03: Operadores Lógicos and / or / not."""

tiene_ticket = False
es_vip = False
edad = 22

# opcion 1: usando operadores lógicos and / or
# Cortocircuito: si tiene_ticket es False, no evalúa lo siguiente
if (tiene_ticket==True and edad >= 18) or es_vip==True:
    print("🎉 ¡Bienvenido al evento exclusivo!")
else:
    print("❌ No cumples los requisitos de ingreso.")


# opcion 2: usando operadores lógicos and / or / not
if tiene_ticket == True:
    if edad >= 18:
        print("🎉 ¡Bienvenido al evento exclusivo!")
    else:
        print("❌ No cumples los requisitos de ingreso.")
else:
    if es_vip == True:
        print("🎉 ¡Bienvenido al evento exclusivo!")
    else:
        print("❌ No cumples los requisitos de ingreso.")