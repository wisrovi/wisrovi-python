#!/usr/bin/env python3
"""
Compilador Maestro de la Documentación Web (MkDocs Material) en docs/
Sincroniza el 100% de los contenidos de las 32 clases, libros digitales,
diagramas Mermaid de alto contraste y metadatos canónicos para academy_python.wisrovi.dev.
"""

import os
import sys
import re
from typing import Dict, Any, List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO
import refine_all_mermaid_styles

DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

def clean_html(text: str) -> str:
    """Limpia etiquetas HTML para que el Markdown se renderice perfectamente."""
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"</?[^>]+>", "", text)
    return text.strip()

# ==============================================================================
# 1. PÁGINA PRINCIPAL: docs/index.md (PORTAL ACADÉMICO WORLD-CLASS)
# ==============================================================================
def build_docs_index() -> str:
    return f"""# 🐍 Academia de Python: De Cero a Agentes de IA

<div class="grid cards" markdown>

-   :material-school: __Programa Completo:__ 4 Cursos &bull; 32 Semanas Formativas
-   :material-account-tie: __Director Académico:__ [{AUTHOR_INFO['name']}]({AUTHOR_INFO['website']})
-   :material-code-tags: __Stack de Ingeniería:__ Python 3.10+, FastAPI, Streamlit, Pydantic, RAG, ReAct Agents, Docker
-   :material-license: __Licencia:__ Código Abierto (MIT)

</div>

<div align="center" style="margin: 1.5rem 0;" markdown>

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisrovi/wisrovi-python)
[![Repository](https://img.shields.io/badge/GitHub-wisrovi--python-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python)
[![PyPI](https://img.shields.io/badge/PyPI-26%2B%20Librerías-3775A9?logo=pypi&logoColor=white)](https://pypi.org/user/wisrovi/)
[![Tests](https://img.shields.io/badge/Pytest-34%20Passing%20100%25-brightgreen.svg?logo=pytest&logoColor=white)](https://github.com/wisrovi/wisrovi-python)

</div>

Bienvenido/a al portal oficial del **Programa Integral de Formación en Python**. Esta plataforma reúne todo el material interactivo, manuales técnicos descargables en PDF, libros digitales y cuadernos ejecutables en Google Colab para formarte desde los fundamentos de la programación hasta el despliegue de **Agentes de Inteligencia Artificial**.

---

## 👤 Dirección Académica y Mentoría

<div class="grid cards" markdown>

-   **{AUTHOR_INFO['name']}**  
    *{AUTHOR_INFO['title']} &bull; Badajoz, España*  
    Ingeniero de software y arquitecto de sistemas de Inteligencia Artificial Generativa. Creador y mantenedor de **wisrovi SUITE** en PyPI con más de 26 paquetes publicados de optimización y rendimiento.
    
    [:octicons-mark-github-16: GitHub]({AUTHOR_INFO['github']}) &bull; [:octicons-globe-16: Sitio Web]({AUTHOR_INFO['website']}) &bull; [:octicons-package-16: PyPI]({AUTHOR_INFO['pypi']})

</div>

---

## 🌀 Metodología Pedagógica: Aprendizaje en Espiral

Nuestra metodología se basa en el **Aprendizaje en Espiral *(Spiral Learning)***: el estudiante nunca memoriza conceptos aislados, sino que los experimenta en ciclos continuos de complejidad creciente:

```mermaid
flowchart TD
    subgraph Espiral["🌀 Ciclo de Aprendizaje en Espiral (32 Semanas)"]
        F1["🌱 Fase 1: Visión Holística (Semanas 1-8)<br/>Primer contacto práctico: print, variables, if, for y funciones en un Gestor CLI."]
        F2["⚡ Fase 2: Rigor Algorítmico (Semanas 9-16)<br/>Análisis Big-O, Pilas, Colas, Tablas Hash, Árboles BST, Grafos y DP Memoizada."]
        F3["🤖 Fase 3: Agentes de IA (Semanas 17-24)<br/>LLMs, Pydantic, Tool Calling, Embeddings Vectoriales, RAG y ciclo ReAct."]
        F4["🛠️ Fase 4: Proyecto Integrador (Semanas 25-32)<br/>FastAPI REST + SQLite ACID + UI Streamlit + Docker Compose + CI/CD."]
        F1 ==> F2
        F2 ==> F3
        F3 ==> F4
    end

    style Espiral fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#ffffff
    style F1 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
    style F2 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ffffff
    style F3 fill:#3b0764,stroke:#c084fc,stroke-width:2px,color:#ffffff
    style F4 fill:#7c2d12,stroke:#fb923c,stroke-width:2px,color:#ffffff
```

!!! tip "🚲 La Regla de la Bicicleta (Pedaleo Activo)"
    Nadie aprende a programar leyendo código ajeno de forma pasiva. El aprendizaje real se consolida cuando abres tu editor, escribes el código por ti mismo, interpretas los mensajes de error de Python y superas los retos con las pruebas de Pytest.

---

## 📚 Mapa General de los 4 Cursos

=== "🎯 Curso 1: Fundamentos (8 Semanas)"
    *   **Nivel:** 100% Principiantes &bull; **Clases:** 8 &bull; **Ejemplos:** 33
    *   **Temario:** Primer vistazo práctico, variables y tipos de datos en memoria, condicionales `if/else`, bucles `for/while`, colecciones mutables, diccionarios O(1), funciones modulares y proyecto CLI.
    *   [📘 Ver Manual Completo del Curso 1](curso-01/book.md) &bull; [🚀 Explorar Clase 01](curso-01/clase-01.md)

=== "⚡ Curso 2: Algoritmos y Estructuras (8 Semanas)"
    *   **Nivel:** Intermedio &bull; **Clases:** 8 &bull; **Ejemplos:** 32
    *   **Temario:** Notación Big-O, pilas y colas con `deque`, tablas hash, búsqueda binaria, QuickSort, árboles BST, grafos BFS/DFS y memoización dinámica con `@lru_cache`.
    *   [📘 Ver Manual Completo del Curso 2](curso-02/book.md) &bull; [🚀 Explorar Clase 01](curso-02/clase-01.md)

=== "🤖 Curso 3: Agentes de Inteligencia Artificial (8 Semanas)"
    *   **Nivel:** Avanzado &bull; **Clases:** 8 &bull; **Ejemplos:** 32
    *   **Temario:** Modelos LLM y tokenización BPE, Prompt Engineering, validación con Pydantic V2, Tool Calling en Python, bases vectoriales y similitud coseno, arquitecturas RAG semánticas, agentes ReAct y sistemas multi-agente.
    *   [📘 Ver Manual Completo del Curso 3](curso-03/book.md) &bull; [🚀 Explorar Clase 01](curso-03/clase-01.md)

=== "🛠️ Curso 4: Proyecto Final Integrador (8 Semanas)"
    *   **Nivel:** Profesional &bull; **Clases:** 8 &bull; **Ejemplos:** 32
    *   **Temario:** Arquitectura limpia desacoplada, Backend FastAPI REST, persistencia relacional SQL ACID, Frontend Streamlit reactivo, streaming de tokens, testing con mocks, contenerización con Docker Compose y CI/CD.
    *   [📘 Ver Manual Completo del Curso 4](curso-04/book.md) &bull; [🚀 Explorar Clase 01](curso-04/clase-01.md)

---

## ⚡ Inicio Rápido (Quickstart)

```bash
# 1. Clonar el repositorio
git clone https://github.com/wisrovi/wisrovi-python.git
cd wisrovi-python

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate

# 3. Instalar dependencias
pip install -e ".[all]"

# 4. Validar suite completa de pruebas
pytest -v
```
"""

# ==============================================================================
# 2. PÁGINAS DE CLASE EN DOCS: docs/curso-XX/clase-YY.md
# ==============================================================================
def build_class_doc_page(meta: Dict[str, Any], mermaid_code: str) -> str:
    c_num = meta["course_num"]
    f_name = meta["folder_name"]
    c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
    
    nb_name = meta["pdf_filename"].replace(".pdf", ".ipynb")
    colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{c_cfg['course_id']}/{f_name}/notebook/{nb_name}"
    pdf_rel_path = f"https://github.com/wisrovi/wisrovi-python/raw/main/{c_cfg['course_id']}/{f_name}/{meta['pdf_filename']}"
    
    p6_code = clean_html(meta.get("p6_code", ""))
    p7_bad = clean_html(meta.get("p7_bad_code", ""))
    p7_good = clean_html(meta.get("p7_good_code", ""))
    
    return f"""# 📘 {meta['class_title']}

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** {c_cfg['course_name']} ({meta['class_code']})
-   :material-signal-cellular-outline: **Nivel:** `{meta['level']}`
-   :material-lightbulb-on: **Metáfora Central:** *«{meta['metaphor']}»*
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar {meta['pdf_filename']}]({pdf_rel_path})

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/{c_cfg['course_id']}/{f_name})

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

{clean_html(meta.get('p4_theory', ''))}

!!! note "🌟 Modelo Mental de la Sesión: «{meta['metaphor']}»"
    {clean_html(meta.get('p4_metaphor_desc', ''))}

### Principios Fundamentales de la Sesión
{clean_html(meta.get('p4_principles', ''))}

!!! info "⚡ Regla de Oro en Python"
    {clean_html(meta.get('p4_golden_rule', ''))}

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

{mermaid_code}

---

## 3. 💻 Código de Implementación Práctica

```python
{p6_code}
```

---

## 4. 🛡️ Buenas Prácticas, Gotchas y Prevención de Errores

!!! warning "⚠️ Trampa Frecuente (Gotcha)"
    {clean_html(meta.get('p7_gotcha', ''))}

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    {p7_bad}
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    {p7_good}
    ```

!!! tip "🔧 Consejo de Ingeniería"
    {clean_html(meta.get('p7_tip', ''))}

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **{clean_html(meta.get('p9_challenge', ''))}**

Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipo.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_{c_num:02d}/test_{f_name.replace('-', '_')}.py
   ```

---

## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
"""

# ==============================================================================
# 3. MANUALES DE CURSO EN DOCS: docs/curso-XX/book.md
# ==============================================================================
def build_course_book_doc(c_num: int) -> str:
    c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
    course_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
    
    class_rows = ""
    for c in course_classes:
        clean_name = c["class_title"].split(":")[-1].strip()
        class_rows += f"| **{c['class_code']}** | [{clean_name}]({c['folder_name'].replace('clase-', 'clase-')}.md) | *«{c['metaphor']}»* |\n"
        
    return f"""# 📚 Manual Oficial: {c_cfg['course_name']}

<div class="grid cards" markdown>

-   :material-school: **Nivel:** `{c_cfg['level']}`
-   :material-calendar-clock: **Duración:** 8 Semanas Formativas
-   :material-account-tie: **Instructor:** [{AUTHOR_INFO['name']}]({AUTHOR_INFO['website']})
-   :material-file-pdf-box: **PDF Completo:** [Descargar {c_cfg['pdf_name']}](https://github.com/wisrovi/wisrovi-python/raw/main/{c_cfg['course_id']}/{c_cfg['pdf_name']})

</div>

---

## 🗺️ Mapa de Clases Semanales

| Semana | Unidad Temática | Metáfora Didáctica |
| :---: | :--- | :--- |
{class_rows}

---

## 🌀 Progresión Formativa del Curso

```mermaid
flowchart TD
    W1["🌱 Semanas 1-2: Fundamentación & Modelo Mental<br/>Sintaxis, tipos en memoria e intuición"] --> W2["⚙️ Semanas 3-5: Flujo, Colecciones & Estructuras<br/>Control de decisiones, bucles y gestión de datos"]
    W2 --> W3["🧩 Semanas 6-7: Modularización & Abstracción<br/>Funciones, diccionarios y contratos tipados"]
    W3 --> W4["🚀 Semana 8: Síntesis & Proyecto Integrador<br/>Construcción de software funcional con tests"]

    style W1 fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style W2 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style W3 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style W4 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Clases del Curso
Haz clic en cualquiera de las clases del menú lateral o de la tabla superior para estudiar la teoría, ejecutar los ejemplos y resolver los retos prácticos.
"""

def generate_all_docs():
    print("=" * 80)
    print("🚀 COMPILANDO PLATAFORMA WEB DOCUMENTAL EN DOCS/ CON CONTENIDOS ACTUALIZADOS")
    print("=" * 80)
    
    # 1. Generar docs/index.md
    index_path = os.path.join(DOCS_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(build_docs_index())
    print("  ✓ Generado docs/index.md")
    
    # 2. Generar CNAME
    cname_path = os.path.join(DOCS_DIR, "CNAME")
    with open(cname_path, "w", encoding="utf-8") as f:
        f.write("academy_python.wisrovi.dev")
    print("  ✓ Generado docs/CNAME (academy_python.wisrovi.dev)")
    
    # 3. Generar las 32 páginas de clase y 4 manuales de curso
    class_mermaids = refine_all_mermaid_styles.CLASS_MERMAIDS
    
    for c_cfg in COURSES_CONFIG:
        c_num = c_cfg["course_num"]
        c_id = c_cfg["course_id"]
        docs_course_dir = os.path.join(DOCS_DIR, f"curso-{c_num:02d}")
        os.makedirs(docs_course_dir, exist_ok=True)
        
        # Manual del curso (book.md)
        book_doc_path = os.path.join(docs_course_dir, "book.md")
        with open(book_doc_path, "w", encoding="utf-8") as f:
            f.write(build_course_book_doc(c_num))
        print(f"  ✓ Generado docs/curso-{c_num:02d}/book.md")
        
        # 8 clases de cada curso
        c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
        for idx, meta in enumerate(c_classes, start=1):
            diag = class_mermaids.get((c_num, meta["folder_name"]))
            if not diag:
                diag = f"""```mermaid
flowchart LR
    IN["📥 1. Datos de Entrada<br/>({meta['metaphor'][:30]}...)"] --> ENG["⚙️ 2. Motor de Ejecución<br/>{meta['class_title'].split(':')[-1].strip()}"]
    ENG --> OUT["🎯 3. Salida / Estado Actualizado<br/>print() / Retorno DTO"]

    style IN fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ENG fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
            class_page_path = os.path.join(docs_course_dir, f"clase-{idx:02d}.md")
            with open(class_page_path, "w", encoding="utf-8") as f:
                f.write(build_class_doc_page(meta, diag))
            print(f"  ✓ Generado docs/curso-{c_num:02d}/clase-{idx:02d}.md ({meta['class_title'][:35]}...)")
            
    print("\n" + "=" * 80)
    print("✨ PLATAFORMA DOCUMENTAL COMPILADA Y 100% SINCRONIZADA EN DOCS/.")
    print("=" * 80)

if __name__ == "__main__":
    generate_all_docs()
