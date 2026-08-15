# 📘 Clase 05: Integración del Motor de IA y Agentes en la App

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 05)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Conectar el Cerebro del Agente al Sistema Nervioso de la Aplicación»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-05-integracion-agente-ia/notebook/clase-05-integracion-agente-ia.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    INP["st.chat_input"] --> POST["POST /api/chat"]
    POST --> STREAM["Generador Streaming de Tokens (yield)"]
    STREAM --> CHAT_UI["st.chat_message (Efecto Escritura en Tiempo Real)"]

    style INP fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style POST fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style STREAM fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style CHAT_UI fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-05-integracion-agente-ia.pdf`](clase-05-integracion-agente-ia.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
