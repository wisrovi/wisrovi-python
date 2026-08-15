# 📘 Clase 01: Arquitectura de Software y Planificación del Proyecto

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 01)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Diseñar los Planos de un Edificio Antes de Poner el Primer Ladrillo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-01-arquitectura-y-planificacion/notebook/clase-01-arquitectura-y-planificacion.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    CONF["BaseSettings / Variables de Entorno"] --> DTO["Modelos DTO (Contratos de Entrada/Salida)"]
    DTO --> DOM["Entidades de Dominio"]
    DOM --> REPO["Patrón Repositorio (Acceso a Datos)"]
    REPO --> DB[("Persistencia SQLite / PostgreSQL")]

    style CONF fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style DTO fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DOM fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style REPO fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DB fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-01-arquitectura-y-planificacion.pdf`](clase-01-arquitectura-y-planificacion.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
