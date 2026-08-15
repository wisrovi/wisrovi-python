# 📘 Clase 08: Proyecto Integrador: Sistema CLI Completo

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 08)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Construyendo tu Primera Aplicación Real de Consola»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-08-proyecto-integrador-basico/notebook/clase-08-proyecto-integrador-basico.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    CLI["🖥️ Interfaz de Terminal CLI"] --> MENU["📋 Menú Interactivo de 4 Opciones"]
    MENU --> READ["⌨️ Lectura con Validación try/except"]
    READ -->|1. Agregar| ADD["➕ TaskManager.agregar_tarea()"]
    READ -->|2. Listar| LST["📊 TaskManager.listar_tareas() en Tabla"]
    READ -->|3. Completar| CMP["✅ TaskManager.marcar_hecha()"]
    READ -->|4. Salir| EXT["👋 Cierre Seguro del Sistema"]
    ADD --> STATE[("💾 Estado de Tareas en Memoria")]
    LST --> STATE
    CMP --> STATE

    style CLI fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style MENU fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style READ fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style ADD fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style LST fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style CMP fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style EXT fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style STATE fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-08-proyecto-integrador-basico.pdf`](clase-08-proyecto-integrador-basico.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
