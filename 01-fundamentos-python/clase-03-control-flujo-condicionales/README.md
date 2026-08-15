# 📘 Clase 03: Control de Flujo: Condicionales (if / elif / else)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 03)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Condicionales como Semáforos y Bifurcaciones en un Tren»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-03-control-flujo-condicionales/notebook/clase-03-control-flujo-condicionales.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    COND["⚖️ Evaluación de Expresión Booleana"] --> IF{"¿Condición Principal<br/>if edad >= 18?"}
    IF -->|True (Verdadero)| B1["🟢 Semáforo Verde<br/>Acceso Autorizado al Sistema"]
    IF -->|False (Falso)| ELIF{"¿Condición Secundaria<br/>elif tiene_permiso?"}
    ELIF -->|True (Verdadero)| B2["🟡 Semáforo Amarillo<br/>Acceso con Supervisión"]
    ELIF -->|False (Falso)| ELSE["🔴 Semáforo Rojo<br/>Acceso Denegado por Defecto"]

    style COND fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style IF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B1 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B2 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style ELSE fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-03-control-flujo-condicionales.pdf`](clase-03-control-flujo-condicionales.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
