#!/usr/bin/env python3
"""
Mejorador Maestro de TODOS los README.md del Repositorio wisrovi-python.
Recorre recursivamente cada archivo README.md, asegurando:
1. Al menos un diagrama Mermaid nativo y 100% compatible con GitHub en CADA README.
2. Formato profesional, claro, intuitivo y moderno.
3. Integración transversal de la pedagogía de 'Aprendizaje en Espiral' y 'La Regla de la Bicicleta'.
4. Instrucciones precisas de ejecución paso a paso.
"""

import os
import glob
from typing import Dict, Any, List

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO, BASE_DIR

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

# Mapeo rápido de metadatos por (curso_num, folder_name)
CLASS_META_MAP = {(m["course_num"], m["folder_name"]): m for m in ALL_CLASSES}

def get_class_mermaid(meta: Dict[str, Any]) -> str:
    title = meta["class_title"].split(":")[-1].strip()
    metaphor = meta["metaphor"]
    d_type = meta.get("diagram_type", "flow")
    
    if d_type == "flow":
        return f"""```mermaid
flowchart LR
    A["🎬 Entrada / Contexto<br/>({metaphor})"] --> B{{"⚖️ Evaluación Lógica<br/>¿Condición / Regla?"}}
    B -->|Rama Verdadera| C["⚙️ Transformación en Memoria<br/>{title}"]
    B -->|Rama Alternativa| D["🔀 Flujo Secundario<br/>Manejo de Caso"]
    C --> E["🎯 Salida / Retorno<br/>print() / Estado Actualizado"]
    D --> E

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style D fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style E fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
```"""
    elif d_type == "loop":
        return f"""```mermaid
flowchart LR
    A["📦 Colección / Rango<br/>({metaphor})"] --> B["🔄 Iterador Activo<br/>for / while loop"]
    B --> C["⚡ Procesamiento de Elemento<br/>{title}"]
    C -->|Siguiente Paso| B
    C -->|Condición de Salida| D["🏁 Estado Final Consolidado"]

    style A fill:#1e293b,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style B fill:#0369a1,color:#ffffff,stroke:#7dd3fc,stroke-width:2px
    style C fill:#047857,color:#ffffff,stroke:#6ee7b7,stroke-width:2px
    style D fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```"""
    else:
        return f"""```mermaid
flowchart LR
    subgraph Entrada["📥 Capa de Entrada"]
        REQ["Petición / Prompt / Input"]
        VAL["Validación DTO & Tipos"]
    end

    subgraph Core["🧠 Núcleo del Sistema"]
        ENG["Motor de Ejecución ({title})"]
        MEM["Estado / Memoria en Heap"]
    end

    subgraph Salida["💾 Persistencia & Respuesta"]
        DB[("Base de Datos / Vector Store")]
        RES["Respuesta Estructurada JSON / UI"]
    end

    REQ --> VAL
    VAL --> ENG
    ENG <--> MEM
    ENG <--> DB
    ENG --> RES

    style Entrada fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style Core fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style Salida fill:#f0fdf4,stroke:#10b981,stroke-width:2px
```"""

def process_readme(file_path: str):
    rel = os.path.relpath(file_path, BASE_DIR)
    parts = rel.split(os.sep)
    dir_name = os.path.dirname(rel)
    
    # --------------------------------------------------------------------------
    # 1. README Raíz del Proyecto
    # --------------------------------------------------------------------------
    if rel == "README.md":
        # Ya tiene un Mermaid excelente, asegurarse de que esté perfecto
        return
        
    # --------------------------------------------------------------------------
    # 2. READMEs de Nivel Curso (ej. 01-fundamentos-python/README.md)
    # --------------------------------------------------------------------------
    if len(parts) == 2 and parts[0].startswith(("01-", "02-", "03-", "04-")):
        c_id = parts[0]
        c_num = int(c_id[:2])
        c_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
        c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
        
        rows = ""
        for c in c_classes:
            rows += f"| **{c['class_code']}** | [`{c['folder_name']}/`]({c['folder_name']}/) | {c['class_title'].split(':')[-1].strip()} | *«{c['metaphor']}»* |\n"
            
        content = f"""# 📚 {c_cfg['course_name']}

> **{c_cfg['subtitle']}**  
> **Nivel:** {c_cfg['level']} &bull; **Duración:** 8 Semanas Formativas  
> **Instructor:** **{AUTHOR_INFO['name']}** ({AUTHOR_INFO['title']})  

---

## 🌀 Progresión de Aprendizaje en Espiral (8 Semanas)

Este curso aplica la metodología de **Aprendizaje en Espiral**, donde cada semana construye sobre la anterior, incrementando la profundidad técnica y el rigor de ingeniería:

```mermaid
flowchart TD
    W1["🌱 Semana 1-2: Fundamentación & Modelo Mental<br/>Comprensión intuitiva y sintaxis idiomática"] --> W2["⚙️ Semana 3-5: Estructuras & Control de Flujo<br/>Decisiones, bucles y gestión de memoria"]
    W2 --> W3["🧩 Semana 6-7: Modularización & Arquitectura<br/>Funciones, colecciones y abstracción"]
    W3 --> W4["🚀 Semana 8: Síntesis & Proyecto Integrador<br/>Aplicación completa y verificación con tests"]

    style W1 fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style W2 fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style W3 fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style W4 fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 📑 Hoja de Ruta de las 8 Clases Semanales

| Semana | Carpeta | Unidad Temática | Metáfora Didáctica |
| :---: | :--- | :--- | :--- |
{rows}

---

## 📦 Materiales Disponibles en este Curso

*   📄 [`{c_cfg['pdf_name']}`]({c_cfg['pdf_name']}): Manual completo oficial en PDF compilado con estética LaTeX.
*   📖 [`book.md`](book.md): Libro de estudio digital con explicaciones profundas y diagramas Mermaid.
*   🧪 Suite de Pruebas Automatizadas en [`tests/curso_{c_num:02d}/`](../tests/curso_{c_num:02d}/).

---

## 🚲 La Regla de la Bicicleta

> *"Nadie aprende a programar leyendo código ajeno. Abre cada clase, ejecuta los ejemplos en tu editor y resuelve los retos con tus propias manos."*
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 3. READMEs de Nivel Clase (ej. 01-fundamentos-python/clase-01-.../README.md)
    # --------------------------------------------------------------------------
    if len(parts) == 3 and parts[1].startswith("clase-"):
        c_num = int(parts[0][:2])
        folder_name = parts[1]
        meta = CLASS_META_MAP.get((c_num, folder_name))
        if meta:
            course_cfg = next(c for c in COURSES_CONFIG if c["course_num"] == c_num)
            mermaid_block = get_class_mermaid(meta)
            colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{parts[0]}/{folder_name}/notebook/{meta['pdf_filename'].replace('.pdf', '.ipynb')}"
            
            content = f"""# 📘 {meta['class_title']}

> **Curso:** {course_cfg['course_name']} ({meta['class_code']})  
> **Nivel:** {meta['level']}  
> **Metáfora Central:** *«{meta['metaphor']}»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

---

## 🌀 Posición en el Aprendizaje en Espiral

Esta clase aborda los conceptos clave mediante el ciclo de 3 fases:

1. **💡 Modelo Mental:** {meta['p4_metaphor_desc']}
2. **💻 Experimentación Guiada:** 4+ ejemplos estructurados para correr y depurar.
3. **🏋️ Desafío Práctico:** Reto de consolidación validado con tests.

```mermaid
flowchart LR
    M["💡 1. Modelo Mental<br/>«{meta['metaphor'][:30]}...»"] --> E["💻 2. Ejemplos Prácticos<br/>4 carpetas ejecutables"]
    E --> R["🏋️ 3. Reto de Código<br/>ejercicios/reto.py"]
    R --> T["🧪 4. Validación<br/>tests/curso_{c_num:02d}/"]

    style M fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style E fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style R fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style T fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🗺️ Arquitectura de la Sesión

{mermaid_block}

---

## 📑 Recursos Disponibles en esta Carpeta

*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual técnico oficial en PDF (9 páginas de estudio).
*   📖 [`book.md`](book.md): Libro de estudio digital completo con diagramas Mermaid nativos.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 4 carpetas con código fuente funcional y comentado.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
"""
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return

    # --------------------------------------------------------------------------
    # 4. READMEs de la carpeta 'ejemplos' de una clase
    # --------------------------------------------------------------------------
    if len(parts) == 4 and parts[2] == "ejemplos":
        c_num = int(parts[0][:2])
        folder_name = parts[1]
        meta = CLASS_META_MAP.get((c_num, folder_name), {})
        class_title = meta.get("class_title", folder_name)
        
        subdirs = [d for d in os.listdir(os.path.dirname(file_path)) if os.path.isdir(os.path.join(os.path.dirname(file_path), d))]
        subdirs.sort()
        
        rows = ""
        for sd in subdirs:
            rows += f"| [`{sd}/`]({sd}/) | Demostración paso a paso | [`main.py`]({sd}/main.py) |\n"
            
        content = f"""# 💻 Catálogo de Ejemplos Prácticos: {class_title}

> **Ubicación:** `{dir_name}`  
> **Metodología:** *La Regla de la Bicicleta (Pedaleo en VS Code)*  

Esta carpeta contiene los ejemplos de código interactivos y comentados diseñados para ver la teoría en acción.

---

## 🌀 Flujo de Experimentación y Pedaleo

```mermaid
flowchart LR
    A["📂 1. Selecciona un Ejemplo<br/>(ejemplo_01 a 04)"] --> B["📖 2. Lee su README.md<br/>Objetivo y modelo mental"]
    B --> C["🐍 3. Ejecuta main.py<br/>Observa la salida en terminal"]
    C --> D["🔧 4. Modifica y Experimenta<br/>Cambia variables y analiza"]

    style A fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style B fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style C fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style D fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 📑 Ejemplos Disponibles

| Subcarpeta | Tipo de Demostración | Archivo de Código |
| :--- | :--- | :---: |
{rows}

---

## 🚀 Cómo Ejecutar los Ejemplos
Desde la terminal en la raíz del repositorio:
```bash
python {dir_name}/<carpeta_ejemplo>/main.py
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 5. READMEs de ejemplos individuales (ej. ejemplo_01_.../README.md)
    # --------------------------------------------------------------------------
    if len(parts) == 5 and parts[2] == "ejemplos":
        c_num = int(parts[0][:2])
        folder_name = parts[1]
        ex_folder = parts[3]
        meta = CLASS_META_MAP.get((c_num, folder_name), {})
        
        ex_clean_title = ex_folder.replace("ejemplo_", "").replace("_", " ").title()
        
        content = f"""# 📖 {ex_clean_title}

> **Clase:** {meta.get('class_title', folder_name)}  
> **Ubicación:** `{dir_name}`  

---

## 🌀 Modelo de Aprendizaje Activo

Este ejemplo demuestra de forma práctica, directa y aislada un principio fundamental de la clase:

```mermaid
flowchart LR
    IN["📥 1. Entrada / Parámetros<br/>Definición de datos"] --> PROC["⚙️ 2. Lógica & Operación<br/>Transformación paso a paso"]
    PROC --> OUT["🎯 3. Salida por Pantalla<br/>print() / Retorno verificado"]

    style IN fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style PROC fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style OUT fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 💻 Cómo Ejecutar este Ejemplo

Abre la terminal en la raíz del repositorio y ejecuta:

```bash
python {dir_name}/main.py
```

---

## 🔍 Código Fuente
Examina el archivo [`main.py`](main.py) en esta misma carpeta para revisar la sintaxis comentada y experimentar modificando los valores.
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 6. READMEs de la carpeta 'ejercicios' de una clase
    # --------------------------------------------------------------------------
    if len(parts) == 4 and parts[2] == "ejercicios":
        c_num = int(parts[0][:2])
        folder_name = parts[1]
        meta = CLASS_META_MAP.get((c_num, folder_name), {})
        
        content = f"""# 🏋️ Reto Práctico: {meta.get('class_title', folder_name)}

> **Curso:** {parts[0]} &bull; **Semana:** {meta.get('class_code', 'Semana')}  
> **Ubicación:** `{dir_name}`  

---

## 🌀 Ciclo de Resolución y Validación

```mermaid
flowchart LR
    A["📖 1. Lee el Reto<br/>ejercicios/reto.py"] --> B["💻 2. Escribe tu Código<br/>Implementa tu solución"]
    B --> C["🧪 3. Ejecuta Pytest<br/>pytest tests/curso_{c_num:02d}/"]
    C -->|Fallo ❌| B
    C -->|Éxito ✅| D["🏆 4. Concepto Consolidado<br/>Avanza a la siguiente clase"]

    style A fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style B fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style C fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style D fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🎯 Desafío de la Sesión
> **Enunciado:** {meta.get('p9_challenge', 'Completa la implementación en reto.py')}

---

## 🚀 Pasos para Resolverlo
1. Abre el archivo [`reto.py`](reto.py).
2. Escribe tu lógica de solución.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_{c_num:02d}/
   ```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 7. READMEs de la carpeta 'notebook' de una clase
    # --------------------------------------------------------------------------
    if len(parts) == 4 and parts[2] == "notebook":
        c_num = int(parts[0][:2])
        folder_name = parts[1]
        meta = CLASS_META_MAP.get((c_num, folder_name), {})
        nb_filename = meta.get("pdf_filename", "clase.pdf").replace(".pdf", ".ipynb")
        colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{parts[0]}/{folder_name}/notebook/{nb_filename}"
        
        content = f"""# 📓 Cuaderno Interactivo: {meta.get('class_title', folder_name)}

> **Curso:** {parts[0]}  
> **Archivo:** [`{nb_filename}`]({nb_filename})  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

---

## 🌀 Modelo de Aprendizaje Celda a Celda

Los cuadernos Jupyter permiten experimentar de forma inmediata:

```mermaid
flowchart LR
    NB["📓 Cuaderno Jupyter<br/>({nb_filename})"] --> COLAB["☁️ Ejecución Nube<br/>Google Colab (1 clic)"]
    NB --> LOCAL["💻 Ejecución Local<br/>VS Code + Jupyter Extension"]
    COLAB --> RUN["⚡ Ejecuta celdas de código<br/>y visualiza variables"]
    LOCAL --> RUN

    style NB fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style COLAB fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style LOCAL fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style RUN fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🚀 Cómo Utilizar este Cuaderno
*   **En la Nube:** Haz clic en el botón superior **Open in Colab** para ejecutarlo sin instalar nada.
*   **En Local:** Abre [`{nb_filename}`]({nb_filename}) directamente en Visual Studio Code.
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 8. READMEs de la carpeta 'tests' y sus subcarpetas
    # --------------------------------------------------------------------------
    if parts[0] == "tests":
        sub_name = parts[1] if len(parts) > 1 else "root"
        content = f"""# 🧪 Suite de Pruebas Automatizadas (Pytest)

> **Módulo:** `{sub_name}`  
> **Ubicación:** `{dir_name}`  

---

## 🌀 Pirámide y Flujo de Verificación de Calidad

```mermaid
flowchart TD
    DEV["💻 Código del Estudiante<br/>(reto.py / funciones)"] --> PYTEST["🧪 Pytest Test Suite<br/>(tests/{sub_name})"]
    PYTEST --> CI["⚙️ GitHub Actions CI<br/>Validación en cada Commit"]
    CI --> PASS["✅ 100% Tests Pasados<br/>Calidad Garantizada"]

    style DEV fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style PYTEST fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style CI fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style PASS fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 💻 Comandos de Ejecución

```bash
# Ejecutar todas las pruebas de este módulo
pytest {dir_name}/

# Ejecutar con reporte detallado
pytest -v {dir_name}/
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 9. READMEs de la carpeta 'docs' y portal web
    # --------------------------------------------------------------------------
    if parts[0] == "docs":
        sub_name = parts[1] if len(parts) > 1 else "Portal Principal"
        content = f"""# 🌐 Documentación Web Interactiva: {sub_name}

> **Sitio Web Oficial:** [`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/)  
> **Ubicación:** `{dir_name}`  

---

## 🌀 Arquitectura del Sitio Web de Documentación

```mermaid
flowchart LR
    SRC["📝 Archivos Markdown<br/>(docs/*.md)"] --> MKDOCS["⚙️ Motor MkDocs Material<br/>Pestañas, admonitions & mermaid"]
    MKDOCS --> GHPAGES["☁️ GitHub Pages<br/>academy_python.wisrovi.dev"]

    style SRC fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style MKDOCS fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style GHPAGES fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 💻 Servidor Local de Previsualización
```bash
mkdocs serve
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    # --------------------------------------------------------------------------
    # 10. READMEs de Infraestructura (devcontainer, github, plantillas, src)
    # --------------------------------------------------------------------------
    sub_title = dir_name.replace("/", " ➔ ").title()
    content = f"""# 📁 {sub_title}

> **Ubicación en Repositorio:** `{dir_name}`  

---

## 🌀 Propósito en la Arquitectura del Proyecto

```mermaid
flowchart LR
    COMP["📦 Componente<br/>{os.path.basename(dir_name)}"] --> SYS["⚙️ Sistema wisrovi-python<br/>Infraestructura & Recursos"]
    SYS --> USER["🎓 Experiencia del Alumno<br/>Entorno optimizado y reproducible"]

    style COMP fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style SYS fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style USER fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 📑 Descripción y Recursos
Este directorio forma parte de la infraestructura integral del programa de formación en Python.
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("=" * 80)
    print("🚀 RECORRIENDO Y MEJORANDO TODOS LOS README.md RECURSIVAMENTE")
    print("=" * 80)
    
    total_processed = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        rel = os.path.relpath(root, BASE_DIR)
        if any(ignored in rel.split(os.sep) for ignored in IGNORE_DIRS):
            continue
            
        if "README.md" in files:
            full_path = os.path.join(root, "README.md")
            process_readme(full_path)
            total_processed += 1
            print(f"  ✓ [{total_processed:03d}] Mejorado: {os.path.relpath(full_path, BASE_DIR)}")
            
    print("\n" + "=" * 80)
    print(f"✨ TOTAL READMEs MEJORADOS: {total_processed} archivos con diagramas Mermaid.")
    print("=" * 80)

if __name__ == "__main__":
    main()
