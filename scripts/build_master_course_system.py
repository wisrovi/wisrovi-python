#!/usr/bin/env python3
"""
Compilador Maestro del Sistema Educativo wisrovi-python.
Genera y compila:
1. Las 32 carpetas de clase con código, ejemplos, ejercicios y tests de pytest.
2. Los 32 archivos book.md individuales con diagramas Mermaid nativos.
3. Los 32 PDFs individuales de 9 páginas con estética LaTeX profesional.
4. Los 4 libros globales book.md y los 4 PDFs globales de cada curso completo.
5. Los 32 cuadernos interactivos Jupyter (.ipynb) con badges de Google Colab.
6. La plataforma web interactiva completa en docs/ con MkDocs Material y mkdocs.yml actualizado.
"""

import os
import sys
import shutil
import tempfile
import subprocess
import json
from typing import Dict, Any, List

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO, BASE_DIR
from build_all_course_pdfs import CSS_STYLE, generate_svg_diagram
from generate_books import clean_html_tags

DOCS_DIR = os.path.join(BASE_DIR, "docs")
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")

def get_mermaid_for_class(diagram_type: str, class_title: str) -> str:
    """Genera diagrama Mermaid nativo y limpio para book.md y MkDocs."""
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
    else: # architecture
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

def build_individual_book_markdown(meta: Dict[str, Any], course_cfg: Dict[str, Any]) -> str:
    """Construye el contenido de book.md para una clase individual."""
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    course_name = course_cfg["course_name"]
    level = meta["level"]
    metaphor = meta["metaphor"]
    pdf_filename = meta["pdf_filename"]
    mermaid_block = get_mermaid_for_class(meta.get("diagram_type", "flow"), class_title)
    code_raw = clean_html_tags(meta["p6_code"])
    bad_code = clean_html_tags(meta["p7_bad_code"])
    good_code = clean_html_tags(meta["p7_good_code"])
    
    return f"""# 📚 {class_title}

> **Programa:** {course_name}  
> **Nivel:** {level}  
> **Metáfora Central:** *«{metaphor}»*  
> **Documento Oficial PDF:** [{pdf_filename}]({pdf_filename})  
> **Instructor:** **{AUTHOR_INFO["name"]}** ({AUTHOR_INFO["title"]})  

---

## 👤 Perfil del Autor y Mentor

### **{AUTHOR_INFO["name"]}**
*{AUTHOR_INFO["title"]} &bull; {AUTHOR_INFO["location"]}*

{AUTHOR_INFO["bio"]}

*   🐙 **GitHub:** [{AUTHOR_INFO["github"].replace("https://", "")}]({AUTHOR_INFO["github"]})
*   💼 **LinkedIn:** [{AUTHOR_INFO["linkedin"].replace("https://", "")}]({AUTHOR_INFO["linkedin"]})
*   🐳 **DockerHub:** [{AUTHOR_INFO["dockerhub"].replace("https://", "")}]({AUTHOR_INFO["dockerhub"]})
*   🌐 **Website:** [{AUTHOR_INFO["website"].replace("https://", "")}]({AUTHOR_INFO["website"]})
*   📦 **PyPI:** [{AUTHOR_INFO["pypi"].replace("https://", "")}]({AUTHOR_INFO["pypi"]})

---

### 🚲 La Regla de la Bicicleta

> *"Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."*

---

## 📑 Tabla de Contenidos de la Sesión

1. [💡 Fundamentación Teórica y Modelo Mental](#1--fundamentación-teórica-y-modelo-mental)
2. [🗺️ Arquitectura y Diagrama de Flujo](#2-️-arquitectura-y-diagrama-de-flujo)
3. [💻 Implementación en Python 3.10+](#3--implementación-en-python-310)
4. [🛡️ Buenas Prácticas y Trampas Frecuentes](#4-️-buenas-prácticas-y-trampas-frecuentes)
5. [🏋️ Desafío de Práctica](#5-️-desafío-de-práctica)
6. [📚 Bibliografía y Enlaces Canónicos](#6--bibliografía-y-enlaces-canónicos)

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

{meta["p4_intro"]}

> [!NOTE]
> **🌟 Metáfora Didáctica:** {meta["p4_metaphor_desc"]}

### Principios Fundamentales

{meta["p4_theory_1"]}

{meta["p4_theory_2"]}

> [!IMPORTANT]
> **⚡ Regla de Oro en Python:** {meta["p4_golden_rule"]}

---

## 2. 🗺️ Arquitectura y Diagrama de Flujo

{meta["p5_desc"]}

{mermaid_block}

### Desglose Paso a Paso del Flujo

| Fase | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **1. Inicialización** | {meta["p5_step1_action"]} | `{meta["p5_step1_state"]}` |
| **2. Evaluación** | {meta["p5_step2_action"]} | `{meta["p5_step2_state"]}` |
| **3. Transformación** | {meta["p5_step3_action"]} | `{meta["p5_step3_state"]}` |
| **4. Retorno / Salida** | {meta["p5_step4_action"]} | `{meta["p5_step4_state"]}` |

> [!TIP]
> **🔍 Visualización Mental:** {meta["p5_mental_tip"]}

---

## 3. 💻 Implementación en Python 3.10+

```python
# {class_code} - Código de Demostración
{code_raw}
```

*{meta["p6_code_analysis"]}*

---

## 4. 🛡️ Buenas Prácticas y Trampas Frecuentes

> [!WARNING]
> **⚠️ Gotcha Frecuente (Trampa de Principiante):** {meta["p7_gotcha"]}

*   **❌ Antipatrón:**
    ```python
{bad_code}
    ```

*   **✅ Patrón Correcto:**
    ```python
{good_code}
    ```

> [!TIP]
> **💡 Consejo Profesional:** {meta["p7_pro_tip"]}

---

## 5. 🏋️ Desafío de Práctica

> **Desafío:** {meta["p9_challenge"]}

Para ejecutar la verificación automática con pytest:
```bash
pytest ejercicios/
```

---

## 6. 📚 Bibliografía y Enlaces Canónicos

| Fuente / Recurso | Descripción | Enlace |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Especificación y biblioteca estándar | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Estándar oficial de formateo y estilo | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Patrones de ingeniería y desarrollo | [realpython.com](https://realpython.com/) |
| **Suite Open Source wisrovi** | Librerías de alto rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |
"""

def build_individual_pdf_html(meta: Dict[str, Any], course_cfg: Dict[str, Any]) -> str:
    """Construye el documento HTML de 9 páginas con estética LaTeX profesional para el PDF individual."""
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    course_name = course_cfg["course_name"]
    level = meta["level"]
    metaphor = meta["metaphor"]
    
    pages = []
    
    # 1. Portada
    p1 = f"""
    <div class="page cover-page">
        <div class="cover-badge">{course_name}</div>
        <div class="cover-course">{class_code} &bull; {level}</div>
        <div class="cover-title">{class_title}</div>
        <div class="cover-subtitle">«{metaphor}»</div>
        <div class="cover-divider"></div>
        <p style="max-width: 520px; color: #cbd5e1; font-size: 9.5pt; font-style: italic; line-height: 1.6;">
            Guía de estudio oficial y manual técnico. Diseñado para dominar la programación en Python
            mediante modelos mentales rigurosos, diagramas de flujo y código de producción.
        </p>
        <div class="cover-meta">
            <strong>Autor & Mentor:</strong> {AUTHOR_INFO["name"]}<br>
            <strong>Rol:</strong> {AUTHOR_INFO["title"]}<br>
            <strong>Python:</strong> 3.10+ &nbsp;|&nbsp; <strong>Licencia:</strong> MIT &nbsp;|&nbsp; <strong>wisrovi SUITE</strong>
        </div>
    </div>
    """
    pages.append(p1)
    
    # 2. Perfil Autor
    p2 = f"""
    <div class="page">
        <div class="header">
            <span>{course_name}</span>
            <span>Perfil del Instructor</span>
        </div>
        <div class="content-body">
            <h2>Acerca del Autor y Mentor</h2>
            <div class="author-card">
                <div class="author-header">
                    <div class="author-avatar">WR</div>
                    <div class="author-info">
                        <h3>{AUTHOR_INFO["name"]}</h3>
                        <p>{AUTHOR_INFO["title"]} &bull; {AUTHOR_INFO["location"]}</p>
                    </div>
                </div>
                <p style="font-size: 8.8pt; line-height: 1.5; color: #334155;">
                    {AUTHOR_INFO["bio"]}
                </p>
                <div class="link-grid">
                    <div class="link-item">🐙 <strong>GitHub:</strong> github.com/wisrovi</div>
                    <div class="link-item">💼 <strong>LinkedIn:</strong> in/wisrovi-rodriguez</div>
                    <div class="link-item">🐳 <strong>DockerHub:</strong> hub.docker.com/u/wisrovi</div>
                    <div class="link-item">🌐 <strong>Website:</strong> wisrovi.dev</div>
                </div>
            </div>

            <h2>Metodología de Aprendizaje: La Regla de la Bicicleta 🚲</h2>
            <p>
                En este programa no creemos en el aprendizaje pasivo. Programar no se aprende memorizando manuales o mirando videos en segundo plano mientras tomas café; se aprende <strong>escribiendo código</strong>, enfrentando errores de sintaxis, depurando variables y viendo cómo responde el intérprete en tiempo real.
            </p>

            <div class="callout callout-emerald">
                <div class="callout-title">💡 El Compromiso Activo del Estudiante</div>
                <p>
                    Abre Visual Studio Code en cada sesión. Escribe cada ejemplo con tus propias manos. Cambia los números, rompe el código deliberadamente para ver el mensaje de error de Python, y luego arréglalo. Ese proceso de experimentación es el que construye sinapsis duraderas.
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Perfil del Autor &bull; wisrovi</span>
        </div>
    </div>
    """
    pages.append(p2)
    
    # 3. Presentación & TOC
    p3 = f"""
    <div class="page">
        <div class="header">
            <span>{course_name}</span>
            <span>Presentación & Hoja de Ruta</span>
        </div>
        <div class="content-body">
            <h2>Presentación de la Sesión</h2>
            <p>
                Bienvenido/a a la <strong>{class_code}</strong> del <strong>{course_name}</strong>. Esta guía técnica está estructurada para proporcionarte las bases conceptuales, arquitectónicas y prácticas indispensables para tu progreso.
            </p>

            <div class="callout callout-purple">
                <div class="callout-title">🎯 Objetivos de la Sesión</div>
                <p><strong>Competencia Conceptual:</strong> {meta["obj_conceptual"]}</p>
                <p><strong>Competencia Práctica:</strong> {meta["obj_practical"]}</p>
            </div>

            <h2>Estructura del Documento</h2>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Sección</th>
                        <th style="width: 45%;">Contenido Temático</th>
                        <th style="width: 30%;">Objetivo Pedagógico</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>Pág 4: Fundamento</strong></td><td>Teoría, Modelo Mental y Metáfora</td><td>Comprensión del concepto</td></tr>
                    <tr><td><strong>Pág 5: Flujo</strong></td><td>Diagrama de Arquitectura de Memoria</td><td>Visualización del flujo interno</td></tr>
                    <tr><td><strong>Pág 6: Código</strong></td><td>Implementación en Python 3.10+</td><td>Patrones idiomáticos (PEP 8)</td></tr>
                    <tr><td><strong>Pág 7: Gotchas</strong></td><td>Antipatrones y Trampas Comunes</td><td>Prevención de bugs en producción</td></tr>
                    <tr><td><strong>Pág 8: Conclusiones</strong></td><td>Cierre de Sesión & Notas de Repaso</td><td>Consolidación del aprendizaje</td></tr>
                    <tr><td><strong>Pág 9: Bibliografía</strong></td><td>Fuentes Canónicas y Desafío</td><td>Ampliación y autoestudio</td></tr>
                </tbody>
            </table>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Hoja de Ruta & Objetivos</span>
        </div>
    </div>
    """
    pages.append(p3)
    
    # 4. Fundamento Teórico
    p4 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>01. Fundamento y Metáfora</span>
        </div>
        <div class="content-body">
            <h2>{class_title}</h2>
            <p>{meta["p4_intro"]}</p>

            <div class="callout callout-amber">
                <div class="callout-title">🌟 Metáfora Central: {metaphor}</div>
                <p>{meta["p4_metaphor_desc"]}</p>
            </div>

            <h3>Principios Teóricos y Modelo Mental</h3>
            <p>{meta["p4_theory_1"]}</p>
            <p>{meta["p4_theory_2"]}</p>

            <div class="callout callout-emerald">
                <div class="callout-title">⚡ Regla de Oro en Python</div>
                <p>{meta["p4_golden_rule"]}</p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Fundamentos Teóricos</span>
        </div>
    </div>
    """
    pages.append(p4)
    
    # 5. Diagrama de Flujo
    p5 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>02. Arquitectura de Flujo</span>
        </div>
        <div class="content-body">
            <h2>Arquitectura y Movimiento de Datos en Memoria</h2>
            <p>{meta["p5_desc"]}</p>

            <div class="diagram-container">
                {generate_svg_diagram(meta.get("diagram_type", "flow"), class_title, metaphor)}
            </div>

            <h3>Desglose Paso a Paso del Diagrama</h3>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Fase del Flujo</th>
                        <th style="width: 45%;">Acción del Intérprete</th>
                        <th style="width: 30%;">Estado en Memoria</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>1. Inicialización</strong></td><td>{meta["p5_step1_action"]}</td><td>{meta["p5_step1_state"]}</td></tr>
                    <tr><td><strong>2. Evaluación</strong></td><td>{meta["p5_step2_action"]}</td><td>{meta["p5_step2_state"]}</td></tr>
                    <tr><td><strong>3. Transformación</strong></td><td>{meta["p5_step3_action"]}</td><td>{meta["p5_step3_state"]}</td></tr>
                    <tr><td><strong>4. Retorno / Salida</strong></td><td>{meta["p5_step4_action"]}</td><td>{meta["p5_step4_state"]}</td></tr>
                </tbody>
            </table>

            <div class="callout">
                <div class="callout-title">🔍 Visualización Mental</div>
                <p>{meta["p5_mental_tip"]}</p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Arquitectura de Flujo</span>
        </div>
    </div>
    """
    pages.append(p5)
    
    # 6. Código de Demostración
    p6 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>03. Implementación Práctica</span>
        </div>
        <div class="content-body">
            <h2>Código de Demostración en Python 3.10+</h2>
            <p>{meta["p6_desc"]}</p>

            <div class="code-wrapper">
                <div class="code-header">
                    <span>main.py (Python 3.10+)</span>
                    <span>PEP 8 Compliant</span>
                </div>
                <div class="code-box">{meta["p6_code"]}</div>
            </div>

            <h3>Análisis de Ingeniería del Código</h3>
            <p style="font-size: 8.8pt; line-height: 1.5; color: #334155;">
                {meta["p6_code_analysis"]}
            </p>

            <div class="callout callout-purple" style="margin-top: 8px;">
                <div class="callout-title">💡 Buena Práctica de Tipado</div>
                <p>
                    El uso sistemático de Type Hints (PEP 484) permite a los editores modernos como VS Code activar autocompletado inteligente y detectar errores antes de la ejecución.
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Código de Demostración</span>
        </div>
    </div>
    """
    pages.append(p6)
    
    # 7. Gotchas y Antipatrones
    p7 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>04. Buenas Prácticas & Gotchas</span>
        </div>
        <div class="content-body">
            <h2>Trampas Frecuentes de Depuración (Gotchas)</h2>
            <p>{meta["p7_intro"]}</p>

            <div class="callout callout-amber">
                <div class="callout-title">⚠️ Gotcha Frecuente (Trampa de Principiante)</div>
                <p>{meta["p7_gotcha"]}</p>
            </div>

            <h3>Comparativa: Antipatrón vs Patrón Recomendado</h3>
            <div class="two-col">
                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 8px;">
                    <div style="color: #991b1b; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; margin-bottom: 4px;">❌ Antipatrón</div>
                    <div style="font-family: 'Fira Code', monospace; font-size: 7.5pt; color: #7f1d1d; white-space: pre-wrap;">{meta["p7_bad_code"]}</div>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 8px;">
                    <div style="color: #166534; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; margin-bottom: 4px;">✅ Patrón Correcto</div>
                    <div style="font-family: 'Fira Code', monospace; font-size: 7.5pt; color: #14532d; white-space: pre-wrap;">{meta["p7_good_code"]}</div>
                </div>
            </div>

            <div class="callout callout-emerald" style="margin-top: 10px;">
                <div class="callout-title">🛡️ Consejo de Resiliencia en Producción</div>
                <p>{meta["p7_pro_tip"]}</p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Buenas Prácticas & Depuración</span>
        </div>
    </div>
    """
    pages.append(p7)
    
    # 8. Conclusiones y Agradecimiento
    p8 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>05. Cierre & Notas de Repaso</span>
        </div>
        <div class="content-body">
            <h2>Conclusiones Clave de la Sesión</h2>
            <p>
                Hemos cubierto los pilares teóricos y prácticos de <strong>{class_title}</strong>. El dominio de esta unidad te proporciona una base sólida para afrontar la siguiente semana formativa.
            </p>

            <div class="callout callout-emerald">
                <div class="callout-title">🏆 Hitos Alcanzados</div>
                <p>
                    Comprensión profunda del modelo mental, capacidad de depuración de gotchas comunes y solidez en la sintaxis idiomática de Python 3.10+.
                </p>
            </div>

            <h2>Notas de Repaso Rápido</h2>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 30%;">Concepto</th>
                        <th style="width: 70%;">Punto Clave a Recordar</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>1. Modelo Mental</strong></td><td>{metaphor}</td></tr>
                    <tr><td><strong>2. Regla de Oro</strong></td><td>{meta["p4_golden_rule"]}</td></tr>
                    <tr><td><strong>3. Gotcha Crítico</strong></td><td>{meta["p7_gotcha"]}</td></tr>
                    <tr><td><strong>4. Buenas Prácticas</strong></td><td>{meta["p7_pro_tip"]}</td></tr>
                </tbody>
            </table>

            <div class="callout" style="margin-top: 10px;">
                <div class="callout-title">🤝 Mensaje del Instructor</div>
                <p>
                    ¡Felicitaciones por completar esta lección! Recuerda que la constancia y el pedaleo diario en tu editor de código son los que te convertirán en un programador excepcional.
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Cierre & Notas</span>
        </div>
    </div>
    """
    pages.append(p8)
    
    # 9. Bibliografía y Desafío
    p9 = f"""
    <div class="page">
        <div class="header">
            <span>{class_code} &bull; {course_name}</span>
            <span>06. Bibliografía & Desafío</span>
        </div>
        <div class="content-body">
            <h2>Fuentes Bibliográficas Oficiales</h2>
            <p>
                Para profundizar en los estándares formales del lenguaje y sus implementaciones internas, consulta la documentación canónica:
            </p>

            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 30%;">Recurso Oficial</th>
                        <th style="width: 45%;">Descripción</th>
                        <th style="width: 25%;">Enlace</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>Documentación Python 3</strong></td><td>Especificación canónica y biblioteca estándar</td><td>docs.python.org/3/</td></tr>
                    <tr><td><strong>PEP 8 — Style Guide</strong></td><td>Estándar oficial de formateo y estilo</td><td>peps.python.org/pep-0008/</td></tr>
                    <tr><td><strong>Real Python Tutorials</strong></td><td>Patrones de desarrollo e ingeniería</td><td>realpython.com</td></tr>
                    <tr><td><strong>Suite wisrovi en GitHub</strong></td><td>Paquetes open source de alto rendimiento</td><td>github.com/wisrovi</td></tr>
                </tbody>
            </table>

            <h2>🏋️ Desafío Práctico para el Estudiante</h2>
            <div class="callout callout-purple">
                <div class="callout-title">🎯 Reto de la Semana</div>
                <p>{meta["p9_challenge"]}</p>
            </div>

            <div class="callout callout-emerald" style="margin-top: 8px;">
                <div class="callout-title">🧪 Validación Automatizada</div>
                <p>
                    Ejecuta <code>pytest ejercicios/</code> en tu terminal de VS Code para verificar automáticamente la validez de tu solución.
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{class_title}</span>
            <span>Bibliografía & Desafío</span>
        </div>
    </div>
    """
    pages.append(p9)
    
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{class_title}</title>
<style>
{CSS_STYLE}
</style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""
    return full_html

def compile_pdf_from_html(html_content: str, output_pdf_path: str) -> bool:
    """Compila HTML a PDF usando Chrome Headless en una carpeta temporal."""
    temp_dir = tempfile.mkdtemp(prefix="build_pdf_")
    try:
        temp_html = os.path.join(temp_dir, "doc.html")
        temp_pdf = os.path.join(temp_dir, "output.pdf")
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={temp_pdf}",
            temp_html
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(temp_pdf):
            shutil.copy2(temp_pdf, output_pdf_path)
            return True
        return False
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def generate_jupyter_notebook(meta: Dict[str, Any], course_cfg: Dict[str, Any]) -> str:
    """Genera un archivo .ipynb con soporte de Google Colab."""
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    metaphor = meta["metaphor"]
    course_name = course_cfg["course_name"]
    code_raw = clean_html_tags(meta["p6_code"])
    nb_filename = meta["pdf_filename"].replace(".pdf", ".ipynb")
    colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/notebooks/{nb_filename})"
    
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# 🐍 {class_title}\n",
                f"### **{course_name}**\n\n",
                f"{colab_badge}\n\n",
                f"> **Metáfora Central:** *«{metaphor}»*  \n",
                f"> **Instructor:** **{AUTHOR_INFO['name']}** ({AUTHOR_INFO['title']})  \n",
                f"> **Licencia:** MIT | **Python:** 3.10+\n\n",
                "---\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## 1. 💡 Fundamentación Teórica\n\n",
                f"{meta['p4_intro']}\n\n",
                f"> **Metáfora Didáctica:** {meta['p4_metaphor_desc']}\n\n",
                f"{meta['p4_theory_1']}\n\n",
                f"{meta['p4_theory_2']}\n\n",
                f"**⚡ Regla de Oro:** {meta['p4_golden_rule']}\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## 2. 💻 Implementación de Código Ejecutable\n\n",
                f"{meta['p6_desc']}\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                f"# {class_code} - Demostración\n",
                code_raw
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## 3. 🛡️ Buenas Prácticas y Trampas Frecuentes\n\n",
                f"⚠️ **Gotcha:** {meta['p7_gotcha']}\n\n",
                f"💡 **Consejo Profesional:** {meta['p7_pro_tip']}\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"## 4. 🏋️ Desafío de Práctica\n\n",
                f"> **Reto:** {meta['p9_challenge']}\n\n",
                f"Escribe y ejecuta tu solución en la celda siguiente:\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Tu solución aquí:\n",
                "\n"
            ]
        }
    ]
    
    nb = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python", "version": "3.11.0"},
            "orig_nbformat": 4
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    nb_path = os.path.join(NOTEBOOKS_DIR, nb_filename)
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    return nb_filename

def build_global_course_assets(course_cfg: Dict[str, Any], class_list: List[Dict[str, Any]]):
    """Construye el book.md global y el PDF completo para un curso de 8 clases."""
    course_dir = os.path.join(BASE_DIR, course_cfg["course_id"])
    pdf_name = course_cfg["pdf_name"]
    final_pdf_path = os.path.join(course_dir, pdf_name)
    book_path = os.path.join(course_dir, "book.md")
    
    # 1. Global book.md
    md_lines = [
        f"# 📚 {course_cfg['course_name']}\n\n",
        f"> **{course_cfg['subtitle']}**  \n",
        f"> **Nivel:** {course_cfg['level']}  \n",
        f"> **Duración:** 8 Semanas (1 Clase por semana)  \n",
        f"> **Instructor:** **{AUTHOR_INFO['name']}** ({AUTHOR_INFO['title']})  \n",
        f"> **Licencia:** MIT | **Python:** 3.10+  \n\n",
        "---\n\n",
        "## 📑 Hoja de Ruta y Tabla de Contenidos (8 Semanas)\n\n",
        "| Semana / Clase | Título | Metáfora Central | Carpeta |\n",
        "| :---: | :--- | :--- | :---: |\n"
    ]
    for c in class_list:
        md_lines.append(f"| **{c['class_code']}** | {c['class_title']} | *«{c['metaphor']}»* | [`{c['folder_name']}/`]({c['folder_name']}/) |\n")
    md_lines.append("\n---\n\n")
    
    for c in class_list:
        mermaid_block = get_mermaid_for_class(c.get("diagram_type", "flow"), c["class_title"])
        code_raw = clean_html_tags(c["p6_code"])
        bad_code = clean_html_tags(c["p7_bad_code"])
        good_code = clean_html_tags(c["p7_good_code"])
        
        md_lines.append(f"""
# 📖 {c['class_code']}: {c['class_title']}

> **Metáfora:** *«{c['metaphor']}»*  
> **Objetivo:** {c['obj_conceptual']}  

### 1. Fundamentos Teóricos
{c['p4_intro']}

> [!NOTE]
> **Metáfora Didáctica:** {c['p4_metaphor_desc']}

{c['p4_theory_1']}

> [!IMPORTANT]
> **Regla de Oro:** {c['p4_golden_rule']}

### 2. Diagrama de Arquitectura
{mermaid_block}

### 3. Implementación en Python
```python
# {c['class_code']}
{code_raw}
```

### 4. Gotchas y Buenas Prácticas
> [!WARNING]
> **Gotcha:** {c['p7_gotcha']}

*   **❌ Antipatrón:**
    ```python
{bad_code}
    ```
*   **✅ Patrón Correcto:**
    ```python
{good_code}
    ```

---
""")
    
    with open(book_path, "w", encoding="utf-8") as f:
        f.writelines(md_lines)
    print(f"  ✓ Creado book.md global en {course_cfg['course_id']}/book.md")
    
    # 2. Global PDF HTML
    pages_html = []
    
    # Portada Global
    p_cov = f"""
    <div class="page cover-page">
        <div class="cover-badge">Programa Integral de Formación en Python (8 Semanas)</div>
        <div class="cover-course">{course_cfg['level']}</div>
        <div class="cover-title" style="font-size: 24pt;">{course_cfg['course_name']}</div>
        <div class="cover-subtitle" style="font-size: 12pt; margin-bottom: 25px;">«{course_cfg['subtitle']}»</div>
        <div class="cover-divider"></div>
        <p style="max-width: 540px; color: #cbd5e1; font-size: 9.5pt; font-style: italic; line-height: 1.6;">
            Manual completo del curso compilado oficialmente. Incluye el desglose de las 8 clases semanales,
            diagramas de arquitectura, código fuente comentado, resolución de gotchas y bibliografía de estudio.
        </p>
        <div class="cover-meta" style="margin-top: 25px;">
            <strong>Instructor:</strong> {AUTHOR_INFO["name"]}<br>
            <strong>Total Clases:</strong> 8 Semanas &nbsp;|&nbsp; <strong>Python:</strong> 3.10+ &nbsp;|&nbsp; <strong>Licencia:</strong> MIT
        </div>
    </div>
    """
    pages_html.append(p_cov)
    
    # Presentación & Autor
    p_auth = f"""
    <div class="page">
        <div class="header"><span>{course_cfg['course_name']}</span><span>Perfil del Instructor</span></div>
        <div class="content-body">
            <h2>Acerca del Autor y Mentor</h2>
            <div class="author-card">
                <div class="author-header">
                    <div class="author-avatar">WR</div>
                    <div class="author-info">
                        <h3>{AUTHOR_INFO["name"]}</h3>
                        <p>{AUTHOR_INFO["title"]} &bull; {AUTHOR_INFO["location"]}</p>
                    </div>
                </div>
                <p style="font-size: 8.8pt; line-height: 1.5; color: #334155;">{AUTHOR_INFO["bio"]}</p>
                <div class="link-grid">
                    <div class="link-item">🐙 <strong>GitHub:</strong> github.com/wisrovi</div>
                    <div class="link-item">💼 <strong>LinkedIn:</strong> in/wisrovi-rodriguez</div>
                    <div class="link-item">🐳 <strong>DockerHub:</strong> hub.docker.com/u/wisrovi</div>
                    <div class="link-item">🌐 <strong>Website:</strong> wisrovi.dev</div>
                </div>
            </div>
            <h2>Metodología: La Regla de la Bicicleta 🚲</h2>
            <p>Aprender a programar es pedalear en VS Code: la experimentación práctica diaria es la clave del dominio técnico.</p>
        </div>
        <div class="footer"><span>{course_cfg['course_name']}</span><span>Manual Completo</span></div>
    </div>
    """
    pages_html.append(p_auth)
    
    # TOC
    toc_rows = ""
    for c in class_list:
        toc_rows += f"<tr><td><strong>{c['class_code']}</strong></td><td><strong>{c['class_title']}</strong></td><td>«{c['metaphor'][:50]}...»</td></tr>"
    p_toc = f"""
    <div class="page">
        <div class="header"><span>{course_cfg['course_name']}</span><span>Índice General (8 Semanas)</span></div>
        <div class="content-body">
            <h2>Plan de Estudios de las 8 Semanas</h2>
            <table class="styled-table">
                <thead><tr><th style="width:18%;">Semana</th><th style="width:45%;">Unidad Temática</th><th style="width:37%;">Metáfora</th></tr></thead>
                <tbody>{toc_rows}</tbody>
            </table>
        </div>
        <div class="footer"><span>{course_cfg['course_name']}</span><span>Índice General</span></div>
    </div>
    """
    pages_html.append(p_toc)
    
    # Cada clase en 3 páginas dentro del libro global
    for c in class_list:
        # Pág 1: Teoría
        p_t = f"""
        <div class="page">
            <div class="header"><span>{course_cfg['course_name']} &bull; {c['class_code']}</span><span>Teoría & Metáfora</span></div>
            <div class="content-body">
                <h2>{c['class_title']}</h2>
                <p>{c['p4_intro']}</p>
                <div class="callout callout-amber"><div class="callout-title">🌟 Metáfora: {c['metaphor']}</div><p>{c['p4_metaphor_desc']}</p></div>
                <h3>Principios Teóricos</h3>
                <p>{c['p4_theory_1']}</p>
                <p>{c['p4_theory_2']}</p>
                <div class="callout callout-emerald"><div class="callout-title">⚡ Regla de Oro</div><p>{c['p4_golden_rule']}</p></div>
            </div>
            <div class="footer"><span>{c['class_title']}</span><span>Fundamentos</span></div>
        </div>
        """
        pages_html.append(p_t)
        
        # Pág 2: Diagrama
        p_d = f"""
        <div class="page">
            <div class="header"><span>{course_cfg['course_name']} &bull; {c['class_code']}</span><span>Arquitectura de Flujo</span></div>
            <div class="content-body">
                <h2>Arquitectura y Movimiento de Datos</h2>
                <p>{c['p5_desc']}</p>
                <div class="diagram-container">{generate_svg_diagram(c.get('diagram_type', 'flow'), c['class_title'], c['metaphor'])}</div>
                <table class="styled-table">
                    <thead><tr><th>Fase</th><th>Acción del Intérprete</th><th>Estado Memoria</th></tr></thead>
                    <tbody>
                        <tr><td><strong>1. Inicio</strong></td><td>{c['p5_step1_action']}</td><td>{c['p5_step1_state']}</td></tr>
                        <tr><td><strong>2. Proceso</strong></td><td>{c['p5_step2_action']}</td><td>{c['p5_step2_state']}</td></tr>
                        <tr><td><strong>3. Salida</strong></td><td>{c['p5_step4_action']}</td><td>{c['p5_step4_state']}</td></tr>
                    </tbody>
                </table>
            </div>
            <div class="footer"><span>{c['class_title']}</span><span>Diagrama de Flujo</span></div>
        </div>
        """
        pages_html.append(p_d)
        
        # Pág 3: Código y Gotchas
        p_c = f"""
        <div class="page">
            <div class="header"><span>{course_cfg['course_name']} &bull; {c['class_code']}</span><span>Código & Gotchas</span></div>
            <div class="content-body">
                <h2>Implementación en Python 3.10+</h2>
                <div class="code-wrapper">
                    <div class="code-header"><span>main.py (PEP 8)</span><span>Código Ejecutable</span></div>
                    <div class="code-box">{c['p6_code']}</div>
                </div>
                <div class="callout callout-amber" style="margin-top:6px;"><div class="callout-title">⚠️ Gotcha Frecuente</div><p>{c['p7_gotcha']}</p></div>
                <div class="two-col" style="margin-top:6px;">
                    <div style="background:#fef2f2;border:1px solid #fecaca;padding:6px;border-radius:6px;">
                        <div style="color:#991b1b;font-weight:bold;font-size:7.5pt;">❌ Antipatrón</div>
                        <div style="font-family:'Fira Code',monospace;font-size:6.8pt;color:#7f1d1d;">{c['p7_bad_code']}</div>
                    </div>
                    <div style="background:#f0fdf4;border:1px solid #bbf7d0;padding:6px;border-radius:6px;">
                        <div style="color:#166534;font-weight:bold;font-size:7.5pt;">✅ Patrón Correcto</div>
                        <div style="font-family:'Fira Code',monospace;font-size:6.8pt;color:#14532d;">{c['p7_good_code']}</div>
                    </div>
                </div>
            </div>
            <div class="footer"><span>{c['class_title']}</span><span>Código y Patrones</span></div>
        </div>
        """
        pages_html.append(p_c)
        
    # Cierre Global
    p_end = f"""
    <div class="page">
        <div class="header"><span>{course_cfg['course_name']}</span><span>Cierre & Bibliografía</span></div>
        <div class="content-body">
            <h2>Conclusiones Generales del Curso</h2>
            <p>Has completado las 8 semanas de <strong>{course_cfg['course_name']}</strong>.</p>
            <div class="callout callout-emerald"><div class="callout-title">🏆 Certificación del Nivel</div><p>Dominio conceptual y práctico consolidado.</p></div>
            <h2>Bibliografía Canónica</h2>
            <table class="styled-table">
                <thead><tr><th>Recurso</th><th>Descripción</th><th>Enlace</th></tr></thead>
                <tbody>
                    <tr><td><strong>Documentación Oficial Python</strong></td><td>Especificación canónica</td><td>docs.python.org/3/</td></tr>
                    <tr><td><strong>PEP 8</strong></td><td>Guía de estilo</td><td>peps.python.org/pep-0008/</td></tr>
                    <tr><td><strong>wisrovi SUITE</strong></td><td>Librerías open source</td><td>github.com/wisrovi</td></tr>
                </tbody>
            </table>
        </div>
        <div class="footer"><span>{course_cfg['course_name']}</span><span>Cierre del Curso</span></div>
    </div>
    """
    pages_html.append(p_end)
    
    global_html = f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><title>{course_cfg['course_name']}</title><style>{CSS_STYLE}</style></head><body>{''.join(pages_html)}</body></html>"
    compile_pdf_from_html(global_html, final_pdf_path)
    print(f"  ✅ PDF Global Creado: {final_pdf_path} ({os.path.getsize(final_pdf_path)} bytes)")

def clean_old_redundant_dirs():
    """Limpia carpetas antiguas de 3 módulos para que cada curso tenga únicamente clase-01 a clase-08."""
    print("\n🧹 Limpiando directorios antiguos no estandarizados...")
    for c_id in ["02-algoritmos-estructuras", "03-agentes-ia"]:
        c_path = os.path.join(BASE_DIR, c_id)
        for entry in os.listdir(c_path):
            full_p = os.path.join(c_path, entry)
            if os.path.isdir(full_p) and not entry.startswith("clase-"):
                shutil.rmtree(full_p)
                print(f"  - Eliminado directorio obsoleto: {full_p}")

def main():
    print("=" * 80)
    print("🚀 EJECUTANDO GENERADOR MAESTRO DE 32 CLASES (8 CLASES x 4 CURSOS)")
    print(f"👤 Autor: {AUTHOR_INFO['name']}")
    print("=" * 80)
    
    clean_old_redundant_dirs()
    os.makedirs(NOTEBOOKS_DIR, exist_ok=True)
    
    # 1. Procesar cada clase individual
    print("\n📦 [FASE 1] Creando carpetas, archivos, tests y PDFs para las 32 clases...")
    
    course_map = {c["course_num"]: c for c in COURSES_CONFIG}
    notebook_list = []
    
    for meta in ALL_CLASSES:
        course_cfg = course_map[meta["course_num"]]
        class_dir = os.path.join(BASE_DIR, course_cfg["course_id"], meta["folder_name"])
        ejemplos_dir = os.path.join(class_dir, "ejemplos")
        ejercicios_dir = os.path.join(class_dir, "ejercicios")
        
        os.makedirs(ejemplos_dir, exist_ok=True)
        os.makedirs(ejercicios_dir, exist_ok=True)
        
        # README.md
        with open(os.path.join(class_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# 📘 {meta['class_title']}\n\n"
                    f"> **Curso:** {course_cfg['course_name']}  \n"
                    f"> **Nivel:** {meta['level']}  \n"
                    f"> **Metáfora:** *«{meta['metaphor']}»*  \n\n"
                    f"## 📑 Contenidos de esta carpeta\n"
                    f"*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual oficial en PDF (9 páginas).\n"
                    f"*   📖 [`book.md`](book.md): Libro de estudio digital con diagramas Mermaid.\n"
                    f"*   💻 `ejemplos/`: Scripts de código funcional y demostraciones.\n"
                    f"*   🏋️ `ejercicios/`: Retos prácticos con tests unitarios automatizados (`pytest`).\n")
            
        # book.md
        book_md_content = build_individual_book_markdown(meta, course_cfg)
        with open(os.path.join(class_dir, "book.md"), "w", encoding="utf-8") as f:
            f.write(book_md_content)
            
        # ejemplos/main.py
        with open(os.path.join(ejemplos, "main.py") if 'ejemplos' in locals() and os.path.exists(ejemplos) else os.path.join(ejemplos_dir, "main.py"), "w", encoding="utf-8") as f:
            f.write(f'"""{meta["class_title"]} - Código de Demostración."""\n' + clean_html_tags(meta["p6_code"]) + '\n')
            
        # ejercicios/reto.py
        with open(os.path.join(ejercicios_dir, "reto.py"), "w", encoding="utf-8") as f:
            f.write(f'"""Reto de {meta["class_title"]}."""\n# {meta["p9_challenge"]}\n')
            
        # ejercicios/test_c<N>_<folder>.py
        test_filename = f"test_c{meta['course_num']}_{meta['folder_name'].replace('-', '_')}.py"
        with open(os.path.join(ejercicios_dir, test_filename), "w", encoding="utf-8") as f:
            f.write(meta["test_logic"])
            
        # PDF Individual (9 páginas)
        pdf_path = os.path.join(class_dir, meta["pdf_filename"])
        html_content = build_individual_pdf_html(meta, course_cfg)
        compile_pdf_from_html(html_content, pdf_path)
        print(f"  ✓ [C{meta['course_num']}] {meta['class_code']} Generada: {meta['folder_name']} (PDF: {os.path.getsize(pdf_path)} bytes)")
        
        # Notebook Jupyter (.ipynb)
        nb_name = generate_jupyter_notebook(meta, course_cfg)
        notebook_list.append((meta["class_title"], nb_name))

    # 2. Generar notebooks/README.md
    with open(os.path.join(NOTEBOOKS_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("# 📓 Cuadernos Interactivos de Jupyter (Google Colab)\n\n"
                "Ejecuta cada una de las 32 clases celda a celda en la nube con un solo clic:\n\n"
                "| Curso / Clase | Cuaderno Jupyter | Enlace Directo a Colab |\n"
                "| :--- | :---: | :---: |\n")
        for title, nb_name in notebook_list:
            badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/notebooks/{nb_name})"
            f.write(f"| **{title}** | [`{nb_name}`]({nb_name}) | {badge} |\n")
    print(f"\n✓ Creados los 32 cuadernos Jupyter en notebooks/")

    # 3. Libros y PDFs Globales para los 4 cursos
    print("\n📦 [FASE 2] Compilando Libros y PDFs Globales para los 4 cursos...")
    for c_cfg in COURSES_CONFIG:
        c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_cfg["course_num"]]
        build_global_course_assets(c_cfg, c_classes)

    # 4. Regenerar Portal Web en docs/ y actualizar mkdocs.yml
    print("\n📦 [FASE 3] Sincronizando la plataforma web interactiva en docs/...")
    
    # docs/index.md
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(f"""# 🐍 Programa Integral de Formación en Python
### *De Cero a Agentes de Inteligencia Artificial (32 Semanas)*

<div class="grid cards" markdown>

-   :material-school: __Nivel:__ Principiante a Avanzado (4 Cursos &bull; 32 Clases)
-   :material-account-tie: __Instructor:__ [William Rodríguez (Wisrovi)](https://wisrovi.dev)
-   :material-code-tags: __Tecnologías:__ Python 3.10+, FastAPI, Streamlit, Pydantic, RAG, ReAct Agents
-   :material-license: __Licencia:__ Código Abierto (MIT)

</div>

Bienvenido/a a la plataforma web interactiva del **Programa de Formación en Python**. Esta academia online está estructurada en **4 cursos de 8 semanas cada uno (32 clases en total)** con contenido exhaustivo, código interactivo, cuadernos de Google Colab y pruebas automatizadas.

---

## 🚀 Hoja de Ruta del Programa (32 Semanas)

```mermaid
flowchart TD
    C1["🎯 Curso 1: Fundamentos Básicos de Python<br/>(Semanas 1 a 8 - Principiantes)"] --> C2["🚀 Curso 2: Algoritmos y Estructuras de Datos<br/>(Semanas 9 a 16 - Intermedio)"]
    C2 --> C3["🤖 Curso 3: Creación y Desarrollo de Agentes de IA<br/>(Semanas 17 a 24 - Avanzado)"]
    C3 --> C4["🛠️ Curso 4: Taller Práctico & Proyecto Final<br/>(Semanas 25 a 32 - Integrador)"]

    style C1 fill:#2b5c8f,color:#fff,stroke:#fff,stroke-width:2px
    style C2 fill:#3b7a57,color:#fff,stroke:#fff,stroke-width:2px
    style C3 fill:#6b4c9a,color:#fff,stroke:#fff,stroke-width:2px
    style C4 fill:#c05621,color:#fff,stroke:#fff,stroke-width:2px
```

---

## 📚 Explorador de los 4 Cursos

=== "🎯 Curso 1: Fundamentos (8 Semanas)"
    *   **Público:** Principiantes Absolutos.
    *   **Temas:** Variables, Condicionales, Bucles, Listas, Diccionarios, Funciones y Proyecto CLI.
    *   [👉 Ver Curso 1 Completo](curso-01/book.md)

=== "🚀 Curso 2: Algoritmos y Estructuras (8 Semanas)"
    *   **Público:** Nivel Intermedio y preparación para entrevistas de ingeniería.
    *   **Temas:** Big-O, Pilas/Colas con `deque`, Sets O(1), Búsqueda Binaria, QuickSort, Árboles BST, Grafos BFS/DFS y Memoización.
    *   [👉 Ver Curso 2 Completo](curso-02/book.md)

=== "🤖 Curso 3: Agentes de Inteligencia Artificial (8 Semanas)"
    *   **Público:** Nivel Avanzado en IA aplicada.
    *   **Temas:** LLMs, Prompt Engineering, Pydantic V2, Tool Calling, Embeddings, RAG, Ciclo ReAct y Multi-Agentes.
    *   [👉 Ver Curso 3 Completo](curso-03/book.md)

=== "🛠️ Curso 4: Proyecto Final Integrador (8 Semanas)"
    *   **Público:** Nivel Profesional y Portafolio.
    *   **Temas:** Arquitectura Limpia, Backend FastAPI, Base de Datos SQL ACID, Frontend Streamlit, Integración de IA, Pytest, Docker Compose y CI/CD.
    *   [👉 Ver Curso 4 Completo](curso-04/book.md)
""")

    # Generar docs/curso-01 a docs/curso-04
    for c_cfg in COURSES_CONFIG:
        c_num = c_cfg["course_num"]
        c_docs_dir = os.path.join(DOCS_DIR, f"curso-{c_num:02d}")
        os.makedirs(c_docs_dir, exist_ok=True)
        
        c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
        
        # docs/curso-XX/book.md
        shutil.copy2(os.path.join(BASE_DIR, c_cfg["course_id"], "book.md"), os.path.join(c_docs_dir, "book.md"))
        
        # docs/curso-XX/clase-01.md a clase-08.md
        for i, meta in enumerate(c_classes, 1):
            class_src_book = os.path.join(BASE_DIR, c_cfg["course_id"], meta["folder_name"], "book.md")
            shutil.copy2(class_src_book, os.path.join(c_docs_dir, f"clase-{i:02d}.md"))
            
    # Actualizar mkdocs.yml con la navegación completa de 32 clases
    mkdocs_yaml = f"""site_name: "🐍 Programa Integral de Formación en Python"
site_description: "De Cero a Agentes de Inteligencia Artificial - 32 Semanas por Wisrovi Rodríguez"
site_author: "William Rodríguez (Wisrovi)"
site_url: "https://academy_python.wisrovi.dev/"
repo_url: "https://github.com/wisrovi/wisrovi-python"
repo_name: "wisrovi/wisrovi-python"

theme:
  name: material
  language: es
  palette:
    - scheme: default
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-7
        name: Modo Oscuro
    - scheme: slate
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-4
        name: Modo Claro
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - navigation.instant
    - search.suggest
    - search.highlight
    - content.code.copy

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - tables
  - attr_list
  - md_in_html

nav:
  - 🏠 Inicio: index.md
  - 🎯 Curso 1 (Fundamentos):
      - 📘 Manual del Curso 1: curso-01/book.md
      - Clase 01 (Panorama General): curso-01/clase-01.md
      - Clase 02 (Variables y Tipos): curso-01/clase-02.md
      - Clase 03 (Condicionales): curso-01/clase-03.md
      - Clase 04 (Bucles): curso-01/clase-04.md
      - Clase 05 (Listas y Colecciones): curso-01/clase-05.md
      - Clase 06 (Diccionarios y Sets): curso-01/clase-06.md
      - Clase 07 (Funciones y Scope): curso-01/clase-07.md
      - Clase 08 (Proyecto Integrador CLI): curso-01/clase-08.md
  - 🚀 Curso 2 (Algoritmos):
      - 📘 Manual del Curso 2: curso-02/book.md
      - Clase 01 (Notación Big-O): curso-02/clase-01.md
      - Clase 02 (Pilas y Colas con deque): curso-02/clase-02.md
      - Clase 03 (Tablas Hash y Sets O(1)): curso-02/clase-03.md
      - Clase 04 (Búsqueda Binaria): curso-02/clase-04.md
      - Clase 05 (QuickSort y MergeSort): curso-02/clase-05.md
      - Clase 06 (Árboles BST): curso-02/clase-06.md
      - Clase 07 (Grafos y Recorridos BFS/DFS): curso-02/clase-07.md
      - Clase 08 (Recursividad y Memoización DP): curso-02/clase-08.md
  - 🤖 Curso 3 (Agentes de IA):
      - 📘 Manual del Curso 3: curso-03/book.md
      - Clase 01 (Fundamentos LLM & Tokens): curso-03/clase-01.md
      - Clase 02 (Prompt Engineering & Few-Shot): curso-03/clase-02.md
      - Clase 03 (Structured Outputs & Pydantic): curso-03/clase-03.md
      - Clase 04 (Tool Calling en Python): curso-03/clase-04.md
      - Clase 05 (Embeddings & Similitud Coseno): curso-03/clase-05.md
      - Clase 06 (Arquitecturas RAG): curso-03/clase-06.md
      - Clase 07 (Agentes Autónomos ReAct): curso-03/clase-07.md
      - Clase 08 (Sistemas Multi-Agente & Guardrails): curso-03/clase-08.md
  - 🛠️ Curso 4 (Proyecto Final):
      - 📘 Manual del Curso 4: curso-04/book.md
      - Clase 01 (Arquitectura & Planificación): curso-04/clase-01.md
      - Clase 02 (Backend API FastAPI): curso-04/clase-02.md
      - Clase 03 (Persistencia SQL & ACID): curso-04/clase-03.md
      - Clase 04 (Frontend Streamlit): curso-04/clase-04.md
      - Clase 05 (Integración del Motor de IA): curso-04/clase-05.md
      - Clase 06 (Testing Pytest & Mocks): curso-04/clase-06.md
      - Clase 07 (Docker & Docker Compose): curso-04/clase-07.md
      - Clase 08 (Despliegue CI/CD & Portafolio): curso-04/clase-08.md
  - 📚 Guías de Onboarding:
      - 💻 Guía VS Code: guia-vscode.md
      - 🐙 Guía GitHub: guia-github.md
      - 📜 Reglas de Comunidad: reglas-comunidad.md
      - ❓ Preguntas Frecuentes: faq.md
"""
    with open(os.path.join(BASE_DIR, "mkdocs.yml"), "w", encoding="utf-8") as f:
        f.write(mkdocs_yaml)
    print("  ✓ Actualizado mkdocs.yml con las 32 clases distribuidas en 4 cursos.")

    print("\n" + "=" * 80)
    print("✨ GENERACIÓN MAESTRA DE 32 CLASES COMPLETADA EXITOSAMENTE.")
    print("=" * 80)

if __name__ == "__main__":
    main()
