#!/usr/bin/env python3
"""
🧪 Simulador Visual de Memoria Heap y Referencias en Python
Herramienta interactiva para explorar en tiempo real:
1. Direcciones de memoria hexadecimales (id).
2. Operador de identidad ('is') vs operador de igualdad ('==').
3. Inmutabilidad de tipos primitivos (int, float, str, bool).
4. Tamaño en bytes en memoria RAM (sys.getsizeof).
"""

import sys

def separador(titulo: str):
    print("\n" + "=" * 65)
    print(f"🔬 {titulo.upper()}")
    print("=" * 65)

def main():
    print("🚀 INICIANDO SIMULADOR DE MEMORIA (CLASE 02: VARIABLES Y TIPOS)")
    
    # --------------------------------------------------------------------------
    # 1. Las Cajas Etiquetadas en Memoria
    # --------------------------------------------------------------------------
    separador("1. Asignación y Referencias en Memoria")
    nombre_a = "Python 3.12"
    nombre_b = nombre_a
    
    print(f"Variable nombre_a: '{nombre_a}' | Dirección: {hex(id(nombre_a))} | Bytes: {sys.getsizeof(nombre_a)}")
    print(f"Variable nombre_b: '{nombre_b}' | Dirección: {hex(id(nombre_b))} | Bytes: {sys.getsizeof(nombre_b)}")
    print(f"¿Apuntan al mismo objeto en memoria? (nombre_a is nombre_b): {nombre_a is nombre_b}")
    
    # --------------------------------------------------------------------------
    # 2. Inmutabilidad en Acción (Reasignación)
    # --------------------------------------------------------------------------
    separador("2. Inmutabilidad y Reasignación de Memoria")
    print("⚡ Modificando nombre_a...")
    nombre_a += " (Edición 2026)"
    
    print(f"Variable nombre_a: '{nombre_a}' | Nueva Dirección: {hex(id(nombre_a))}")
    print(f"Variable nombre_b: '{nombre_b}' | Dirección Original: {hex(id(nombre_b))}")
    print(f"¿Siguen apuntando al mismo objeto? (nombre_a is nombre_b): {nombre_a is nombre_b}")
    print("💡 Conclusión: Los tipos primitivos en Python son inmutables; modificar crea un objeto nuevo.")

    # --------------------------------------------------------------------------
    # 3. Igualdad de Contenido (==) vs Identidad de Memoria (is)
    # --------------------------------------------------------------------------
    separador("3. Operador '==' vs Operador 'is'")
    lista_1 = [1, 2, 3]
    lista_2 = [1, 2, 3]
    
    print(f"lista_1: {lista_1} | Dirección: {hex(id(lista_1))}")
    print(f"lista_2: {lista_2} | Dirección: {hex(id(lista_2))}")
    print(f"¿Tienen el mismo contenido? (lista_1 == lista_2): {lista_1 == lista_2} (Verdadero)")
    print(f"¿Son el mismo objeto en memoria? (lista_1 is lista_2): {lista_1 is lista_2} (Falso)")
    print("💡 Regla de Oro: Usa '==' para comparar valores y 'is' para verificar identidad de objeto o 'None'.")

    # --------------------------------------------------------------------------
    # 4. Tabla de Inspección de Tipos Primitivos
    # --------------------------------------------------------------------------
    separador("4. Tabla de Tipos Primitivos y Consumo de Memoria")
    ejemplos = [
        (42, "Entero (int)"),
        (3.14159, "Flotante (float)"),
        ("Hola Mundo", "Texto (str)"),
        (True, "Booleano (bool)"),
        (None, "Nulo (NoneType)")
    ]
    print(f"{'Valor':<15} | {'Tipo':<15} | {'Bytes en RAM':<12} | {'Dirección Hexadecimal'}")
    print("-" * 65)
    for val, tipo_desc in ejemplos:
        print(f"{str(val):<15} | {type(val).__name__:<15} | {sys.getsizeof(val):<12} | {hex(id(val))}")

    # --------------------------------------------------------------------------
    # 5. Funciones ('La Licuadora') y Paso de Parámetros en Memoria
    # --------------------------------------------------------------------------
    separador("5. Paso de Variables a Funciones (Call by Object Reference)")
    
    def procesar_saldo(monto: float, bono: float) -> float:
        print(f"  -> [Scope Local Función] ID 'monto' recibido: {hex(id(monto))}")
        nuevo_monto = monto + bono
        print(f"  -> [Scope Local Función] ID 'nuevo_monto' creado: {hex(id(nuevo_monto))}")
        return nuevo_monto

    saldo_cuenta: float = 1500.50
    bonificacion: float = 250.0
    
    print(f"Variable global 'saldo_cuenta': {saldo_cuenta} | ID: {hex(id(saldo_cuenta))}")
    saldo_final = procesar_saldo(saldo_cuenta, bonificacion)
    print(f"Variable global 'saldo_final':  {saldo_final} | ID: {hex(id(saldo_final))}")
    print("💡 Conclusión: La función recibe la referencia del objeto; al sumar se instancia un nuevo float en el Heap.")

    print("\n✨ SIMULACIÓN DE MEMORIA COMPLETADA EXITOSAMENTE.\n")

if __name__ == "__main__":
    main()
