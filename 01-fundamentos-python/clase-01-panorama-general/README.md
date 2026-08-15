# 📘 Clase 01: Primer Vistazo Práctico (print, variables, if, for)

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 01)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-01-panorama-general/notebook/clase-01-panorama-general.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    P1["1. El Megáfono<br/>print('Hola Mundo')"] --> P2["2. Las Cajas Etiquetadas<br/>edad = 25 (Variables)"]
    P2 --> P3{"3. El Semáforo<br/>¿edad >= 18? (if/else)"}
    P3 -->|Verdadero| P4["4. La Cinta Transportadora<br/>for item in lista (Bucles)"]
    P3 -->|Falso| P4
    P4 --> P5["5. La Licuadora<br/>def funcion(entradas) -> salida"]

    style P1 fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style P2 fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style P3 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style P4 fill:#1e3a8a,color:#fff,stroke:#60a5fa,stroke-width:2px
    style P5 fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-01-panorama-general.pdf`](clase-01-panorama-general.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
