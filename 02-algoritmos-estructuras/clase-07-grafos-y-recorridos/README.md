# 📘 Clase 07: Grafos, Matrices de Adyacencia y Recorridos BFS/DFS

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 07)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Grafos como Redes de Ciudades y Rutas de Vuelo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-07-grafos-y-recorridos/notebook/clase-07-grafos-y-recorridos.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    G["Grafo: Lista de Adyacencia"] --> BFS["BFS: Cola deque ➔ Exploración por Niveles"]
    G --> DFS["DFS: Pila / Recursión ➔ Exploración en Profundidad"]
    BFS --> VIS["Conjunto de Nodos Visitados (set)"]
    DFS --> VIS

    style G fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style BFS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style DFS fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style VIS fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-07-grafos-y-recorridos.pdf`](clase-07-grafos-y-recorridos.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
