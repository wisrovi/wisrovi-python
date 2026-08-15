# 📘 Clase 06: Diccionarios y Conjuntos (Sets)

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 06**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Diccionarios como un Casillero con Llaves Únicas»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-06-diccionarios/notebook/clase-06-diccionarios.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-06-diccionarios.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Diccionarios como un Casillero con Llaves Únicas»* (Un diccionario es como un casillero: con tu llave (clave) abres instantáneamente el compartimento (valor).).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart LR
    KEY["🔑 Clave: 'usuario'"] --> HASH["⚡ Función Hash O(1)"]
    HASH --> BUCKET["📦 Posición en Memoria"]
    BUCKET --> VAL["🎯 Valor: 'wisrovi'"]
    BUCKET --> GET["🛡️ .get(clave, default)<br/>Búsqueda segura sin KeyError"]
    BUCKET --> SET["✨ set() Conjuntos<br/>Deduplicación & Operaciones & / | / -"]

    style KEY fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style HASH fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BUCKET fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style VAL fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style GET fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style SET fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-06-diccionarios/
├── 📄 clase-06-diccionarios.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-06-diccionarios.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Crea una función que reciba un texto y cuente la frecuencia de cada palabra con un diccionario.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_06_diccionarios.py
```
