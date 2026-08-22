# 📘 Clase 02: Variables, Tipos de Datos y Funciones con Type Hints

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 02**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«Variables como Cajas Etiquetadas en Memoria y la Licuadora Tipada (PEP 484)»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-02-variables-y-tipos/notebook/clase-02-variables-y-tipos.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-02-variables-y-tipos.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«Variables como Cajas Etiquetadas en Memoria»* y cómo se transmiten referencias de objetos a funciones (`def`).
*   **Competencia Práctica:** Escribir, ejecutar y depurar funciones en Python aplicando *Type Hints* (PEP 484), *casting* explícito y formateo con f-strings.
*   **Competencia de Ingeniería:** Resolver el reto de la calculadora modular y verificar su correcto funcionamiento con la suite de pruebas automatizadas (`pytest`).

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart LR
    subgraph Memoria["🧠 Memoria Heap"]
        OBJ1["💵 total_cuenta = 100.0 (float)"]
        OBJ2["🏷️ porcentaje = 15.0 (float)"]
        RET["🎯 propina = 15.0 (float)"]
    end

    subgraph Funcion["🥤 Función 'calcular_propina' (PEP 484)"]
        INPUT["📥 Parámetros Tipados<br/>(total_cuenta: float, porcentaje: float)"]
        LOGIC["⚙️ Operación & Casting<br/>total_cuenta * (porcentaje / 100)"]
        OUT["📤 Retorno Tipado<br/>-> float"]
        INPUT --> LOGIC --> OUT
    end

    OBJ1 -.->|Pasa Referencia| INPUT
    OBJ2 -.->|Pasa Referencia| INPUT
    OUT -.->|Crea en Heap| RET

    style Memoria fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style Funcion fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OBJ1 fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style OBJ2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style RET fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-02-variables-y-tipos/
├── 📄 clase-02-variables-y-tipos.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-02-variables-y-tipos.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de 6 ejemplos modulares con funciones
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y funciones modulares a implementar
    ├── 🐍 ejercicio_02_perfil_usuario.py # Ejercicio guiado de perfil de usuario
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Construye una calculadora de propinas y facturación modular implementando `calcular_propina`, `calcular_total_por_persona` y `formatear_factura` con tipado PEP 484.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_02.py
```

