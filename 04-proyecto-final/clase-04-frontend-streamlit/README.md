# 📘 Clase 04: Desarrollo del Frontend: Dashboards con Streamlit

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 04)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«Streamlit como el Salón de Control Visual para tu Backend de Python»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-04-frontend-streamlit/notebook/clase-04-frontend-streamlit.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart LR
    UI["Widgets: st.text_input / st.button"] --> STATE["st.session_state (Preservación de Estado)"]
    STATE --> API["requests.post('http://api:8000')"]
    API --> REND["Renderizado: st.dataframe / st.metric / Tabs"]

    style UI fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style STATE fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style API fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style REND fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-04-frontend-streamlit.pdf`](clase-04-frontend-streamlit.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
