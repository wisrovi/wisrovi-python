#!/usr/bin/env python3
"""
Motor de Contenidos y Guía Pedagógica del Tutor Virtual.
Estructura las 32 clases en 4 cursos, organizando cada sesión en 4 pasos:
1. Concepto & Metáfora
2. Demostración Interactiva
3. Arenero / Playground con Memoria
4. Desafío Evaluado & Pistas Socráticas
"""

from typing import Dict, List, Any, Optional

CLASS_CURRICULUM = {
    "1-1": {
        "course_num": 1,
        "class_num": 1,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 01: Primer Vistazo Práctico (print, variables, if, for, def)",
        "metaphor": "El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)",
        "theory": """En esta sesión inaugural exploramos los 4 pilares esenciales de cualquier software:
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
        "challenge_prompt": "Crea una función llamada `evaluar_estudiante(nombre: str, edad: int)` que retorne el texto 'Mayor de edad' si tiene 18 o más, o 'Menor de edad' en caso contrario.",
        "challenge_starter": """def evaluar_estudiante(nombre: str, edad: int) -> str:
    # ✍️ Escribe aquí tu solución
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
""",
        "socratic_hints": [
            "💡 Pista 1: Recuerda usar la sentencia 'if edad >= 18:' para verificar la mayoría de edad.",
            "💡 Pista 2: La función debe retornar exactamente las cadenas 'Mayor de edad' o 'Menor de edad'.",
            "💡 Pista 3: Comprueba que el tipo de retorno sea 'str'."
        ],
        "boss_battle": False
    },
    "1-2": {
        "course_num": 1,
        "class_num": 2,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 02: Variables, Tipos de Datos y Memoria Heap",
        "metaphor": "Las Cajas Etiquetadas en Memoria (Punteros e Inmutabilidad)",
        "theory": """En Python, las variables no contienen datos directamente; son **etiquetas que apuntan a objetos en la memoria Heap**:
1. **Tipos Primitivos**: `int`, `float`, `str`, `bool`. Son **inmutables** (no pueden alterarse tras crearse).
2. **Identidad (`id`)**: La dirección física en RAM donde reside el objeto.
3. **`==` vs `is`**: `==` compara si dos objetos tienen el mismo valor de contenido; `is` comprueba si son exactamente el mismo bloque de memoria física.""",
        "mermaid": """flowchart LR
    A["🏷️ Variable: nombre_a<br/>'Python'"] -->|Apunta a| OBJ["📦 Objeto en Heap<br/>0x7f... | 'Python' | 54 Bytes"]
    B["🏷️ Variable: nombre_b<br/>'Python'"] -->|Apunta a| OBJ

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    B fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style OBJ fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px""",
        "demo_code": """# Inspección de Identidad y Memoria
a = "Python"
b = a

print(f"Dirección de 'a': {hex(id(a))}")
print(f"Dirección de 'b': {hex(id(b))}")
print(f"¿Apuntan al mismo objeto?: {a is b}")

# Reasignación crea un nuevo objeto en el Heap
a = a + " 3.12"
print(f"Nueva dirección de 'a': {hex(id(a))}")
print(f"¿Siguen siendo el mismo objeto?: {a is b}")""",
        "playground_code": """# 🔬 ARENERO DE MEMORIA: Observa cómo cambia la memoria
x = 100
y = x
print("x:", x, "| y:", y, "| x is y:", x is y)

x = x + 1
print("Tras x = x + 1 -> x:", x, "| y:", y, "| x is y:", x is y)""",
        "challenge_prompt": "Crea una función `identificar_tipo_y_tamano(valor)` que retorne una tupla con (nombre_del_tipo, tamano_en_bytes_usando_sys).",
        "challenge_starter": """import sys

def identificar_tipo_y_tamano(valor) -> tuple:
    # ✍️ Escribe aquí tu solución
    tipo_nombre = type(valor).__name__
    tamano = sys.getsizeof(valor)
    return (tipo_nombre, tamano)
""",
        "socratic_hints": [
            "💡 Pista 1: Usa 'type(valor).__name__' para obtener el nombre del tipo como texto ('int', 'str', etc.).",
            "💡 Pista 2: Usa 'sys.getsizeof(valor)' para calcular el tamaño en memoria RAM.",
            "💡 Pista 3: Retorna una tupla de dos elementos '(tipo, tamano)'."
        ],
        "boss_battle": False
    },
    "1-8": {
        "course_num": 1,
        "class_num": 8,
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "title": "Clase 08: Proyecto Integrador: Sistema de Gestión CLI (Boss Battle)",
        "metaphor": "El Tablero de Control y el Casco de Seguridad (try / except)",
        "theory": """¡Bienvenido a la primera **Batalla de Jefe (Boss Battle)** del programa!
Aquí integrarás los 4 pilares:
1. Menú interactivo con `while True`.
2. Persistencia en diccionario/lista en memoria.
3. Funciones modulares tipadas con PEP 484.
4. Manejo robusto de errores con `try / except` para evitar que el programa colapse ante entradas inválidas.""",
        "mermaid": """flowchart TD
    M["🖥️ 1. Menú CLI Interactivo"] --> C{"🔀 2. Opción del Usuario"}
    C -->|1. Crear Registro| INS["➕ Inserción Validada en Memoria"]
    C -->|2. Consultar| QRY["🔍 Búsqueda y Filtro O(1)"]
    C -->|3. Salir| EXT["🏁 Salida Segura"]
    INS --> ERR{"🛡️ try / except"}
    ERR -->|Entrada Inválida| MSG["⚠️ Mensaje de Advertencia Amigable"]
    ERR -->|Correcto| SUC["✅ Registro Guardado con Éxito"]

    style M fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style INS fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style ERR fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style SUC fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style MSG fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style EXT fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px""",
        "demo_code": """# Estructura del Gestor CLI
inventario = {}

def registrar_item(nombre: str, cantidad: int):
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
    inventario[nombre] = cantidad
    return True

try:
    registrar_item("Laptop", 5)
    print("Inventario actual:", inventario)
except ValueError as e:
    print("Error:", e)""",
        "playground_code": """# 🔬 ARENERO: Diseña tus comandos de consola
comandos = {"help": "Muestra ayuda", "status": "Ver estado", "exit": "Salir"}
comando = "status"

if comando in comandos:
    print(f"Ejecutando: {comandos[comando]}")""",
        "challenge_prompt": "Construye la clase `GestorInventario` con métodos `agregar_producto(nombre, stock)` y `obtener_stock(nombre)`. Debe lanzar `KeyError` si el producto no existe y `ValueError` si el stock es negativo.",
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
            "💡 Pista 1: Usa un diccionario interno 'self._stock' para almacenar las existencias.",
            "💡 Pista 2: Lanza 'ValueError' con 'raise ValueError(...)' cuando stock < 0.",
            "💡 Pista 3: Lanza 'KeyError' cuando 'nombre not in self._stock'."
        ],
        "boss_battle": True
    }
}

class TutorEngine:
    """Motor que suministra el currículo y la metadata pedagógica."""

    @classmethod
    def get_all_classes_summary(cls) -> List[Dict[str, Any]]:
        """Retorna la lista de todas las clases disponibles."""
        summary = []
        for key, item in CLASS_CURRICULUM.items():
            summary.append({
                "key": key,
                "course_num": item["course_num"],
                "class_num": item["class_num"],
                "title": item["title"],
                "metaphor": item["metaphor"],
                "boss_battle": item.get("boss_battle", False)
            })
        return summary

    @classmethod
    def get_class_content(cls, course_num: int, class_num: int) -> Optional[Dict[str, Any]]:
        """Retorna el contenido completo de una clase."""
        key = f"{course_num}-{class_num}"
        if key in CLASS_CURRICULUM:
            return CLASS_CURRICULUM[key]
            
        # Fallback genérico para clases restantes
        return {
            "course_num": course_num,
            "class_num": class_num,
            "course_name": f"Curso {course_num}: Programa de Formación",
            "title": f"Clase {class_num:02d}: Unidad Temática de Especialización",
            "metaphor": "El Engranaje y la Cinta Transportadora de Datos",
            "theory": f"Estudio técnico de la Semana {class_num:02d} correspondiente al Curso {course_num}.",
            "mermaid": """flowchart LR
    A["📥 Entrada"] --> B["⚙️ Procesamiento"] --> C["🎯 Salida"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px""",
            "demo_code": f"# Código de la Semana {class_num:02d}\nprint('Ejecutando sesión formativa {course_num}.{class_num}')",
            "playground_code": "# Arenero de pruebas interactivo\nx = 10\nprint('x:', x)",
            "challenge_prompt": f"Implementa la función de la Semana {class_num:02d} cumpliendo los contratos de tipado.",
            "challenge_starter": "def solucion():\n    return True\n",
            "socratic_hints": [
                "💡 Pista 1: Revisa los contratos de entrada y salida.",
                "💡 Pista 2: Ejecuta las pruebas unitarias para validar tu código."
            ],
            "boss_battle": (class_num == 8)
        }
