"""Ejercicio: Implementar validador de paréntesis balanceados."""

def son_parentesis_validos(cadena: str) -> bool:
    pila = []
    mapa = {")": "(", "}": "{", "]": "["}
    for char in cadena:
        if char in mapa.values():
            pila.append(char)
        elif char in mapa:
            if not pila or pila.pop() != mapa[char]:
                return False
    return len(pila) == 0

if __name__ == "__main__":
    test = "{[()()]}"
    print(f"¿Es '{test}' válido?:", son_parentesis_validos(test))
