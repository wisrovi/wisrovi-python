# 📖 04 Testclient Fastapi

> **Clase:** Clase 06: Testing Riguroso con Pytest, Mocks y Calidad  
> **Script:** [`main.py`](main.py)  

Pruebas de API con TestClient.

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
python 04-proyecto-final/clase-06-testing-y-calidad/ejemplos/ejemplo_04_testclient_fastapi/main.py
```
