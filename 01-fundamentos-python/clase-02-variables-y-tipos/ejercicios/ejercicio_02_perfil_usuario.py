# ==============================================================================
# 🏋️ CLASE 2 - Ejercicio Práctico: Perfil de Usuario con Funciones y Tipado
# ==============================================================================

def procesar_perfil_consumo(ciudad: str, precio_bebida_str: str, cantidad: int = 5) -> str:
    """Convierte la entrada de precio a float y genera un informe de consumo tipado."""
    precio_num: float = float(precio_bebida_str)
    total: float = precio_num * cantidad
    
    return (
        f"\n--- PERFIL GENERADO ---\n"
        f"Ciudad:               {ciudad.strip()}\n"
        f"Precio por bebida:    ${precio_num:.2f}\n"
        f"Cantidad semanal:     {cantidad}\n"
        f"Total estimado ({cantidad}x): ${total:.2f}"
    )

if __name__ == "__main__":
    try:
        ciudad_input = input("1. ¿En qué ciudad vives?: ")
        precio_input = input("2. Precio de tu bebida favorita ($): ")
        
        resultado = procesar_perfil_consumo(ciudad_input, precio_input)
        print(resultado)
    except ValueError:
        print("⚠️ Error: Ingresa un valor numérico válido para el precio.")

