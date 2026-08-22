"""Ejemplo 03: F-Strings Avanzados y Funciones de Formateo Financiero."""

def generar_recibo_compra(producto: str, precio_base: float, descuento: float) -> str:
    """Genera un recibo estructurado aplicando alineación, porcentajes y formato decimal."""
    monto_descuento: float = precio_base * descuento
    total_final: float = precio_base - monto_descuento
    
    recibo = (
        f"{'=' * 45}\n"
        f"{'RESUMEN DE COMPRA':^45}\n"
        f"{'=' * 45}\n"
        f"Producto:     {producto:<25}\n"
        f"Precio Base:  ${precio_base:>8.2f}\n"
        f"Descuento:    {descuento * 100:>7.1f}%\n"
        f"Ahorro:       ${monto_descuento:>8.2f}\n"
        f"{'-' * 45}\n"
        f"Total Pagar:  ${total_final:>8.2f}\n"
        f"{'=' * 45}"
    )
    return recibo

recibo_texto = generar_recibo_compra("Teclado Mecánico RGB", 89.9543, 0.15)
print(recibo_texto)

