# 📘 Clase 08: Sistemas Multi-Agente, Supervisión y Guardrails

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 08)  
> **Nivel:** Nivel 3 - Avanzado &bull; **Metáfora:** *«Una Empresa de Agentes Especializados Coordinados por un Director»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-08-sistemas-multi-agente/notebook/clase-08-sistemas-multi-agente.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    USER["Petición Compleja"] --> SUP["Agente Supervisor / Orquestador"]
    SUP -->|Delega Investigación| AG1["Agente Investigador (RAG / Web)"]
    AG1 -->|Retorna Datos| SUP
    SUP -->|Delega Redacción| AG2["Agente Redactor (Formateo Markdown)"]
    AG2 -->|Retorna Borrador| SUP
    SUP -->|Delega Validación| AG3["Agente Auditor (Guardrails & Calidad)"]
    AG3 -->|Aprobado| OUT["Respuesta Final Consolidada"]

    style USER fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style SUP fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style AG1 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style AG2 fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style AG3 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style OUT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-08-sistemas-multi-agente.pdf`](clase-08-sistemas-multi-agente.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
