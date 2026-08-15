#!/usr/bin/env python3
"""
Sincroniza los archivos book.md de cada curso y clase dentro de la carpeta docs/ para MkDocs Material.
"""

import os
import shutil

BASE_DIR = "/home/wisrovi/Documents/wisrovi-python"
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# 1. Crear docs/index.md
index_content = """# 🐍 Programa Integral de Formación en Python

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Nivel](https://img.shields.io/badge/Nivel-Principiante_a_Avanzado-brightgreen.svg)
![CI Status](https://img.shields.io/badge/CI-Passing-success.svg)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)

Bienvenido/a al portal web oficial del **Programa Integral de Formación en Python: De Cero a Agentes de IA**.

---

## 🎯 Mapa de Aprendizaje (4 Niveles)

```mermaid
flowchart TD
    C1["🎯 Curso 1: Fundamentos de Python\n(8 Clases - 100% Principiantes)"] --> C2["🚀 Curso 2: Algoritmos Avanzados\ny Estructuras de Datos"]
    C2 --> C3["🤖 Curso 3: Creación y Desarrollo\nde Agentes de IA"]
    C3 --> C4["🛠️ Curso 4: Taller Práctico &\nProyecto Final Personalizado"]

    style C1 fill:#2b5c8f,color:#fff,stroke:#fff,stroke-width:2px
    style C2 fill:#3b7a57,color:#fff,stroke:#fff,stroke-width:2px
    style C3 fill:#6b4c9a,color:#fff,stroke:#fff,stroke-width:2px
    style C4 fill:#c05621,color:#fff,stroke:#fff,stroke-width:2px
```

---

## 📚 Acceso Directo a los Manuales

| Curso | Nivel | Contenidos Clave | Enlace al Manual |
| :---: | :--- | :--- | :---: |
| **Curso 1** | **Fundamentos Básicos** | 8 Clases: variables, if, for, def, colecciones y proyecto CLI | [📘 Ver Curso 1](curso-01/book.md) |
| **Curso 2** | **Algoritmos y Estructuras** | Pilas, colas, sets, Big-O, búsqueda binaria y recursión | [📘 Ver Curso 2](curso-02/book.md) |
| **Curso 3** | **Agentes de IA** | LLMs, Tool Calling, memoria vectorial, RAG y ciclo ReAct | [📘 Ver Curso 3](curso-03/book.md) |
| **Curso 4** | **Proyecto Integrador** | FastAPI + Streamlit, Chatbots con memoria y bases de datos | [📘 Ver Curso 4](curso-04/book.md) |

---

## 👤 Acerca del Instructor

**William Rodríguez (Wisrovi)**  
*AI Solutions Architect & Principal Software Engineer &bull; Badajoz, España*

* 🐙 **GitHub:** [github.com/wisrovi](https://github.com/wisrovi)
* 💼 **LinkedIn:** [linkedin.com/in/wisrovi-rodriguez](https://www.linkedin.com/in/wisrovi-rodriguez/)
* 🐳 **DockerHub:** [hub.docker.com/u/wisrovi](https://hub.docker.com/u/wisrovi)
* 🌐 **Website:** [wisrovi.dev](https://wisrovi.dev)

> *"La regla de la bicicleta: Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."* 🚴‍♂️
"""

def sync_docs():
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)
        
    # Curso 1
    c1_dir = os.path.join(DOCS_DIR, "curso-01")
    os.makedirs(c1_dir, exist_ok=True)
    shutil.copy2(f"{BASE_DIR}/01-fundamentos-python/book.md", f"{c1_dir}/book.md")
    for i in range(1, 9):
        names = [
            "clase-01-panorama-general", "clase-02-variables-y-tipos", "clase-03-control-flujo-condicionales",
            "clase-04-control-flujo-bucles", "clase-05-listas-y-colecciones", "clase-06-diccionarios",
            "clase-07-funciones", "clase-08-proyecto-integrador-basico"
        ]
        shutil.copy2(f"{BASE_DIR}/01-fundamentos-python/{names[i-1]}/book.md", f"{c1_dir}/clase-{i:02d}.md")
        
    # Curso 2
    c2_dir = os.path.join(DOCS_DIR, "curso-02")
    os.makedirs(c2_dir, exist_ok=True)
    shutil.copy2(f"{BASE_DIR}/02-algoritmos-estructuras/book.md", f"{c2_dir}/book.md")
    names2 = [
        "01-estructuras-datos-avanzadas", "02-algoritmos-ordenamiento-busqueda", "03-recursividad-optimizacion"
    ]
    for i, n in enumerate(names2, 1):
        shutil.copy2(f"{BASE_DIR}/02-algoritmos-estructuras/{n}/book.md", f"{c2_dir}/modulo-{i:02d}.md")

    # Curso 3
    c3_dir = os.path.join(DOCS_DIR, "curso-03")
    os.makedirs(c3_dir, exist_ok=True)
    shutil.copy2(f"{BASE_DIR}/03-agentes-ia/book.md", f"{c3_dir}/book.md")
    names3 = [
        "01-fundamentos-ia-llm", "02-herramientas-y-memoria", "03-construccion-de-agentes"
    ]
    for i, n in enumerate(names3, 1):
        shutil.copy2(f"{BASE_DIR}/03-agentes-ia/{n}/book.md", f"{c3_dir}/modulo-{i:02d}.md")

    # Curso 4
    c4_dir = os.path.join(DOCS_DIR, "curso-04")
    os.makedirs(c4_dir, exist_ok=True)
    shutil.copy2(f"{BASE_DIR}/04-proyecto-final/book.md", f"{c4_dir}/book.md")
    names4 = [
        "01-aplicacion-web", "02-chatbot-inteligente", "03-sistema-gestion-bd"
    ]
    for i, n in enumerate(names4, 1):
        shutil.copy2(f"{BASE_DIR}/04-proyecto-final/plantillas/{n}/book.md", f"{c4_dir}/track-{i:02d}.md")

    print("✓ Sincronizados todos los archivos en docs/ para MkDocs Material.")

if __name__ == "__main__":
    sync_docs()
