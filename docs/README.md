# 🌐 Documentación Web: Root

> **Sitio Web:** [`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/)  
> **Ubicación:** `docs`  

---

## 🗺️ Flujo de Publicación Web

```mermaid
flowchart LR
    MD["Archivos Markdown (docs/*.md)"] --> MKD["Motor MkDocs Material"]
    MKD --> GHP["GitHub Pages (academy_python.wisrovi.dev)"]

    style MD fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MKD fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style GHP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Servidor Local
```bash
mkdocs serve
```
