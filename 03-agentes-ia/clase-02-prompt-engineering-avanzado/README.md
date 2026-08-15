# 📘 Clase 02: Prompt Engineering Avanzado y Few-Shot Learning

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 02)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«Prompts como Especificaciones Precisas para un Consultor Experto»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-02-prompt-engineering-avanzado/notebook/clase-02-prompt-engineering-avanzado.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    SYS["System Prompt (Rol y Restricciones)"] --> CTX["Few-Shot Examples (Pares In-Context)"]
    CTX --> COT["Chain of Thought ('Pensemos paso a paso')"]
    COT --> USR["User Prompt"]
    USR --> LLM["LLM ➔ Respuesta Precisa y Sin Alucinaciones"]

    style SYS fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style CTX fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style COT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style LLM fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-02-prompt-engineering-avanzado.pdf`](clase-02-prompt-engineering-avanzado.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
