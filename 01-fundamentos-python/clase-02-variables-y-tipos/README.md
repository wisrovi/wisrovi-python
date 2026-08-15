# 📘 Clase 02: Variables, Tipos de Datos y Operadores

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 02)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Variables como Cajas Etiquetadas en Memoria»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-02-variables-y-tipos/notebook/clase-02-variables-y-tipos.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    VAL["Valor Literal ('45.90')"] --> STR["str (Texto Inmutable)"]
    STR --> CAST["Casting: float()"]
    CAST --> FLT["float (45.90)"]
    FLT --> TRUNC["Casting: int()"]
    TRUNC --> INT["int (45)"]
    INT --> MEM["Referencia en Memoria<br/>id(objeto)"]

    style VAL fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style STR fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
    style CAST fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style FLT fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style TRUNC fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style INT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style MEM fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-02-variables-y-tipos.pdf`](clase-02-variables-y-tipos.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
