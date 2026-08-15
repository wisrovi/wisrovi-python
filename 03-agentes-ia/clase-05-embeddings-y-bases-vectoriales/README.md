# 📘 Clase 05: Embeddings y Representación Vectorial Semántica

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 05)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«Embeddings como Coordenadas GPS del Significado de las Palabras»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-05-embeddings-y-bases-vectoriales/notebook/clase-05-embeddings-y-bases-vectoriales.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    DOC["Texto de Entrada"] --> EMB["Modelo de Embedding"]
    EMB --> VEC["Vector Flotante [0.12, -0.45, ..., 0.88]"]
    VEC --> COS["Cálculo de Similitud Coseno (Distancia Angular)"]
    COS --> RANK["Ranking de Relevancia Semántica"]

    style DOC fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style EMB fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style VEC fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style COS fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style RANK fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-05-embeddings-y-bases-vectoriales.pdf`](clase-05-embeddings-y-bases-vectoriales.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
