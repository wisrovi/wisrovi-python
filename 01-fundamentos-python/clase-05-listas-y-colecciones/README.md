# 📘 Clase 05: Listas, Tuplas y Colecciones Básicas

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 05)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Listas como Archivadores Modulares y Tuplas como Documentos Notariados»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-05-listas-y-colecciones/notebook/clase-05-listas-y-colecciones.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    L["Lista: ['A', 'B', 'C', 'D']"] --> OP["Operaciones de Mutación"]
    OP --> APP["append('E') ➔ Final"]
    OP --> INS["insert(1, 'X') ➔ Posición"]
    OP --> POP["pop() ➔ Extrae último"]
    L --> SLICE["Slicing [inicio:fin:paso]"]
    SLICE --> SUB["Sublistas & Reversión [::-1]"]

    style L fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style OP fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style APP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style INS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style POP fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style SLICE fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-05-listas-y-colecciones.pdf`](clase-05-listas-y-colecciones.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
