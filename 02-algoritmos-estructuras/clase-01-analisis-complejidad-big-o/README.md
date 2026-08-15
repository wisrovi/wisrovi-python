# 📘 Clase 01: Análisis de Complejidad y Notación Big-O

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 01)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Medir el Rendimiento de un Algoritmo a Medida que Crece la Entrada»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-01-analisis-complejidad-big-o/notebook/clase-01-analisis-complejidad-big-o.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    O1["O(1) Constante<br/>Acceso a Dict/List"] --> ON["O(n) Lineal<br/>Búsqueda Secuencial"]
    ON --> OLOGN["O(n log n)<br/>MergeSort / Timsort"]
    OLOGN --> ON2["O(n²) Cuadrático<br/>Bucles Anidados"]

    style O1 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style ON fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style OLOGN fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ON2 fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-01-analisis-complejidad-big-o.pdf`](clase-01-analisis-complejidad-big-o.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
