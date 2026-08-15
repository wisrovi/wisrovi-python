# 📘 Clase 08: Sistemas Multi-Agente, Supervisión y Guardrails

<div align="center">

**Curso 3: Creación y Desarrollo de Agentes de IA** &bull; **Semana CLASE 08**  
*Nivel:* `Nivel 3 - Avanzado` &bull; *Metáfora Central:* **«Una Empresa de Agentes Especializados Coordinados por un Director»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-08-sistemas-multi-agente/notebook/clase-08-sistemas-multi-agente.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-08-sistemas-multi-agente.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Una Empresa de Agentes Especializados Coordinados por un Director»* (Es como una agencia de noticias: el reportero investiga los hechos, el redactor escribe la noticia y el editor jefe revisa la calidad.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart LR
    IN["📥 1. Datos de Entrada<br/>(Una Empresa de Agentes Especia...)"] --> ENG["⚙️ 2. Motor de Procesamiento<br/>Sistemas Multi-Agente, Supervisión y Guardrails"]
    ENG --> OUT["🎯 3. Salida Verificada<br/>Estado en Memoria / Retorno"]

    style IN fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ENG fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-08-sistemas-multi-agente/
├── 📄 clase-08-sistemas-multi-agente.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-08-sistemas-multi-agente.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Diseña un sistema con un Agente Programador y un Agente Revisor de Código que valide pruebas unitarias.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_03/test_clase_08_sistemas_multi_agente.py
```
