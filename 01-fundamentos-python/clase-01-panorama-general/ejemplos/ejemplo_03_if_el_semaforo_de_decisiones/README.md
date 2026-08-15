# 📖 03 If El Semaforo De Decisiones

> **Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
> **Archivo de Código:** [`main.py`](main.py)  

Demostración práctica y ejecutable de este concepto fundamental de Python.

---

## 🗺️ Flujo de Ejecución del Ejemplo

```mermaid
flowchart TD
    DATA["👤 Visitante: Estatura = 1.55 m"] --> COND{"⚖️ ¿Estatura >= 1.40 m?"}
    COND -->|True (Sí)| GREEN["🟢 SEMÁFORO VERDE<br/>¡Adelante! Puedes subir a la montaña rusa 🎢"]
    COND -->|False (No)| RED["🔴 SEMÁFORO ROJO<br/>Aún eres bajo para este juego 🛑"]

    style DATA fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style COND fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style GREEN fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style RED fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```

---

## 💻 Ejecución desde Terminal
```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_03_if_el_semaforo_de_decisiones/main.py
```
