# 📖 03 Mensajes Pydantic Grafo

> **Clase:** Clase 08: Sistemas Multi-Agente, Supervisión y Guardrails  
> **Script:** [`main.py`](main.py)  

Paso de Mensajes Tipado.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    DICT["{'id': 1, 'name': 'Ana'}"] --> MODEL["User(BaseModel)"]
    MODEL --> VAL["Validación estricta de tipos"]
    VAL --> DUMP["user.model_dump() ➔ Dict sanitizado"]

    style DICT fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style MODEL fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style DUMP fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 03-agentes-ia/clase-08-sistemas-multi-agente/ejemplos/ejemplo_03_mensajes_pydantic_grafo/main.py
```
