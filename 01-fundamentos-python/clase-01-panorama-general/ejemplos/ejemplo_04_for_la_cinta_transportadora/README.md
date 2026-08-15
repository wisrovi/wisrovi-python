# 📖 04 For La Cinta Transportadora

> **Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
> **Script:** [`main.py`](main.py)  

Ejemplo 04: La Cinta Transportadora (Bucle for).

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    LST["['Manzanas', 'Leche', 'Pan', 'Café']"] --> FOR["for producto in lista:"]
    FOR --> PKG["Empacar: 'Manzanas'"]
    PKG --> NEXT["Siguiente elemento..."]
    NEXT --> FOR
    NEXT --> DONE["✅ Todos los elementos empacados"]

    style LST fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style FOR fill:#0369a1,color:#fff,stroke:#38bdf8,stroke-width:2px
    style PKG fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style DONE fill:#334155,color:#fff,stroke:#94a3b8,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_04_for_la_cinta_transportadora/main.py
```
