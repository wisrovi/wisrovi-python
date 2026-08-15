# 📘 Clase 07: Grafos, Matrices de Adyacencia y Recorridos BFS/DFS

> **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 07)  
> **Nivel:** Nivel 2 - Intermedio  
> **Metáfora Central:** *«Grafos como Redes de Ciudades y Rutas de Vuelo»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-07-grafos-y-recorridos/notebook/clase-07-grafos-y-recorridos.ipynb)

---

## 🌀 Posición en el Aprendizaje en Espiral

Esta clase aborda los conceptos clave mediante el ciclo de 3 fases:

1. **💡 Modelo Mental:** Un grafo es un mapa de aeropuertos (nodos) conectados por vuelos (aristas).
2. **💻 Experimentación Guiada:** 4+ ejemplos estructurados para correr y depurar.
3. **🏋️ Desafío Práctico:** Reto de consolidación validado con tests.

```mermaid
flowchart LR
    M["💡 1. Modelo Mental<br/>«Grafos como Redes de Ciudades ...»"] --> E["💻 2. Ejemplos Prácticos<br/>4 carpetas ejecutables"]
    E --> R["🏋️ 3. Reto de Código<br/>ejercicios/reto.py"]
    R --> T["🧪 4. Validación<br/>tests/curso_02/"]

    style M fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style E fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style R fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style T fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🗺️ Arquitectura de la Sesión

```mermaid
flowchart LR
    A["🎬 Entrada / Contexto<br/>(Grafos como Redes de Ciudades y Rutas de Vuelo)"] --> B{"⚖️ Evaluación Lógica<br/>¿Condición / Regla?"}
    B -->|Rama Verdadera| C["⚙️ Transformación en Memoria<br/>Grafos, Matrices de Adyacencia y Recorridos BFS/DFS"]
    B -->|Rama Alternativa| D["🔀 Flujo Secundario<br/>Manejo de Caso"]
    C --> E["🎯 Salida / Retorno<br/>print() / Estado Actualizado"]
    D --> E

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style D fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
    style E fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Carpeta

*   📄 [`clase-07-grafos-y-recorridos.pdf`](clase-07-grafos-y-recorridos.pdf): Manual técnico oficial en PDF (9 páginas de estudio).
*   📖 [`book.md`](book.md): Libro de estudio digital completo con diagramas Mermaid nativos.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 4 carpetas con código fuente funcional y comentado.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
