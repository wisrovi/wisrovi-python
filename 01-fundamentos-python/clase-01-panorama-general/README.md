# 📘 Clase 01: Primer Vistazo Práctico (print, variables, if, for)

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 01**  
*Nivel:* `Nivel 1 - Principiante` &bull; *Metáfora Central:* **«El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)»**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-01-panorama-general/notebook/clase-01-panorama-general.ipynb)
[![PDF Oficial](https://img.shields.io/badge/Manual-PDF%209%20Páginas-red.svg?logo=adobeacrobatreader&logoColor=white)](clase-01-panorama-general.pdf)
[![Libro Digital](https://img.shields.io/badge/Libro-book.md-blue.svg?logo=markdown&logoColor=white)](book.md)

</div>

---

## 🎯 Objetivos de Aprendizaje de la Sesión

*   **Competencia Conceptual:** Comprender el modelo mental de *«El Megáfono (print), Las Cajas (variables), El Semáforo (if) y La Cinta Transportadora (for)»* (Aprender a programar es como dominar 4 herramientas esenciales: el Megáfono (print) anuncia resultados, las Cajas (variables) guardan datos, el Semáforo (if) decide qué camino tomar y la Cinta Transportadora (for) procesa elementos uno tras otro.).
*   **Competencia Práctica:** Escribir, ejecutar y depurar scripts en Python aplicando buenas prácticas (PEP 8) y tipado.
*   **Competencia de Ingeniería:** Resolver el reto práctico de la sesión y verificar su correcto funcionamiento con la suite de pruebas automatizadas.

---

## 🗺️ Mapa de Arquitectura y Flujo de Ejecución

```mermaid
flowchart TD
    COMP["💻 Computadora (Tu Asistente)"] --> P0["📢 print() ➔ El Megáfono<br/>Muestra mensajes y resultados en pantalla"]
    COMP --> P1["📦 Variables ➔ Cajas de Mudanza<br/>Guardan valores en memoria con '='"]
    COMP --> P2["🚦 if / else ➔ El Semáforo de Decisiones<br/>Evalúa condiciones lógicas (True / False)"]
    COMP --> P3["🔄 for ➔ La Cinta Transportadora<br/>Procesa colecciones elemento a elemento"]
    COMP --> P4["⚙️ def ➔ La Licuadora<br/>Recibe ingredientes (entradas) y retorna el jugo (salida)"]

    style COMP fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style P0 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style P1 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style P2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style P3 fill:#7c3aed,color:#ffffff,stroke:#a78bfa,stroke-width:2px
    style P4 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📂 Organización de Materiales en esta Clase

```text
clase-01-panorama-general/
├── 📄 clase-01-panorama-general.pdf       # Manual técnico oficial de estudio (9 páginas)
├── 📖 book.md                     # Libro digital interactivo con diagramas Mermaid
├── 📝 README.md                   # Esta guía general de la clase
├── 📁 notebook/                   # Cuaderno Jupyter interactivo
│   ├── 📓 clase-01-panorama-general.ipynb
│   └── 📝 README.md               # Guía con badge a Google Colab
├── 📁 ejemplos/                   # Carpetas de código estructurado paso a paso
│   └── 📝 README.md               # Catálogo de ejemplos con comandos de ejecución
└── 📁 ejercicios/                 # Reto práctico para el estudiante
    ├── 🐍 reto.py                 # Enunciado y plantilla del ejercicio
    └── 📝 README.md               # Instrucciones de resolución y comandos pytest
```

---

## 🏋️ Desafío Práctico de la Sesión
> **Enunciado:** Crea un script que defina una lista de 3 alumnos con sus notas, use un for para recorrerlos y un if/else para imprimir si cada uno aprobó (nota >= 60) o reprobó.

Abre el archivo [`ejercicios/reto.py`](ejercicios/reto.py), completa tu implementación y valida tu código ejecutando:
```bash
pytest tests/curso_01/test_clase_01_panorama_general.py
```
