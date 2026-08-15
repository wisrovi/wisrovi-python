#!/usr/bin/env python3
"""
Auditor y Generador Exhaustivo de README.md para TODOS los directorios del repositorio.
Garantiza que ninguna carpeta quede sin su respectivo archivo README.md explicativo.
"""

import os
from typing import List, Tuple

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

def generate_custom_readme_content(dir_path: str) -> str:
    rel_path = os.path.relpath(dir_path, BASE_DIR)
    parts = rel_path.split(os.sep)
    folder_name = os.path.basename(dir_path)
    
    # Caso 1: Carpetas 'ejemplos' dentro de una clase
    if folder_name == "ejemplos" and len(parts) >= 3:
        course_name = parts[0]
        class_name = parts[1]
        subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
        subdirs.sort()
        
        md = f"# 💻 Ejemplos de Código: {class_name}\n\n"
        md += f"> **Curso:** `{course_name}`  \n"
        md += f"> **Ubicación:** `{rel_path}`  \n\n"
        md += "Esta carpeta contiene los scripts prácticos y casos de uso demostrativos diseñados para afianzar los conceptos de la clase.\n\n"
        md += "## 📑 Índice de Ejemplos en esta Carpeta\n\n"
        md += "| Subcarpeta | Descripción | Script Principal |\n"
        md += "| :--- | :--- | :---: |\n"
        for sd in subdirs:
            md += f"| [`{sd}/`]({sd}/) | Caso práctico demostrativo | [`main.py`]({sd}/main.py) |\n"
        md += "\n## 🚀 Cómo ejecutar cualquiera de los ejemplos\n"
        md += "Abre la terminal en la raíz del repositorio y ejecuta:\n"
        md += f"```bash\npython {rel_path}/<nombre_del_ejemplo>/main.py\n```\n"
        return md

    # Caso 2: Carpetas 'ejercicios' dentro de una clase
    elif folder_name == "ejercicios" and len(parts) >= 3:
        course_name = parts[0]
        class_name = parts[1]
        return f"""# 🏋️ Ejercicios y Retos Prácticos: {class_name}

> **Curso:** `{course_name}`  
> **Ubicación:** `{rel_path}`  

Esta carpeta contiene el reto práctico de la sesión para consolidar tus conocimientos y poner a prueba tu lógica.

## 🎯 Instrucciones para el Estudiante
1. Abre el archivo [`reto.py`](reto.py) en Visual Studio Code.
2. Lee el enunciado y completa la implementación requerida.
3. Para validar que tu solución sea correcta, ejecuta la suite de pruebas desde la terminal:
   ```bash
   pytest tests/
   ```
"""

    # Caso 3: Carpetas 'notebook' dentro de una clase
    elif folder_name == "notebook" and len(parts) >= 3:
        course_name = parts[0]
        class_name = parts[1]
        nb_files = [f for f in os.listdir(dir_path) if f.endswith(".ipynb")]
        nb_name = nb_files[0] if nb_files else f"{class_name}.ipynb"
        colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{rel_path}/{nb_name}"
        return f"""# 📓 Cuaderno Interactivo (Jupyter Notebook)

> **Clase:** `{class_name}`  
> **Curso:** `{course_name}`  

Este cuaderno contiene la teoría, explicaciones interactivas, modelos mentales y celdas de código ejecutables celda por celda.

## ☁️ Abrir en Google Colab con 1 Clic
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})

## 💻 Ejecución Local en Visual Studio Code
Abre el archivo [`{nb_name}`]({nb_name}) directamente en tu editor VS Code con la extensión de Jupyter instalada.
"""

    # Caso 4: Carpeta 'src' o subcarpetas de código fuente
    elif folder_name == "src" or "src" in parts:
        return f"""# 📦 Código Fuente y Paquetes Internos

> **Módulo:** `{folder_name}`  
> **Ruta:** `{rel_path}`  

Este directorio alberga la lógica fuente y herramientas CLI (`wisrovi`) que gestionan las utilidades de línea de comandos del repositorio.
"""

    # Caso 5: Subcarpetas de docs
    elif "docs" in parts:
        return f"""# 🌐 Documentación Web: {folder_name}

> **Ruta:** `{rel_path}`  

Contenido fuente en Markdown compilado automáticamente por MkDocs Material para el portal interactivo [`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/).
"""

    # Caso Genérico
    else:
        items = os.listdir(dir_path)
        subfolders = [i for i in items if os.path.isdir(os.path.join(dir_path, i)) and i not in IGNORE_DIRS]
        files = [i for i in items if os.path.isfile(os.path.join(dir_path, i)) and not i.startswith(".")]
        
        md = f"# 📁 {folder_name}\n\n"
        md += f"> **Ubicación:** `{rel_path}`  \n\n"
        md += "Directorio de recursos y materiales del programa de formación en Python.\n\n"
        if subfolders:
            md += "## 📂 Subcarpetas\n"
            for sf in sorted(subfolders):
                md += f"*   📁 [`{sf}/`]({sf}/)\n"
            md += "\n"
        if files:
            md += "## 📄 Archivos Destacados\n"
            for fl in sorted(files):
                if fl != "README.md":
                    md += f"*   📄 [`{fl}`]({fl})\n"
            md += "\n"
        return md

def ensure_all_readmes():
    print("=" * 80)
    print("🔍 AUDITANDO Y GENERANDO README.md EN TODAS LAS CARPETAS DEL REPOSITORIO")
    print("=" * 80)
    
    missing_count = 0
    updated_count = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Filtrar directorios ignorados
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        rel = os.path.relpath(root, BASE_DIR)
        if any(ignored in rel.split(os.sep) for ignored in IGNORE_DIRS):
            continue
            
        readme_path = os.path.join(root, "README.md")
        
        # Si no existe README.md, crearlo
        if not os.path.exists(readme_path):
            content = generate_custom_readme_content(root)
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✨ [CREADO] {os.path.relpath(readme_path, BASE_DIR)}")
            missing_count += 1
        else:
            # Si es una carpeta 'ejemplos' o 'ejercicios', actualizar para que esté 100% enriquecido
            folder_name = os.path.basename(root)
            if folder_name in ["ejemplos", "ejercicios"]:
                content = generate_custom_readme_content(root)
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(content)
                updated_count += 1
                
    print("\n" + "=" * 80)
    print(f"✨ RESULTADO: {missing_count} READMEs creados y {updated_count} actualizados.")
    print("✨ CADA CARPETA DEL REPOSITORIO CUENTA AHORA CON SU RESPECTIVO README.md.")
    print("=" * 80)

if __name__ == "__main__":
    ensure_all_readmes()
