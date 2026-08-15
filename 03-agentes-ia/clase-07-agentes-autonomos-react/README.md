# 📘 Clase 07: Agentes Autónomos y el Ciclo Cognitivo ReAct

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 07)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«El Agente como un Detective que Piensa, Actúa y Observa hasta Resolver el Caso»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-07-agentes-autonomos-react/notebook/clase-07-agentes-autonomos-react.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    START["Inicio de Tarea"] --> THOUGHT["1. Thought: Razonamiento del siguiente paso"]
    THOUGHT --> ACT{"¿Requiere Acción?"}
    ACT -->|Sí| ACTION["2. Action: Ejecutar Tool (buscar / calcular)"]
    ACTION --> OBS["3. Observation: Resultado obtenido"]
    OBS --> THOUGHT
    ACT -->|No| FINAL["🎯 Final Answer: Entregar respuesta al usuario"]

    style START fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style THOUGHT fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style ACTION fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style OBS fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style FINAL fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-07-agentes-autonomos-react.pdf`](clase-07-agentes-autonomos-react.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
