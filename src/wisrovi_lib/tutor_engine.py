#!/usr/bin/env python3
"""
Motor de Contenidos y Guía Pedagógica del Tutor Virtual (Wisrovi Academy).
Estructura las 32 clases semanales a través de los 4 Cursos Oficiales:
1. Curso 1: Fundamentos Básicos de Python (Clases 01-08)
2. Curso 2: Algoritmos Avanzados y Estructuras de Datos (Clases 01-08)
3. Curso 3: Desarrollo de Agentes de Inteligencia Artificial (Clases 01-08)
4. Curso 4: Taller Práctico & Proyecto Integrador Full-Stack (Clases 01-08)
"""

from typing import Dict, List, Any, Optional

CLASS_CURRICULUM: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # CURSO 1: FUNDAMENTOS BÁSICOS DE PYTHON (01-08)
    # =========================================================================
    "1-1": {
        "course_num": 1,
        "class_num": 1,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 01: Primer Vistazo Práctico (print, variables, if, for, def)",
        "metaphor": "El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)",
        "theory": """En esta sesión inaugural exploramos los 4 pilares esenciales del software:
1. **El Megáfono (`print`)**: Comunica datos y resultados al usuario en consola.
2. **Las Cajas Etiquetadas (Variables)**: Guardan información en memoria RAM mediante asignación `=`.
3. **El Semáforo (`if/else`)**: Evalúa condiciones booleanas (`True`/`False`) para bifurcar el camino lógico.
4. **La Cinta Transportadora (`for`)**: Procesa colecciones de elementos uno tras otro de forma secuencial.""",
        "mermaid": """flowchart LR
    A["📢 1. El Megáfono<br/>print('¡Hola!')"] --> B["📦 2. Las Cajas<br/>usuario = 'Wisrovi'"]
    B --> C{"🚦 3. El Semáforo<br/>¿edad >= 18?"}
    C -->|Verdadero| D["⚙️ 4. La Cinta<br/>for item in lista"]
    C -->|Falso| E["⛔ Acceso Denegado"]
    D --> F["🎯 Retorno / Salida"]
    E --> F

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style E fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style F fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """# 1. El Megáfono (print)
print("¡Bienvenido a Wisrovi Academy!")

# 2. Las Cajas (Variables)
usuario = "Wisrovi"
nivel = 1

# 3. El Semáforo (if/else)
if nivel == 1:
    print(f"Hola {usuario}, inicias como: Aprendiz")

# 4. La Cinta Transportadora (for)
habilidades = ["Variables", "Condicionales", "Bucles", "Funciones"]
for h in habilidades:
    print("-> Dominando:", h)""",
        "playground_code": """# 🔬 ARENERO DE PRUEBAS: Experimenta con variables y condiciones
nombre = "Alex"
edad = 20
es_programador = True

print(f"Estudiante: {nombre} | Edad: {edad}")

if edad >= 18 and es_programador:
    print("🚀 ¡Listo para construir Agentes de IA!")
else:
    print("🌱 Continúa aprendiendo paso a paso.")""",
        "challenge_prompt": "Crea una función llamada `evaluar_estudiante(nombre: str, edad: int) -> str` que retorne el texto 'Mayor de edad' si tiene 18 o más, o 'Menor de edad' en caso contrario.",
        "challenge_starter": """def evaluar_estudiante(nombre: str, edad: int) -> str:
    # ✍️ Escribe aquí tu solución
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
""",
        "socratic_hints": [
            "💡 Pista 1: Usa la condición 'if edad >= 18:' para verificar la mayoría de edad.",
            "💡 Pista 2: La función debe retornar exactamente las cadenas 'Mayor de edad' o 'Menor de edad'.",
            "💡 Pista 3: Comprueba que el tipo de retorno sea 'str'."
        ],
        "boss_battle": False
    },

    "1-2": {
        "course_num": 1,
        "class_num": 2,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 02: Variables, Tipos de Datos y Funciones con Type Hints",
        "metaphor": "Las Cajas Etiquetadas en Memoria y la Licuadora Tipada (PEP 484)",
        "theory": """En Python, las variables son **etiquetas que apuntan a objetos en la memoria RAM**.
1. **Tipos Primitivos & Type Hints (PEP 484)**: `int`, `float`, `str`, `bool`. Anotar parámetros (`x: float`) y retorno (`-> float`) previene errores de diseño.
2. **Inmutabilidad**: Modificar un tipo primitivo crea un *nuevo* objeto en una dirección hex diferente.
3. **Inspección de Memoria**: `type()`, `id()` y `sys.getsizeof()` revelan la huella física del dato.""",
        "mermaid": """flowchart LR
    subgraph Entrada["📥 Variables en Heap"]
        V1["💵 total = 100.0<br/>(float | 24 B)"]
        V2["🏷️ tasa = 15<br/>(int | 28 B)"]
    end
    subgraph Funcion["🥤 Función Tipada"]
        PARAMS["Parámetros: (total: float, tasa: float)"]
        OP["Operación: total * (tasa / 100)"]
        RET["Retorno: -> float"]
        PARAMS --> OP --> RET
    end
    subgraph Salida["📤 Objeto Resultado"]
        RES["🎯 15.0 (float)"]
    end
    V1 --> PARAMS
    V2 --> PARAMS
    RET --> RES
    style Entrada fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style Funcion fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style Salida fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """import sys

def calcular_propina(total_cuenta: float, porcentaje: float) -> float:
    return total_cuenta * (porcentaje / 100.0)

propina = calcular_propina(100.0, 15.0)
print(f"Propina: ${propina:.2f} | Memoria: {sys.getsizeof(propina)} bytes")""",
        "playground_code": """import sys
entero = 42
flotante = 3.1416
texto = "Wisrovi"

print(f"Tipo entero: {type(entero).__name__} | Bytes: {sys.getsizeof(entero)}")
print(f"Tipo texto:  {type(texto).__name__}  | Bytes: {sys.getsizeof(texto)}")""",
        "challenge_prompt": "Crea una función llamada `identificar_tipo_y_tamano(valor: Any) -> tuple[str, int]` que retorne una tupla con el nombre del tipo (ej: 'int', 'str') y su tamaño en bytes mediante `sys.getsizeof(valor)`.",
        "challenge_starter": """import sys
from typing import Any, Tuple

def identificar_tipo_y_tamano(valor: Any) -> Tuple[str, int]:
    # ✍️ Retorna (nombre_tipo, tamano_bytes)
    return (type(valor).__name__, sys.getsizeof(valor))
""",
        "socratic_hints": [
            "💡 Pista 1: Usa `type(valor).__name__` para obtener la cadena con el nombre del tipo.",
            "💡 Pista 2: Usa `sys.getsizeof(valor)` para obtener los bytes ocupados en RAM.",
            "💡 Pista 3: Retorna ambos valores dentro de una tupla `(tipo_str, bytes_int)`."
        ],
        "boss_battle": False
    },

    "1-3": {
        "course_num": 1,
        "class_num": 3,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 03: Control de Flujo: Condicionales (if / elif / else)",
        "metaphor": "El Semáforo y las Puertas Lógicas",
        "theory": """El control de flujo permite a un programa tomar decisiones inteligentes:
1. **Bifurcaciones `if / elif / else`**: Evalúan expresiones booleanas de arriba hacia abajo.
2. **Operadores de Comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
3. **Operadores Lógicos**: `and`, `or`, `not` para componer reglas complejas.""",
        "mermaid": """flowchart TD
    A["🚦 Entrada: Nota del Examen"] --> B{"¿nota >= 90?"}
    B -->|Sí| C["🌟 Excelente"]
    B -->|No| D{"¿nota >= 60?"}
    D -->|Sí| E["✅ Aprobado"]
    D -->|No| F["❌ Reprobado"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style E fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style F fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px""",
        "demo_code": """def clasificar_nota(nota: float) -> str:
    if nota >= 90:
        return "Excelente"
    elif nota >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

print("85 ->", clasificar_nota(85))
print("95 ->", clasificar_nota(95))
print("45 ->", clasificar_nota(45))""",
        "playground_code": """edad = 21
tiene_pase_vip = True

if edad >= 18 and tiene_pase_vip:
    print("💎 Acceso al salón VIP concedido")
elif edad >= 18:
    print("🎫 Acceso general concedido")
else:
    print("⛔ Acceso denegado a menores")""",
        "challenge_prompt": "Crea una función llamada `clasificar_calificacion(nota: float) -> str` que retorne 'Excelente' si nota >= 90, 'Aprobado' si 60 <= nota < 90, y 'Reprobado' si nota < 60.",
        "challenge_starter": """def clasificar_calificacion(nota: float) -> str:
    # ✍️ Escribe tu lógica condicional
    if nota >= 90:
        return "Excelente"
    elif nota >= 60:
        return "Aprobado"
    return "Reprobado"
""",
        "socratic_hints": [
            "💡 Pista 1: Empieza evaluando el caso más restrictivo: `if nota >= 90:`",
            "💡 Pista 2: Usa `elif nota >= 60:` para el caso de Aprobado.",
            "💡 Pista 3: Retorna 'Reprobado' en el `else:` final."
        ],
        "boss_battle": False
    },

    "1-4": {
        "course_num": 1,
        "class_num": 4,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 04: Control de Flujo: Bucles (for / while & range)",
        "metaphor": "La Cinta Transportadora y el Contador Infinito",
        "theory": """Los bucles automatizan tareas repetitivas de forma determinista:
1. **Bucle `for`**: Itera sobre secuencias finitas (`range`, listas, cadenas).
2. **Bucle `while`**: Repite mientras una condición booleana sea verdadera.
3. **Sentencias de Control**: `break` para abortar y `continue` para saltar a la siguiente iteración.""",
        "mermaid": """flowchart LR
    A["📦 range(inicio, fin + 1)"] --> B["⚙️ for numero in rango"]
    B --> C{"¿Es Par? (numero % 2 == 0)"}
    C -->|Sí| D["➕ Sumar al Acumulador"]
    C -->|No| E["⏭️ Saltar"]
    D --> F["🎯 Retornar Total"]
    E --> B
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style F fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """# Sumar números impares del 1 al 10
total_impares = 0
for i in range(1, 11):
    if i % 2 != 0:
        total_impares += i
print("Suma de impares (1..10):", total_impares)""",
        "playground_code": """contador = 5
while contador > 0:
    print(f"🚀 Despegue en {contador}...")
    contador -= 1
print("🌟 ¡Lanzamiento exitoso!")""",
        "challenge_prompt": "Crea una función `sumar_rango_pares(inicio: int, fin: int) -> int` que retorne la suma de todos los números pares entre `inicio` y `fin` (ambos inclusive).",
        "challenge_starter": """def sumar_rango_pares(inicio: int, fin: int) -> int:
    # ✍️ Acumula los pares
    total = 0
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            total += num
    return total
""",
        "socratic_hints": [
            "💡 Pista 1: Recuerda usar `range(inicio, fin + 1)` para incluir el valor final.",
            "💡 Pista 2: Comprueba si un número es par con `num % 2 == 0`.",
            "💡 Pista 3: Acumula el resultado en una variable `total = 0` y retórnala."
        ],
        "boss_battle": False
    },

    "1-5": {
        "course_num": 1,
        "class_num": 5,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 05: Listas, Tuplas y Colecciones Básicas",
        "metaphor": "El Archivador Dinámico (Listas) y las Cajas Selladas (Tuplas)",
        "theory": """Estructuras lineales de datos para organizar colecciones:
1. **Listas (`list`)**: Mutables, ordenadas, permiten `append`, `pop`, `sort`.
2. **Tuplas (`tuple`)**: Inmutables, ideales para registros de solo lectura o claves hash.
3. **List Comprehensions**: Sintaxis compacta y rápida para filtrar y transformar colecciones.""",
        "mermaid": """flowchart LR
    A["📥 Lista Original: ['sol', 'python', 'ia', 'codigo']"] --> B["⚙️ Filtro: len >= 4"]
    B --> C["🔤 Transformación: .upper()"]
    C --> D["📊 Ordenamiento: sorted()"]
    D --> E["📤 ['CODIGO', 'PYTHON']"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """frutas = ["manzana", "banana", "kiwi", "cereza"]
frutas_largas = [f.upper() for f in frutas if len(f) > 5]
print("Frutas de más de 5 letras:", sorted(frutas_largas))""",
        "playground_code": """lenguajes = ["Python", "Rust", "Go", "TypeScript"]
lenguajes.append("C++")
print("Total lenguajes:", len(lenguajes))
print("Primer y último:", lenguajes[0], lenguajes[-1])""",
        "challenge_prompt": "Crea una función `filtrar_y_ordenar_palabras(palabras: list[str]) -> list[str]` que filtre palabras con longitud >= 4, las transforme a mayúsculas y las devuelva ordenadas alfabéticamente.",
        "challenge_starter": """def filtrar_y_ordenar_palabras(palabras: list[str]) -> list[str]:
    # ✍️ Filtra longitud >= 4, convierte a .upper() y retorna sorted()
    resultado = [p.upper() for p in palabras if len(p) >= 4]
    return sorted(resultado)
""",
        "socratic_hints": [
            "💡 Pista 1: Puedes usar una list comprehension: `[p.upper() for p in palabras if len(p) >= 4]`",
            "💡 Pista 2: Usa la función nativa `sorted(...)` para ordenar la lista resultante.",
            "💡 Pista 3: Verifica que palabras de menos de 4 letras sean descartadas."
        ],
        "boss_battle": False
    },

    "1-6": {
        "course_num": 1,
        "class_num": 6,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 06: Diccionarios y Conjuntos (Sets)",
        "metaphor": "La Agenda Telefónica O(1) y el Filtro de Elementos Únicos",
        "theory": """Estructuras basadas en tablas hash para acceso ultra-rápido $O(1)$:
1. **Diccionarios (`dict`)**: Pares clave-valor (`{key: value}`). Métodos `.get()`, `.keys()`, `.values()`, `.items()`.
2. **Conjuntos (`set`)**: Colecciones no duplicadas (`{1, 2, 3}`). Operaciones de unión `|`, intersección `&` y diferencia `-`.""",
        "mermaid": """flowchart LR
    A["📝 Texto: 'python es genial python es potente'"] --> B["⚙️ split() en palabras"]
    B --> C["📦 Diccionario Hash O(1)"]
    C --> D["📊 {'python': 2, 'es': 2, 'genial': 1, 'potente': 1}"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """texto = "hola mundo hola python"
frecuencia = {}
for p in texto.split():
    frecuencia[p] = frecuencia.get(p, 0) + 1
print("Frecuencia de palabras:", frecuencia)""",
        "playground_code": """tags_a = {"python", "ai", "backend"}
tags_b = {"ai", "frontend", "docker"}
print("Intersección:", tags_a & tags_b)
print("Unión completa:", tags_a | tags_b)""",
        "challenge_prompt": "Crea una función `contar_frecuencia_palabras(texto: str) -> dict[str, int]` que reciba un texto, lo divida en palabras (en minúsculas) y retorne un diccionario con el conteo de apariciones de cada palabra.",
        "challenge_starter": """def contar_frecuencia_palabras(texto: str) -> dict[str, int]:
    # ✍️ Divide con .lower().split() y cuenta con dict
    frecuencias = {}
    for palabra in texto.lower().split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias
""",
        "socratic_hints": [
            "💡 Pista 1: Convierte el texto a minúsculas con `texto.lower()` y sepáralo con `.split()`.",
            "💡 Pista 2: Usa `frecuencias.get(palabra, 0) + 1` para incrementar la cuenta de forma segura.",
            "💡 Pista 3: Retorna el diccionario final."
        ],
        "boss_battle": False
    },

    "1-7": {
        "course_num": 1,
        "class_num": 7,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 07: Funciones, Parámetros (*args, **kwargs) y Scope",
        "metaphor": "La Licuadora Modular (Entradas Flexibles ➔ Resultado)",
        "theory": """Modularización avanzada del código y reutilización:
1. **Parámetros Posicionales y con Nombre (`*args`, `**kwargs`)**: Permiten funciones de aridad variable.
2. **Scope (LEGB)**: Local, Enclosing, Global, Built-in. Las variables locales viven solo durante la ejecución de la función.
3. **Docstrings & Retornos Múltiples**: Documentar el contrato y retornar diccionarios estructurados.""",
        "mermaid": """flowchart LR
    A["📥 *numeros: (10, 20, 30, 40)"] --> B["🥤 Función calcular_estadisticas"]
    B --> C["📊 total = 100"]
    B --> D["📈 promedio = 25.0"]
    B --> E["🔝 max = 40 | 🔻 min = 10"]
    C & D & E --> F["📤 dict con estadísticas"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style F fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def resumen_ventas(*montos: float) -> dict:
    if not montos: return {"total": 0.0, "promedio": 0.0}
    return {
        "total": sum(montos),
        "promedio": sum(montos) / len(montos),
        "max": max(montos)
    }

print(resumen_ventas(120.5, 450.0, 89.9))""",
        "playground_code": """def saludar_usuario(nombre: str, **opciones):
    prefijo = opciones.get("titulo", "Ingeniero")
    print(f"👋 Saludos, {prefijo} {nombre}")

saludar_usuario("Wisrovi", titulo="Architect")""",
        "challenge_prompt": "Crea una función `calcular_estadisticas(*numeros: float) -> dict[str, float]` que acepte cualquier cantidad de números y retorne un dict con las claves: 'total', 'promedio', 'max' y 'min'.",
        "challenge_starter": """def calcular_estadisticas(*numeros: float) -> dict[str, float]:
    # ✍️ Calcula total, promedio, max y min
    if not numeros:
        return {"total": 0.0, "promedio": 0.0, "max": 0.0, "min": 0.0}
    return {
        "total": float(sum(numeros)),
        "promedio": float(sum(numeros) / len(numeros)),
        "max": float(max(numeros)),
        "min": float(min(numeros))
    }
""",
        "socratic_hints": [
            "💡 Pista 1: Usa `*numeros` para recibir una tupla de valores numéricos variables.",
            "💡 Pista 2: Calcula `sum(numeros)`, `max(numeros)` y `min(numeros)` con las funciones nativas.",
            "💡 Pista 3: Retorna el diccionario con las 4 claves exactas."
        ],
        "boss_battle": False
    },

    "1-8": {
        "course_num": 1,
        "class_num": 8,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 08: Proyecto Integrador: Sistema CLI y Manejo de Excepciones",
        "metaphor": "El Tablero de Control y el Casco de Seguridad (try/except)",
        "theory": """Integración total de los fundamentos de Python en una clase orientada a objetos con control robusto de errores:
1. **Clases y Métodos (`class`, `__init__`)**: Encapsulación de estado y lógica de negocio.
2. **Excepciones (`try`, `except`, `raise`)**: `ValueError`, `KeyError` para contratos defensivos.
3. **Persistencia en Memoria**: Gestión de catálogos mediante diccionarios internos protegidos.""",
        "mermaid": """flowchart TD
    A["🛒 GestorInventario"] --> B["➕ agregar_producto(nombre, stock)"]
    A --> C["🔍 obtener_stock(nombre)"]
    B --> D{"¿stock < 0?"}
    D -->|Sí| E["💥 raise ValueError"]
    D -->|No| F["💾 Guardar en _stock"]
    C --> G{"¿nombre en _stock?"}
    G -->|No| H["💥 raise KeyError"]
    G -->|Sí| I["📤 Retornar stock"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style E fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style H fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style F fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style I fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """class GestorInventarioDemo:
    def __init__(self):
        self._stock = {}

    def agregar(self, item: str, cant: int):
        if cant < 0: raise ValueError("Stock negativo")
        self._stock[item] = self._stock.get(item, 0) + cant

g = GestorInventarioDemo()
g.agregar("Laptop", 5)
print("Inventario:", g._stock)""",
        "playground_code": """try:
    edad = int("veinte")
except ValueError as e:
    print(f"⚠️ Error capturado con éxito: {e}")""",
        "challenge_prompt": "Crea una clase `GestorInventario` con métodos: `__init__(self)` (inicializa dict `self._stock`), `agregar_producto(self, nombre: str, stock: int)` (lanza `ValueError` si stock < 0) y `obtener_stock(self, nombre: str) -> int` (lanza `KeyError` si no existe).",
        "challenge_starter": """class GestorInventario:
    def __init__(self):
        self._stock = {}

    def agregar_producto(self, nombre: str, stock: int):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        self._stock[nombre] = stock

    def obtener_stock(self, nombre: str) -> int:
        if nombre not in self._stock:
            raise KeyError("Producto no encontrado")
        return self._stock[nombre]
""",
        "socratic_hints": [
            "💡 Pista 1: Inicializa `self._stock = {}` en el método `__init__`.",
            "💡 Pista 2: Usa `raise ValueError(...)` cuando `stock < 0`.",
            "💡 Pista 3: Usa `raise KeyError(...)` si `nombre not in self._stock`."
        ],
        "boss_battle": True
    },

    # =========================================================================
    # CURSO 2: ALGORITMOS AVANZADOS Y ESTRUCTURAS DE DATOS (01-08)
    # =========================================================================
    "2-1": {
        "course_num": 2,
        "class_num": 1,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 01: Análisis de Complejidad y Notación Big-O",
        "metaphor": "El Velocímetro y el Odómetro Big-O (Tiempo vs Espacio)",
        "theory": """La notación Big-O formaliza la eficiencia asintótica de un algoritmo al crecer el tamaño $N$:
1. **$O(1)$ Constante**: Acceso a array por índice o búsqueda en tabla hash.
2. **$O(N)$ Lineal**: Búsqueda en listas no ordenadas o un único bucle.
3. **$O(N^2)$ Cuadrático**: Bucles anidados comparando todos contra todos.
4. **Optimización con Conjuntos**: Transformar búsquedas $O(N^2)$ en $O(N)$ usando `set`.""",
        "mermaid": """flowchart LR
    A["📥 Lista con N elementos"] --> B{"Estrategia"}
    B -->|Bucles Anidados| C["❌ O(N²) Ineficiente"]
    B -->|Uso de Hash Set| D["✅ O(N) Tiempo Óptimo"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style C fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """# Detección de duplicados en O(N) vs O(N^2)
def tiene_duplicados_rapido(items: list) -> bool:
    return len(items) != len(set(items))

print("[1, 2, 3, 2] ->", tiene_duplicados_rapido([1, 2, 3, 2]))
print("[1, 2, 3, 4] ->", tiene_duplicados_rapido([1, 2, 3, 4]))""",
        "playground_code": """lista_grande = list(range(10000)) + [42]
vistos = set()
duplicados = [x for x in lista_grande if x in vistos or vistos.add(x)]
print("Duplicado encontrado en O(N):", duplicados)""",
        "challenge_prompt": "Crea una función `encontrar_duplicados_o_n(lista: list[int]) -> set[int]` que encuentre y retorne todos los números que aparecen más de una vez en tiempo lineal O(N) usando un `set` auxiliar.",
        "challenge_starter": """def encontrar_duplicados_o_n(lista: list[int]) -> set[int]:
    # ✍️ Encuentra duplicados en O(N)
    vistos = set()
    duplicados = set()
    for num in lista:
        if num in vistos:
            duplicados.add(num)
        else:
            vistos.add(num)
    return duplicados
""",
        "socratic_hints": [
            "💡 Pista 1: Mantén un conjunto `vistos = set()` para registrar números procesados.",
            "💡 Pista 2: Si el número ya está en `vistos`, agrégalo a `duplicados.add(num)`.",
            "💡 Pista 3: Retorna el conjunto `duplicados`."
        ],
        "boss_battle": False
    },

    "2-2": {
        "course_num": 2,
        "class_num": 2,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 02: Pilas (Stacks) y Colas (Queues) con collections.deque",
        "metaphor": "La Pila de Platos (LIFO) y la Fila del Banco (FIFO)",
        "theory": """Estructuras fundamentales de control secuencial:
1. **Pila (Stack - LIFO)**: Last-In, First-Out. Usada para llamadas a funciones, parseo de paréntesis y backtracking.
2. **Cola (Queue - FIFO)**: First-In, First-Out. Usada para procesamiento de tareas en segundo plano y BFS.
3. **`collections.deque`**: Estructura de doble extremo con inserción/extracción $O(1)$ en ambos lados.""",
        "mermaid": """flowchart LR
    subgraph Pila["🥞 Pila (LIFO)"]
        P1["push('(')"] --> P2["push('[')"] --> P3["pop() -> ']' matched"]
    end
    subgraph Cola["🚶 Cola (FIFO)"]
        Q1["append(cliente_1)"] --> Q2["append(cliente_2)"] --> Q3["popleft() -> cliente_1"]
    end
    style Pila fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style Cola fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px""",
        "demo_code": """from collections import deque

cola = deque(["Tarea 1", "Tarea 2", "Tarea 3"])
cola.append("Tarea 4")
atendida = cola.popleft()
print(f"Atendida: {atendida} | En cola:", list(cola))""",
        "playground_code": """pila = []
pila.append("Página 1")
pila.append("Página 2")
print("Atrás a:", pila.pop())""",
        "challenge_prompt": "Crea una función `validar_parentesis(cadena: str) -> bool` que use una pila (`list`) para verificar si los símbolos '()', '[]' y '{}' están correctamente balanceados y anidados.",
        "challenge_starter": """def validar_parentesis(cadena: str) -> bool:
    # ✍️ Usa una pila para validar balance de () [] {}
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for char in cadena:
        if char in pares.values():
            pila.append(char)
        elif char in pares:
            if not pila or pila.pop() != pares[char]:
                return False
    return len(pila) == 0
""",
        "socratic_hints": [
            "💡 Pista 1: Empuja los caracteres de apertura `(`, `[`, `{` a la pila.",
            "💡 Pista 2: Al encontrar uno de cierre, comprueba si coincide con el `pop()` de la pila.",
            "💡 Pista 3: Retorna `True` únicamente si al final la pila queda vacía (`len(pila) == 0`)."
        ],
        "boss_battle": False
    },

    "2-3": {
        "course_num": 2,
        "class_num": 3,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 03: Tablas Hash y Conjuntos (Sets) para Búsqueda O(1)",
        "metaphor": "El Casillero Postal Inteligente",
        "theory": """Búsquedas en tiempo constante $O(1)$ gracias al direccionamiento por dispersión (Hashing):
1. **Función Hash**: Convierte una clave en un índice numérico de memoria.
2. **Patrón Two-Sum**: Resolver el problema de la suma objetivo en $O(N)$ usando un mapa hash en lugar de $O(N^2)$.
3. **Resolución de Colisiones**: Encadenamiento y sondeo lineal internos en CPython.""",
        "mermaid": """flowchart LR
    A["📥 nums = [2, 7, 11, 15], target = 9"] --> B["⚙️ Iterar num=2: complemento=7"]
    B --> C["💾 Guardar {2: 0} en hash map"]
    C --> D["⚙️ Iterar num=7: complemento=2"]
    D --> E["🎯 ¡Encontrado! Retornar (0, 1)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def two_sum_demo(nums: list[int], target: int) -> tuple[int, int]:
    vistos = {}
    for idx, n in enumerate(nums):
        comp = target - n
        if comp in vistos:
            return (vistos[comp], idx)
        vistos[n] = idx
    return (-1, -1)

print(two_sum_demo([2, 7, 11, 15], 9))""",
        "playground_code": """tabla = {"usuario_1": "Ana", "usuario_2": "Carlos"}
print("Búsqueda O(1):", tabla.get("usuario_1"))""",
        "challenge_prompt": "Crea una función `two_sum_hash(nums: list[int], objetivo: int) -> tuple[int, int]` que encuentre y retorne los dos índices `(i, j)` cuya suma sea igual a `objetivo` en tiempo $O(N)$.",
        "challenge_starter": """def two_sum_hash(nums: list[int], objetivo: int) -> tuple[int, int]:
    # ✍️ Implementa el patrón Two-Sum en O(N)
    mapa = {}
    for i, num in enumerate(nums):
        complemento = objetivo - num
        if complemento in mapa:
            return (mapa[complemento], i)
        mapa[num] = i
    return (-1, -1)
""",
        "socratic_hints": [
            "💡 Pista 1: Almacena cada número y su índice en un diccionario: `mapa[num] = i`.",
            "💡 Pista 2: Para cada número, calcula `complemento = objetivo - num` y consulta `if complemento in mapa:`.",
            "💡 Pista 3: Retorna la tupla con los dos índices `(mapa[complemento], i)`."
        ],
        "boss_battle": False
    },

    "2-4": {
        "course_num": 2,
        "class_num": 4,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 04: Algoritmos de Búsqueda: Lineal vs Binaria O(log n)",
        "metaphor": "El Diccionario Abierto por la Mitad",
        "theory": """Estrategias de búsqueda y división logarítmica:
1. **Búsqueda Lineal**: $O(N)$ explorando elemento por elemento.
2. **Búsqueda Binaria**: $O(\\log N)$ descartando la mitad del espacio de búsqueda en cada paso sobre colecciones ordenadas.
3. **Punteros `left`, `right`, `mid`**: Evitar desbordamientos y manejar correctamente condiciones de parada (`left <= right`).""",
        "mermaid": """flowchart TD
    A["📥 Lista Ordenada [10, 20, 30, 40, 50], target=30"] --> B["📍 mid = (0 + 4)//2 -> arr[2]=30"]
    B -->|arr[mid] == target| C["🎯 ¡Encontrado en índice 2!"]
    B -->|arr[mid] < target| D["👉 left = mid + 1"]
    B -->|arr[mid] > target| E["👈 right = mid - 1"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def busqueda_binaria_demo(arr: list[int], x: int) -> int:
    izq, der = 0, len(arr) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if arr[medio] == x: return medio
        elif arr[medio] < x: izq = medio + 1
        else: der = medio - 1
    return -1

datos = [10, 20, 30, 40, 50, 60, 70]
print("Buscar 40:", busqueda_binaria_demo(datos, 40))""",
        "playground_code": """import bisect
ordenados = [5, 15, 25, 35, 45]
idx = bisect.bisect_left(ordenados, 25)
print("Índice con módulo bisect:", idx)""",
        "challenge_prompt": "Crea una función `busqueda_binaria(ordenados: list[int], objetivo: int) -> int` que retorne el índice del elemento `objetivo` en la lista ordenada, o `-1` si no existe.",
        "challenge_starter": """def busqueda_binaria(ordenados: list[int], objetivo: int) -> int:
    # ✍️ Implementa búsqueda binaria iterativa
    left, right = 0, len(ordenados) - 1
    while left <= right:
        mid = (left + right) // 2
        if ordenados[mid] == objetivo:
            return mid
        elif ordenados[mid] < objetivo:
            left = mid + 1
        else:
            right = mid - 1
    return -1
""",
        "socratic_hints": [
            "💡 Pista 1: Inicializa `left = 0` y `right = len(ordenados) - 1`.",
            "💡 Pista 2: En cada iteración calcula `mid = (left + right) // 2`.",
            "💡 Pista 3: Si `ordenados[mid] < objetivo`, avanza `left = mid + 1`; en caso contrario `right = mid - 1`."
        ],
        "boss_battle": False
    },

    "2-5": {
        "course_num": 2,
        "class_num": 5,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 05: Algoritmos de Ordenamiento: QuickSort y MergeSort",
        "metaphor": "El Organizador de Barajas de Cartas (Divide y Vencerás)",
        "theory": """Algoritmos de ordenamiento basados en el paradigma *Divide y Vencerás*:
1. **QuickSort**: Selecciona un pivote y particiona los elementos en menores, iguales y mayores ($O(N \\log N)$ promedio).
2. **MergeSort**: Divide la lista recursivamente en mitades y las combina de forma ordenada ($O(N \\log N)$ garantizado).
3. **Timsort**: El algoritmo híbrido nativo de Python (`sorted()` / `.sort()`).""",
        "mermaid": """flowchart TD
    A["📥 [8, 3, 1, 7, 0, 10, 2]"] --> B["📍 Pivote = 7"]
    B --> C["Menores: [3, 1, 0, 2]"]
    B --> D["Iguales: [7]"]
    B --> E["Mayores: [8, 10]"]
    C --> F["quick_sort(Menores)"]
    E --> G["quick_sort(Mayores)"]
    F & D & G --> H["📤 [0, 1, 2, 3, 7, 8, 10]"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style H fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def quick_sort_demo(lista: list[int]) -> list[int]:
    if len(lista) <= 1: return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort_demo(menores) + iguales + quick_sort_demo(mayores)

print("Ordenado:", quick_sort_demo([64, 34, 25, 12, 22, 11, 90]))""",
        "playground_code": """desordenados = [9, 3, 7, 1, 5]
print("Timsort nativo:", sorted(desordenados))""",
        "challenge_prompt": "Crea una función `quick_sort(arr: list[int]) -> list[int]` que implemente el algoritmo QuickSort recursivo dividiendo por un elemento pivote.",
        "challenge_starter": """def quick_sort(arr: list[int]) -> list[int]:
    # ✍️ Implementa QuickSort recursivo
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
""",
        "socratic_hints": [
            "💡 Pista 1: El caso base es `if len(arr) <= 1: return arr`.",
            "💡 Pista 2: Elige un pivote como `arr[len(arr) // 2]`.",
            "💡 Pista 3: Concatena `quick_sort(menores) + iguales + quick_sort(mayores)`."
        ],
        "boss_battle": False
    },

    "2-6": {
        "course_num": 2,
        "class_num": 6,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 06: Árboles Binarios de Búsqueda (BST) y Recorridos",
        "metaphor": "El Árbol Genealógico de Decisiones",
        "theory": """Estructura jerárquica no lineal con propiedad de ordenamiento:
1. **Propiedad BST**: Para todo nodo, los valores a la izquierda son menores y a la derecha son mayores.
2. **Recorrido In-Order (Izquierda -> Raíz -> Derecha)**: Visita los nodos en orden ascendente exacto.
3. **Complejidad**: Búsqueda e inserción en $O(\\log N)$ si el árbol está balanceado.""",
        "mermaid": """flowchart TD
    A["(10) Raíz"] --> B["(5) Izquierda"]
    A --> C["(15) Derecha"]
    B --> D["(2)"]
    B --> E["(7)"]
    C --> F["(12)"]
    C --> G["(20)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px""",
        "demo_code": """class NodoBST:
    def __init__(self, val: int):
        self.val = val
        self.izq = None
        self.der = None

raiz = NodoBST(10)
raiz.izq = NodoBST(5)
raiz.der = NodoBST(15)
print(f"Raíz: {raiz.val}, Izq: {raiz.izq.val}, Der: {raiz.der.val}")""",
        "playground_code": """def in_order_traversal(nodo, res):
    if nodo:
        in_order_traversal(nodo.izq, res)
        res.append(nodo.val)
        in_order_traversal(nodo.der, res)""",
        "challenge_prompt": "Crea una clase `NodoBST` con atributos `val`, `izq` y `der`, y una función `in_order(raiz: Optional[NodoBST]) -> list[int]` que retorne la lista de valores en recorrido in-order (orden ascendente).",
        "challenge_starter": """from typing import Optional, List

class NodoBST:
    def __init__(self, val: int):
        self.val = val
        self.izq: Optional['NodoBST'] = None
        self.der: Optional['NodoBST'] = None

def in_order(raiz: Optional[NodoBST]) -> List[int]:
    # ✍️ Recorrido in-order recursivo
    res = []
    def recorrer(n):
        if n:
            recorrer(n.izq)
            res.append(n.val)
            recorrer(n.der)
    recorrer(raiz)
    return res
""",
        "socratic_hints": [
            "💡 Pista 1: En un recorrido in-order, visita primero `n.izq`, luego procesa `n.val` y finalmente `n.der`.",
            "💡 Pista 2: Usa una función auxiliar recursiva que acumule en una lista `res`.",
            "💡 Pista 3: Retorna la lista resultante."
        ],
        "boss_battle": False
    },

    "2-7": {
        "course_num": 2,
        "class_num": 7,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 07: Grafos, Listas de Adyacencia y Recorridos BFS/DFS",
        "metaphor": "El Mapa de Metro y Vuelos (Redes de Conexión)",
        "theory": """Modelado de redes, rutas y relaciones complejas:
1. **Representación con Listas de Adyacencia**: `grafo = {'A': ['B', 'C'], 'B': ['D']}` en $O(V + E)$.
2. **BFS (Breadth-First Search)**: Búsqueda en anchura mediante cola (`deque`), garantiza el camino más corto en grafos no ponderados.
3. **DFS (Depth-First Search)**: Búsqueda en profundidad mediante pila o recursión.""",
        "mermaid": """flowchart LR
    A["(A) Inicio"] --> B["(B)"]
    A --> C["(C)"]
    B --> D["(D) Destino"]
    C --> D
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']
}

def bfs_recorrido(g, inicio):
    visitados = set([inicio])
    cola = deque([inicio])
    orden = []
    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        for vecino in g.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return orden

print("Recorrido BFS:", bfs_recorrido(grafo, 'A'))""",
        "playground_code": """grafo_simple = {"Madrid": ["Barcelona", "Sevilla"], "Barcelona": ["Valencia"]}
print("Conexiones de Madrid:", grafo_simple["Madrid"])""",
        "challenge_prompt": "Crea una función `bfs_camino_mas_corto(grafo: dict[str, list[str]], inicio: str, destino: str) -> list[str]` que use BFS y retorne la lista de nodos del camino más corto desde `inicio` hasta `destino`.",
        "challenge_starter": """from collections import deque
from typing import Dict, List

def bfs_camino_mas_corto(grafo: Dict[str, List[str]], inicio: str, destino: str) -> List[str]:
    # ✍️ Encuentra la ruta más corta usando BFS con cola de rutas
    if inicio == destino:
        return [inicio]
    cola = deque([[inicio]])
    visitados = set([inicio])
    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]
        for vecino in grafo.get(nodo, []):
            if vecino == destino:
                return ruta + [vecino]
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(ruta + [vecino])
    return []
""",
        "socratic_hints": [
            "💡 Pista 1: Guarda en la cola la ruta completa: `cola = deque([[inicio]])`.",
            "💡 Pista 2: En cada paso extrae la ruta actual y explora los vecinos del último nodo `ruta[-1]`.",
            "💡 Pista 3: Cuando un vecino sea igual a `destino`, retorna inmediatamente `ruta + [vecino]`."
        ],
        "boss_battle": False
    },

    "2-8": {
        "course_num": 2,
        "class_num": 8,
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "title": "Clase 08: Recursividad y Programación Dinámica con Memoización",
        "metaphor": "Las Muñecas Rusas y el Bloc de Notas de Resultados",
        "theory": """Optimización exponencial $O(2^N)$ a lineal $O(N)$ mediante subproblemas superpuestos:
1. **Subestructura Óptima**: La solución global se compone de las soluciones óptimas de sus partes.
2. **Memoización (Top-Down)**: Almacenar en caché (`dict` o `@lru_cache`) los resultados ya computados.
3. **Tabulación (Bottom-Up)**: Construir la tabla de soluciones de forma iterativa desde el caso base.""",
        "mermaid": """flowchart TD
    A["fib(5)"] --> B["fib(4)"]
    A --> C["fib(3) [📦 Cached]"]
    B --> D["fib(3)"]
    B --> E["fib(2) [📦 Cached]"]
    D --> F["fib(2)"]
    D --> G["fib(1)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(50) en microsegundos:", fibonacci(50))""",
        "playground_code": """def fib_bottom_up(n: int) -> int:
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print("Fib(10):", fib_bottom_up(10))""",
        "challenge_prompt": "Crea una función `fibonacci_dinamico(n: int) -> int` que calcule el n-ésimo número de Fibonacci en tiempo $O(N)$ utilizando programación dinámica o memoización.",
        "challenge_starter": """def fibonacci_dinamico(n: int) -> int:
    # ✍️ Implementa Fibonacci en O(N) sin recomputar
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
""",
        "socratic_hints": [
            "💡 Pista 1: Puedes usar un enfoque iterativo con dos variables `a = 0, b = 1`.",
            "💡 Pista 2: En un bucle de `2` a `n + 1`, actualiza `a, b = b, a + b`.",
            "💡 Pista 3: Retorna `b` al finalizar el bucle."
        ],
        "boss_battle": True
    },

    # =========================================================================
    # CURSO 3: DESARROLLO DE AGENTES DE INTELIGENCIA ARTIFICIAL (01-08)
    # =========================================================================
    "3-1": {
        "course_num": 3,
        "class_num": 1,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 01: Fundamentos de LLMs, Tokens y Arquitectura Transformer",
        "metaphor": "El Traductor de Sílabas y Piezas de LEGO (Tokens & Context Window)",
        "theory": """Los Modelos de Lenguaje Grande (LLMs) procesan texto transformado en tokens:
1. **Tokenización**: División de palabras en fragmentos semánticos (1 token ≈ 4 caracteres / 0.75 palabras).
2. **Context Window**: Límite de atención del modelo (ej: 128k tokens).
3. **Cálculo de Consumo**: Medición de tokens de entrada (Prompt) y salida (Completion) para presupuestación.""",
        "mermaid": """flowchart LR
    A["📝 Texto Original: 'Agentes de IA'"] --> B["🧩 Tokenizador: [1420, 310, 8950]"]
    B --> C["🧠 Modelo Transformer (Attention)"]
    C --> D["📤 Predicción del Siguiente Token"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def estimar_tokens_demo(texto: str) -> int:
    # Regla empírica estándar: ~4 caracteres por token
    return max(1, len(texto) // 4)

print("Tokens estimados para 'Wisrovi Python Academy':", estimar_tokens_demo("Wisrovi Python Academy"))""",
        "playground_code": """texto_prompt = "Explica la teoría de la relatividad en 3 puntos."
tokens = len(texto_prompt.split()) * 1.3
print(f"Aproximación de tokens: {tokens:.1f}")""",
        "challenge_prompt": "Crea una función `estimar_costo_tokens(texto: str, precio_por_1k: float = 0.002) -> dict[str, Any]` que estime los tokens (asumiendo 1 token = 4 caracteres) y retorne un dict con: 'caracteres', 'tokens_estimados' y 'costo_usd'.",
        "challenge_starter": """from typing import Dict, Any

def estimar_costo_tokens(texto: str, precio_por_1k: float = 0.002) -> Dict[str, Any]:
    # ✍️ Calcula caracteres, tokens_estimados y costo_usd
    chars = len(texto)
    tokens = max(1, chars // 4)
    costo = (tokens / 1000.0) * precio_por_1k
    return {
        "caracteres": chars,
        "tokens_estimados": tokens,
        "costo_usd": round(costo, 6)
    }
""",
        "socratic_hints": [
            "💡 Pista 1: Calcula los tokens como `max(1, len(texto) // 4)`.",
            "💡 Pista 2: El costo es `(tokens / 1000.0) * precio_por_1k`.",
            "💡 Pista 3: Retorna el diccionario con las claves exactas requeridas."
        ],
        "boss_battle": False
    },

    "3-2": {
        "course_num": 3,
        "class_num": 2,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 02: Prompt Engineering Avanzado y Few-Shot Learning",
        "metaphor": "El Director de Cine y el Guión Técnico (Instrucción + Ejemplos)",
        "theory": """Técnicas deterministas para maximizar la fidelidad y precisión del LLM:
1. **System Prompt**: Define el rol, restricciones y tono de respuesta.
2. **Few-Shot Learning**: Proporcionar ejemplos demostrativos (Input -> Output) antes de la consulta.
3. **Delimitadores Semánticos**: Uso de Markdown (```, ###) para separar instrucciones de datos de usuario.""",
        "mermaid": """flowchart TD
    A["🎬 System Prompt: 'Eres un Arquitecto de Software'"] --> B["📋 Few-Shot Examples: (Input -> Output)"]
    B --> C["👤 User Prompt: 'Diseña la BD'"]
    C --> D["🎯 Respuesta Altamente Precisa y Estructurada"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def formatear_prompt(rol: str, tarea: str, entrada: str) -> str:
    return f\"\"\"### SYSTEM
Eres un {rol}.

### INSTRUCCIÓN
{tarea}

### INPUT
{entrada}

### RESPUESTA:\"\"\"

print(formatear_prompt("Traductor Técnico", "Traduce a inglés", "Base de datos vectoriales"))""",
        "playground_code": """ejemplos = [("positivo", "Me encantó"), ("negativo", "Pésimo servicio")]
for label, txt in ejemplos:
    print(f"Ejemplo: '{txt}' -> {label}")""",
        "challenge_prompt": "Crea una función `construir_prompt_few_shot(rol: str, tarea: str, ejemplos: list[tuple[str, str]], input_usuario: str) -> str` que arme un prompt concatenando el rol, la tarea, los pares de ejemplos 'Entrada: X -> Salida: Y' y la entrada final del usuario.",
        "challenge_starter": """def construir_prompt_few_shot(rol: str, tarea: str, ejemplos: list[tuple[str, str]], input_usuario: str) -> str:
    # ✍️ Estructura el prompt con System, Examples y User Input
    lineas = [
        f"ROL: {rol}",
        f"TAREA: {tarea}",
        "EJEMPLOS:"
    ]
    for inp, out in ejemplos:
        lineas.append(f"Entrada: {inp} -> Salida: {out}")
    lineas.append(f"ENTRADA USUARIO: {input_usuario}")
    lineas.append("RESPUESTA:")
    return "\\n".join(lineas)
""",
        "socratic_hints": [
            "💡 Pista 1: Incluye la cabecera `ROL: {rol}` y `TAREA: {tarea}`.",
            "💡 Pista 2: Itera sobre `ejemplos` formateando cada tupla como `Entrada: {inp} -> Salida: {out}`.",
            "💡 Pista 3: Une todas las líneas con `\\n`."
        ],
        "boss_battle": False
    },

    "3-3": {
        "course_num": 3,
        "class_num": 3,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 03: Salidas Estructuradas y Validación Tipada con Pydantic V2",
        "metaphor": "El Inspector de Aduanas y el Formulario Rígido (Validación Estricta)",
        "theory": """Garantizar que las respuestas del LLM cumplan con contratos de software sin alucinaciones:
1. **Esquemas Pydantic (`BaseModel`)**: Tipado estático con `Field(ge=..., le=...)` y validadores.
2. **Extracción JSON Forzada**: Conversión de texto no estructurado en objetos fuertemente tipados.
3. **Manejo de Errores de Validación**: `ValidationError` para reintentar prompts automáticamente.""",
        "mermaid": """flowchart LR
    A["📝 JSON LLM: '{\"entidad\": \"Python\", \"confianza\": 0.95}'"] --> B["🛂 Pydantic BaseModel Validator"]
    B -->|Válido| C["📦 Objeto Python Seguro ExtractionSchema"]
    B -->|Inválido| D["💥 ValidationError & Retry"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style D fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px""",
        "demo_code": """from pydantic import BaseModel, Field

class UsuarioIA(BaseModel):
    nombre: str
    edad: int = Field(ge=0, le=120)
    habilidades: list[str]

u = UsuarioIA(nombre="Wisrovi", edad=30, habilidades=["FastAPI", "Agentes"])
print("Modelo validado:", u.model_dump_json())""",
        "playground_code": """import json
raw_json = '{"nombre": "Agent-01", "score": 98.5}'
parsed = json.loads(raw_json)
print("JSON cargado:", parsed)""",
        "challenge_prompt": "Crea una clase `ExtractionSchema(BaseModel)` con campos: `entidad: str`, `confianza: float = Field(ge=0.0, le=1.0)` y `etiquetas: list[str]`, y una función `validar_extraccion_json(payload_json: str) -> ExtractionSchema` que valide y retorne la instancia.",
        "challenge_starter": """import json
from pydantic import BaseModel, Field

class ExtractionSchema(BaseModel):
    entidad: str
    confianza: float = Field(ge=0.0, le=1.0)
    etiquetas: list[str]

def validar_extraccion_json(payload_json: str) -> ExtractionSchema:
    # ✍️ Deserializa y valida con Pydantic
    datos = json.loads(payload_json)
    return ExtractionSchema(**datos)
""",
        "socratic_hints": [
            "💡 Pista 1: Define `confianza: float = Field(ge=0.0, le=1.0)`.",
            "💡 Pista 2: Usa `json.loads(payload_json)` para obtener el diccionario.",
            "💡 Pista 3: Retorna `ExtractionSchema(**datos)`."
        ],
        "boss_battle": False
    },

    "3-4": {
        "course_num": 3,
        "class_num": 4,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 04: Tool Calling y Function Calling en Python",
        "metaphor": "El Cinturón de Herramientas de Batman (Acciones en el Mundo Real)",
        "theory": """Permitir al Agente de IA invocar funciones de código externo para interactuar con APIs y bases de datos:
1. **Esquema de Herramienta (Tool Schema)**: Nombre, descripción y parámetros tipados en JSON Schema.
2. **Despacho Dinámico**: Enrutar la petición del modelo a la función Python real (`registry.execute(tool_name, **kwargs)`).
3. **Manejo de Errores en Tools**: Retornar mensajes de error descriptivos al LLM para autocorrección.""",
        "mermaid": """flowchart LR
    A["🤖 LLM decide: 'call: sumar(a=10, b=20)'"] --> B["🛠️ ToolRegistry Dispatcher"]
    B --> C["🐍 Ejecución Función Python real"]
    C --> D["📤 Resultado: 30 devuelto al Agente"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """class ToolRegistryDemo:
    def __init__(self): self.tools = {}
    def register(self, name, fn): self.tools[name] = fn
    def run(self, name, **kwargs): return self.tools[name](**kwargs)

reg = ToolRegistryDemo()
reg.register("multiplicar", lambda x, y: x * y)
print("Resultado Tool Call:", reg.run("multiplicar", x=6, y=7))""",
        "playground_code": """def consultar_clima(ciudad: str):
    return f"Soleado en {ciudad}, 24°C"

herramientas = {"get_weather": consultar_clima}
print(herramientas["get_weather"]("Madrid"))""",
        "challenge_prompt": "Crea una clase `ToolRegistry` con métodos: `register(self, name: str, fn: Callable)`, `execute(self, name: str, **kwargs) -> Any` (lanza `KeyError` si la herramienta no está registrada) y `list_tools(self) -> list[str]`.",
        "challenge_starter": """from typing import Callable, Any, Dict, List

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, fn: Callable):
        self._tools[name] = fn

    def execute(self, name: str, **kwargs) -> Any:
        if name not in self._tools:
            raise KeyError(f"Herramienta '{name}' no registrada")
        return self._tools[name](**kwargs)

    def list_tools(self) -> List[str]:
        return list(self._tools.keys())
""",
        "socratic_hints": [
            "💡 Pista 1: Guarda las funciones en un diccionario interno `self._tools = {}`.",
            "💡 Pista 2: En `execute`, verifica `if name not in self._tools: raise KeyError(...)`.",
            "💡 Pista 3: Invoca la función pasando los argumentos con `self._tools[name](**kwargs)`."
        ],
        "boss_battle": False
    },

    "3-5": {
        "course_num": 3,
        "class_num": 5,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 05: Embeddings y Representación Vectorial Semántica",
        "metaphor": "El Mapa de Constelaciones Semánticas (Vectores en el Hiperespacio)",
        "theory": """Transformación de conceptos textuales en vectores numéricos densos de alta dimensión:
1. **Espacio Vectorial**: Textos con significados similares tienen menor distancia angular en el espacio.
2. **Similitud del Coseno**: $\\text{Similitud}(A, B) = \\frac{A \\cdot B}{\\|A\\| \\|B\\|} = \\frac{\\sum A_i B_i}{\\sqrt{\\sum A_i^2} \\sqrt{\\sum B_i^2}}$.
3. **Bases de Datos Vectoriales**: Indexación ANN (Approximate Nearest Neighbors) para búsqueda semántica masiva.""",
        "mermaid": """flowchart LR
    A["📄 Doc A: 'Perro' [0.8, 0.2]"] --> B["📐 Similitud Coseno"]
    C["📄 Doc B: 'Cachorro' [0.78, 0.22]"] --> B
    B --> D["🎯 Similitud: 0.99 (Alta Proximidad)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style C fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """import math

def cos_sim(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    return dot / (norm1 * norm2)

print("Similitud ortogonal:", cos_sim([1, 0], [0, 1]))
print("Similitud paralela:", cos_sim([1, 2], [2, 4]))""",
        "playground_code": """vA = [0.5, 0.5, 0.5]
vB = [0.5, 0.5, 0.5]
print("Mismo vector -> Similitud:", sum(a*b for a,b in zip(vA, vB)))""",
        "challenge_prompt": "Crea una función `similitud_coseno(v1: list[float], v2: list[float]) -> float` que calcule y retorne la similitud del coseno entre dos vectores numéricos de igual dimensión.",
        "challenge_starter": """import math

def similitud_coseno(v1: list[float], v2: list[float]) -> float:
    # ✍️ Calcula (v1 . v2) / (||v1|| * ||v2||)
    if len(v1) != len(v2) or not v1:
        return 0.0
    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(dot / (norm1 * norm2))
""",
        "socratic_hints": [
            "💡 Pista 1: Calcula el producto escalar `dot = sum(a * b for a, b in zip(v1, v2))`.",
            "💡 Pista 2: Calcula las normas euclidianas con `math.sqrt(sum(x * x for x in v))`.",
            "💡 Pista 3: Retorna `dot / (norm1 * norm2)` controlando división por cero."
        ],
        "boss_battle": False
    },

    "3-6": {
        "course_num": 3,
        "class_num": 6,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 06: Arquitecturas RAG (Retrieval-Augmented Generation)",
        "metaphor": "El Estudiante con el Libro Abierto en el Examen (Búsqueda + Contexto)",
        "theory": """Aumentar el conocimiento del LLM inyectando fragmentos recuperados en tiempo real:
1. **Pipeline RAG**: Ingestión -> Chunking -> Vectorización -> Búsqueda Top-K -> Inyección en Prompt.
2. **Reducción de Alucinaciones**: El LLM cita textualmente la información del contexto provisto.
3. **Métricas de Relevancia**: Score de similitud para filtrar documentos irrelevantes.""",
        "mermaid": """flowchart TD
    A["👤 Pregunta Usuario"] --> B["🔍 Búsqueda Vectorial Top-K"]
    B --> C["📚 Documentos Relevantes Recuperados"]
    C & A --> D["🧠 Prompt con Contexto Aumentado"]
    D --> E["🎯 Respuesta Precisa y Verificable"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def simple_rag_mock(query: str, corpus: list[str]) -> list[str]:
    # Filtrar documentos que contengan palabras clave de la consulta
    palabras = set(query.lower().split())
    return [doc for doc in corpus if any(p in doc.lower() for p in palabras)]

docs = ["Python 3.12 incluye mejoras de rendimiento", "Docker permite empaquetar aplicaciones"]
print("Recuperado:", simple_rag_mock("rendimiento en Python", docs))""",
        "playground_code": """contexto = "\\n".join(["- Doc 1: FastAPI", "- Doc 2: Uvicorn"])
prompt_rag = f"Contexto:\\n{contexto}\\n\\nPregunta: ¿Qué es FastAPI?"
print(prompt_rag)""",
        "challenge_prompt": "Crea una clase `SimpleRAGIndex` con métodos: `agregar_documento(self, doc_id: str, texto: str, vector: list[float])` y `buscar_similares(self, vector_query: list[float], top_k: int = 2) -> list[str]` que retorne los IDs de los documentos con mayor similitud coseno.",
        "challenge_starter": """import math
from typing import List, Dict, Tuple

class SimpleRAGIndex:
    def __init__(self):
        self._docs: Dict[str, Tuple[str, List[float]]] = {}

    def agregar_documento(self, doc_id: str, texto: str, vector: List[float]):
        self._docs[doc_id] = (texto, vector)

    def _similitud(self, v1: List[float], v2: List[float]) -> float:
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1)) or 1e-9
        norm2 = math.sqrt(sum(b * b for b in v2)) or 1e-9
        return dot / (norm1 * norm2)

    def buscar_similares(self, vector_query: List[float], top_k: int = 2) -> List[str]:
        # ✍️ Ordena por similitud descendente y retorna top_k IDs
        scores = []
        for doc_id, (_, vec) in self._docs.items():
            s = self._similitud(vector_query, vec)
            scores.append((doc_id, s))
        scores.sort(key=lambda x: x[1], reverse=True)
        return [doc_id for doc_id, _ in scores[:top_k]]
""",
        "socratic_hints": [
            "💡 Pista 1: Almacena los documentos como `self._docs[doc_id] = (texto, vector)`.",
            "💡 Pista 2: Para cada documento calcula la similitud contra `vector_query`.",
            "💡 Pista 3: Ordena por puntaje descendente `scores.sort(key=lambda x: x[1], reverse=True)` y retorna los `doc_id` del top_k."
        ],
        "boss_battle": False
    },

    "3-7": {
        "course_num": 3,
        "class_num": 7,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 07: Agentes Autónomos y el Ciclo Cognitivo ReAct",
        "metaphor": "El Detective Privado (Pensar, Actuar, Observar)",
        "theory": """El paradigma ReAct (Reasoning + Acting) para agentes con autonomía de resolución:
1. **Thought (Pensamiento)**: El agente reflexiona sobre el estado actual y planifica el siguiente paso.
2. **Action (Acción)**: El agente selecciona una herramienta y ejecuta una operación con parámetros.
3. **Observation (Observación)**: El agente recibe el resultado del entorno y decide si continuar o concluir.""",
        "mermaid": """flowchart TD
    A["🎯 Objetivo del Agente"] --> B["🧠 1. Thought (Razonamiento)"]
    B --> C["🛠️ 2. Action (Ejecución Tool)"]
    C --> D["👀 3. Observation (Resultado Entorno)"]
    D --> E{"¿Objetivo Cumplido?"}
    E -->|No| B
    E -->|Sí| F["🏁 Final Answer al Usuario"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style F fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """class SimpleReActDemo:
    def __init__(self): self.pasos = []
    def paso(self, pensamiento, accion, observacion):
        p = {"thought": pensamiento, "action": accion, "observation": observacion}
        self.pasos.append(p)
        return p

agente = SimpleReActDemo()
agente.paso("Necesito el clima de Madrid", "get_weather('Madrid')", "Soleado 22C")
print("Traza del Agente:", agente.pasos)""",
        "playground_code": """traza = [{"thought": "Calcular 2+2", "action": "calc", "obs": "4"}]
print("Pasos ejecutados:", len(traza))""",
        "challenge_prompt": "Crea una clase `ReActAgent` con métodos `registrar_paso(self, thought: str, action: str, observation: str)` y `obtener_traza(self) -> list[dict]` que almacene y retorne el historial completo de pasos.",
        "challenge_starter": """class ReActAgent:
    def __init__(self):
        self._traza = []

    def registrar_paso(self, thought: str, action: str, observation: str):
        # ✍️ Registra el diccionario con thought, action y observation
        self._traza.append({
            "thought": thought,
            "action": action,
            "observation": observation
        })

    def obtener_traza(self) -> list[dict]:
        return self._traza
""",
        "socratic_hints": [
            "💡 Pista 1: Inicializa una lista `self._traza = []` en `__init__`.",
            "💡 Pista 2: En `registrar_paso`, añade un dict con las tres claves `thought`, `action`, `observation`.",
            "💡 Pista 3: Retorna `self._traza` en `obtener_traza()`."
        ],
        "boss_battle": False
    },

    "3-8": {
        "course_num": 3,
        "class_num": 8,
        "course_name": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "title": "Clase 08: Sistemas Multi-Agente, Supervisión y Guardrails",
        "metaphor": "La Agencia de Expertos Especializados con Supervisor de Calidad",
        "theory": """Orquestación de equipos de agentes con roles especializados y políticas de seguridad:
1. **Roles Especializados**: Agente Investigador -> Agente Redactor -> Agente Revisor / Crítico.
2. **Supervisor Central**: Enruta las tareas y valida que ningún agente viole restricciones de seguridad.
3. **Guardrails**: Reglas deterministas que bloquean salidas tóxicas o con alucinaciones antes de entregarlas al usuario.""",
        "mermaid": """flowchart LR
    A["👤 Solicitud"] --> B["🕵️ 1. Investigador (Recupera datos)"]
    B --> C["✍️ 2. Redactor (Genera borrador)"]
    C --> D["🛡️ 3. Supervisor & Guardrails (Auditoría)"]
    D --> E["🎯 Respuesta Certificada de Calidad"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style D fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """class SupervisorMultiAgenteDemo:
    def ejecutar_pipeline(self, texto: str) -> dict:
        investigacion = f"Datos sobre: {texto}"
        redaccion = f"Artículo: {investigacion}"
        aprobado = len(redaccion) > 10
        return {"resultado": redaccion, "guardrail_pass": aprobado}

s = SupervisorMultiAgenteDemo()
print(s.ejecutar_pipeline("Arquitectura de Agentes"))""",
        "playground_code": """roles = ["Researcher", "Coder", "Reviewer"]
print("Equipo de Agentes:", " -> ".join(roles))""",
        "challenge_prompt": "Crea una clase `OrquestadorMultiAgente` con método `procesar_flujo(self, entrada: str) -> dict` que simule el paso por un Investigador (añade '[INVESTIGADO]'), un Redactor (añade '[REDACTADO]') y un Guardrail (verifica que contenga ambas marcas y retorne dict con 'final_output' y 'valid: bool').",
        "challenge_starter": """class OrquestadorMultiAgente:
    def procesar_flujo(self, entrada: str) -> dict:
        # ✍️ Pipeline: Investigador -> Redactor -> Guardrail
        paso1 = f"[INVESTIGADO] {entrada}"
        paso2 = f"[REDACTADO] {paso1}"
        es_valido = "[INVESTIGADO]" in paso2 and "[REDACTADO]" in paso2
        return {
            "final_output": paso2,
            "valid": es_valido
        }
""",
        "socratic_hints": [
            "💡 Pista 1: Añade `[INVESTIGADO]` a la entrada original.",
            "💡 Pista 2: Añade `[REDACTADO]` al resultado de la investigación.",
            "💡 Pista 3: Retorna el diccionario con `final_output` y `valid: True`."
        ],
        "boss_battle": True
    },

    # =========================================================================
    # CURSO 4: TALLER PRÁCTICO & PROYECTO INTEGRADOR FULL-STACK (01-08)
    # =========================================================================
    "4-1": {
        "course_num": 4,
        "class_num": 1,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 01: Arquitectura de Software y Planificación del Proyecto",
        "metaphor": "El Plano del Rascacielos Modular (Clean Architecture)",
        "theory": """Diseño modular y desacoplado para aplicaciones de producción:
1. **Separación de Responsabilidades**: `api` (controladores), `core` (configuración), `models` (entidades), `services` (lógica de negocio).
2. **Inversión de Dependencias**: Los módulos de alto nivel no dependen de los de bajo nivel; ambos dependen de abstracciones.
3. **Verificación de Estructura**: Validar que el proyecto posea todas las capas obligatorias.""",
        "mermaid": """flowchart TD
    A["🌐 Capa API (Endpoints REST)"] --> B["⚙️ Capa Services (Lógica Negocio)"]
    B --> C["💾 Capa Repositories (Persistencia DB)"]
    B --> D["🤖 Capa Agents (Motor de IA)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px""",
        "demo_code": """MODULOS_OBLIGATORIOS = {"api", "core", "models", "services", "tests"}

def validar_modulos(modulos_presentes: list[str]) -> bool:
    return MODULOS_OBLIGATORIOS.issubset(set(modulos_presentes))

print("¿Arquitectura válida?:", validar_modulos(["api", "core", "models", "services", "tests", "ui"]))""",
        "playground_code": """carpetas = ["src/api", "src/services", "src/models", "tests"]
print("Estructura definida:", carpetas)""",
        "challenge_prompt": "Crea una función `validar_estructura_proyecto(modulos: list[str]) -> bool` que retorne `True` si la lista contiene al menos los 5 módulos base: 'api', 'core', 'models', 'services', 'tests'.",
        "challenge_starter": """def validar_estructura_proyecto(modulos: list[str]) -> bool:
    # ✍️ Verifica que contenga api, core, models, services, tests
    requeridos = {"api", "core", "models", "services", "tests"}
    return requeridos.issubset(set(modulos))
""",
        "socratic_hints": [
            "💡 Pista 1: Define el conjunto requerido: `{'api', 'core', 'models', 'services', 'tests'}`.",
            "💡 Pista 2: Usa `.issubset(set(modulos))` para verificar la inclusión.",
            "💡 Pista 3: Retorna el resultado booleano."
        ],
        "boss_battle": False
    },

    "4-2": {
        "course_num": 4,
        "class_num": 2,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 02: Desarrollo del Backend: APIs RESTful con FastAPI",
        "metaphor": "El Mesero de Restaurante de Alta Cocina (Petición -> Cocina -> Plato)",
        "theory": """Construcción de APIs asíncronas de alto rendimiento con FastAPI y validación OpenAPI:
1. **Rutas y Verbos HTTP**: `GET` (consultar), `POST` (crear), `PUT` (actualizar), `DELETE` (eliminar).
2. **Inyección de Dependencias (`Depends`)**: Gestión limpia de sesiones de base de datos y autenticación.
3. **Pydantic Response Models**: Sanitización automática de datos expuestos al cliente.""",
        "mermaid": """flowchart LR
    A["💻 Cliente HTTP (POST /api/items)"] --> B["⚡ FastAPI Router"]
    B --> C["🛂 Pydantic Request Validation"]
    C --> D["⚙️ Lógica de Servicio"]
    D --> E["📤 JSON Response (Status 201)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """from pydantic import BaseModel

class ProductoInput(BaseModel):
    id: int
    nombre: str
    precio: float

def mock_endpoint_crear(payload: dict) -> dict:
    item = ProductoInput(**payload)
    return {"status": "created", "item": item.model_dump()}

print(mock_endpoint_crear({"id": 1, "nombre": "Teclado", "precio": 49.99}))""",
        "playground_code": """routes = ["/api/health", "/api/v1/users", "/api/v1/agents"]
print("Rutas registradas:", routes)""",
        "challenge_prompt": "Crea una función `crear_endpoint_producto(datos: dict) -> dict` que valide los datos con un modelo `ProductModel(id: int, name: str, price: float)` y retorne un dict con `{'status': 'ok', 'data': model.model_dump()}`.",
        "challenge_starter": """from pydantic import BaseModel

class ProductModel(BaseModel):
    id: int
    name: str
    price: float

def crear_endpoint_producto(datos: dict) -> dict:
    # ✍️ Valida con ProductModel y retorna dict de respuesta
    producto = ProductModel(**datos)
    return {
        "status": "ok",
        "data": producto.model_dump()
    }
""",
        "socratic_hints": [
            "💡 Pista 1: Instancia `ProductModel(**datos)`.",
            "💡 Pista 2: Usa `.model_dump()` para serializar el modelo a diccionario.",
            "💡 Pista 3: Retorna `{'status': 'ok', 'data': ...}`."
        ],
        "boss_battle": False
    },

    "4-3": {
        "course_num": 4,
        "class_num": 3,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 03: Persistencia de Datos: Modelado SQL y Transacciones ACID",
        "metaphor": "La Bóveda Acorazada y el Libro Mayor ACID",
        "theory": """Garantía de integridad y consistencia en el almacenamiento relacional:
1. **Propiedades ACID**: Atomicidad, Consistencia, Aislamiento y Durabilidad.
2. **Transacciones SQL**: `BEGIN`, `COMMIT`, `ROLLBACK` para operaciones que no admiten estados intermedios.
3. **SQLite en Memoria / Postgres**: Ejecución segura de consultas parametrizadas contra inyecciones SQL.""",
        "mermaid": """flowchart TD
    A["💳 Transferencia $100"] --> B["🔒 BEGIN TRANSACTION"]
    B --> C["🔻 Restar $100 de Cuenta Origen"]
    C --> D["🔺 Sumar $100 a Cuenta Destino"]
    D --> E{"¿Sin Errores?"}
    E -->|Sí| F["✅ COMMIT"]
    E -->|No| G["⛔ ROLLBACK"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style F fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style G fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px""",
        "demo_code": """import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE cuentas (id TEXT PRIMARY KEY, saldo REAL)")
conn.execute("INSERT INTO cuentas VALUES ('A', 500.0), ('B', 200.0)")
conn.commit()

cursor = conn.cursor()
cursor.execute("SELECT * FROM cuentas")
print("Cuentas iniciales:", cursor.fetchall())""",
        "playground_code": """import sqlite3
c = sqlite3.connect(":memory:")
c.execute("CREATE TABLE logs (msg TEXT)")
c.execute("INSERT INTO logs VALUES ('OK')")
print("Total logs:", c.execute("SELECT count(*) FROM logs").fetchone()[0])""",
        "challenge_prompt": "Crea una función `registrar_transaccion_sqlite(conn: sqlite3.Connection, origen: str, destino: str, monto: float) -> bool` que ejecute de forma transaccional una transferencia descontando `monto` de `origen` y sumando a `destino`, haciendo `commit()` y retornando `True`.",
        "challenge_starter": """import sqlite3

def registrar_transaccion_sqlite(conn: sqlite3.Connection, origen: str, destino: str, monto: float) -> bool:
    # ✍️ Ejecuta la transferencia atómica con commit
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = ?", (monto, origen))
        cursor.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = ?", (monto, destino))
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
""",
        "socratic_hints": [
            "💡 Pista 1: Usa `UPDATE cuentas SET saldo = saldo - ? WHERE id = ?` para el origen.",
            "💡 Pista 2: Usa `UPDATE cuentas SET saldo = saldo + ? WHERE id = ?` para el destino.",
            "💡 Pista 3: Llama a `conn.commit()` y retorna `True`."
        ],
        "boss_battle": False
    },

    "4-4": {
        "course_num": 4,
        "class_num": 4,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 04: Desarrollo del Frontend: Dashboards con Streamlit",
        "metaphor": "El Tablero de Mandos Interactivo y los Componentes Reactivos",
        "theory": """Prototipado rápido y visualización de datos reactiva con Streamlit:
1. **Estado de Sesión (`st.session_state`)**: Persistir estado entre reruns de la interfaz.
2. **Widgets y Métricas**: `st.metric`, `st.chat_input`, `st.chat_message` para interfaces conversacionales.
3. **Consumo de Backend**: Llamadas HTTP vía `requests` o SDK interno hacia el servidor FastAPI.""",
        "mermaid": """flowchart LR
    A["👤 Input de Usuario en Dashboard"] --> B["⚡ Streamlit Rerun"]
    B --> C["📦 st.session_state (Memoria de Sesión)"]
    C --> D["🌐 API Call hacia FastAPI"]
    D --> E["📊 Renderizado de Gráficos y Métricas"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def preparar_session_state(usuario: str, rol: str) -> dict:
    return {
        "usuario": usuario,
        "rol": rol,
        "mensajes": [],
        "autenticado": True
    }

print("Estado de sesión inicializado:", preparar_session_state("Wisrovi", "Admin"))""",
        "playground_code": """metricas = {"usuarios_activos": 1250, "latencia_ms": 15.4}
print("Métricas para dashboard:", metricas)""",
        "challenge_prompt": "Crea una función `preparar_estado_dashboard(usuario: str, metricas: dict) -> dict` que devuelva un diccionario con las claves: 'usuario', 'metricas', 'mensajes' (lista vacía) y 'listo: True'.",
        "challenge_starter": """def preparar_estado_dashboard(usuario: str, metricas: dict) -> dict:
    # ✍️ Estructura el diccionario de sesión para Streamlit
    return {
        "usuario": usuario,
        "metricas": metricas,
        "mensajes": [],
        "listo": True
    }
""",
        "socratic_hints": [
            "💡 Pista 1: Asigna `usuario` a `'usuario'` y `metricas` a `'metricas'`.",
            "💡 Pista 2: Inicializa `'mensajes': []` como lista vacía.",
            "💡 Pista 3: Incluye `'listo': True` y retorna el diccionario."
        ],
        "boss_battle": False
    },

    "4-5": {
        "course_num": 4,
        "class_num": 5,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 05: Integración del Motor de IA y Agentes en la App",
        "metaphor": "El Asistente Inteligente en Vivo (Conexión Frontend - Agente)",
        "theory": """Conexión end-to-end entre la interfaz de usuario y el motor multi-agente:
1. **Streaming de Respuestas (SSE)**: Enviar tokens en tiempo real al usuario.
2. **Contexto Conversacional**: Inyectar el historial de chat en el prompt del agente.
3. **Manejo de Tiempos de Espera (Timeouts)**: Resiliencia ante latencias de red con fallbacks elegantes.""",
        "mermaid": """flowchart LR
    A["💬 Chat Streamlit"] --> B["🌐 FastAPI Endpoint /chat"]
    B --> C["🤖 Motor Agente ReAct + RAG"]
    C --> D["📤 Respuesta Sintetizada"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """def sintetizar_respuesta_agente(query: str, docs: list[str]) -> dict:
    contexto = " | ".join(docs)
    return {
        "status": "ok",
        "query": query,
        "respuesta": f"Basado en [{contexto}], la respuesta es óptima."
    }

print(sintetizar_respuesta_agente("¿Qué es Python?", ["Lenguaje interpreted", "Creado por Guido"]))""",
        "playground_code": """historial = [{"role": "user", "content": "Hola"}, {"role": "assistant", "content": "¡Hola!"}]
print("Longitud del historial:", len(historial))""",
        "challenge_prompt": "Crea una función `procesar_consulta_agente(consulta: str, contexto_rag: list[str]) -> dict` que valide que la consulta no esté vacía y retorne `{'status': 'ok', 'query': consulta, 'fuentes_usadas': len(contexto_rag), 'respuesta': f'Respuesta a: {consulta}'}`.",
        "challenge_starter": """def procesar_consulta_agente(consulta: str, contexto_rag: list[str]) -> dict:
    # ✍️ Procesa la consulta con el contexto RAG
    if not consulta.strip():
        return {"status": "error", "message": "Consulta vacía"}
    return {
        "status": "ok",
        "query": consulta,
        "fuentes_usadas": len(contexto_rag),
        "respuesta": f"Respuesta a: {consulta}"
    }
""",
        "socratic_hints": [
            "💡 Pista 1: Si `not consulta.strip()`, retorna `status: error`.",
            "💡 Pista 2: Calcula `fuentes_usadas = len(contexto_rag)`.",
            "💡 Pista 3: Retorna el diccionario estructurado con status 'ok'."
        ],
        "boss_battle": False
    },

    "4-6": {
        "course_num": 4,
        "class_num": 6,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 06: Testing Riguroso con Pytest, Mocks y Cobertura",
        "metaphor": "El Laboratorio de Control de Calidad y las Pruebas de Estrés",
        "theory": """Garantía de calidad mediante pruebas automatizadas exhaustivas:
1. **Pytest & Fixtures**: Reutilización de estados de prueba limpios y desacoplados.
2. **Mocks & Spies (`unittest.mock`)**: Simulación de llamadas a APIs externas sin gastar tokens reales.
3. **Métricas de Cobertura (Coverage)**: Asegurar un mínimo del 85%+ de líneas evaluadas por la suite.""",
        "mermaid": """flowchart TD
    A["🧪 Suite de Pruebas Pytest"] --> B["🔬 Test Unitarios (Funciones)"]
    A --> C["🌐 Test de Integración (API Endpoints)"]
    A --> D["🎭 Mocks de LLM (Zero Cost)"]
    B & C & D --> E{"¿Cobertura >= 85% y 0 Fallos?"}
    E -->|Sí| F["🏆 Aprobado para Despliegue"]
    E -->|No| G["⛔ Bloqueo en Pipeline"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style F fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style G fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px""",
        "demo_code": """def evaluar_calidad_demo(passed: int, total: int, coverage: float) -> bool:
    return (passed == total) and (coverage >= 85.0)

print("¿Calidad certificada?:", evaluar_calidad_demo(34, 34, 94.5))""",
        "playground_code": """assert 2 + 2 == 4, "Aserción básica válida"
print("Aserción completada.")""",
        "challenge_prompt": "Crea una función `suite_calidad_codigo(cobertura_pct: float, tests_fallidos: int) -> tuple[bool, str]` que retorne `(True, 'Certificado')` si cobertura_pct >= 85.0 y tests_fallidos == 0, o `(False, 'Calidad insuficiente')` en caso contrario.",
        "challenge_starter": """def suite_calidad_codigo(cobertura_pct: float, tests_fallidos: int) -> tuple[bool, str]:
    # ✍️ Valida cobertura >= 85.0 y tests_fallidos == 0
    if cobertura_pct >= 85.0 and tests_fallidos == 0:
        return (True, "Certificado")
    return (False, "Calidad insuficiente")
""",
        "socratic_hints": [
            "💡 Pista 1: Comprueba `cobertura_pct >= 85.0 and tests_fallidos == 0`.",
            "💡 Pista 2: Si cumple, retorna `(True, 'Certificado')`.",
            "💡 Pista 3: En caso contrario retorna `(False, 'Calidad insuficiente')`."
        ],
        "boss_battle": False
    },

    "4-7": {
        "course_num": 4,
        "class_num": 7,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 07: Containerización Profesional con Docker y Compose",
        "metaphor": "El Contenedor de Carga Estandarizado (Reproducibilidad Total)",
        "theory": """Empaquetado inmutable y orquestación multi-servicio para producción:
1. **Dockerfile Multi-Stage**: Reducción drástica del tamaño de la imagen final y seguridad non-root.
2. **Docker Compose**: Orquestación coordinada de backend (FastAPI), frontend (Streamlit) y base de datos (Postgres).
3. **Healthchecks & Variables de Entorno**: Configuración estandarizada vía `.env`.""",
        "mermaid": """flowchart TD
    subgraph Compose["🐳 Docker Compose Orchestrator"]
        B["⚡ Backend (FastAPI :8000)"]
        F["📊 Frontend (Streamlit :8501)"]
        D["🐘 Base de Datos (Postgres :5432)"]
        F --> B
        B --> D
    end
    style Compose fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style F fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px""",
        "demo_code": """def generar_compose_yaml(servicios: list[str]) -> str:
    return f\"\"\"version: '3.8'
services:
  \"\"\" + \"\\n  \".join(f\"{s}:\\n    image: wisrovi/{s}:latest\" for s in servicios)

print(generar_compose_yaml(["fastapi_app", "streamlit_ui"]))""",
        "playground_code": """servicios = ["backend", "frontend", "db"]
print("Servicios listos para compose:", servicios)""",
        "challenge_prompt": "Crea una función `generar_dockerfile_python(version: str = '3.11-slim', port: int = 8000) -> str` que retorne una cadena con un Dockerfile estándar conteniendo las directivas: `FROM python:{version}`, `WORKDIR /app`, `EXPOSE {port}` y `CMD [\"uvicorn\", \"main:app\"]`.",
        "challenge_starter": """def generar_dockerfile_python(version: str = "3.11-slim", port: int = 8000) -> str:
    # ✍️ Genera el contenido del Dockerfile
    return f\"\"\"FROM python:{version}
WORKDIR /app
COPY . /app
EXPOSE {port}
CMD ["uvicorn", "main:app"]\"\"\"
""",
        "socratic_hints": [
            "💡 Pista 1: Incluye `FROM python:{version}` y `WORKDIR /app`.",
            "💡 Pista 2: Incluye `EXPOSE {port}` con el puerto parametrizado.",
            "💡 Pista 3: Retorna la cadena completa formateada."
        ],
        "boss_battle": False
    },

    "4-8": {
        "course_num": 4,
        "class_num": 8,
        "course_name": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "title": "Clase 08: Despliegue en la Nube, CI/CD y Portafolio Final",
        "metaphor": "La Cinta de Ensamblaje Automatizada hacia Producción",
        "theory": """Cierre magistral del programa de 32 semanas:
1. **GitHub Actions CI/CD**: Automatización de linting (`ruff`), testing (`pytest`), build de imágenes y despliegue.
2. **Zero-Downtime Deployment**: Estrategia de despliegue blue/green y validación de endpoints de salud (`/health`).
3. **Acreditación Final & Portafolio**: Generación del Diploma Maestro Oficial de 160 Horas avalado por William Rodríguez (Wisrovi).""",
        "mermaid": """flowchart LR
    A["🐙 Git Push (main)"] --> B["🧪 CI Workflow (Pytest & Ruff)"]
    B --> C["🐳 Build Docker & Container Scan"]
    C --> D["🚀 CD Deploy to Cloud (FastAPI + Streamlit)"]
    D --> E["🏆 Master AI Engineer Certified (160h)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
        "demo_code": """class PipelineDespliegueDemo:
    def ejecutar(self, etapas: list[str]) -> bool:
        for e in etapas:
            print(f"-> Ejecutando etapa CI/CD: {e}... OK")
        return True

p = PipelineDespliegueDemo()
p.ejecutar(["lint", "test", "security_scan", "build", "deploy"])""",
        "playground_code": """print("🌟 ¡Has alcanzado la cima del Programa Integral de Formación en Python!")
print("🎓 32 Clases Completadas con Éxito.")""",
        "challenge_prompt": "Crea una clase `PipelineDespliegue` con método `ejecutar_fases(self, fases: list[str]) -> dict` que valide que todas las fases requeridas ('lint', 'test', 'build', 'deploy') estén presentes en `fases`, retornando `{'status': 'success', 'fases_ejecutadas': len(fases), 'desplegado': True}` o `{'status': 'failed', 'desplegado': False}` si falta alguna.",
        "challenge_starter": """class PipelineDespliegue:
    def ejecutar_fases(self, fases: list[str]) -> dict:
        # ✍️ Valida que contenga lint, test, build y deploy
        requeridas = {"lint", "test", "build", "deploy"}
        if requeridas.issubset(set(fases)):
            return {
                "status": "success",
                "fases_ejecutadas": len(fases),
                "desplegado": True
            }
        return {
            "status": "failed",
            "desplegado": False
        }
""",
        "socratic_hints": [
            "💡 Pista 1: Define `requeridas = {'lint', 'test', 'build', 'deploy'}`.",
            "💡 Pista 2: Verifica si `requeridas.issubset(set(fases))`.",
            "💡 Pista 3: Retorna `status: 'success'` si se cumplen todas las fases."
        ],
        "boss_battle": True
    }
}

class TutorEngine:
    """Motor que suministra el currículo y la metadata pedagógica de las 32 clases."""

    @classmethod
    def get_all_classes_summary(cls) -> List[Dict[str, Any]]:
        """Retorna la lista de todas las 32 clases disponibles."""
        summary = []
        for key, item in CLASS_CURRICULUM.items():
            summary.append({
                "key": key,
                "course_num": item["course_num"],
                "class_num": item["class_num"],
                "course_name": item["course_name"],
                "title": item["title"],
                "metaphor": item["metaphor"],
                "boss_battle": item.get("boss_battle", False)
            })
        return summary

    @classmethod
    def get_class_content(cls, course_num: int, class_num: int) -> Optional[Dict[str, Any]]:
        """Retorna el contenido completo de una clase específica."""
        key = f"{course_num}-{class_num}"
        return CLASS_CURRICULUM.get(key)
