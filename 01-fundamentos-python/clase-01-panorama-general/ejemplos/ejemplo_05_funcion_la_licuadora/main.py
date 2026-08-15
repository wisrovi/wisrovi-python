"""Ejemplo 05: La Licuadora (Funciones con def)."""
def licuadora(fruta1: str, fruta2: str) -> str:
    """Recibe ingredientes y devuelve un batido preparado."""
    return f"Batido refrescante de {fruta1} con {fruta2} 🥤"

# Invocamos la función
resultado = licuadora("Fresa 🍓", "Plátano 🍌")
print(resultado)
