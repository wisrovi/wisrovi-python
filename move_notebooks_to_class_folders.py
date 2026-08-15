#!/usr/bin/env python3
"""
Mueve y genera cada cuaderno Jupyter (.ipynb) directamente dentro de la carpeta
de su clase correspondiente (junto a su PDF, book.md y ejemplos), actualizando
los enlaces de Google Colab para máxima intuición y orden.
"""

import os
import shutil
import json

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, AUTHOR_INFO, BASE_DIR
from generate_books import clean_html_tags

DOCS_DIR = os.path.join(BASE_DIR, "docs")
OLD_NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")

def build_class_notebook(meta: dict, course_cfg: dict) -> dict:
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    metaphor = meta["metaphor"]
    course_name = course_cfg["course_name"]
    course_id = course_cfg["course_id"]
    folder_name = meta["folder_name"]
    nb_filename = meta["pdf_filename"].replace(".pdf", ".ipynb")
    code_raw = clean_html_tags(meta["p6_code"])
    
    # Enlace exacto a Google Colab dentro de la carpeta de la clase
    colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{course_id}/{folder_name}/{nb_filename}"
    colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# 🐍 {class_title}\n",
                f"### **{course_name} ({class_code})**\n\n",
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
                f"## 1. 💡 Fundamentación Teórica y Modelo Mental\n\n",
                f"{meta['p4_intro']}\n\n",
                f"> **Metáfora Didáctica:** {meta['p4_metaphor_desc']}\n\n",
                f"{meta['p4_theory_1']}\n\n",
                f"{meta['p4_theory_2']}\n\n",
                f"**⚡ Regla de Oro en Python:** {meta['p4_golden_rule']}\n"
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
                f"# {class_code} - Código de Demostración\n",
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
                f"## 4. 🏋️ Desafío Práctico de la Clase\n\n",
                f"> **Reto:** {meta['p9_challenge']}\n\n",
                f"¡Escribe y prueba tu solución en la siguiente celda interactiva!\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Escribe tu solución aquí:\n",
                "\n"
            ]
        }
    ]
    
    return {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python", "version": "3.11.0"},
            "orig_nbformat": 4
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

def main():
    print("=" * 80)
    print("🚀 UBICANDO CUADERNOS JUPYTER (.ipynb) DIRECTAMENTE EN CADA CLASE")
    print("=" * 80)
    
    # 1. Limpiar carpeta raíz antigua /notebooks
    if os.path.exists(OLD_NOTEBOOKS_DIR):
        shutil.rmtree(OLD_NOTEBOOKS_DIR)
        print("  🧹 Eliminada carpeta global /notebooks de la raíz.")
        
    course_map = {c["course_num"]: c for c in COURSES_CONFIG}
    
    for meta in ALL_CLASSES:
        course_cfg = course_map[meta["course_num"]]
        class_dir = os.path.join(BASE_DIR, course_cfg["course_id"], meta["folder_name"])
        nb_filename = meta["pdf_filename"].replace(".pdf", ".ipynb")
        nb_path = os.path.join(class_dir, nb_filename)
        
        # Generar JSON de notebook
        nb_json = build_class_notebook(meta, course_cfg)
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_json, f, indent=2, ensure_ascii=False)
            
        colab_url = f"https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/{course_cfg['course_id']}/{meta['folder_name']}/{nb_filename}"
        colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
        
        # Actualizar README.md de la clase
        readme_path = os.path.join(class_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# 📘 {meta['class_title']}\n\n"
                    f"> **Curso:** {course_cfg['course_name']}  \n"
                    f"> **Nivel:** {meta['level']}  \n"
                    f"> **Metáfora:** *«{meta['metaphor']}»*  \n\n"
                    f"{colab_badge}\n\n"
                    f"## 📑 Recursos Disponibles en esta Carpeta\n"
                    f"*   📓 [`{nb_filename}`]({nb_filename}): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.\n"
                    f"*   📄 [`{meta['pdf_filename']}`]({meta['pdf_filename']}): Manual oficial en PDF (9 páginas con estética LaTeX).\n"
                    f"*   📖 [`book.md`](book.md): Libro de estudio digital con diagramas Mermaid nativos.\n"
                    f"*   💻 `ejemplos/`: 4 carpetas con scripts de código funcional y sus READMEs.\n"
                    f"*   🏋️ `ejercicios/`: Retos prácticos con suite de tests automatizados (`pytest`).\n")
            
        # Actualizar página correspondiente en docs/ para MkDocs
        doc_class_path = os.path.join(DOCS_DIR, f"curso-{course_cfg['course_num']:02d}", f"clase-{int(meta['class_code'].replace('CLASE ', '')):02d}.md")
        if os.path.exists(doc_class_path):
            with open(doc_class_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Añadir badge de Colab en el header de la web si no está
            if "[![Open In Colab]" not in content:
                content = content.replace("</div>\n\n---", f"</div>\n\n{colab_badge}\n\n---")
                with open(doc_class_path, "w", encoding="utf-8") as f:
                    f.write(content)
                    
        print(f"  ✓ [C{meta['course_num']}] {meta['folder_name']}/{nb_filename} generado.")
        
    print("\n" + "=" * 80)
    print("✨ TODOS LOS CUADERNOS JUPYTER ESTÁN AHORA JUNTO A SU CLASE.")
    print("=" * 80)

if __name__ == "__main__":
    main()
