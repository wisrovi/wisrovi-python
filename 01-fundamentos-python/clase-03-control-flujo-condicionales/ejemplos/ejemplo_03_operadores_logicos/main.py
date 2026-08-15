"""Ejemplo 03: Operadores Lógicos and / or / not."""
tiene_ticket = True
es_vip = False
edad = 22

# Cortocircuito: si tiene_ticket es False, no evalúa lo siguiente
if (tiene_ticket and edad >= 18) or es_vip:
    print("🎉 ¡Bienvenido al evento exclusivo!")
else:
    print("❌ No cumples los requisitos de ingreso.")
