"""Ejemplo 02: Casting y Conversión Segura de Tipos con Funciones."""

def calcular_precio_total(precio_str: str, cantidad_str: str, impuesto_porcentaje: float = 21.0) -> float:
    """Realiza casting explícito de cadenas a float e int, y calcula el total con impuestos."""
    precio_unitario: float = float(precio_str)
    cantidad: int = int(cantidad_str)
    
    subtotal: float = precio_unitario * cantidad
    total_con_impuesto: float = subtotal * (1 + (impuesto_porcentaje / 100))
    return round(total_con_impuesto, 2)

entrada_precio: str = "45.90"
entrada_cantidad: str = "3"

total_pagar = calcular_precio_total(entrada_precio, entrada_cantidad)

print(f"Precio recibido (str):    '{entrada_precio}'")
print(f"Cantidad recibida (str):  '{entrada_cantidad}'")
print(f"Total calculado con IVA:  ${total_pagar:.2f} (Tipo retornado: {type(total_pagar).__name__})")

