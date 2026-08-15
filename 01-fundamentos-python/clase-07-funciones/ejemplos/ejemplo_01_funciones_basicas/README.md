# 📖 01 Funciones Basicas

> **Clase:** Clase 07: Funciones, Parámetros y Scope  
> **Script:** [`main.py`](main.py)  

Ejemplo 01: Funciones Puras.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart LR
    IN1["'Fresa 🍓'"] --> BLEND["def licuadora(fruta1, fruta2):"]
    IN2["'Plátano 🍌'"] --> BLEND
    BLEND --> PROC["Procesamiento & Concatenación"]
    PROC --> OUT["return 'Batido refrescante de Fresa con Plátano 🥤'"]

    style IN1 fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
    style IN2 fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style BLEND fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal

```bash
python 01-fundamentos-python/clase-07-funciones/ejemplos/ejemplo_01_funciones_basicas/main.py
```
