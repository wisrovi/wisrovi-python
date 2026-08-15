# 📘 Clase 08: Proyecto Integrador: Sistema CLI Completo

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 08**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Construyendo tu Primera Aplicación Real de Consola»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-08-proyecto-integrador-basico/notebook/clase-08-proyecto-integrador-basico.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-08-proyecto-integrador-basico.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Construyendo tu Primera Aplicación Real de Consola»* (Construir tu primera aplicación es como armar tu propia bicicleta: cada pieza encaja para ponerla en marcha.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart TD
    CLI["🖥️ Interfaz de Terminal CLI"] --> MENU["📋 Menú Interactivo de 4 Opciones"]
    MENU --> READ["⌨️ Lectura con Validación try/except"]
    READ -->|1. Agregar| ADD["➕ TaskManager.agregar_tarea()"]
    READ -->|2. Listar| LST["📊 TaskManager.listar_tareas() en Tabla"]
    READ -->|3. Completar| CMP["✅ TaskManager.marcar_hecha()"]
    READ -->|4. Salir| EXT["👋 Cierre Seguro del Sistema"]
    ADD --> STATE[("💾 Estado de Tareas en Memoria")]
    LST --> STATE
    CMP --> STATE

    style CLI fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style MENU fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style READ fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style ADD fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style LST fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style CMP fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style EXT fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style STATE fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-08-proyecto-integrador-basico/
├── 📄 clase-08-proyecto-integrador-basico.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-08-proyecto-integrador-basico.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Amplía el TaskManager para permitir marcar tareas como completadas y eliminarlas por ID.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_08_proyecto_integrador_basico.py
```
