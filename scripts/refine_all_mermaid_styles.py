#!/usr/bin/env python3
"""
Refinador de Estilo y Narrativa Visual para TODOS los Diagramas Mermaid.
Aplica el estándar visual premium de alto contraste, colores vibrantes HSL/Hex,
iconografía rica y etiquetas explícitas que narran la esencia de cada carpeta y clase,
100% compatibles y renderizables por GitHub Markdown y MkDocs Material.
"""

import os
import sys
from typing import Dict, Any

# Agregar directorio actual a sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, BASE_DIR

CLASS_META_MAP = {(m["course_num"], m["folder_name"]): m for m in ALL_CLASSES}

# ==============================================================================
# DEFINICIONES ESPECÍFICAS DE DIAGRAMAS MERMAID PREMIUM PARA LAS 32 CLASES
# ==============================================================================
CLASS_MERMAIDS = {
    # CURSO 1: FUNDAMENTOS
    (1, "clase-01-panorama-general"): """```mermaid
flowchart TD
    COMP["💻 Computadora (Tu Asistente)"] --> P0["📢 print() ➔ El Megáfono<br/>Muestra mensajes y resultados en pantalla"]
    COMP --> P1["📦 Variables ➔ Cajas de Mudanza<br/>Guardan valores en memoria con '='"]
    COMP --> P2["🚦 if / else ➔ El Semáforo de Decisiones<br/>Evalúa condiciones lógicas (True / False)"]
    COMP --> P3["🔄 for ➔ La Cinta Transportadora<br/>Procesa colecciones elemento a elemento"]
    COMP --> P4["⚙️ def ➔ La Licuadora<br/>Recibe ingredientes (entradas) y retorna el jugo (salida)"]

    style COMP fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style P0 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style P1 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style P2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style P3 fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style P4 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```""",

    (1, "clase-02-variables-y-tipos"): """```mermaid
flowchart LR
    INPUT["📥 Entrada del Usuario<br/>'45.90' (str)"] --> CAST1["⚙️ float('45.90')<br/>Conversión Decimal"]
    CAST1 --> FLOAT_VAL["💵 45.90 (float)<br/>Número Flotante"]
    FLOAT_VAL --> CAST2["⚙️ int(45.90)<br/>Truncado a Entero"]
    CAST2 --> INT_VAL["🔢 45 (int)<br/>Número Entero"]
    INT_VAL --> MEM["🧠 Memoria Heap<br/>id(objeto) & Inmutabilidad"]

    style INPUT fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style CAST1 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style FLOAT_VAL fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style CAST2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style INT_VAL fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style MEM fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```""",

    (1, "clase-03-control-flujo-condicionales"): """```mermaid
flowchart TD
    COND["⚖️ Evaluación de Expresión Booleana"] --> IF{"¿Condición Principal<br/>if edad >= 18?"}
    IF -->|True (Verdadero)| B1["🟢 Semáforo Verde<br/>Acceso Autorizado al Sistema"]
    IF -->|False (Falso)| ELIF{"¿Condición Secundaria<br/>elif tiene_permiso?"}
    ELIF -->|True (Verdadero)| B2["🟡 Semáforo Amarillo<br/>Acceso con Supervisión"]
    ELIF -->|False (Falso)| ELSE["🔴 Semáforo Rojo<br/>Acceso Denegado por Defecto"]

    style COND fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style IF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B1 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B2 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style ELSE fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```""",

    (1, "clase-04-control-flujo-bucles"): """```mermaid
flowchart TD
    SEQ["📦 Secuencia o Rango<br/>range(1, 10) o lista"] --> ITER["🔄 Iterador del Bucle (for / while)"]
    ITER --> BODY["⚡ Ejecutar Bloque del Bucle"]
    BODY --> CTRL{"¿Instrucción Especial?"}
    CTRL -->|continue| ITER
    CTRL -->|break| EXIT["🛑 Salida Inmediata del Ciclo"]
    CTRL -->|Flujo Normal| NEXT{"¿Fin de Secuencia?"}
    NEXT -->|No| ITER
    NEXT -->|Sí| EXIT

    style SEQ fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style NEXT fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
    style EXIT fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```""",

    (1, "clase-05-listas-y-colecciones"): """```mermaid
flowchart LR
    LISTA["📚 Lista Mutable<br/>['Python', 'Docker', 'FastAPI']"] --> MUT["🔧 Métodos de Mutación"]
    MUT --> APP["append('Git') ➔ Inserta al final"]
    MUT --> INS["insert(1, 'SQL') ➔ Inserta en índice"]
    MUT --> POP["pop() ➔ Extrae último elemento"]
    LISTA --> SLICE["✂️ Slicing [inicio:fin:paso]<br/>lista[::-1] ➔ Invertir lista"]
    LISTA --> COMP["⚡ List Comprehension<br/>[x**2 for x in nums if x%2==0]"]

    style LISTA fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style MUT fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style APP fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style INS fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style POP fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style SLICE fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style COMP fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
```""",

    (1, "clase-06-diccionarios"): """```mermaid
flowchart LR
    KEY["🔑 Clave: 'usuario'"] --> HASH["⚡ Función Hash O(1)"]
    HASH --> BUCKET["📦 Posición en Memoria"]
    BUCKET --> VAL["🎯 Valor: 'wisrovi'"]
    BUCKET --> GET["🛡️ .get(clave, default)<br/>Búsqueda segura sin KeyError"]
    BUCKET --> SET["✨ set() Conjuntos<br/>Deduplicación & Operaciones & / | / -"]

    style KEY fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style HASH fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BUCKET fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style VAL fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style GET fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style SET fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
```""",

    (1, "clase-07-funciones"): """```mermaid
flowchart TD
    CALL["🚀 Invocación: calcular_total(precio=100, iva=0.21)"] --> STACK["🥞 Call Stack: Push Frame de Función"]
    STACK --> SCOPE{"🔍 Resolución de Ámbito LEGB"}
    SCOPE -->|1. Local| L["Variables locales dentro de la función"]
    SCOPE -->|2. Global| G["Constantes globales del módulo"]
    SCOPE -->|3. Built-in| B["Funciones estándar (len, print, range)"]
    L --> RET["🎯 return total_calculado"]
    RET --> POP_F["🥞 Pop Frame ➔ Retornar valor al llamador"]

    style CALL fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style STACK fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style SCOPE fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style RET fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style POP_F fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```""",

    (1, "clase-08-proyecto-integrador-basico"): """```mermaid
flowchart TD
    CLI["🖥️ Interfaz de Terminal CLI"] --> MENU["📋 Menú Interactivo de 4 Opciones"]
    MENU --> READ["⌨️ Lectura con Validación try/except"]
    READ -->|1. Agregar| ADD["➕ TaskManager.agregar_tarea()"]
    READ -->|2. Listar| LST["📊 TaskManager.listar_tareas() en Tabla"]
    READ -->|3. Completar| CMP["✅ TaskManager.marcar_hecha()"]
    READ -->|4. Salir| EXT["👋 Cierre Seguro del Sistema"]
    ADD --> STATE[("💾 Estado de Tareas en Memoria")]
    LST --> STATE
    CMP --> STATE

    style CLI fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style MENU fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style READ fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style ADD fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style LST fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style CMP fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style EXT fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style STATE fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```"""
}

# ==============================================================================
# MERMAIDS ESPECÍFICOS PARA LOS 5 EJEMPLOS DE CLASE 01
# ==============================================================================
C1_EXAMPLES_MERMAID = {
    "ejemplo_01_print_y_mensajes": """```mermaid
flowchart LR
    TXT["📝 '¡Hola mundo!' (str)"] --> PRINT["📢 Función print()"]
    NUM["🔢 2026 (int sin comillas)"] --> PRINT
    PRINT --> STDOUT["🖥️ Buffer de Salida Estándar (stdout)"]
    STDOUT --> CONSOLE["✨ Impresión en Pantalla / Consola"]

    style TXT fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style NUM fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PRINT fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style STDOUT fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style CONSOLE fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```""",

    "ejemplo_02_variables_cajas_etiquetadas": """```mermaid
flowchart LR
    TAG1["🏷️ Etiqueta 'mi_nombre'"] --> BOX1["📦 Caja en Memoria ('Ana María')"]
    TAG2["🏷️ Etiqueta 'mi_edad'"] --> BOX2["📦 Caja en Memoria (28)"]
    REASIGN["⚡ Reasignación: mi_edad = 29"] --> BOX3["📦 Nueva Caja en Memoria (29)"]

    style TAG1 fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style BOX1 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style TAG2 fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style BOX2 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style REASIGN fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BOX3 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```""",

    "ejemplo_03_if_el_semaforo_de_decisiones": """```mermaid
flowchart TD
    DATA["👤 Visitante: Estatura = 1.55 m"] --> COND{"⚖️ ¿Estatura >= 1.40 m?"}
    COND -->|True (Sí)| GREEN["🟢 SEMÁFORO VERDE<br/>¡Adelante! Puedes subir a la montaña rusa 🎢"]
    COND -->|False (No)| RED["🔴 SEMÁFORO ROJO<br/>Aún eres bajo para este juego 🛑"]

    style DATA fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style COND fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style GREEN fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style RED fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```""",

    "ejemplo_04_for_la_cinta_transportadora": """```mermaid
flowchart LR
    LST["🛒 Lista: ['Manzanas 🍎', 'Leche 🥛', 'Pan 🍞', 'Café ☕']"] --> CINTA["🔄 Cinta Transportadora (for producto in lista:)"]
    CINTA --> PACK1["📦 Empacando: Manzanas 🍎"]
    PACK1 --> PACK2["📦 Empacando: Leche 🥛"]
    PACK2 --> PACK3["📦 Empacando: Pan 🍞"]
    PACK3 --> PACK4["📦 Empacando: Café ☕"]
    PACK4 --> DONE["✅ Todos los productos empacados"]

    style LST fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style CINTA fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style PACK1 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK2 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK3 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK4 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style DONE fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```""",

    "ejemplo_05_funcion_la_licuadora": """```mermaid
flowchart LR
    IN1["🍓 Fresa (fruta1)"] --> BLENDER["🍹 def licuadora(fruta1, fruta2):<br/>Procesa y mezcla ingredientes"]
    IN2["🍌 Plátano (fruta2)"] --> BLENDER
    BLENDER --> OUT["🥤 return 'Batido refrescante de Fresa con Plátano'"]

    style IN1 fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style IN2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BLENDER fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
}

def apply_refinements():
    print("=" * 80)
    print("🚀 APLICANDO REFINAMIENTO DE MERMAID VISUAL PREMIUM EN TODO EL REPOSITORIO")
    print("=" * 80)
    
    # 1. Actualizar Clase 01 README y ejemplos
    c1_dir = os.path.join(BASE_DIR, "01-fundamentos-python", "clase-01-panorama-general")
    c1_readme = os.path.join(c1_dir, "README.md")
    
    meta_c1 = CLASS_META_MAP.get((1, "clase-01-panorama-general"))
    if meta_c1 and os.path.exists(c1_readme):
        c1_diag = CLASS_MERMAIDS.get((1, "clase-01-panorama-general"))
        content = f"""# 📘 {meta_c1['class_title']}

> **Curso:** Curso 1: Fundamentos Básicos de Python ({meta_c1['class_code']})  
> **Nivel:** {meta_c1['level']} &bull; **Metáfora Central:** *«{meta_c1['metaphor']}»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-01-panorama-general/notebook/clase-01-panorama-general.ipynb)

---

## 🗺️ Mapa Conceptual: Los 4 Pilares de la Programación

{c1_diag}

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-01-panorama-general.pdf`](clase-01-panorama-general.pdf): Manual técnico oficial en PDF (9 páginas con estética LaTeX).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 5 carpetas de código con demostraciones comentadas paso a paso.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
"""
        with open(c1_readme, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ Actualizado 01-fundamentos-python/clase-01-panorama-general/README.md")

    # 2. Actualizar los 5 ejemplos de Clase 01
    for ex_folder, mermaid_code in C1_EXAMPLES_MERMAID.items():
        ex_path = os.path.join(c1_dir, "ejemplos", ex_folder, "README.md")
        if os.path.exists(ex_path):
            ex_title = ex_folder.replace("ejemplo_", "").replace("_", " ").title()
            content = f"""# 📖 {ex_title}

> **Clase:** {meta_c1['class_title']}  
> **Archivo de Código:** [`main.py`](main.py)  

Demostración práctica y ejecutable de este concepto fundamental de Python.

---

## 🗺️ Flujo de Ejecución del Ejemplo

{mermaid_code}

---

## 💻 Ejecución desde Terminal
```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/{ex_folder}/main.py
```
"""
            with open(ex_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Actualizado ejemplo {ex_folder}")

    # 3. Aplicar a las demás 31 clases
    for (c_num, f_name), meta in CLASS_META_MAP.items():
        if (c_num, f_name) == (1, "clase-01-panorama-general"):
            continue
            
        c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
        c_dir = os.path.join(BASE_DIR, c_cfg["course_id"], f_name)
        c_readme = os.path.join(c_dir, "README.md")
        
        if os.path.exists(c_readme):
            # Obtener diagrama refinado
            diag = CLASS_MERMAIDS.get((c_num, f_name))
            if not diag:
                # Generar diagrama con colores y estilos premium
                diag = f"""```mermaid
flowchart LR
    A["📥 1. Entrada de Datos<br/>({meta['metaphor'][:30]}...)"] --> B["⚙️ 2. Motor de Ejecución<br/>{meta['class_title'].split(':')[-1].strip()}"]
    B --> C["🎯 3. Salida / Estado Actualizado<br/>print() / Retorno DTO"]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
            nb_name = meta["pdf_filename"].replace(".pdf", ".ipynb")
            colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{c_cfg['course_id']}/{f_name}/notebook/{nb_name}"
            
            content = f"""# 📘 {meta['class_title']}

> **Curso:** {c_cfg['course_name']} ({meta['class_code']})  
> **Nivel:** {meta['level']} &bull; **Metáfora:** *«{meta['metaphor']}»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

{diag}

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
"""
            with open(c_readme, "w", encoding="utf-8") as f:
                f.write(content)

    print("\n" + "=" * 80)
    print("✨ ESTÁNDAR MERMAID PREMIUM APLICADO CON ÉXITO EN TODAS LAS CLASES Y EJEMPLOS.")
    print("=" * 80)

if __name__ == "__main__":
    apply_refinements()
