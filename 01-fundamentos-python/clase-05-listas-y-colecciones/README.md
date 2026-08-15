# 📘 Clase 05: Listas, Tuplas y Colecciones Básicas

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 05)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Listas como Archivadores Modulares y Tuplas como Documentos Notariados»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-05-listas-y-colecciones/notebook/clase-05-listas-y-colecciones.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    LISTA["📚 Lista Mutable<br/>['Python', 'Docker', 'FastAPI']"] --> MUT["🔧 Métodos de Mutación"]
    MUT --> APP["append('Git') ➔ Inserta al final"]
    MUT --> INS["insert(1, 'SQL') ➔ Inserta en índice"]
    MUT --> POP["pop() ➔ Extrae último elemento"]
    LISTA --> SLICE["✂️ Slicing [inicio:fin:paso]<br/>lista[::-1] ➔ Invertir lista"]
    LISTA --> COMP["⚡ List Comprehension<br/>[x**2 for x in nums if x%2==0]"]

    style LISTA fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style MUT fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style APP fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style INS fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style POP fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style SLICE fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style COMP fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-05-listas-y-colecciones.pdf`](clase-05-listas-y-colecciones.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
