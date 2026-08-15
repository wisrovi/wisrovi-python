#!/usr/bin/env python3
"""
Genera la plataforma web interactiva completa (Libro Digital de la Academia) en docs/
con sintaxis nativa de MkDocs Material: Admonitions (!!! note, !!! tip), pestañas de código,
Mermaid verificado 100% compatible y contenido exhaustivo.
"""

import os
import shutil
from typing import Dict, Any, List

from build_all_course_pdfs import CLASSES_METADATA, AUTHOR_INFO, BASE_DIR
from generate_books import clean_html_tags

DOCS_DIR = os.path.join(BASE_DIR, "docs")

def get_mkdocs_mermaid(diagram_type: str, class_title: str) -> str:
    """Genera diagramas Mermaid 100% compatibles con MkDocs Material sin errores de sintaxis."""
    if diagram_type == "flow":
        return """```mermaid
flowchart LR
    A["🎬 1. Entrada / Input"] --> B{"⚖️ 2. ¿Condición Booleana?"}
    B -->|Sí / True| C["⚙️ 3. Procesamiento y Transformación"]
    B -->|No / False| D["🔀 3b. Rama Alternativa (Else)"]
    C --> E["🎯 4. Retorno / Salida (print / return)"]
    D --> E

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style D fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style E fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
    elif diagram_type == "loop":
        return """```mermaid
flowchart LR
    A["📦 Colección / Rango"] --> B["🔄 Iterador (for / while)"]
    B --> C["⚡ Ejecuta Cuerpo del Bucle"]
    C -->|Siguiente Iteración| B
    C -->|break / Fin de Rango| D["🏁 Fin del Ciclo"]

    style A fill:#1e293b,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style B fill:#0369a1,color:#ffffff,stroke:#7dd3fc,stroke-width:2px
    style C fill:#047857,color:#ffffff,stroke:#6ee7b7,stroke-width:2px
    style D fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```"""
    elif diagram_type == "architecture":
        return """```mermaid
flowchart LR
    subgraph Entrada["📥 Capa de Entrada"]
        UI["Prompt / UI / Request"]
        VAL["Validación DTO / Input"]
    end

    subgraph Core["🧠 Núcleo de Ejecución & Lógica"]
        ENG["Motor / Algoritmo / LLM"]
        MEM["Estado / Memoria"]
        TOOL["Herramientas / Funciones"]
    end

    subgraph Salida["💾 Persistencia y Respuesta"]
        DB[("Base de Datos / Vector Store")]
        RES["Salida Formateada JSON / UI"]
    end

    UI --> VAL
    VAL --> ENG
    ENG <--> MEM
    ENG <--> TOOL
    TOOL --> DB
    ENG --> RES

    style Entrada fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style Core fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style Salida fill:#f0fdf4,stroke:#10b981,stroke-width:2px
```"""
    else:
        return f"""```mermaid
flowchart TD
    A["{class_title}"] --> B["Procesamiento Lógico"]
    B --> C["Resultado Final"]
```"""

def build_rich_class_doc(meta: Dict[str, Any]) -> str:
    """Construye una página web completa, didáctica y exhaustiva para una clase."""
    
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    course_name = meta["course_name"]
    course_num = meta["course_num"]
    level = meta["level"]
    metaphor = meta["metaphor"]
    diagram_type = meta.get("diagram_type", "flow")
    
    mermaid_block = get_mkdocs_mermaid(diagram_type, class_title)
    code_raw = clean_html_tags(meta["p6_code"])
    bad_code_raw = clean_html_tags(meta["p7_bad_code"])
    good_code_raw = clean_html_tags(meta["p7_good_code"])
    pdf_filename = meta["pdf_filename"]
    
    md = f"""# {class_title}

<div class="grid cards" markdown>

-   :material-school: __Nivel:__ {level}
-   :material-book-open-page-variant: __Curso:__ {course_name}
-   :material-lightbulb-on: __Metáfora:__ *«{metaphor}»*
-   :material-file-pdf-box: __Descargar PDF:__ [{pdf_filename}](https://github.com/wisrovi/wisrovi-python/blob/main/{meta['target_dir'].replace(BASE_DIR + '/', '')}/{pdf_filename})

</div>

---

## 🎯 Objetivos de Aprendizaje

!!! abstract "Competencias Clave de la Sesión"
    *   **Competencia Conceptual:** {meta["obj_conceptual"]}
    *   **Competencia Práctica:** {meta["obj_practical"]}

---

## 1. 💡 Fundamentos Teóricos y Modelo Mental

{meta["p4_intro"]}

!!! note "🌟 Metáfora Central: {meta['metaphor']}"
    {meta["p4_metaphor_desc"]}

### Principios Fundamentales

{meta["p4_theory_1"]}

{meta["p4_theory_2"]}

!!! tip "⚡ Regla de Oro en Python"
    {meta["p4_golden_rule"]}

---

## 2. 🗺️ Diagrama de Arquitectura y Flujo de Control

{meta["p5_desc"]}

{mermaid_block}

### Desglose Paso a Paso del Flujo

| Fase del Flujo | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **1. Inicialización** | {meta["p5_step1_action"]} | `{meta["p5_step1_state"]}` |
| **2. Evaluación** | {meta["p5_step2_action"]} | `{meta["p5_step2_state"]}` |
| **3. Transformación** | {meta["p5_step3_action"]} | `{meta["p5_step3_state"]}` |
| **4. Retorno / Salida** | {meta["p5_step4_action"]} | `{meta["p5_step4_state"]}` |

!!! info "🔍 Visualización Mental"
    {meta["p5_mental_tip"]}

---

## 3. 💻 Implementación Práctica en Python

{meta["p6_desc"]}

```python title="main.py - Python 3.10+ (PEP 8)" linenums="1"
{code_raw}
```

### Análisis Detallado del Código

{meta["p6_code_analysis"]}

---

## 4. 🛡️ Buenas Prácticas, Gotchas y Depuración

{meta["p7_intro"]}

!!! warning "⚠️ Gotcha Frecuente (Trampa de Principiante)"
    {meta["p7_gotcha"]}

### Comparativa: Patrón Recomendado vs Antipatrón

=== "✅ Patrón Pythonic Recomendado"
    ```python
{good_code_raw}
    ```

=== "❌ Antipatrón / Mal Código"
    ```python
{bad_code_raw}
    ```

!!! success "🛡️ Consejo de Resiliencia en Producción"
    {meta["p7_pro_tip"]}

---

## 5. 🏋️ Ejercicios y Desafío de Autoestudio

!!! example "Desafío Práctico Recomendado"
    {meta["p9_challenge"]}

???+ tip "🧪 Cómo validar tu solución con Pytest"
    Abre tu terminal en VS Code y ejecuta:
    ```bash
    pytest {meta['target_dir'].replace(BASE_DIR + '/', '')}/ejercicios/
    ```

---

## 6. 📚 Fuentes y Referencias Oficiales

| Fuente / Recurso | Descripción Temática | Enlace Oficial |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Referencia canónica del lenguaje y librería estándar | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Guía oficial de estilo, formato e indentación | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Artículos técnicos y patrones de desarrollo moderno | [realpython.com](https://realpython.com/) |
| **Suite Open Source wisrovi** | Paquetes Python para orquestación y rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |
"""
    return md

def build_rich_course_book_doc(course_id: str, title: str, subtitle: str, level: str, class_list: List[Dict[str, Any]]) -> str:
    """Construye la página principal interactiva del libro de cada curso."""
    
    md = f"""# 📚 {title}

> **{subtitle}**  
> **Nivel:** {level} &bull; **Instructor:** **{AUTHOR_INFO['name']}** ({AUTHOR_INFO['title']})

---

## 🗺️ Mapa de Contenidos del Curso

```mermaid
flowchart TD
"""
    for idx, c in enumerate(class_list, 1):
        clean_name = c['class_title'].replace('Clase ', 'C').replace('Módulo ', 'M').replace('Track ', 'T')
        if idx < len(class_list):
            next_c = class_list[idx]['class_title'].replace('Clase ', 'C').replace('Módulo ', 'M').replace('Track ', 'T')
            md += f'    N{idx}["{c["class_code"]}: {clean_name}"] --> N{idx+1}["{class_list[idx]["class_code"]}: {next_c}"]\n'
            
    md += f"""
    style N1 fill:#2b5c8f,color:#fff,stroke:#fff,stroke-width:2px
```

---

## 📑 Unidades Didácticas del Curso

| Unidad | Título | Metáfora Central | Enfoque Principal |
| :---: | :--- | :--- | :--- |
"""
    for c in class_list:
        md += f"| **{c['class_code']}** | **{c['class_title']}** | *«{c['metaphor']}»* | {c['obj_conceptual'][:80]}... |\n"
        
    md += f"""
---

## 🚲 Metodología: La Regla de la Bicicleta

> *"Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."*

!!! tip "Cómo estudiar este curso"
    1. Lee la lección temática de cada unidad.
    2. Analiza el diagrama de flujo y comprende el movimiento de los datos en memoria.
    3. Escribe y ejecuta el código en VS Code o en Google Colab.
    4. Resuelve los ejercicios y valida tu código ejecutando `pytest`.
"""
    return md

def build_academy_index():
    """Genera la página de inicio completa del portal web."""
    return f"""# 🐍 Programa Integral de Formación en Python
### *De Cero a Agentes de Inteligencia Artificial*

<div class="grid cards" markdown>

-   :material-school: __Nivel:__ Principiante a Avanzado
-   :material-account-tie: __Instructor:__ [William Rodríguez (Wisrovi)](https://wisrovi.dev)
-   :material-code-tags: __Tecnologías:__ Python 3.10+, FastAPI, Streamlit, Pydantic, RAG, ReAct Agents
-   :material-license: __Licencia:__ Código Abierto (MIT)

</div>

Bienvenido/a a la plataforma web interactiva del **Programa de Formación en Python**. Esta academia online está diseñada para guiarte paso a paso desde que escribes tu primera línea de código hasta el desarrollo y despliegue de **Agentes de Inteligencia Artificial Autónomos** y aplicaciones web de producción.

---

## 🚀 La Ruta de Aprendizaje (4 Niveles Secuenciales)

```mermaid
flowchart TD
    C1["🎯 Curso 1: Fundamentos de Python<br/>(8 Clases - 100% Principiantes)"] --> C2["🚀 Curso 2: Algoritmos Avanzados<br/>y Estructuras de Datos"]
    C2 --> C3["🤖 Curso 3: Creación y Desarrollo<br/>de Agentes de IA"]
    C3 --> C4["🛠️ Curso 4: Taller Práctico &<br/>Proyecto Final Personalizado"]

    style C1 fill:#2b5c8f,color:#fff,stroke:#fff,stroke-width:2px
    style C2 fill:#3b7a57,color:#fff,stroke:#fff,stroke-width:2px
    style C3 fill:#6b4c9a,color:#fff,stroke:#fff,stroke-width:2px
    style C4 fill:#c05621,color:#fff,stroke:#fff,stroke-width:2px
```

---

## 📚 Explorador de Cursos

=== "🎯 Curso 1: Fundamentos (8 Clases)"
    *   **Público objetivo:** 100% Principiantes que nunca han programado.
    *   **Contenidos:** Variables, Tipos de Datos, Condicionales (`if`/`else`), Bucles (`for`/`while`), Listas, Diccionarios, Funciones (`def`) y Proyecto CLI.
    *   [👉 Ir al Curso 1](curso-01/book.md)

=== "🚀 Curso 2: Algoritmos y Estructuras"
    *   **Público objetivo:** Nivel Intermedio enfocado en optimización y entrevistas técnicas.
    *   **Contenidos:** Pilas (LIFO), Colas (FIFO), Sets, Análisis Big-O ($\mathcal{{O}}(n)$), Búsqueda Binaria, QuickSort y Programación Dinámica con Memoización (`@lru_cache`).
    *   [👉 Ir al Curso 2](curso-02/book.md)

=== "🤖 Curso 3: Agentes de Inteligencia Artificial"
    *   **Público objetivo:** Nivel Avanzado para ingenieros de IA.
    *   **Contenidos:** Modelos LLM, Validación Tipada con Pydantic, Tool Calling / Function Calling, Memoria Vectorial y RAG, y Arquitectura de Agentes ReAct.
    *   [👉 Ir al Curso 3](curso-03/book.md)

=== "🛠️ Curso 4: Taller Práctico y Proyecto Final"
    *   **Público objetivo:** Integración profesional y portafolio.
    *   **Contenidos:** Aplicación Web Full-Stack (FastAPI + Streamlit), Chatbot Inteligente con Memoria y Sistema Transaccional con Base de Datos SQL.
    *   [👉 Ir al Curso 4](curso-04/book.md)

---

## 👤 Acerca del Instructor y Mentor

<div class="grid cards" markdown>

<div>
<h3>William Rodríguez (Wisrovi)</h3>
<p><strong>AI Solutions Architect & Principal Software Engineer</strong> &bull; Badajoz, España</p>

Ingeniero y arquitecto de software especializado en Inteligencia Artificial Generativa, sistemas multi-agente, Visión por Computador e infraestructuras MLOps de alta disponibilidad. Creador y mantenedor de la suite de software libre <strong>wisrovi SUITE</strong> en PyPI con más de 26 bibliotecas enfocadas en orquestación de pipelines, caching distribuido y optimización de bases de datos.

*   🐙 **GitHub:** [github.com/wisrovi](https://github.com/wisrovi)
*   💼 **LinkedIn:** [linkedin.com/in/wisrovi-rodriguez](https://www.linkedin.com/in/wisrovi-rodriguez/)
*   🐳 **DockerHub:** [hub.docker.com/u/wisrovi](https://hub.docker.com/u/wisrovi)
*   🌐 **Website:** [wisrovi.dev](https://wisrovi.dev)
</div>

</div>

---

## 🚲 Filosofía de Estudio: La Regla de la Bicicleta

!!! quote "La Regla de Oro"
    *"Por más libros que leas o explicaciones que escuches sobre cómo guardar el equilibrio, si no te subes a la bicicleta y pedaleas por ti mismo, nunca vas a aprender a andar en bici."*

Aprender a programar es una habilidad 100% práctica. Esta plataforma incluye código fuente ejecutable, cuadernos de Google Colab y pruebas automatizadas con `pytest` para cada lección. ¡Abre tu editor, escribe el código y experimenta! 🚴‍♂️
"""

def main():
    print("=" * 70)
    print("🌐 REGENERANDO PORTAL WEB INTERACTIVO EN docs/ PARA MKDOCS MATERIAL")
    print("=" * 70)
    
    # 1. Crear docs/index.md
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(build_academy_index())
    print("  ✓ Creado docs/index.md (Portal Principal)")

    # 2. Generar Curso 1
    c1_dir = os.path.join(DOCS_DIR, "curso-01")
    os.makedirs(c1_dir, exist_ok=True)
    c1_classes = [m for m in CLASSES_METADATA if "01-fundamentos-python" in m["target_dir"]]
    
    with open(os.path.join(c1_dir, "book.md"), "w", encoding="utf-8") as f:
        f.write(build_rich_course_book_doc("c1", "Curso 1: Fundamentos Básicos de Python", "De Cero a Programador: Los 4 Pilares Lógicos y Proyecto CLI", "Principiantes Absolutos", c1_classes))
        
    for i, c in enumerate(c1_classes, 1):
        with open(os.path.join(c1_dir, f"clase-{i:02d}.md"), "w", encoding="utf-8") as f:
            f.write(build_rich_class_doc(c))
        print(f"  ✓ Generado docs/curso-01/clase-{i:02d}.md")

    # 3. Generar Curso 2
    c2_dir = os.path.join(DOCS_DIR, "curso-02")
    os.makedirs(c2_dir, exist_ok=True)
    c2_classes = [m for m in CLASSES_METADATA if "02-algoritmos-estructuras" in m["target_dir"]]
    
    with open(os.path.join(c2_dir, "book.md"), "w", encoding="utf-8") as f:
        f.write(build_rich_course_book_doc("c2", "Curso 2: Algoritmos Avanzados y Estructuras de Datos", "Optimización de Memoria, Big-O, Pilas, Colas y Programación Dinámica", "Intermedio", c2_classes))
        
    for i, c in enumerate(c2_classes, 1):
        with open(os.path.join(c2_dir, f"modulo-{i:02d}.md"), "w", encoding="utf-8") as f:
            f.write(build_rich_class_doc(c))
        print(f"  ✓ Generado docs/curso-02/modulo-{i:02d}.md")

    # 4. Generar Curso 3
    c3_dir = os.path.join(DOCS_DIR, "curso-03")
    os.makedirs(c3_dir, exist_ok=True)
    c3_classes = [m for m in CLASSES_METADATA if "03-agentes-ia" in m["target_dir"]]
    
    with open(os.path.join(c3_dir, "book.md"), "w", encoding="utf-8") as f:
        f.write(build_rich_course_book_doc("c3", "Curso 3: Creación y Desarrollo de Agentes de IA", "Modelos LLM, Tool Calling, Memoria Vectorial, RAG y Agentes Autónomos ReAct", "Avanzado", c3_classes))
        
    for i, c in enumerate(c3_classes, 1):
        with open(os.path.join(c3_dir, f"modulo-{i:02d}.md"), "w", encoding="utf-8") as f:
            f.write(build_rich_class_doc(c))
        print(f"  ✓ Generado docs/curso-03/modulo-{i:02d}.md")

    # 5. Generar Curso 4
    c4_dir = os.path.join(DOCS_DIR, "curso-04")
    os.makedirs(c4_dir, exist_ok=True)
    c4_classes = [m for m in CLASSES_METADATA if "04-proyecto-final" in m["target_dir"]]
    
    with open(os.path.join(c4_dir, "book.md"), "w", encoding="utf-8") as f:
        f.write(build_rich_course_book_doc("c4", "Curso 4: Taller Práctico & Proyecto Final Personalizado", "Construcción de Soluciones Reales: Full-Stack Web, Chatbot Inteligente y BD SQL", "Integrador", c4_classes))
        
    for i, c in enumerate(c4_classes, 1):
        with open(os.path.join(c4_dir, f"track-{i:02d}.md"), "w", encoding="utf-8") as f:
            f.write(build_rich_class_doc(c))
        print(f"  ✓ Generado docs/curso-04/track-{i:02d}.md")

    print("\n✨ Portal web interactivo completamente generado en docs/.")

if __name__ == "__main__":
    main()
