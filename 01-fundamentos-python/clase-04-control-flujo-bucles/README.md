# 📘 Clase 04: Control de Flujo: Bucles (for / while)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 04)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Bucles como una Cinta Transportadora de Fábrica»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-04-control-flujo-bucles/notebook/clase-04-control-flujo-bucles.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    SEQ["📦 Secuencia o Rango<br/>range(1, 10) o lista"] --> ITER["🔄 Iterador del Bucle (for / while)"]
    ITER --> BODY["⚡ Ejecutar Bloque del Bucle"]
    BODY --> CTRL{"¿Instrucción Especial?"}
    CTRL -->|continue| ITER
    CTRL -->|break| EXIT["🛑 Salida Inmediata del Ciclo"]
    CTRL -->|Flujo Normal| NEXT{"¿Fin de Secuencia?"}
    NEXT -->|No| ITER
    NEXT -->|Sí| EXIT

    style SEQ fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style NEXT fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
    style EXIT fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-04-control-flujo-bucles.pdf`](clase-04-control-flujo-bucles.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
