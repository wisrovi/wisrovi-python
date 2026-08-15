# 📘 Clase 01: Fundamentos de LLMs, Tokens y Arquitectura Transformer

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 01)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«Modelos de Lenguaje como Motores de Predicción Probabilística»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-01-fundamentos-llm-tokenizacion/notebook/clase-01-fundamentos-llm-tokenizacion.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    TXT["Texto: 'Inteligencia Artificial'"] --> BPE["Tokenizador BPE"]
    BPE --> TOK["Tokens: ['Intelig', 'encia', ' Artific', 'ial']"]
    TOK --> IDS["IDs Numéricos: [4521, 8934, 120]"]
    IDS --> LLM["Modelo LLM (Inferencia)"]

    style TXT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style BPE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TOK fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style LLM fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-01-fundamentos-llm-tokenizacion.pdf`](clase-01-fundamentos-llm-tokenizacion.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
