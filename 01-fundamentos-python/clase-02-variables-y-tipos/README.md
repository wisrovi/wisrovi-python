# 📘 Clase 02: Variables, Tipos de Datos y Operadores

> **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 02)  
> **Nivel:** Nivel 1 - Principiante &bull; **Metáfora:** *«Variables como Cajas Etiquetadas en Memoria»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-02-variables-y-tipos/notebook/clase-02-variables-y-tipos.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    INPUT["📥 Entrada del Usuario<br/>'45.90' (str)"] --> CAST1["⚙️ float('45.90')<br/>Conversión Decimal"]
    CAST1 --> FLOAT_VAL["💵 45.90 (float)<br/>Número Flotante"]
    FLOAT_VAL --> CAST2["⚙️ int(45.90)<br/>Truncado a Entero"]
    CAST2 --> INT_VAL["🔢 45 (int)<br/>Número Entero"]
    INT_VAL --> MEM["🧠 Memoria Heap<br/>id(objeto) & Inmutabilidad"]

    style INPUT fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style CAST1 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style FLOAT_VAL fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style CAST2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style INT_VAL fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style MEM fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-02-variables-y-tipos.pdf`](clase-02-variables-y-tipos.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab con 1 clic.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
