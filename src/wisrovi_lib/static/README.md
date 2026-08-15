# 🎨 Interfaz Web Estática del Tutor Virtual (`wisrovi_lib/static`)

Esta carpeta contiene los archivos de la aplicación web Single-Page Application (SPA) para la experiencia gamificada del estudiante.

---

## 🗺️ Componentes de la Interfaz

```mermaid
flowchart LR
    HTML["📄 index.html<br/>(Estructura y Pestañas)"] --> CSS["🎨 app.css<br/>(Diseño Neo-Cyber & Glassmorphism)"]
    HTML --> JS["⚡ app.js<br/>(Lógica Reactiva, Memoria & Confeti)"]
    JS --> API["🌐 Backend FastAPI (/api/...)"]

    style HTML fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style CSS fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style JS fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style API fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

* **`index.html`**: Estructura semántica con barra de XP, visor Mermaid, editor de código, arenero y modal de certificación.
* **`app.css`**: Sistema de diseño con paleta de alto contraste, temas oscuros y adaptabilidad responsive.
* **`app.js`**: Controlador de eventos, renderizado en vivo de gráficos de memoria, ejecuciones asíncronas y animaciones de victoria.
