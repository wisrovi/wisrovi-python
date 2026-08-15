#!/usr/bin/env python3
"""
Mueve los cuadernos Jupyter a su propia subcarpeta 'notebook/' dentro de cada clase,
con su archivo .ipynb y su README.md dedicado, actualizando todos los badges de Google Colab.
"""

import os
import shutil

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, BASE_DIR

DOCS_DIR = os.path.join(BASE_DIR, "docs")

def organize_class_notebooks():
    print("=" * 80)
    print("🚀 ORGANIZANDO CUADERNOS EN SUBCARPETAS /notebook/ DENTRO DE CADA CLASE")
    print("=" * 80)
    
    course_map = {c["course_num"]: c for c in COURSES_CONFIG}
    
    for meta in ALL_CLASSES:
        course_cfg = course_map[meta["course_num"]]
        class_dir = os.path.join(BASE_DIR, course_cfg["course_id"], meta["folder_name"])
        nb_filename = meta["pdf_filename"].replace(".pdf", ".ipynb")
        
        old_nb_path = os.path.join(class_dir, nb_filename)
        notebook_subfolder = os.path.join(class_dir, "notebook")
        os.makedirs(notebook_subfolder, exist_ok=True)
        new_nb_path = os.path.join(notebook_subfolder, nb_filename)
        
        # Mover o copiar .ipynb a la subcarpeta notebook/
        if os.path.exists(old_nb_path):
            shutil.move(old_nb_path, new_nb_path)
            
        colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{course_cfg['course_id']}/{meta['folder_name']}/notebook/{nb_filename}"
        colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
        
        # Crear README.md dentro de la carpeta notebook/
        with open(os.path.join(notebook_subfolder, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"# 📓 Cuaderno Interactivo: {meta['class_title']}\n\n"
                    f"> **Curso:** {course_cfg['course_name']}  \n"
                    f"> **Metáfora:** *«{meta['metaphor']}»*  \n\n"
                    f"## ☁️ Ejecutar en la Nube con 1 Clic\n"
                    f"{colab_badge}\n\n"
                    f"## 💻 Ejecutar Localmente en VS Code\n"
                    f"Abre el archivo [`{nb_filename}`]({nb_filename}) directamente en Visual Studio Code con la extensión de Jupyter instalada.\n")
            
        # Actualizar README.md principal de la clase
        readme_path = os.path.join(class_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# 📘 {meta['class_title']}\n\n"
                    f"> **Curso:** {course_cfg['course_name']}  \n"
                    f"> **Nivel:** {meta['level']}  \n"
                    f"> **Metáfora:** *«{meta['metaphor']}»*  \n\n"
                    f"{colab_badge}\n\n"
                    f"## 📑 Estructura de la Clase\n"
                    f"*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual de estudio en PDF (9 páginas).\n"
                    f"*   📖 [`book.md`](book.md): Libro de estudio digital con diagramas Mermaid.\n"
                    f"*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter (`.ipynb`) con soporte para Google Colab.\n"
                    f"*   📁 `ejemplos/`: 4 carpetas con scripts de código funcional y sus explicaciones.\n"
                    f"*   📁 `ejercicios/`: Reto práctico para afianzar conceptos.\n")
            
        # Actualizar enlace en docs/ para MkDocs
        doc_class_path = os.path.join(DOCS_DIR, f"curso-{course_cfg['course_num']:02d}", f"clase-{int(meta['class_code'].replace('CLASE ', '')):02d}.md")
        if os.path.exists(doc_class_path):
            with open(doc_class_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Asegurar que el badge apunte a la subcarpeta /notebook/
            old_colab_pattern = f"{course_cfg['course_id']}/{meta['folder_name']}/{nb_filename}"
            new_colab_pattern = f"{course_cfg['course_id']}/{meta['folder_name']}/notebook/{nb_filename}"
            if old_colab_pattern in content:
                content = content.replace(old_colab_pattern, new_colab_pattern)
                with open(doc_class_path, "w", encoding="utf-8") as f:
                    f.write(content)
                    
        print(f"  ✓ [C{meta['course_num']}] {meta['folder_name']}/notebook/{nb_filename} organizado.")
        
    print("\n" + "=" * 80)
    print("✨ TODOS LOS CUADERNOS TIENEN SU PROPIA CARPETA /notebook/.")
    print("=" * 80)

if __name__ == "__main__":
    organize_class_notebooks()
