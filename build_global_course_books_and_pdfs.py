#!/usr/bin/env python3
"""
Generador de libros y PDFs globales para cada uno de los 4 cursos en wisrovi-python.
Unifica todo el material educativo, diagramas, código, perfil de autor y referencias.
"""

import os
import shutil
import tempfile
import subprocess
from typing import Dict, Any, List

from build_all_course_pdfs import CLASSES_METADATA, AUTHOR_INFO, CSS_STYLE, BASE_DIR, generate_svg_diagram
from generate_books import get_mermaid_diagram, clean_html_tags

COURSES_DEF = [
    {
        "id": "01-fundamentos-python",
        "folder": os.path.join(BASE_DIR, "01-fundamentos-python"),
        "title": "Curso 1: Fundamentos Básicos de Python",
        "subtitle": "De Cero a Programador: Los 4 Pilares Lógicos, Colecciones y Proyecto Integrador",
        "level": "Nivel 1 (100% Principiantes Absolutos)",
        "classes_filter": lambda m: "01-fundamentos-python" in m["target_dir"],
        "pdf_name": "curso-01-fundamentos-python.pdf"
    },
    {
        "id": "02-algoritmos-estructuras",
        "folder": os.path.join(BASE_DIR, "02-algoritmos-estructuras"),
        "title": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "subtitle": "Optimización de Memoria, Notación Big-O, Pilas, Colas, Búsqueda Binaria y Programación Dinámica",
        "level": "Nivel 2 (Intermedio)",
        "classes_filter": lambda m: "02-algoritmos-estructuras" in m["target_dir"],
        "pdf_name": "curso-02-algoritmos-estructuras.pdf"
    },
    {
        "id": "03-agentes-ia",
        "folder": os.path.join(BASE_DIR, "03-agentes-ia"),
        "title": "Curso 3: Creación y Desarrollo de Agentes de IA",
        "subtitle": "Modelos LLM, Inferencia, Tool Calling, Memoria Vectorial, RAG y Arquitecturas ReAct",
        "level": "Nivel 3 (Avanzado)",
        "classes_filter": lambda m: "03-agentes-ia" in m["target_dir"],
        "pdf_name": "curso-03-agentes-ia.pdf"
    },
    {
        "id": "04-proyecto-final",
        "folder": os.path.join(BASE_DIR, "04-proyecto-final"),
        "title": "Curso 4: Taller Práctico & Proyecto Final Personalizado",
        "subtitle": "Construcción de Soluciones Reales: Full-Stack Web, Chatbots de Atención y Sistemas de Gestión ACID",
        "level": "Nivel 4 (Integrador / Profesional)",
        "classes_filter": lambda m: "04-proyecto-final" in m["target_dir"],
        "pdf_name": "curso-04-proyecto-final.pdf"
    }
]

def build_global_course_html(course_info: Dict[str, Any], class_list: List[Dict[str, Any]]) -> str:
    """Construye el documento HTML completo del curso con estética LaTeX para imprimir en PDF."""
    
    title = course_info["title"]
    subtitle = course_info["subtitle"]
    level = course_info["level"]
    
    pages_html = []
    
    # 1. PORTADA GLOBAL DEL CURSO
    cover_html = f"""
    <div class="page cover-page">
        <div class="cover-badge">Programa Integral de Formación en Python</div>
        <div class="cover-course">{level}</div>
        <div class="cover-title" style="font-size: 26pt;">{title}</div>
        <div class="cover-subtitle" style="font-size: 13pt; margin-bottom: 25px;">«{subtitle}»</div>
        <div class="cover-divider"></div>
        <p style="max-width: 540px; color: #cbd5e1; font-size: 10pt; font-style: italic; line-height: 1.6;">
            Manual completo del curso compilado oficialmente. Incluye fundamentación teórica, metáforas conceptuales,
            diagramas de arquitectura, código fuente comentado, resolución de gotchas y bibliografía de estudio.
        </p>
        <div class="cover-meta" style="margin-top: 25px;">
            <strong>Instructor Principal:</strong> {AUTHOR_INFO["name"]}<br>
            <strong>Rol:</strong> {AUTHOR_INFO["title"]}<br>
            <strong>Total de Módulos / Clases:</strong> {len(class_list)} &nbsp;|&nbsp; <strong>Python:</strong> 3.10+ &nbsp;|&nbsp; <strong>Licencia:</strong> MIT
        </div>
    </div>
    """
    pages_html.append(cover_html)
    
    # 2. PRESENTACIÓN DEL AUTOR
    author_page = f"""
    <div class="page">
        <div class="header">
            <span>{title}</span>
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

            <h2>Estructura del Manual de Curso</h2>
            <p>
                Este libro unificado contiene el desglose secuencial de cada módulo formativo, estructurado con rigor de ingeniería y diseñado para servir como manual de referencia permanente.
            </p>
        </div>
        <div class="footer">
            <span>{title}</span>
            <span>Manual del Curso &bull; wisrovi</span>
        </div>
    </div>
    """
    pages_html.append(author_page)
    
    # 3. TABLA GENERAL DE CONTENIDOS DEL CURSO
    toc_rows = ""
    for idx, c in enumerate(class_list, 1):
        toc_rows += f"""
        <tr>
            <td><strong>{c['class_code']}</strong></td>
            <td><strong>{c['class_title']}</strong><br><span style="font-size: 7.8pt; color: #64748b;">«{c['metaphor']}»</span></td>
            <td style="font-size: 8pt; color: #334155;">{c['obj_conceptual'][:80]}...</td>
        </tr>
        """
        
    toc_page = f"""
    <div class="page">
        <div class="header">
            <span>{title}</span>
            <span>Índice General de Contenidos</span>
        </div>
        <div class="content-body">
            <h2>Plan de Estudios y Hoja de Ruta</h2>
            <p style="margin-bottom: 6px;">El curso está dividido en las siguientes unidades temáticas secuenciales:</p>
            
            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Código</th>
                        <th style="width: 45%;">Unidad y Metáfora</th>
                        <th style="width: 40%;">Objetivo Principal</th>
                    </tr>
                </thead>
                <tbody>
                    {toc_rows}
                </tbody>
            </table>

            <div class="callout callout-purple" style="margin-top: 10px;">
                <div class="callout-title">🎯 Criterio de Progresión</div>
                <p>
                    Cada unidad construye sobre los cimientos de la anterior. Se recomienda dominar la teoría, analizar el diagrama de arquitectura y replicar el código de cada sección antes de avanzar a la siguiente.
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{title}</span>
            <span>Índice General</span>
        </div>
    </div>
    """
    pages_html.append(toc_page)
    
    # 4. PÁGINAS DE CADA CLASE (Teoría, Diagrama, Código, Gotchas)
    for c in class_list:
        # Página A: Fundamentos y Metáfora
        p_teoria = f"""
        <div class="page">
            <div class="header">
                <span>{title} &bull; {c['class_code']}</span>
                <span>01. Fundamento y Metáfora</span>
            </div>
            <div class="content-body">
                <h2>{c['class_title']}</h2>
                <p>{c['p4_intro']}</p>

                <div class="callout callout-amber">
                    <div class="callout-title">🌟 Metáfora Central: {c['metaphor']}</div>
                    <p>{c['p4_metaphor_desc']}</p>
                </div>

                <h3>Principios Teóricos y Modelo Mental</h3>
                <p>{c['p4_theory_1']}</p>
                <p>{c['p4_theory_2']}</p>

                <div class="callout callout-emerald">
                    <div class="callout-title">⚡ Regla de Oro en Python</div>
                    <p>{c['p4_golden_rule']}</p>
                </div>
            </div>
            <div class="footer">
                <span>{c['class_title']}</span>
                <span>Fundamentos Teóricos</span>
            </div>
        </div>
        """
        pages_html.append(p_teoria)
        
        # Página B: Diagrama y Arquitectura
        p_diag = f"""
        <div class="page">
            <div class="header">
                <span>{title} &bull; {c['class_code']}</span>
                <span>02. Arquitectura de Flujo</span>
            </div>
            <div class="content-body">
                <h2>{c['p5_title']}</h2>
                <p>{c['p5_desc']}</p>

                <div class="diagram-container">
                    {generate_svg_diagram(c.get("diagram_type", "flow"), c["class_title"], c["metaphor"])}
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
                        <tr><td><strong>1. Inicialización</strong></td><td>{c['p5_step1_action']}</td><td>{c['p5_step1_state']}</td></tr>
                        <tr><td><strong>2. Evaluación</strong></td><td>{c['p5_step2_action']}</td><td>{c['p5_step2_state']}</td></tr>
                        <tr><td><strong>3. Transformación</strong></td><td>{c['p5_step3_action']}</td><td>{c['p5_step3_state']}</td></tr>
                        <tr><td><strong>4. Retorno / Salida</strong></td><td>{c['p5_step4_action']}</td><td>{c['p5_step4_state']}</td></tr>
                    </tbody>
                </table>

                <div class="callout">
                    <div class="callout-title">🔍 Visualización Mental</div>
                    <p>{c['p5_mental_tip']}</p>
                </div>
            </div>
            <div class="footer">
                <span>{c['class_title']}</span>
                <span>Arquitectura de Flujo</span>
            </div>
        </div>
        """
        pages_html.append(p_diag)
        
        # Página C: Código y Gotchas
        p_code = f"""
        <div class="page">
            <div class="header">
                <span>{title} &bull; {c['class_code']}</span>
                <span>03. Implementación & Buenas Prácticas</span>
            </div>
            <div class="content-body">
                <h2>{c['p6_title']}</h2>
                <div class="code-wrapper">
                    <div class="code-header">
                        <span>main.py (Python 3.10+)</span>
                        <span>PEP 8 Compliant</span>
                    </div>
                    <div class="code-box">{c['p6_code']}</div>
                </div>

                <div class="callout callout-amber" style="margin-top: 6px;">
                    <div class="callout-title">⚠️ Gotcha Frecuente (Trampa de Principiante)</div>
                    <p>{c['p7_gotcha']}</p>
                </div>

                <div class="two-col" style="margin-top: 6px;">
                    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 6px;">
                        <div style="color: #991b1b; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8pt; margin-bottom: 2px;">❌ Antipatrón</div>
                        <div style="font-family: 'Fira Code', monospace; font-size: 7.2pt; color: #7f1d1d; white-space: pre-wrap;">{c['p7_bad_code']}</div>
                    </div>
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 6px;">
                        <div style="color: #166534; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8pt; margin-bottom: 2px;">✅ Patrón Correcto</div>
                        <div style="font-family: 'Fira Code', monospace; font-size: 7.2pt; color: #14532d; white-space: pre-wrap;">{c['p7_good_code']}</div>
                    </div>
                </div>
            </div>
            <div class="footer">
                <span>{c['class_title']}</span>
                <span>Código y Patrones</span>
            </div>
        </div>
        """
        pages_html.append(p_code)

    # 5. PÁGINA FINAL DE CONCLUSIONES Y BIBLIOGRAFÍA GLOBAL
    final_page = f"""
    <div class="page">
        <div class="header">
            <span>{title}</span>
            <span>Conclusiones y Bibliografía</span>
        </div>
        <div class="content-body">
            <h2>Conclusiones Generales del Curso</h2>
            <p>
                Has completado el recorrido integral de <strong>{title}</strong>. El dominio de estos conceptos te sitúa con una ventaja competitiva sólida para el desarrollo de software profesional e Inteligencia Artificial.
            </p>

            <div class="callout callout-emerald">
                <div class="callout-title">🏆 Hitos Alcanzados</div>
                <p>
                    Comprensión profunda de la arquitectura, asimilación de patrones de diseño idiomáticos en Python, resolución de problemas algorítmicos y capacidad de integración de proyectos reales.
                </p>
            </div>

            <h2>Fuentes Bibliográficas Canónicas</h2>
            <table class="styled-table">
                <thead>
                    <tr>
                        <th style="width: 30%;">Recurso</th>
                        <th style="width: 45%;">Descripción</th>
                        <th style="width: 25%;">Enlace</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><strong>Documentación Oficial Python</strong></td><td>Especificación canónica del lenguaje</td><td>docs.python.org/3/</td></tr>
                    <tr><td><strong>PEP 8 - Style Guide</strong></td><td>Estándar oficial de formateo y estilo</td><td>peps.python.org/pep-0008/</td></tr>
                    <tr><td><strong>Real Python Tutorials</strong></td><td>Patrones profesionales de ingeniería</td><td>realpython.com</td></tr>
                    <tr><td><strong>Suite wisrovi en GitHub</strong></td><td>Librerías open source de alto rendimiento</td><td>github.com/wisrovi</td></tr>
                </tbody>
            </table>

            <div class="callout" style="margin-top: 10px;">
                <div class="callout-title">🤝 Agradecimiento del Instructor</div>
                <p>
                    Gracias por tu disciplina, curiosidad y compromiso en cada lección. Continúa pedaleando y construyendo software con propósito. ¡Nos vemos en el siguiente nivel!
                </p>
            </div>
        </div>
        <div class="footer">
            <span>{title}</span>
            <span>Cierre & Referencias</span>
        </div>
    </div>
    """
    pages_html.append(final_page)
    
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{title} - Libro Completo</title>
<style>
{CSS_STYLE}
</style>
</head>
<body>
{''.join(pages_html)}
</body>
</html>"""
    return full_html

def build_global_course_markdown(course_info: Dict[str, Any], class_list: List[Dict[str, Any]]) -> str:
    """Construye el archivo book.md global para la carpeta raíz del curso."""
    
    title = course_info["title"]
    subtitle = course_info["subtitle"]
    level = course_info["level"]
    
    md_sections = []
    
    # Encabezado
    header = f"""# 📚 {title}

> **Nivel:** {level}  
> **Enfoque:** {subtitle}  
> **Python Version:** 3.10+ | **Licencia:** MIT  
> **Instructor:** **{AUTHOR_INFO["name"]}** ({AUTHOR_INFO["title"]})  

---

## 👤 Perfil del Instructor y Mentor

### **{AUTHOR_INFO["name"]}**
*{AUTHOR_INFO["title"]} &bull; {AUTHOR_INFO["location"]}*

{AUTHOR_INFO["bio"]}

*   🐙 **GitHub:** [{AUTHOR_INFO["github"].replace("https://", "")}]({AUTHOR_INFO["github"]})
*   💼 **LinkedIn:** [{AUTHOR_INFO["linkedin"].replace("https://", "")}]({AUTHOR_INFO["linkedin"]})
*   🐳 **DockerHub:** [{AUTHOR_INFO["dockerhub"].replace("https://", "")}]({AUTHOR_INFO["dockerhub"]})
*   🌐 **Website:** [{AUTHOR_INFO["website"].replace("https://", "")}]({AUTHOR_INFO["website"]})
*   📦 **PyPI:** [{AUTHOR_INFO["pypi"].replace("https://", "")}]({AUTHOR_INFO["pypi"]})

---

### 🚲 Filosofía de Aprendizaje: La Regla de la Bicicleta

> *"Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."*

---

## 📑 Hoja de Ruta y Tabla de Contenidos del Curso

| Módulo / Clase | Título Temático | Metáfora Central | Enlace a Carpeta |
| :---: | :--- | :--- | :---: |
"""
    for c in class_list:
        folder_rel = os.path.basename(c["target_dir"])
        header += f"| **{c['class_code']}** | {c['class_title']} | *{c['metaphor']}* | [`{folder_rel}/`]({folder_rel}/) |\n"
        
    header += "\n---\n"
    md_sections.append(header)
    
    # Cada módulo / clase en detalle
    for idx, c in enumerate(class_list, 1):
        mermaid_block = get_mermaid_diagram(c.get("diagram_type", "flow"), c["class_title"])
        code_raw = clean_html_tags(c["p6_code"])
        bad_code = clean_html_tags(c["p7_bad_code"])
        good_code = clean_html_tags(c["p7_good_code"])
        
        section_md = f"""
# 📖 {c['class_code']}: {c['class_title']}

> **Metáfora:** *«{c['metaphor']}»*  
> **Objetivo:** {c['obj_conceptual']}  

### 1. Fundamentación y Modelo Mental

{c['p4_intro']}

> [!NOTE]
> **Metáfora Didáctica:** {c['p4_metaphor_desc']}

{c['p4_theory_1']}

{c['p4_theory_2']}

> [!IMPORTANT]
> **Regla de Oro:** {c['p4_golden_rule']}

### 2. Arquitectura de Flujo

{mermaid_block}

| Fase | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **Inicialización** | {c['p5_step1_action']} | `{c['p5_step1_state']}` |
| **Evaluación** | {c['p5_step2_action']} | `{c['p5_step2_state']}` |
| **Transformación** | {c['p5_step3_action']} | `{c['p5_step3_state']}` |
| **Salida / Retorno** | {c['p5_step4_action']} | `{c['p5_step4_state']}` |

### 3. Implementación en Python

```python
# {c['class_code']} - main.py
{code_raw}
```

*{c['p6_code_analysis']}*

### 4. Gotchas Comunes y Buenas Prácticas

> [!WARNING]
> **Trampa de Principiante:** {c['p7_gotcha']}

*   **❌ Antipatrón:**
    ```python
    {bad_code}
    ```
*   **✅ Patrón Correcto:**
    ```python
    {good_code}
    ```

> [!TIP]
> **Consejo Profesional:** {c['p7_pro_tip']}

---
"""
        md_sections.append(section_md)
        
    # Cierre y Bibliografía
    footer = f"""
## 🏆 Conclusiones Generales de {title}

Has completado el manual de referencia completo para este nivel. Continúa profundizando y aplicando estos conceptos en proyectos reales.

### 📚 Bibliografía Oficial y Enlaces Recomendados

| Recurso | Enfoque | Enlace |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Referencia canónica del lenguaje | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Estándar de formato y estilo | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Artículos técnicos y buenas prácticas | [realpython.com](https://realpython.com/) |
| **Suite Open Source wisrovi** | Librerías de alto rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |
"""
    md_sections.append(footer)
    
    return "\n".join(md_sections)

def build_course_global(course_info: Dict[str, Any]):
    """Genera el PDF global y el book.md para un curso completo."""
    
    folder = course_info["folder"]
    pdf_name = course_info["pdf_name"]
    final_pdf_path = os.path.join(folder, pdf_name)
    book_path = os.path.join(folder, "book.md")
    
    classes_in_course = [m for m in CLASSES_METADATA if course_info["classes_filter"](m)]
    
    print(f"\n==================================================")
    print(f"📦 [CURSO GLOBAL] {course_info['title']}")
    print(f"   📂 Carpeta destino: {folder}")
    print(f"   📑 Módulos incluidos: {len(classes_in_course)}")
    print(f"==================================================")
    
    # 1. Escribir book.md global
    course_md = build_global_course_markdown(course_info, classes_in_course)
    with open(book_path, "w", encoding="utf-8") as f:
        f.write(course_md)
    print(f"  ✓ Creado book.md global ({os.path.getsize(book_path)} bytes)")
    
    # 2. Compilar PDF global en carpeta temporal
    temp_dir = tempfile.mkdtemp(prefix=f"build_global_{course_info['id']}_")
    try:
        html_content = build_global_course_html(course_info, classes_in_course)
        temp_html_path = os.path.join(temp_dir, "course.html")
        temp_pdf_path = os.path.join(temp_dir, pdf_name)
        
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={temp_pdf_path}",
            temp_html_path
        ]
        
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  ❌ Error compilando PDF: {res.stderr}")
            return False
            
        info_res = subprocess.run(["pdfinfo", temp_pdf_path], capture_output=True, text=True)
        pages_line = [l for l in info_res.stdout.split("\n") if l.startswith("Pages:")]
        pages_count = pages_line[0] if pages_line else "Pages: Desconocido"
        
        shutil.copy2(temp_pdf_path, final_pdf_path)
        print(f"  ✅ PDF Global Creado con éxito: {final_pdf_path} ({pages_count}, {os.path.getsize(final_pdf_path)} bytes)")
        return True
        
    except Exception as e:
        print(f"  ❌ Excepción: {e}")
        return False
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"  🧹 Carpeta temporal eliminada: {temp_dir}")

def main():
    print("=" * 70)
    print("🚀 GENERANDO LIBROS Y PDFs GLOBALES PARA LOS 4 CURSOS")
    print(f"👤 Autor: {AUTHOR_INFO['name']}")
    print("=" * 70)
    
    for c_info in COURSES_DEF:
        build_course_global(c_info)
        
    print("\n" + "=" * 70)
    print("✨ TODOS LOS CURSOS GLOBALES HAN SIDO GENERADOS.")
    print("=" * 70)

if __name__ == "__main__":
    main()
