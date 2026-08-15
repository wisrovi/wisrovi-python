# 📘 Clase 07: Agentes Autónomos y el Ciclo Cognitivo ReAct

> **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 07)  
> **Nivel:** Nivel 3 - Avanzado  
> **Metáfora Central:** *«El Agente como un Detective que Piensa, Actúa y Observa hasta Resolver el Caso»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-07-agentes-autonomos-react/notebook/clase-07-agentes-autonomos-react.ipynb)

---

## 🌀 Posición en el Aprendizaje en Espiral

Esta clase aborda los conceptos clave mediante el ciclo de 3 fases:

1. **💡 Modelo Mental:** Un agente es como un detective: piensa qué pista necesita (Thought), busca el dato con una herramienta (Action), analiza el resultado (Observation) y repite.
2. **💻 Experimentación Guiada:** 4+ ejemplos estructurados para correr y depurar.
3. **🏋️ Desafío Práctico:** Reto de consolidación validado con tests.

```mermaid
flowchart LR
    M["💡 1. Modelo Mental<br/>«El Agente como un Detective qu...»"] --> E["💻 2. Ejemplos Prácticos<br/>4 carpetas ejecutables"]
    E --> R["🏋️ 3. Reto de Código<br/>ejercicios/reto.py"]
    R --> T["🧪 4. Validación<br/>tests/curso_03/"]

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
        ENG["Motor de Ejecución (Agentes Autónomos y el Ciclo Cognitivo ReAct)"]
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

*   📄 [`clase-07-agentes-autonomos-react.pdf`](clase-07-agentes-autonomos-react.pdf): Manual técnico oficial en PDF (9 páginas de estudio).
*   📖 [`book.md`](book.md): Libro de estudio digital completo con diagramas Mermaid nativos.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 4 carpetas con código fuente funcional y comentado.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
