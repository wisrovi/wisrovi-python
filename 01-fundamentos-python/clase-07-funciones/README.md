# 📘 Clase 07: Funciones, Parámetros y Scope

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 07)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Funciones como Máquinas Reutilizables de una Fábrica»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-07-funciones/notebook/clase-07-funciones.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    CALL["🚀 Invocación: calcular_total(precio=100, iva=0.21)"] --> STACK["🥞 Call Stack: Push Frame de Función"]
    STACK --> SCOPE{"🔍 Resolución de Ámbito LEGB"}
    SCOPE -->|1. Local| L["Variables locales dentro de la función"]
    SCOPE -->|2. Global| G["Constantes globales del módulo"]
    SCOPE -->|3. Built-in| B["Funciones estándar (len, print, range)"]
    L --> RET["🎯 return total_calculado"]
    RET --> POP_F["🥞 Pop Frame ➔ Retornar valor al llamador"]

    style CALL fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style STACK fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style SCOPE fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style RET fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style POP_F fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-07-funciones.pdf`](clase-07-funciones.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
