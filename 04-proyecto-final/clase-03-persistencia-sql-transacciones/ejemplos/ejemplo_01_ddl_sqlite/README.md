# 📖 01 Ddl Sqlite

> **Clase:** Clase 03: Persistencia de Datos: Modelado SQL y Transacciones ACID  
> **Script:** [`main.py`](main.py)  

Creación de Tablas DDL.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    CONN["sqlite3.connect(':memory:')"] --> TX["with conn: Transacción Segura"]
    TX --> SQL["conn.execute('INSERT ... (?, ?)', (val1, val2))"]
    SQL --> DSK["Persistencia / Commit en Memoria"]

    style CONN fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style TX fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style SQL fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style DSK fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 04-proyecto-final/clase-03-persistencia-sql-transacciones/ejemplos/ejemplo_01_ddl_sqlite/main.py
```
