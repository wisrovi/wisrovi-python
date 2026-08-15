# 📘 Clase 08: Despliegue en la Nube, CI/CD y Portafolio Final

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 08)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Lanzamiento a Producción y Presentación de tu Proyecto ante el Mundo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-08-despliegue-cicd-portafolio/notebook/clase-08-despliegue-cicd-portafolio.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    GIT["git push origin main"] --> GHA["GitHub Actions CI/CD"]
    GHA --> TST["1. Ejecución de Tests Pytest"]
    TST --> BLD["2. Build & Verificación de Contenedores"]
    BLD --> DEPLOY["3. Despliegue Cloud & Portafolio de Graduación"]

    style GIT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style GHA fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
    style TST fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style BLD fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DEPLOY fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-08-despliegue-cicd-portafolio.pdf`](clase-08-despliegue-cicd-portafolio.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
