# 🐍 Programa Integral de Formación en Python: De Cero a Agentes de IA

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisrovi/wisrovi-python)
[![CI / Tests](https://github.com/wisrovi/wisrovi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/wisrovi/wisrovi-python/actions/workflows/ci.yml)
[![Web Documentation](https://img.shields.io/badge/Docs-academy__python.wisrovi.dev-6366f1.svg?logo=materialformkdocs&logoColor=white)](https://academy_python.wisrovi.dev/)
[![Test Suite](https://img.shields.io/badge/Pytest-34%20Passing%20100%25-brightgreen.svg?logo=pytest&logoColor=white)](tests/)
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)

**Un ecosistema académico y profesional diseñado para transformar a estudiantes sin experiencia previa en ingenieros capaces de concebir, programar y desplegar aplicaciones reales y Agentes de Inteligencia Artificial.**

[🌐 Explorar Portal Web Interactivo](https://academy_python.wisrovi.dev/) &bull; [🚀 Abrir en Codespaces con 1 Clic](https://codespaces.new/wisrovi/wisrovi-python) &bull; [📚 Ver Cursos](#-la-ruta-maestra-de-formación-4-cursos--32-semanas)

</div>

---

## 👤 Acerca del Autor y Mentor

### **William Rodríguez (Wisrovi)**
*AI Solutions Architect & Principal Software Engineer &bull; Badajoz, España*

Ingeniero y arquitecto de software especializado en **Inteligencia Artificial Generativa**, sistemas multi-agente, Visión por Computador e infraestructuras MLOps de alta disponibilidad. Diseñador del currículo integral y mantenedor del ecosistema de software libre **wisrovi SUITE** en PyPI con más de 26 bibliotecas enfocadas en orquestación de flujos de datos, bases de datos y algoritmos de alto rendimiento.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-wisrovi-181717?logo=github&logoColor=white)](https://github.com/wisrovi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wisrovi%20Rodríguez-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wisrovi-rodriguez/)
[![PyPI](https://img.shields.io/badge/PyPI-26%2B%20Packages-3775A9?logo=pypi&logoColor=white)](https://pypi.org/user/wisrovi/)
[![DockerHub](https://img.shields.io/badge/DockerHub-wisrovi-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/u/wisrovi)
[![Website](https://img.shields.io/badge/Website-wisrovi.dev-000000?logo=google-chrome&logoColor=white)](https://wisrovi.dev)

</div>

---

## 🌀 Modelo Pedagógico: Aprendizaje en Espiral *(Spiral Learning)*

El diseño curricular de este programa no enseña conceptos de forma aislada ni se apoya en la memorización de sintaxis abstracta. En su lugar, implementa el **Aprendizaje en Espiral**, un modelo pedagógico donde el conocimiento se adquiere a través de iteraciones progresivas de complejidad y profundidad técnica:

```mermaid
flowchart TD
    subgraph Espiral["🌀 Ciclo de Aprendizaje en Espiral (32 Semanas)"]
        F1["🎯 Fase 1: Visión Holística & Gancho Temprano (Semana 1)<br/>El alumno experimenta los 4 pilares en conjunto (print, variables, if, for)<br/>Comprende de inmediato para qué sirve el software."]
        F2["🔍 Fase 2: Profundización & Rigor de Ingeniería (Semanas 2 a 24)<br/>Estructuras en memoria, tipos inmutables, Big-O, grafos, LLMs, Tool Calling y RAG.<br/>Análisis de complejidad, gotchas y prevención de errores."]
        F3["🛠️ Fase 3: Síntesis & Creación de Producto (Semanas 25 a 32)<br/>Integración Full-Stack: FastAPI + Streamlit + SQLite ACID + Agente IA.<br/>Testing automatizado, Dockerización y despliegue CI/CD."]
        F1 ==> F2
        F2 ==> F3
    end

    style Espiral fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#ffffff
    style F1 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
    style F2 fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#ffffff
    style F3 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ffffff
```

### 🚲 La Regla de la Bicicleta *(Pedaleo Activo en Código)*
> *"Por más conferencias que escuches o libros que leas sobre cómo guardar el equilibrio, si no te subes a la bicicleta y pedaleas por ti mismo, jamás aprenderás a montar."*

Cada clase está concebida para la acción inmediata:
1. **Modelos Mentales:** Metáforas físicas del mundo real (El Megáfono, Las Cajas, El Semáforo, La Licuadora).
2. **Ejemplos Vivos:** Al menos 4 carpetas con scripts ejecutables y comentados por clase.
3. **Autoevaluación:** Pruebas unitarias automatizadas (`pytest`) que validan la solución del alumno en milisegundos.

---

## 🚀 La Ruta Maestra de Formación (4 Cursos &bull; 32 Semanas)

```mermaid
flowchart LR
    C1["🎯 Curso 1: Fundamentos<br/>(8 Semanas &bull; 0 a 100)"] --> C2["⚡ Curso 2: Algoritmos<br/>(8 Semanas &bull; Big-O & Data)"]
    C2 --> C3["🤖 Curso 3: Agentes IA<br/>(8 Semanas &bull; LLM & RAG)"]
    C3 --> C4["🛠️ Curso 4: Proyecto Final<br/>(8 Semanas &bull; Full-Stack & Deploy)"]

    style C1 fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style C2 fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
    style C3 fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style C4 fill:#9a3412,color:#ffffff,stroke:#fb923c,stroke-width:2px
```

---

## 📚 Mapa Detallado del Programa Académico

| Curso | Enfoque Principal | Manual PDF Oficial | Libro Digital | Cuadernos | Hito de Graduación |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | [**Fundamentos Básicos de Python**](01-fundamentos-python/)<br/>8 Clases &bull; 33 Ejemplos | [📄 PDF Completo](01-fundamentos-python/curso-01-fundamentos-python.pdf) | [📖 book.md](01-fundamentos-python/book.md) | 8 Notebooks (Colab) | Construcción de una aplicación interactiva CLI con validación robusta y control de excepciones. |
| **2** | [**Algoritmos y Estructuras de Datos**](02-algoritmos-estructuras/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](02-algoritmos-estructuras/curso-02-algoritmos-estructuras.pdf) | [📖 book.md](02-algoritmos-estructuras/book.md) | 8 Notebooks (Colab) | Dominio de complejidad Big-O, pilas, colas, BST, grafos y recursión dinámica con `@lru_cache`. |
| **3** | [**Desarrollo de Agentes de IA**](03-agentes-ia/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](03-agentes-ia/curso-03-agentes-ia.pdf) | [📖 book.md](03-agentes-ia/book.md) | 8 Notebooks (Colab) | Creación de pipelines RAG, Tool Calling con Pydantic, embeddings vectoriales y ciclo ReAct. |
| **4** | [**Proyecto Integrador & Taller Full-Stack**](04-proyecto-final/)<br/>8 Clases &bull; 32 Ejemplos | [📄 PDF Completo](04-proyecto-final/curso-04-proyecto-final.pdf) | [📖 book.md](04-proyecto-final/book.md) | 8 Notebooks (Colab) | Aplicación Web en producción (FastAPI + Streamlit + SQLite ACID + Docker Compose + CI/CD). |

---

## ⚡ Inicio Rápido (Quickstart)

### Opción A: Programar en la Nube con 1 Clic (Sin Instalaciones)
Haz clic en el siguiente botón para desplegar tu entorno completo de Visual Studio Code en la nube con Python, extensiones y dependencias preconfiguradas:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisrovi/wisrovi-python)

### Opción B: Configuración en tu Máquina Local
```bash
# 1. Clonar el repositorio
git clone https://github.com/wisrovi/wisrovi-python.git
cd wisrovi-python

# 2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar paquetes y herramientas en modo editable
pip install -e ".[all]"

# 4. Validar el entorno ejecutando la suite completa de pruebas
pytest
```

---

## 🧪 Verificación Automatizada de Calidad (Pytest)

Toda la infraestructura de pruebas está centralizada en la carpeta [`/tests`](tests/) para mantener el código de los alumnos limpio y libre de archivos secundarios:

```bash
# Ejecutar todas las pruebas del repositorio (34 tests en < 0.3s)
pytest

# Ejecutar pruebas por módulo específico
pytest tests/curso_01/
pytest tests/curso_02/
pytest tests/curso_03/
pytest tests/curso_04/

# O utilizar la herramienta CLI oficial
wisrovi test 1
```

---

## 🗺️ Estructura del Repositorio

```text
wisrovi-python/
├── 📁 .devcontainer/                   # 💻 Entorno reproducible para Codespaces y contenedores
├── 📁 .github/                         # ⚙️ Workflows CI/CD, issue templates y automatizaciones
├── 📁 01-fundamentos-python/           # 🎯 Curso 1: Fundamentos (8 Clases con PDF, libro, notebook y ejemplos)
├── 📁 02-algoritmos-estructuras/       # ⚡ Curso 2: Algoritmos & Estructuras (8 Clases)
├── 📁 03-agentes-ia/                   # 🤖 Curso 3: Agentes de Inteligencia Artificial (8 Clases)
├── 📁 04-proyecto-final/               # 🛠️ Curso 4: Proyecto Integrador Full-Stack (8 Clases)
├── 📁 docs/                            # 🌐 Portal web oficial (academy_python.wisrovi.dev)
├── 📁 scripts/                         # 🔧 Herramientas internas de compilación y mantenimiento
├── 📁 src/                             # 📦 Código fuente de la CLI oficial wisrovi
├── 📁 tests/                           # 🧪 Suites de pruebas unitarias centralizadas
├── 📄 mkdocs.yml                       # 📑 Configuración del portal web documental
├── 📄 pyproject.toml                   # 📦 Especificación estándar de dependencias Python
└── 📄 README.md                        # 📌 Portal principal de navegación
```

---

## 📜 Licencia y Comunidad

Este proyecto se publica bajo los términos de la **Licencia MIT**. Puedes usarlo, estudiarlo, compartirlo y adaptarlo con total libertad tanto para fines académicos como comerciales.

Si este programa de formación aporta valor a tu carrera profesional, **te invitamos a dejar una ⭐️ en GitHub** para apoyar el desarrollo de software libre en español.
