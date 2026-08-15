# 📘 Clase 04: Desarrollo del Frontend: Dashboards con Streamlit

<div align="center">

**Curso 4: Taller Práctico & Proyecto Final Integrador** &bull; **Semana CLASE 04**  
*Nivel:* `Nivel 4 - Integrador` &bull; *Metáfora Central:* **«Streamlit como el Salón de Control Visual para tu Backend de Python»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-04-frontend-streamlit/notebook/clase-04-frontend-streamlit.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-04-frontend-streamlit.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Streamlit como el Salón de Control Visual para tu Backend de Python»* (Es como un tablero de mandos de automóvil donde cada botón y pantalla se conecta directamente al motor de tu backend.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart LR
    IN["📥 1. Datos de Entrada<br/>(Streamlit como el Salón de Con...)"] --> ENG["⚙️ 2. Motor de Procesamiento<br/>Dashboards con Streamlit"]
    ENG --> OUT["🎯 3. Salida Verificada<br/>Estado en Memoria / Retorno"]

    style IN fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ENG fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-04-frontend-streamlit/
├── 📄 clase-04-frontend-streamlit.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-04-frontend-streamlit.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Crea una vista con st.tabs para alternar entre el formulario de registro y la tabla de datos.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_04/test_clase_04_frontend_streamlit.py
```
