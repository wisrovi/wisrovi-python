# 📘 Clase 08: Proyecto Integrador: Sistema CLI Completo

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 08)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Construyendo tu Primera Aplicación Real de Consola»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-08-proyecto-integrador-basico/notebook/clase-08-proyecto-integrador-basico.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    CLI["Bucle Principal CLI"] --> MENU["Mostrar Opciones de Menú"]
    MENU --> IN["Lectura de Opción con try/except"]
    IN -->|1. Agregar| TM_ADD["TaskManager.agregar_tarea()"]
    IN -->|2. Listar| TM_LST["TaskManager.listar_tareas()"]
    IN -->|3. Salir| TM_EXT["Cierre Seguro del Programa"]
    TM_ADD --> STATE[("Estado en Memoria")]
    TM_LST --> STATE

    style CLI fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MENU fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style IN fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style TM_ADD fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style TM_LST fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style STATE fill:#4c1d95,color:#fff,stroke:#a78bfa,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-08-proyecto-integrador-basico.pdf`](clase-08-proyecto-integrador-basico.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
