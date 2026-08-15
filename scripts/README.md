# 🛠️ Herramientas de Compilación y Mantenimiento del Repositorio

> **Ubicación:** `scripts/`  
> **Uso:** Exclusivo para administradores y compilación automatizada (CI/CD).  
> **Audiencia:** Los estudiantes no necesitan ejecutar estos scripts para su formación.

---

## 🗺️ Arquitectura del Sistema de Compilación

```mermaid
flowchart TD
    META["📋 all_32_classes_metadata.py<br/>(Metadatos Canónicos de las 32 Clases)"] --> BUILD["⚙️ build_master_course_system.py<br/>(Compilador Maestro de PDFs y Libros)"]
    BUILD --> PDFS["📄 32 PDFs de Clases + 4 PDFs Globales<br/>(Compilados con Chrome Headless & CSS LaTeX)"]
    BUILD --> BOOKS["📖 32 Libros book.md + 4 Libros Globales<br/>(Diagramas Mermaid nativos)"]
    BUILD --> DOCS["🌐 docs/ (Plataforma Web MkDocs)<br/>academy_python.wisrovi.dev"]
    BUILD --> NBS["📓 Cuadernos Jupyter (.ipynb)<br/>(Organizados en /notebook/ con Google Colab)"]

    style META fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style BUILD fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PDFS fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style BOOKS fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style DOCS fill:#b45309,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style NBS fill:#065f46,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Catálogo de Scripts de Utilidad

| Script | Descripción del Proceso |
| :--- | :--- |
| **`all_32_classes_metadata.py`** | Diccionario central con la teoría, código, modelos mentales y retos de las 32 clases. |
| **`build_master_course_system.py`** | Compilador integral de PDFs, `book.md`, `.ipynb`, `docs/` y `mkdocs.yml`. |
| **`generate_all_class_examples.py`** | Generador de las 128+ subcarpetas de ejemplos estructurados con `main.py` y `README.md`. |
| **`centralize_tests_in_root.py`** | Centraliza todas las suites de Pytest en la carpeta `/tests/`. |
| **`refine_all_mermaid_styles.py`** | Aplica el estándar de estilo visual moderno a todos los diagramas Mermaid del repositorio. |
| **`ensure_all_readmes.py`** | Auditoría y verificación de que cada directorio cuente con su archivo `README.md`. |
