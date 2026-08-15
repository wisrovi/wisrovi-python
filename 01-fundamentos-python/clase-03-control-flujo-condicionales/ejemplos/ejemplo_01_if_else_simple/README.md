# 📖 01 If Else Simple

> **Clase:** Clase 03: Control de Flujo: Condicionales (if / elif / else)  
> **Script:** [`main.py`](main.py)  

Ejemplo 01: Condicionales Simples.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart TD
    DATA["Estatura = 1.55 m"] --> COND{"¿Estatura >= 1.40 m?"}
    COND -->|True| GREEN["🚦 SEMÁFORO VERDE: Acceso Autorizado 🎢"]
    COND -->|False| RED["🚦 SEMÁFORO ROJO: Acceso Denegado 🛑"]

    style DATA fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style COND fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style GREEN fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style RED fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 01-fundamentos-python/clase-03-control-flujo-condicionales/ejemplos/ejemplo_01_if_else_simple/main.py
```
