# 📘 Clase 03: Control de Flujo: Condicionales (if / elif / else)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 03)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Condicionales como Semáforos y Bifurcaciones en un Tren»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-03-control-flujo-condicionales/notebook/clase-03-control-flujo-condicionales.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    IN["Entrada de Datos"] --> EVAL{"¿Condición if principal?"}
    EVAL -->|True| B1["Bloque 1: Ejecutar código if"]
    EVAL -->|False| ELIF{"¿Condición secundaria elif?"}
    ELIF -->|True| B2["Bloque 2: Ejecutar código elif"]
    ELIF -->|False| ELSE["Bloque 3: Rama por defecto else"]
    B1 --> OUT["Continuación del Programa"]
    B2 --> OUT
    ELSE --> OUT

    style IN fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style EVAL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B1 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B2 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style ELSE fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style OUT fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-03-control-flujo-condicionales.pdf`](clase-03-control-flujo-condicionales.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
