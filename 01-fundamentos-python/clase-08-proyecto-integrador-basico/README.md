# 📘 Clase 08: Proyecto Integrador: Sistema CLI Completo

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 08)  
> **Nivel:** Nivel 1 - Principiante  
> **Metáfora Central:** *«Construyendo tu Primera Aplicación Real de Consola»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-08-proyecto-integrador-basico/notebook/clase-08-proyecto-integrador-basico.ipynb)

---

## 🌀 Posición en el Aprendizaje en Espiral

Esta clase aborda los conceptos clave mediante el ciclo de 3 fases:

1. **💡 Modelo Mental:** Construir tu primera aplicación es como armar tu propia bicicleta: cada pieza encaja para ponerla en marcha.
2. **💻 Experimentación Guiada:** 4+ ejemplos estructurados para correr y depurar.
3. **🏋️ Desafío Práctico:** Reto de consolidación validado con tests.

```mermaid
flowchart LR
    M["💡 1. Modelo Mental<br/>«Construyendo tu Primera Aplica...»"] --> E["💻 2. Ejemplos Prácticos<br/>4 carpetas ejecutables"]
    E --> R["🏋️ 3. Reto de Código<br/>ejercicios/reto.py"]
    R --> T["🧪 4. Validación<br/>tests/curso_01/"]

    style M fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style E fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style R fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style T fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🗺️ Arquitectura de la Sesión

```mermaid
flowchart LR
    subgraph Entrada["📥 Capa de Entrada"]
        REQ["Petición / Prompt / Input"]
        VAL["Validación DTO & Tipos"]
    end

    subgraph Core["🧠 Núcleo del Sistema"]
        ENG["Motor de Ejecución (Sistema CLI Completo)"]
        MEM["Estado / Memoria en Heap"]
    end

    subgraph Salida["💾 Persistencia & Respuesta"]
        DB[("Base de Datos / Vector Store")]
        RES["Respuesta Estructurada JSON / UI"]
    end

    REQ --> VAL
    VAL --> ENG
    ENG <--> MEM
    ENG <--> DB
    ENG --> RES

    style Entrada fill:#f8fafc,stroke:#3b82f6,stroke-width:2px
    style Core fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px
    style Salida fill:#f0fdf4,stroke:#10b981,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Carpeta

*   📄 [`clase-08-proyecto-integrador-basico.pdf`](clase-08-proyecto-integrador-basico.pdf): Manual técnico oficial en PDF (9 páginas de estudio).
*   📖 [`book.md`](book.md): Libro de estudio digital completo con diagramas Mermaid nativos.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 4 carpetas con código fuente funcional y comentado.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
