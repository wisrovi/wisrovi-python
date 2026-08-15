# 📖 04 For La Cinta Transportadora

> **Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
> **Archivo de Código:** [`main.py`](main.py)  

Demostración práctica y ejecutable de este concepto fundamental de Python.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    LST["🛒 Lista: ['Manzanas 🍎', 'Leche 🥛', 'Pan 🍞', 'Café ☕']"] --> CINTA["🔄 Cinta Transportadora (for producto in lista:)"]
    CINTA --> PACK1["📦 Empacando: Manzanas 🍎"]
    PACK1 --> PACK2["📦 Empacando: Leche 🥛"]
    PACK2 --> PACK3["📦 Empacando: Pan 🍞"]
    PACK3 --> PACK4["📦 Empacando: Café ☕"]
    PACK4 --> DONE["✅ Todos los productos empacados"]

    style LST fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style CINTA fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style PACK1 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK2 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK3 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style PACK4 fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style DONE fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal
```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_04_for_la_cinta_transportadora/main.py
```
