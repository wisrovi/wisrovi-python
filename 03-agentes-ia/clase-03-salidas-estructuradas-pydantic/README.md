# 📘 Clase 03: Salidas Estructuradas y Validación Tipada con Pydantic V2

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 03)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«Pydantic como la Aduana Estricta de Datos para Respuestas de IA»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-03-salidas-estructuradas-pydantic/notebook/clase-03-salidas-estructuradas-pydantic.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    RAW["Raw JSON del LLM"] --> PYD["Pydantic BaseModel Validation"]
    PYD -->|Inválido| ERR["ValidationError (Reintentar con Prompt)"]
    PYD -->|Válido| DTO["Objeto Python Tipado (DTO)"]
    DTO --> APP["Consumo Seguro en Backend"]

    style RAW fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style PYD fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ERR fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style DTO fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-03-salidas-estructuradas-pydantic.pdf`](clase-03-salidas-estructuradas-pydantic.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
