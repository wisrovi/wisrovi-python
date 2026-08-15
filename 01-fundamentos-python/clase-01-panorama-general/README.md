# 📘 Clase 01: Primer Vistazo Práctico (print, variables, if, for)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 01)  
> **Nivel:** Nivel 1 - Principiante  
> **Metáfora Central:** *«El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-01-panorama-general/notebook/clase-01-panorama-general.ipynb)

---

## 🌀 Posición en el Aprendizaje en Espiral

Esta clase aborda los conceptos clave mediante el ciclo de 3 fases:

1. **💡 Modelo Mental:** Aprender a programar es como dominar 4 herramientas esenciales: el Megáfono (print) anuncia resultados, las Cajas (variables) guardan datos, el Semáforo (if) decide qué camino tomar y la Cinta Transportadora (for) procesa elementos uno tras otro.
2. **💻 Experimentación Guiada:** 4+ ejemplos estructurados para correr y depurar.
3. **🏋️ Desafío Práctico:** Reto de consolidación validado con tests.

```mermaid
flowchart LR
    M["💡 1. Modelo Mental<br/>«El Megáfono (print), Las Cajas...»"] --> E["💻 2. Ejemplos Prácticos<br/>4 carpetas ejecutables"]
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
    A["🎬 Entrada / Contexto<br/>(El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for))"] --> B{"⚖️ Evaluación Lógica<br/>¿Condición / Regla?"}
    B -->|Rama Verdadera| C["⚙️ Transformación en Memoria<br/>Primer Vistazo Práctico (print, variables, if, for)"]
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

*   📄 [`clase-01-panorama-general.pdf`](clase-01-panorama-general.pdf): Manual técnico oficial en PDF (9 páginas de estudio).
*   📖 [`book.md`](book.md): Libro de estudio digital completo con diagramas Mermaid nativos.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): 4 carpetas con código fuente funcional y comentado.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
