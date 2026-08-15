# 📖 01 Basemodel Pydantic

> **Clase:** Clase 03: Salidas Estructuradas y Validación Tipada con Pydantic V2  
> **Script:** [`main.py`](main.py)  

Modelo BaseModel de Pydantic.

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
python 03-agentes-ia/clase-03-salidas-estructuradas-pydantic/ejemplos/ejemplo_01_basemodel_pydantic/main.py
```
