# 📘 Clase 02: Pilas (Stacks) y Colas (Queues) con collections.deque

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 02)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Pilas LIFO como Platos Apilados y Colas FIFO como la Fila del Supermercado»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-02-pilas-y-colas/notebook/clase-02-pilas-y-colas.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    subgraph Pila["🥞 Pila (Stack LIFO)"]
        P_IN["push(X) ➔ Tope"] --> P_OUT["pop() ➔ Extrae Tope"]
    end
    subgraph Cola["🚶‍♂️ Cola (Queue FIFO - deque)"]
        Q_IN["append(X) ➔ Final"] --> Q_OUT["popleft() ➔ Atiende Primero (O(1))"]
    end

    style Pila fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style Cola fill:#f0fdf4,stroke:#10b981,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-02-pilas-y-colas.pdf`](clase-02-pilas-y-colas.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
