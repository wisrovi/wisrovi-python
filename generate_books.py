#!/usr/bin/env python3
"""
Generador de archivos book.md para cada una de las 17 clases/módulos del repositorio wisrovi-python.
Cada book.md reproduce el contenido completo del PDF con formato Markdown enriquecido y diagramas Mermaid nativos.
"""

import os
from typing import Dict, Any

from build_all_course_pdfs import CLASSES_METADATA, AUTHOR_INFO, BASE_DIR

def get_mermaid_diagram(diagram_type: str, class_title: str) -> str:
    """Genera diagramas Mermaid nativos compatibles con GitHub."""
    if diagram_type == "flow":
        return """```mermaid
flowchart LR
    A["🎬 1. Entrada / Input"] --> B{"⚖️ 2. ¿Condición Booleana?"}
    B -- "Sí (True)" --> C["⚙️ 3. Procesamiento y Transformación"]
    B -- "No (False / Else)" --> D["🔀 3b. Flujo Alternativo"]
    C --> E["🎯 4. Retorno / Salida (print / return)"]
    D --> E

    style A fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style D fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style E fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```"""
    elif diagram_type == "loop":
        return """```mermaid
flowchart LR
    A["📦 Colección / Rango"] --> B["🔄 Iterador (for / while)"]
    B --> C["⚡ Ejecuta Cuerpo del Bucle"]
    C -- "Siguiente Iteración" --> B
    C -- "break / Condición Agotada" --> D["🏁 Fin del Ciclo"]

    style A fill:#1e293b,color:#fff,stroke:#38bdf8,stroke-width:2px
    style B fill:#0369a1,color:#fff,stroke:#7dd3fc,stroke-width:2px
    style C fill:#047857,color:#fff,stroke:#6ee7b7,stroke-width:2px
    style D fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
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
        RES["Salida Formateada JSON/UI"]
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

def clean_html_tags(text: str) -> str:
    """Limpia etiquetas HTML para formato Markdown limpio."""
    return (
        text.replace('<span class="cm">', '')
            .replace('<span class="kw">', '')
            .replace('<span class="fn">', '')
            .replace('<span class="bi">', '')
            .replace('<span class="st">', '')
            .replace('<span class="nu">', '')
            .replace('<span class="op">', '')
            .replace('</span>', '')
            .replace('&gt;', '>')
            .replace('&lt;', '<')
            .replace('&amp;', '&')
            .replace('\\n', '\n')
            .replace('\\"', '"')
            .replace("\\'", "'")
    )

def build_book_markdown(meta: Dict[str, Any]) -> str:
    """Genera el contenido completo de book.md para una clase."""
    
    course_name = meta["course_name"]
    course_num = meta["course_num"]
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    metaphor = meta["metaphor"]
    level = meta["level"]
    diagram_type = meta.get("diagram_type", "flow")
    
    mermaid_block = get_mermaid_diagram(diagram_type, class_title)
    code_raw = clean_html_tags(meta["p6_code"])
    bad_code_raw = clean_html_tags(meta["p7_bad_code"])
    good_code_raw = clean_html_tags(meta["p7_good_code"])
    
    md = f"""# 📖 {class_title}

> **Programa:** {course_name} (Nivel {course_num})  
> **Nivel de Dificultad:** {level}  
> **Metáfora Central:** *«{metaphor}»*  
> **Python Version:** 3.10+ | **Licencia:** MIT  

---

## 👤 Acerca del Autor y Mentor

### **{AUTHOR_INFO["name"]}**
**{AUTHOR_INFO["title"]}** &bull; *{AUTHOR_INFO["location"]}*

{AUTHOR_INFO["bio"]}

*   🐙 **GitHub:** [{AUTHOR_INFO["github"].replace("https://", "")}]({AUTHOR_INFO["github"]})
*   💼 **LinkedIn:** [{AUTHOR_INFO["linkedin"].replace("https://", "")}]({AUTHOR_INFO["linkedin"]})
*   🐳 **DockerHub:** [{AUTHOR_INFO["dockerhub"].replace("https://", "")}]({AUTHOR_INFO["dockerhub"]})
*   🌐 **Website:** [{AUTHOR_INFO["website"].replace("https://", "")}]({AUTHOR_INFO["website"]})
*   📦 **PyPI:** [{AUTHOR_INFO["pypi"].replace("https://", "")}]({AUTHOR_INFO["pypi"]})

---

### 🚲 Metodología de Aprendizaje: La Regla de la Bicicleta

> *"Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."*

> [!TIP]
> **El Compromiso Activo del Estudiante:** Abre Visual Studio Code en cada sesión. Escribe cada ejemplo con tus propias manos. Cambia los números, rompe el código deliberadamente para ver el mensaje de error de Python, y luego arréglalo.

---

## 📑 Tabla de Contenidos

| Capítulo | Tema | Enfoque Principal |
| :--- | :--- | :--- |
| **01** | **Fundamentos & Metáfora** | {meta["p4_title"]} |
| **02** | **Arquitectura de Flujo** | {meta["p5_title"]} |
| **03** | **Implementación Práctica** | {meta["p6_title"]} |
| **04** | **Patrones & Debugging** | {meta["p7_title"]} |
| **05** | **Conclusiones & Cierre** | Resumen ejecutivo, notas del mentor y agradecimiento |
| **06** | **Bibliografía & Recursos** | Fuentes oficiales y retos de autoestudio |

### 🎯 Objetivos de Aprendizaje

*   **Competencia Conceptual:** {meta["obj_conceptual"]}
*   **Competencia Práctica:** {meta["obj_practical"]}

---

## 1. 💡 {meta["p4_title"]}

{meta["p4_intro"]}

> [!NOTE]
> ### 🌟 Metáfora Central: {meta["metaphor"]}
> {meta["p4_metaphor_desc"]}

### Principios Teóricos y Modelo Mental

{meta["p4_theory_1"]}

{meta["p4_theory_2"]}

> [!IMPORTANT]
> ### ⚡ Regla de Oro en Python
> {meta["p4_golden_rule"]}

---

## 2. 🗺️ {meta["p5_title"]}

{meta["p5_desc"]}

### Diagrama Visual del Flujo

{mermaid_block}

### Desglose Paso a Paso del Flujo

| Fase del Flujo | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **1. Inicialización** | {meta["p5_step1_action"]} | `{meta["p5_step1_state"]}` |
| **2. Evaluación** | {meta["p5_step2_action"]} | `{meta["p5_step2_state"]}` |
| **3. Transformación** | {meta["p5_step3_action"]} | `{meta["p5_step3_state"]}` |
| **4. Retorno / Salida** | {meta["p5_step4_action"]} | `{meta["p5_step4_state"]}` |

> [!TIP]
> **Visualización Mental:** {meta["p5_mental_tip"]}

---

## 3. 💻 {meta["p6_title"]}

{meta["p6_desc"]}

```python
# main.py - Python 3.10+ PEP 8 Compliant
{code_raw}
```

### Análisis del Código Fuente

{meta["p6_code_analysis"]}

---

## 4. 🛡️ {meta["p7_title"]}

{meta["p7_intro"]}

> [!WARNING]
> ### ⚠️ Gotcha Frecuente (Trampa de Principiante)
> {meta["p7_gotcha"]}

### Comparativa: Antipatrón vs Patrón Recomendado

#### ❌ Antipatrón / Mal Código:
```python
{bad_code_raw}
```

#### ✅ Patrón Pythonic / Correcto:
```python
{good_code_raw}
```

> [!TIP]
> **Consejo de Resiliencia en Producción:** {meta["p7_pro_tip"]}

---

## 5. 🏆 Conclusiones y Resumen Ejecutivo

{meta["p8_summary"]}

> [!NOTE]
> ### 🎖️ Logro Alcanzado
> {meta["p8_achievement"]}

### 📝 Notas del Instructor
{meta["p8_instructor_notes"]}

### 🤝 Mensaje de Agradecimiento
Muchas gracias por tu entusiasmo, disciplina y dedicación al participar en este programa formativo. La programación es un superpoder que transforma vidas cuando se ejerce con constancia y curiosidad. ¡Nos vemos en la próxima sesión para seguir construyendo juntos! 💻🚀

---

## 6. 📚 Bibliografía y Fuentes de Estudio

| Fuente / Recurso | Descripción Temática | Enlace Oficial |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Referencia canónica del lenguaje y librería estándar | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Guía oficial de estilo, formato e indentación | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Artículos técnicos y patrones de desarrollo moderno | [realpython.com](https://realpython.com/) |
| **Python Type Checking (PEP 484)** | Anotaciones de tipo y análisis estático | [docs.python.org/typing](https://docs.python.org/3/library/typing.html) |
| **Suite Open Source wisrovi** | Paquetes Python para orquestación y rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |

> [!TIP]
> ### 🏋️ Desafío de Autoestudio Recomendado
> {meta["p9_challenge"]}
"""
    return md

def main():
    print("=" * 70)
    print("📖 GENERANDO ARCHIVOS book.md PARA TODAS LAS CLASES Y CURSOS")
    print(f"📦 Total de clases a procesar: {len(CLASSES_METADATA)}")
    print("=" * 70 + "\n")
    
    count = 0
    for meta in CLASSES_METADATA:
        target_dir = meta["target_dir"]
        book_path = os.path.join(target_dir, "book.md")
        
        md_content = build_book_markdown(meta)
        
        with open(book_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        file_size = os.path.getsize(book_path)
        print(f"  ✓ [{meta['class_code']}] {meta['class_title']}")
        print(f"    -> Creado: {book_path} ({file_size} bytes)")
        count += 1
        
    print("\n" + "=" * 70)
    print(f"✨ COMPLETADO: {count}/{len(CLASSES_METADATA)} archivos book.md generados con éxito.")
    print("=" * 70)

if __name__ == "__main__":
    main()
