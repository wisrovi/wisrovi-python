# 📘 Clase 04: Control de Flujo: Bucles (for / while)

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 04**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Bucles como una Cinta Transportadora de Fábrica»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-04-control-flujo-bucles/notebook/clase-04-control-flujo-bucles.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-04-control-flujo-bucles.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Bucles como una Cinta Transportadora de Fábrica»* (El bucle 'for' es como una cinta transportadora donde inspeccionas cada paquete uno a uno hasta terminar.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart TD
    SEQ["📦 Secuencia o Rango<br/>range(1, 10) o lista"] --> ITER["🔄 Iterador del Bucle (for / while)"]
    ITER --> BODY["⚡ Ejecutar Bloque del Bucle"]
    BODY --> CTRL{"¿Instrucción Especial?"}
    CTRL -->|continue| ITER
    CTRL -->|break| EXIT["🛑 Salida Inmediata del Ciclo"]
    CTRL -->|Flujo Normal| NEXT{"¿Fin de Secuencia?"}
    NEXT -->|No| ITER
    NEXT -->|Sí| EXIT

    style SEQ fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style NEXT fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
    style EXIT fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-04-control-flujo-bucles/
├── 📄 clase-04-control-flujo-bucles.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-04-control-flujo-bucles.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Escribe un programa que imprima la tabla de multiplicar de un número del 1 al 10.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_04_control_flujo_bucles.py
```
