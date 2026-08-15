# 📖 03 If El Semaforo De Decisiones

> **Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
> **Script:** [`main.py`](main.py)  

Ejemplo 03: El Semáforo de Decisiones (if / else).

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
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_03_if_el_semaforo_de_decisiones/main.py
```
