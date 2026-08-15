# 📘 Clase 03: Control de Flujo: Condicionales (if / elif / else)

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 03**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Condicionales como Semáforos y Bifurcaciones en un Tren»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-03-control-flujo-condicionales/notebook/clase-03-control-flujo-condicionales.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-03-control-flujo-condicionales.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Condicionales como Semáforos y Bifurcaciones en un Tren»* (Un condicional es como una aguja ferroviaria que desvía el tren según el color del semáforo.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart TD
    COND["⚖️ Evaluación de Expresión Booleana"] --> IF{"¿Condición Principal<br/>if edad >= 18?"}
    IF -->|True (Verdadero)| B1["🟢 Semáforo Verde<br/>Acceso Autorizado al Sistema"]
    IF -->|False (Falso)| ELIF{"¿Condición Secundaria<br/>elif tiene_permiso?"}
    ELIF -->|True (Verdadero)| B2["🟡 Semáforo Amarillo<br/>Acceso con Supervisión"]
    ELIF -->|False (Falso)| ELSE["🔴 Semáforo Rojo<br/>Acceso Denegado por Defecto"]

    style COND fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style IF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B1 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B2 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style ELSE fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-03-control-flujo-condicionales/
├── 📄 clase-03-control-flujo-condicionales.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-03-control-flujo-condicionales.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Diseña un clasificador de acceso por edad y membresía VIP.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_03_control_flujo_condicionales.py
```
