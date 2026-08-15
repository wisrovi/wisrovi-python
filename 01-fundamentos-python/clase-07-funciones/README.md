# 📘 Clase 07: Funciones, Parámetros y Scope

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 07**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Funciones como Máquinas Reutilizables de una Fábrica»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-07-funciones/notebook/clase-07-funciones.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-07-funciones.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Funciones como Máquinas Reutilizables de una Fábrica»* (Una función es como un electrodoméstico: introduces ingredientes (argumentos) y recibes el resultado (return).).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart TD
    CALL["🚀 Invocación: calcular_total(precio=100, iva=0.21)"] --> STACK["🥞 Call Stack: Push Frame de Función"]
    STACK --> SCOPE{"🔍 Resolución de Ámbito LEGB"}
    SCOPE -->|1. Local| L["Variables locales dentro de la función"]
    SCOPE -->|2. Global| G["Constantes globales del módulo"]
    SCOPE -->|3. Built-in| B["Funciones estándar (len, print, range)"]
    L --> RET["🎯 return total_calculado"]
    RET --> POP_F["🥞 Pop Frame ➔ Retornar valor al llamador"]

    style CALL fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style STACK fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style SCOPE fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style RET fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style POP_F fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-07-funciones/
├── 📄 clase-07-funciones.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-07-funciones.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Escribe una función que reciba una lista de números y retorne el mínimo, el máximo y el promedio.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_07_funciones.py
```
