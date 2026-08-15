---
name: wisrovi-course-standards
description: >-
  Estándar oficial de diseño instruccional, compilación de libros digitales,
  generación de PDFs estilo LaTeX con Chrome Headless, documentación MkDocs Material
  y arquitectura limpia de repositorios educativos para proyectos de William Rodríguez (Wisrovi).
---

# Wisrovi Course & Documentation Standards

Esta skill contiene los estándares, plantillas y procedimientos canónicos para crear, mantener y compilar repositorios educativos y de ingeniería de software para el ecosistema **wisrovi**.

---

## 1. Reglas Invariables de Arquitectura

1. **Raíz 100% Limpia:** Cero scripts `.py` de soporte en la raíz del repositorio. Todo script de mantenimiento, compilación o scaffolding debe ubicarse en `scripts/` con su respectivo `scripts/README.md`.
2. **Cobertura Universal de READMEs:** Toda carpeta existente (incluyendo subcarpetas de ejemplos y retos) debe tener un `README.md` explicativo, contextual y sin texto genérico repetitivo.
3. **Tests Centralizados:** Las suites de Pytest residen exclusivamente en `/tests/` (`tests/curso_01/`, etc.) para no saturar las carpetas de trabajo de los alumnos.
4. **Cuadernos Jupyter:** Cada clase tiene su carpeta `clase-XX-.../notebook/` con el `.ipynb`, su `README.md` y badge interactivo de Google Colab.

---

## 2. Generación de PDFs Estilo LaTeX (Chrome Headless)

El flujo canónico para generar PDFs de 9 páginas con tipografía académica:

```python
import os
import subprocess
import tempfile

def compile_latex_pdf_from_html(html_content: str, dest_pdf_path: str):
    temp_dir = tempfile.mkdtemp()
    temp_html = os.path.join(temp_dir, "document.html")
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={dest_pdf_path}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    
    # Limpieza del temporal
    os.remove(temp_html)
    os.rmdir(temp_dir)
```

### Reglas del CSS del PDF:
* Tipografía académica (`font-family: 'Latin Modern Roman', 'Computer Modern', 'Georgia', serif;`).
* Portada elegante con título, autor (*William Rodríguez (Wisrovi)*), badge de versión y tabla de contenidos.
* 9 páginas estructuradas por clase, con número de página y pie de página en `@page`.

---

## 3. Diagramas Mermaid Nativos

Todos los diagramas deben seguir el patrón de alto contraste y compatibilidad con GitHub y MkDocs:
* Usar `flowchart LR` o `flowchart TD`.
* Nodos descriptivos con emojis y subtítulos explicativos.
* Separar líneas con `<br/>` en lugar de saltos crudos.
* Paleta visual:
  - Base / Entorno: `style ID fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px`
  - Procesos / Motores: `style ID fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px`
  - Éxito / Salida: `style ID fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px`
  - Decisiones / Condicionales: `style ID fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px`
  - Alertas / Errores: `style ID fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px`

---

## 4. Despliegue en GitHub Pages (MkDocs Material)

* Portal web en `docs/` con `docs/index.md`, `docs/CNAME` y carpetas por curso.
* `mkdocs.yml` con tema `material`, extensiones `pymdownx.superfences` (Mermaid), `admonition` y `tabbed`.
* Workflow `.github/workflows/docs.yml`:
  - `actions/checkout@v4` con `fetch-depth: 0`.
  - Configurar `git config user.name "github-actions[bot]"` y `git config user.email "github-actions[bot]@users.noreply.github.com"`.
  - Comando `mkdocs gh-deploy --force`.
