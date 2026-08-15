#!/usr/bin/env python3
"""
Elevador Maestro de la Documentación: Redefine TODOS los README.md del Repositorio.
Produce textos profesionales, didácticos, modernos, fluidos y con diagramas Mermaid
de alto contraste para la totalidad de las 32 clases, 4 cursos, ejemplos y suites de tests.
"""

import os
import sys
from typing import Dict, Any, List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO

IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".system_generated",
    ".ruff_cache",
    ".idea",
    ".vscode",
    "site"
}

CLASS_META_MAP = {(m["course_num"], m["folder_name"]): m for m in ALL_CLASSES}

# ==============================================================================
# 1. GENERACIÓN DEL README RAÍZ (NIVEL PORTAFOLIO DE CLASE MUNDIAL)
# ==============================================================================
def generate_root_readme() -> str:
    return f"""# 🐍 Programa Integral de Formación en Python: De Cero a Agentes de IA

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisrovi/wisrovi-python)
[![CI / Tests](https://github.com/wisrovi/wisrovi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/wisrovi/wisrovi-python/actions/workflows/ci.yml)
[![Web Documentation](https://img.shields.io/badge/Docs-academy__python.wisrovi.dev-6366f1.svg?logo=materialformkdocs&logoColor=white)](https://academy_python.wisrovi.dev/)
[![Test Suite](https://img.shields.io/badge/Pytest-34%20Passing%20100%25-brightgreen.svg?logo=pytest&logoColor=white)](tests/)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)

**Un ecosistema académico y profesional diseñado para transformar a estudiantes sin experiencia previa en ingenieros capaces de concebir, programar y desplegar aplicaciones reales y Agentes de Inteligencia Artificial.**

[🌐 Explorar Portal Web Interactivo](https://academy_python.wisrovi.dev/) &bull; [🚀 Abrir en Codespaces con 1 Clic](https://codespaces.new/wisrovi/wisrovi-python) &bull; [📚 Ver Cursos](#-la-ruta-maestra-de-formación-4-cursos--32-semanas)

</div>

---

## 👤 Acerca del Autor y Mentor

### **{AUTHOR_INFO['name']}**
*AI Solutions Architect & Principal Software Engineer &bull; Badajoz, España*

Ingeniero y arquitecto de software especializado en **Inteligencia Artificial Generativa**, sistemas multi-agente, Visión por Computador e infraestructuras MLOps de alta disponibilidad. Diseñador del currículo integral y mantenedor del ecosistema de software libre **wisrovi SUITE** en PyPI con más de 26 bibliotecas enfocadas en orquestación de flujos de datos, bases de datos y algoritmos de alto rendimiento.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-wisrovi-181717?logo=github&logoColor=white)](https://github.com/wisrovi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wisrovi%20Rodríguez-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wisrovi-rodriguez/)
[![PyPI](https://img.shields.io/badge/PyPI-26%2B%20Packages-3775A9?logo=pypi&logoColor=white)](https://pypi.org/user/wisrovi/)
[![DockerHub](https://img.shields.io/badge/DockerHub-wisrovi-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/u/wisrovi)
[![Website](https://img.shields.io/badge/Website-wisrovi.dev-000000?logo=google-chrome&logoColor=white)](https://wisrovi.dev)

</div>

---

## 🌀 Modelo Pedagógico: Aprendizaje en Espiral *(Spiral Learning)*

El diseño curricular de este programa no enseña conceptos de forma aislada ni se apoya en la memorización de sintaxis abstracta. En su lugar, implementa el **Aprendizaje en Espiral**, un modelo pedagógico donde el conocimiento se adquiere a través de iteraciones progresivas de complejidad y profundidad técnica:

```mermaid
flowchart TD
    subgraph Espiral["🌀 Ciclo de Aprendizaje en Espiral (32 Semanas)"]
        F1["🎯 Fase 1: Visión Holística & Gancho Temprano (Semana 1)<br/>El alumno experimenta los 4 pilares en conjunto (print, variables, if, for)<br/>Comprende de inmediato para qué sirve el software."]
        F2["🔍 Fase 2: Profundización & Rigor de Ingeniería (Semanas 2 a 24)<br/>Estructuras en memoria, tipos inmutables, Big-O, grafos, LLMs, Tool Calling y RAG.<br/>Análisis de complejidad, gotchas y prevención de errores."]
        F3["🛠️ Fase 3: Síntesis & Creación de Producto (Semanas 25 a 32)<br/>Integración Full-Stack: FastAPI + Streamlit + SQLite ACID + Agente IA.<br/>Testing automatizado, Dockerización y despliegue CI/CD."]
        F1 ==> F2
        F2 ==> F3
    end

    style Espiral fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#ffffff
    style F1 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
    style F2 fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#ffffff
    style F3 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ffffff
```

### 🚲 La Regla de la Bicicleta *(Pedaleo Activo en Código)*
> *"Por más conferencias que escuches o libros que leas sobre cómo guardar el equilibrio, si no te subes a la bicicleta y pedaleas por ti mismo, jamás aprenderás a montar."*

Cada clase está concebida para la acción inmediata:
1. **Modelos Mentales:** Metáforas físicas del mundo real (El Megáfono, Las Cajas, El Semáforo, La Licuadora).
2. **Ejemplos Vivos:** Al menos 4 carpetas con scripts ejecutables y comentados por clase.
3. **Autoevaluación:** Pruebas unitarias automatizadas (`pytest`) que validan la solución del alumno en milisegundos.

---

## 🚀 La Ruta Maestra de Formación (4 Cursos &bull; 32 Semanas)

```mermaid
flowchart LR
    C1["🎯 Curso 1: Fundamentos<br/>(8 Semanas &bull; 0 a 100)"] --> C2["⚡ Curso 2: Algoritmos<br/>(8 Semanas &bull; Big-O & Data)"]
    C2 --> C3["🤖 Curso 3: Agentes IA<br/>(8 Semanas &bull; LLM & RAG)"]
    C3 --> C4["🛠️ Curso 4: Proyecto Final<br/>(8 Semanas &bull; Full-Stack & Deploy)"]

    style C1 fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style C2 fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
    style C3 fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style C4 fill:#9a3412,color:#ffffff,stroke:#fb923c,stroke-width:2px
```

---

## 📚 Mapa Detallado del Programa Académico

| Curso | Enfoque Principal | Manual PDF Oficial | Libro Digital | Cuadernos | Hito de Graduación |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | [**Fundamentos Básicos de Python**](01-fundamentos-python/)<br/>8 Clases &bull; 33 Ejemplos | [📄 PDF Completo](01-fundamentos-python/curso-01-fundamentos-python.pdf) | [📖 book.md](01-fundamentos-python/book.md) | 8 Notebooks (Colab) | Construcción de una aplicación interactiva CLI con validación robusta y control de excepciones. |
| **2** | [**Algoritmos y Estructuras de Datos**](02-algoritmos-estructuras/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](02-algoritmos-estructuras/curso-02-algoritmos-estructuras.pdf) | [📖 book.md](02-algoritmos-estructuras/book.md) | 8 Notebooks (Colab) | Dominio de complejidad Big-O, pilas, colas, BST, grafos y recursión dinámica con `@lru_cache`. |
| **3** | [**Desarrollo de Agentes de IA**](03-agentes-ia/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](03-agentes-ia/curso-03-agentes-ia.pdf) | [📖 book.md](03-agentes-ia/book.md) | 8 Notebooks (Colab) | Creación de pipelines RAG, Tool Calling con Pydantic, embeddings vectoriales y ciclo ReAct. |
| **4** | [**Proyecto Integrador & Taller Full-Stack**](04-proyecto-final/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](04-proyecto-final/curso-04-proyecto-final.pdf) | [📖 book.md](04-proyecto-final/book.md) | 8 Notebooks (Colab) | Aplicación Web en producción (FastAPI + Streamlit + SQLite ACID + Docker Compose + CI/CD). |

---

## ⚡ Inicio Rápido (Quickstart)

### Opción A: Programar en la Nube con 1 Clic (Sin Instalaciones)
Haz clic en el siguiente botón para desplegar tu entorno completo de Visual Studio Code en la nube con Python, extensiones y dependencias preconfiguradas:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisrovi/wisrovi-python)

### Opción B: Configuración en tu Máquina Local
```bash
# 1. Clonar el repositorio
git clone https://github.com/wisrovi/wisrovi-python.git
cd wisrovi-python

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate

# 3. Instalar paquetes y herramientas en modo editable
pip install -e ".[all]"

# 4. Validar el entorno ejecutando la suite completa de pruebas
pytest
```

---

## 🧪 Verificación Automatizada de Calidad (Pytest)

Toda la infraestructura de pruebas está centralizada en la carpeta [`/tests`](tests/) para mantener el código de los alumnos limpio y libre de archivos secundarios:

```bash
# Ejecutar todas las pruebas del repositorio (34 tests en < 0.3s)
pytest

# Ejecutar pruebas por módulo específico
pytest tests/curso_01/
pytest tests/curso_02/
pytest tests/curso_03/
pytest tests/curso_04/

# O utilizar la herramienta CLI oficial
wisrovi test 1
```

---

## 🗺️ Estructura del Repositorio

```text
wisrovi-python/
├── 📁 .devcontainer/                   # 💻 Entorno reproducible para Codespaces y contenedores
├── 📁 .github/                         # ⚙️ Workflows CI/CD, issue templates y automatizaciones
├── 📁 01-fundamentos-python/           # 🎯 Curso 1: Fundamentos (8 Clases con PDF, libro, notebook y ejemplos)
├── 📁 02-algoritmos-estructuras/       # ⚡ Curso 2: Algoritmos & Estructuras (8 Clases)
├── 📁 03-agentes-ia/                   # 🤖 Curso 3: Agentes de Inteligencia Artificial (8 Clases)
├── 📁 04-proyecto-final/               # 🛠️ Curso 4: Proyecto Integrador Full-Stack (8 Clases)
├── 📁 docs/                            # 🌐 Portal web oficial (academy_python.wisrovi.dev)
├── 📁 scripts/                         # 🔧 Herramientas internas de compilación y mantenimiento
├── 📁 src/                             # 📦 Código fuente de la CLI oficial wisrovi
├── 📁 tests/                           # 🧪 Suites de pruebas unitarias centralizadas
├── 📄 mkdocs.yml                       # 📑 Configuración del portal web documental
├── 📄 pyproject.toml                   # 📦 Especificación estándar de dependencias Python
└── 📄 README.md                        # 📌 Portal principal de navegación
```

---

## 📜 Licencia y Comunidad

Este proyecto se publica bajo los términos de la **Licencia MIT**. Puedes usarlo, estudiarlo, compartirlo y adaptarlo con total libertad tanto para fines académicos como comerciales.

Si este programa de formación aporta valor a tu carrera profesional, **te invitamos a dejar una ⭐️ en GitHub** para apoyar el desarrollo de software libre en español.
"""

# ==============================================================================
# 2. GENERACIÓN DE READMES DE CLASE (PROFESIONAL, CLARO Y RIGUROSO)
# ==============================================================================
def generate_class_readme(meta: Dict[str, Any], mermaid_code: str) -> str:
    c_num = meta["course_num"]
    c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
    nb_name = meta["pdf_filename"].replace(".pdf", ".ipynb")
    colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{c_cfg['course_id']}/{meta['folder_name']}/notebook/{nb_name}"
    
    return f"""# 📘 {meta['class_title']}

<div align="center">

**{c_cfg['course_name']}** &bull; **Semana {meta['class_code'].replace('C1-', '').replace('C2-', '').replace('C3-', '').replace('C4-', '')}**  
*Nivel:* `{meta['level']}` &bull; *Metáfora Central:* **«{meta['metaphor']}»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)]({meta['pdf_filename']})
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«{meta['metaphor']}»* ({meta['p4_metaphor_desc']}).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

{mermaid_code}

---

## 📂 Organización de Materiales en esta Clase

```text
{meta['folder_name']}/
├── 📄 {meta['pdf_filename']}       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 {nb_name}
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** {meta['p9_challenge']}

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_{c_num:02d}/test_{meta['folder_name'].replace('-', '_')}.py
```
"""

# ==============================================================================
# 3. GENERACIÓN DE READMES DE CARPETA 'EJEMPLOS'
# ==============================================================================
def generate_ejemplos_folder_readme(c_num: int, f_name: str, meta: Dict[str, Any], subdirs: List[str]) -> str:
    rows = ""
    for sd in sorted(subdirs):
        clean = sd.replace("ejemplo_", "").replace("_", " ").title()
        rows += f"| [`{sd}/`]({sd}/) | {clean} | [`main.py`]({sd}/main.py) |\n"
        
    return f"""# 💻 Catálogo de Ejemplos Prácticos: {meta.get('class_title', f_name)}

> **Ubicación:** `{meta.get('course_id', 'curso')}/{f_name}/ejemplos`  
> **Filosofía:** *Aprender programando mediante casos de uso aislados, legibles y comentados.*

---

## 🗺️ Flujo de Estudio Recomendado

```mermaid
flowchart LR
    A["📂 1. Selecciona un Ejemplo<br/>(Del caso más simple al más avanzado)"] --> B["📖 2. Revisa su README.md<br/>Comprende el objetivo y el diagrama"]
    B --> C["🐍 3. Ejecuta main.py<br/>Observa el comportamiento en terminal"]
    C --> D["🔧 4. Modifica y Experimenta<br/>Cambia variables y analiza los efectos"]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Ejemplos Disponibles en esta Clase

| Directorio | Caso de Uso Demostrado | Script Principal |
| :--- | :--- | :---: |
{rows}

---

## 🚀 Cómo Ejecutar Cualquier Ejemplo
Abre tu terminal en la raíz del repositorio y ejecuta:
```bash
python {meta.get('course_id', '01-fundamentos-python')}/{f_name}/ejemplos/<nombre_del_ejemplo>/main.py
```
"""

# ==============================================================================
# 4. GENERACIÓN DE READMEs DE EJEMPLOS INDIVIDUALES
# ==============================================================================
def generate_single_example_readme(c_num: int, f_name: str, ex_folder: str, meta: Dict[str, Any], mermaid_code: str, summary_desc: str) -> str:
    clean_title = ex_folder.replace("ejemplo_", "").replace("_", " ").title()
    course_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
    
    return f"""# 📖 {clean_title}

<div align="center">

**Clase:** {meta.get('class_title', f_name)}  
*Script de Ejecución:* [`main.py`](main.py)

</div>

---

## 🎯 Propósito del Ejemplo
{summary_desc}

---

## 🗺️ Diagrama de Flujo del Script

{mermaid_code}

---

## 🔍 Aspectos Clave a Observar en el Código

1. **Claridad Sintáctica:** Estructura modular, tipado explícito y apego a la guía de estilo oficial PEP 8.
2. **Transformación de Datos:** Cómo se declaran las entradas, se procesan en memoria y se devuelven al usuario.
3. **Robustez:** Prevención de comportamientos inesperados mediante nombres expresivos y control lógico.

---

## 💻 Ejecución desde la Terminal

Desde la raíz del proyecto, ejecuta:

```bash
python {course_cfg['course_id']}/{f_name}/ejemplos/{ex_folder}/main.py
```
"""

# ==============================================================================
# 5. GENERACIÓN DE READMEs DE 'EJERCICIOS'
# ==============================================================================
def generate_ejercicios_readme(c_num: int, f_name: str, meta: Dict[str, Any]) -> str:
    test_file = f"test_{f_name.replace('-', '_')}.py"
    course_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
    
    return f"""# 🏋️ Reto Práctico: {meta.get('class_title', f_name)}

<div align="center">

**{course_cfg['course_name']}** &bull; **Semana {meta.get('class_code', '01')}**  
*Archivo de Trabajo:* [`reto.py`](reto.py) &bull; *Suite de Validación:* [`tests/curso_{c_num:02d}/{test_file}`](../../tests/curso_{c_num:02d}/{test_file})

</div>

---

## 🎯 Enunciado del Desafío

> **{meta.get('p9_challenge', 'Completa la implementación en el archivo reto.py')}**

---

## 🗺️ Ciclo de Resolución y Feedback Automatizado

```mermaid
flowchart LR
    A["📖 1. Leer reto.py<br/>Comprende los requisitos y tipos"] --> B["💻 2. Implementar Solución<br/>Escribe tu lógica en VS Code"]
    B --> C["🧪 3. Ejecutar Pytest<br/>pytest tests/curso_{c_num:02d}/"]
    C -->|Fallo ❌| D["🔍 4. Depuración<br/>Analiza el mensaje de error"]
    D --> B
    C -->|Pasa 100% ✅| E["🏆 5. ¡Hito Superado!<br/>Avanza a la siguiente clase"]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 🚀 Pasos para Resolver el Reto

1. Abre [`reto.py`](reto.py) en tu editor.
2. Lee las firmas de función, docstrings y restricciones.
3. Escribe tu solución reemplazando los comentarios `TODO`.
4. Valida tu solución en cualquier momento ejecutando en la terminal:
   ```bash
   pytest tests/curso_{c_num:02d}/
   ```
"""

# ==============================================================================
# EJECUCIÓN PRINCIPAL
# ==============================================================================
def upgrade_all_readmes():
    print("=" * 80)
    print("🚀 ELEVANDO LA CALIDAD, PROFUNDIDAD Y ESTILO DE TODOS LOS READMEs")
    print("=" * 80)
    
    # 1. Escribir README Raíz
    root_readme_path = os.path.join(BASE_DIR, "README.md")
    with open(root_readme_path, "w", encoding="utf-8") as f:
        f.write(generate_root_readme())
    print("  ✨ [RAÍZ] Actualizado README.md principal con diseño world-class.")
    
    # 2. Cargar refinador de Mermaids para reutilizar diagramas
    import refine_all_mermaid_styles
    class_mermaids = refine_all_mermaid_styles.CLASS_MERMAIDS
    c1_ex_mermaids = refine_all_mermaid_styles.C1_EXAMPLES_MERMAID
    
    # 3. Recorrer directorios de clases
    for meta in ALL_CLASSES:
        c_num = meta["course_num"]
        f_name = meta["folder_name"]
        c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
        c_dir = os.path.join(BASE_DIR, c_cfg["course_id"], f_name)
        
        if not os.path.exists(c_dir):
            continue
            
        # A. README de la Clase
        class_readme_path = os.path.join(c_dir, "README.md")
        diag = class_mermaids.get((c_num, f_name))
        if not diag:
            diag = f"""```mermaid
flowchart LR
    IN["📥 1. Datos de Entrada<br/>({meta['metaphor'][:30]}...)"] --> ENG["⚙️ 2. Motor de Procesamiento<br/>{meta['class_title'].split(':')[-1].strip()}"]
    ENG --> OUT["🎯 3. Salida Verificada<br/>Estado en Memoria / Retorno"]

    style IN fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ENG fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
        with open(class_readme_path, "w", encoding="utf-8") as f:
            f.write(generate_class_readme(meta, diag))
            
        # B. README de carpeta 'ejemplos'
        ejemplos_dir = os.path.join(c_dir, "ejemplos")
        if os.path.exists(ejemplos_dir):
            subdirs = [d for d in os.listdir(ejemplos_dir) if os.path.isdir(os.path.join(ejemplos_dir, d))]
            ej_readme_path = os.path.join(ejemplos_dir, "README.md")
            with open(ej_readme_path, "w", encoding="utf-8") as f:
                f.write(generate_ejemplos_folder_readme(c_num, f_name, meta, subdirs))
                
            # C. READMEs individuales de cada ejemplo
            for sd in subdirs:
                single_ex_dir = os.path.join(ejemplos_dir, sd)
                single_readme_path = os.path.join(single_ex_dir, "README.md")
                main_py_path = os.path.join(single_ex_dir, "main.py")
                
                summary = "Demostración estructurada del concepto técnico correspondiente a este módulo."
                if os.path.exists(main_py_path):
                    with open(main_py_path, "r", encoding="utf-8") as f_py:
                        code = f_py.read()
                        if '"""' in code:
                            summary = code.split('"""')[1].strip()
                            
                ex_diag = c1_ex_mermaids.get(sd)
                if not ex_diag:
                    clean_sd = sd.replace("ejemplo_", "").replace("_", " ").title()
                    ex_diag = f"""```mermaid
flowchart LR
    A["📥 Entrada de Parámetros<br/>({clean_sd})"] --> B["⚙️ Transformación Lógica<br/>Ejecución en Python"]
    B --> C["🎯 Salida por Consola<br/>print() / Retorno Seguro"]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
                with open(single_readme_path, "w", encoding="utf-8") as f:
                    f.write(generate_single_example_readme(c_num, f_name, sd, meta, ex_diag, summary))
                    
        # D. README de carpeta 'ejercicios'
        ejercicios_dir = os.path.join(c_dir, "ejercicios")
        if os.path.exists(ejercicios_dir):
            ejer_readme_path = os.path.join(ejercicios_dir, "README.md")
            with open(ejer_readme_path, "w", encoding="utf-8") as f:
                f.write(generate_ejercicios_readme(c_num, f_name, meta))

    print("\n" + "=" * 80)
    print("✨ ACTUALIZACIÓN MAESTRA COMPLETADA: Todos los READMEs han sido elevados de nivel.")
    print("=" * 80)

if __name__ == "__main__":
    upgrade_all_readmes()
