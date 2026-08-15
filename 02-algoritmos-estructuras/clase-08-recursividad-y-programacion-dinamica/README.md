# 📘 Clase 08: Recursividad y Programación Dinámica con Memoización

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 08)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Programación Dinámica como Recordar el Pasado para no Resolverlo Dos Veces»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-08-recursividad-y-programacion-dinamica/notebook/clase-08-recursividad-y-programacion-dinamica.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    N["Llamada fib(n)"] --> CHK{"¿Está en Caché @lru_cache?"}
    CHK -->|Sí| HIT["🎯 Retorno Instantáneo O(1)"]
    CHK -->|No| CALC["Calcular fib(n-1) + fib(n-2)"]
    CALC --> STORE["Almacenar en Tabla DP"]
    STORE --> HIT

    style N fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style CHK fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style HIT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style STORE fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-08-recursividad-y-programacion-dinamica.pdf`](clase-08-recursividad-y-programacion-dinamica.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
