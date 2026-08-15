#!/usr/bin/env python3
"""
Genera cuadernos interactivos de Jupyter (.ipynb) con badges de Google Colab
para todas las clases del repositorio wisrovi-python.
"""

import os
import json

from build_all_course_pdfs import CLASSES_METADATA, AUTHOR_INFO, BASE_DIR
from generate_books import clean_html_tags

NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")
os.makedirs(NOTEBOOKS_DIR, exist_ok=True)

def create_notebook(meta: dict) -> dict:
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    metaphor = meta["metaphor"]
    course_name = meta["course_name"]
    code_raw = clean_html_tags(meta["p6_code"])
    
    nb_filename = f"{meta['pdf_filename'].replace('.pdf', '.ipynb')}"
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
                f"## 4. 🏋️ Desafío de Práctica para el Estudiante\n\n",
                f"> **Reto:** {meta['p9_challenge']}\n\n",
                f"¡Escribe y prueba tu solución en la siguiente celda!\n"
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
    
    notebook = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.11.0"
            },
            "orig_nbformat": 4
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return nb_filename, notebook

def main():
    print("=" * 70)
    print("📓 GENERANDO CUADERNOS JUPYTER (.ipynb) CON SOPORTE GOOGLE COLAB")
    print("=" * 70)
    
    index_md = ["# 📓 Cuadernos Interactivos de Jupyter (Google Colab)\n\n"]
    index_md.append("Ejecuta cada lección celda a celda en la nube con un solo clic:\n\n")
    index_md.append("| Curso / Clase | Cuaderno Jupyter | Enlace Directo a Colab |\n")
    index_md.append("| :--- | :---: | :---: |\n")
    
    for meta in CLASSES_METADATA:
        nb_filename, nb_json = create_notebook(meta)
        nb_path = os.path.join(NOTEBOOKS_DIR, nb_filename)
        
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_json, f, indent=2, ensure_ascii=False)
            
        badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/notebooks/{nb_filename})"
        index_md.append(f"| **{meta['class_title']}** | [`{nb_filename}`]({nb_filename}) | {badge} |\n")
        print(f"  ✓ Creado: notebooks/{nb_filename}")
        
    with open(os.path.join(NOTEBOOKS_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.writelines(index_md)
        
    print("\n✨ Cuadernos generados y listados en notebooks/README.md")

if __name__ == "__main__":
    main()
