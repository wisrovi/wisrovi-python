# 📘 Clase 06: Diccionarios y Conjuntos (Sets)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 06)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Diccionarios como un Casillero con Llaves Únicas»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-06-diccionarios/notebook/clase-06-diccionarios.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    KEY["🔑 Clave: 'usuario'"] --> HASH["⚡ Función Hash O(1)"]
    HASH --> BUCKET["📦 Posición en Memoria"]
    BUCKET --> VAL["🎯 Valor: 'wisrovi'"]
    BUCKET --> GET["🛡️ .get(clave, default)<br/>Búsqueda segura sin KeyError"]
    BUCKET --> SET["✨ set() Conjuntos<br/>Deduplicación & Operaciones & / | / -"]

    style KEY fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style HASH fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BUCKET fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style VAL fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style GET fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style SET fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-06-diccionarios.pdf`](clase-06-diccionarios.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
