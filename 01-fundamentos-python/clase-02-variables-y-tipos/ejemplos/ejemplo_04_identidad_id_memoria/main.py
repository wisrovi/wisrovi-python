"""Ejemplo 04: Identidad en Memoria (id), Operador 'is' y Parámetros en Funciones."""


def modificar_contador(
    contador: int,
) -> int:
    """Demuestra que los enteros son inmutables: modificarlos dentro de la función crea un nuevo objeto."""

    print(f"  [Dentro de función] ID al recibir:            {hex(id(contador))}")

    contador = contador + 10

    print(f"  [Dentro de función] ID tras 'contador + 10':  {hex(id(contador))}")

    return contador


saldo_original: int = 100

print(f"1. ID 'saldo_original' fuera de la función:     {hex(id(saldo_original))}")

saldo_nuevo = modificar_contador(saldo_original)

print(
    f"2. ID 'saldo_original' tras la llamada:         {hex(id(saldo_original))} (Valor: {saldo_original})"
)
print(
    f"3. ID 'saldo_nuevo' retornado:                  {hex(id(saldo_nuevo))} (Valor: {saldo_nuevo})"
)
print(
    f"¿Apuntan al mismo bloque de memoria?:           {saldo_original is saldo_nuevo}"
)
