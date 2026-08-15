# 📘 Clase 07: Funciones, Parámetros y Scope

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 07)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Funciones como Máquinas Reutilizables de una Fábrica»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-07-funciones/notebook/clase-07-funciones.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    CALL["Llamada: calcular(base=5, altura=3)"] --> FRAME["Push Stack Frame (Ámbito Local)"]
    FRAME --> SCOPE{"Resolución de Nombres LEGB"}
    SCOPE -->|1. Local| L_VAR["Variables de función"]
    SCOPE -->|2. Global| G_VAR["Módulo global"]
    SCOPE -->|3. Built-in| B_VAR["Funciones estándar (len, print)"]
    L_VAR --> RET["return resultado"]
    RET --> POP_F["Pop Stack Frame ➔ Devolver Control"]

    style CALL fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FRAME fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SCOPE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style RET fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style POP_F fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-07-funciones.pdf`](clase-07-funciones.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
