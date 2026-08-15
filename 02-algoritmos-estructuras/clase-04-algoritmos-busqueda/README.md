# 📘 Clase 04: Algoritmos de Búsqueda: Lineal vs Binaria O(log n)

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 04)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Búsqueda Binaria como Buscar una Palabra en el Diccionario Dividiendo a la Mitad»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-04-algoritmos-busqueda/notebook/clase-04-algoritmos-busqueda.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    ARR["Arreglo Ordenado: [1, 3, 5, 7, 9, 11]"] --> MID["Calcular Punto Medio (Mid)"]
    MID --> CMP{"¿Mid == Target?"}
    CMP -->|Sí| FOUND["🎯 Elemento Encontrado en O(log n)"]
    CMP -->|Menor| RIGHT["Descartar Mitad Izquierda (L = Mid + 1)"]
    CMP -->|Mayor| LEFT["Descartar Mitad Derecha (R = Mid - 1)"]
    RIGHT --> MID
    LEFT --> MID

    style ARR fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MID fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style CMP fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style FOUND fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-04-algoritmos-busqueda.pdf`](clase-04-algoritmos-busqueda.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
