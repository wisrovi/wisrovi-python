# 📘 Clase 03: Tablas Hash y Conjuntos (Sets) para Búsqueda O(1)

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 03)  
> **Nivel:** Nivel 2 - Intermedio &bull; **Metáfora:** *«Tablas Hash como un Fichero con Índice Alfabético Instantáneo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-03-tablas-hash-y-sets/notebook/clase-03-tablas-hash-y-sets.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    K["Clave 'email'"] --> H["hash('email') % Buckets"]
    H --> B["Index Bucket"]
    B --> V["Valor O(1)"]
    V --> TWOSUM["Two-Sum: Target - Num en Hashmap (O(n))"]

    style K fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style H fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style TWOSUM fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-03-tablas-hash-y-sets.pdf`](clase-03-tablas-hash-y-sets.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
