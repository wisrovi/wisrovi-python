# 📘 Clase 04: Control de Flujo: Bucles (for / while)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 04)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Bucles como una Cinta Transportadora de Fábrica»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-04-control-flujo-bucles/notebook/clase-04-control-flujo-bucles.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    INIT["Colección o Rango de Datos"] --> ITER["Iterador: for item in secuencia / while condicion"]
    ITER --> BODY["Ejecutar cuerpo del bucle"]
    BODY --> CTRL{"¿Control de Flujo?"}
    CTRL -->|continue| ITER
    CTRL -->|break| END["Salida Inmediata del Bucle"]
    CTRL -->|Flujo normal| NEXT{"¿Quedan elementos?"}
    NEXT -->|Sí| ITER
    NEXT -->|No| END

    style INIT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style END fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-04-control-flujo-bucles.pdf`](clase-04-control-flujo-bucles.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
