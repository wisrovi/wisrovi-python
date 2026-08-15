# 📖 01 App Minima

> **Clase:** Clase 02: Desarrollo del Backend: APIs RESTful con FastAPI  
> **Script:** [`main.py`](main.py)  

API Mínima con FastAPI.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    CLIENT["Cliente HTTP (Curl / Browser)"] --> GET["GET /ping"]
    GET --> APP["FastAPI App Router"]
    APP --> JSON["Retorno JSON: {'status': 'ok'}"]

    style CLIENT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style GET fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style JSON fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 04-proyecto-final/clase-02-backend-fastapi/ejemplos/ejemplo_01_app_minima/main.py
```
