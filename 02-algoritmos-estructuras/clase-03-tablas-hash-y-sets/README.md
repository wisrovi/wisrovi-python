# 📘 Clase 03: Tablas Hash y Conjuntos (Sets) para Búsqueda O(1)

<div align="center">

**Curso 2: Algoritmos Avanzados y Estructuras de Datos** &bull; **Semana CLASE 03**  
*Nivel:* `Nivel 2 - Intermedio` &bull; *Metáfora Central:* **«Tablas Hash como un Fichero con Índice Alfabético Instantáneo»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-03-tablas-hash-y-sets/notebook/clase-03-tablas-hash-y-sets.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-03-tablas-hash-y-sets.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Tablas Hash como un Fichero con Índice Alfabético Instantáneo»* (Es como un conserje de hotel que sabe instantáneamente el casillero de cada huésped con solo mirar su apellido.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart LR
    IN["📥 1. Datos de Entrada<br/>(Tablas Hash como un Fichero co...)"] --> ENG["⚙️ 2. Motor de Procesamiento<br/>Tablas Hash y Conjuntos (Sets) para Búsqueda O(1)"]
    ENG --> OUT["🎯 3. Salida Verificada<br/>Estado en Memoria / Retorno"]

    style IN fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ENG fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-03-tablas-hash-y-sets/
├── 📄 clase-03-tablas-hash-y-sets.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-03-tablas-hash-y-sets.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Implementa una función que encuentre el primer carácter no repetido en una cadena en tiempo O(n).

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_02/test_clase_03_tablas_hash_y_sets.py
```
