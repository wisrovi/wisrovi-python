# 🌐 Documentación Web Interactiva: curso-04

> **Sitio Web Oficial:** [`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/)  
> **Ubicación:** `docs/curso-04`  

---

## 🌀 Arquitectura del Sitio Web de Documentación

```mermaid
flowchart LR
    SRC["📝 Archivos Markdown<br/>(docs/*.md)"] --> MKDOCS["⚙️ Motor MkDocs Material<br/>Pestañas, admonitions & mermaid"]
    MKDOCS --> GHPAGES["☁️ GitHub Pages<br/>academy_python.wisrovi.dev"]

    style SRC fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style MKDOCS fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style GHPAGES fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 💻 Servidor Local de Previsualización
```bash
mkdocs serve
```
