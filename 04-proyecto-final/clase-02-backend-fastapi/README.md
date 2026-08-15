# 📘 Clase 02: Desarrollo del Backend: APIs RESTful con FastAPI

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 02)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«FastAPI como un Centro Logístico de Alta Velocidad para Peticiones HTTP»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-02-backend-fastapi/notebook/clase-02-backend-fastapi.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    REQ["HTTP Request (JSON)"] --> ROUTE["FastAPI Router"]
    ROUTE --> DEP["Depends() Inyección de Dependencias"]
    DEP --> VAL["Validación Pydantic"]
    VAL --> SERV["Capa de Servicio"]
    SERV --> RES["HTTP 200 OK + Swagger UI /docs"]

    style REQ fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style ROUTE fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DEP fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style SERV fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style RES fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-02-backend-fastapi.pdf`](clase-02-backend-fastapi.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
