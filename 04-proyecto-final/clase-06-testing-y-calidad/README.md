# 📘 Clase 06: Testing Riguroso con Pytest, Mocks y Calidad

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 06)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Los Tests como el Control de Calidad y Pruebas de Choque de un Vehículo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-06-testing-y-calidad/notebook/clase-06-testing-y-calidad.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    PYT["Pytest Runner"] --> FIX["Fixtures: Base de Datos en Memoria"]
    FIX --> MCK["unittest.mock: Simulación de APIs Externas"]
    MCK --> TCLI["TestClient: Verificación de Endpoints FastAPI"]
    TCLI --> REP["Reporte de Cobertura y Aserciones"]

    style PYT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FIX fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style MCK fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TCLI fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style REP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-06-testing-y-calidad.pdf`](clase-06-testing-y-calidad.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
