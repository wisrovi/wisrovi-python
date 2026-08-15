# 📘 Clase 07: Containerización Profesional con Docker y Compose

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 07)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Docker como Contenedores Estándar de Carga Marítima para Software»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-07-docker-y-compose/notebook/clase-07-docker-y-compose.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    subgraph Compose["🐳 docker-compose.yml"]
        API["Service: FastAPI (Backend :8000)"]
        UI["Service: Streamlit (Frontend :8501)"]
        DB[("Service: PostgreSQL (:5432)")]
        UI --> API
        API --> DB
    end

    style Compose fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style API fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style UI fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style DB fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-07-docker-y-compose.pdf`](clase-07-docker-y-compose.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
