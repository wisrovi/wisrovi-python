# 📘 Clase 05: Algoritmos de Ordenamiento: QuickSort y MergeSort

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 05)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Ordenar Barajas de Cartas con Divide y Vencerás»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-05-algoritmos-ordenamiento/notebook/clase-05-algoritmos-ordenamiento.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    L["Lista Desordenada [38, 27, 43, 3, 9]"] --> PIV["Seleccionar Pivote (43)"]
    PIV --> PART["Partición: [x < P] + [P] + [x > P]"]
    PART --> REC["QuickSort Recursivo en Sublistas"]
    REC --> SORTED["Lista Ordenada en O(n log n)"]

    style L fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style PIV fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style PART fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SORTED fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-05-algoritmos-ordenamiento.pdf`](clase-05-algoritmos-ordenamiento.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
