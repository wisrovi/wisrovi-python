# 📖 03 If El Semaforo De Decisiones

<div align="center">

**Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
*Script de Ejecución:* [`main.py`](main.py)

</div>

---

## 🎯 Propósito del Ejemplo
Ejemplo 03: El Semáforo de Decisiones (if / else).

---

## 🗺️ Diagrama de Flujo del Script

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

## 🔍 Aspectos Clave a Observar en el Código

1. **Claridad Sintáctica:** Estructura modular, tipado explícito y apego a la guía de estilo oficial PEP 8.
2. **Transformación de Datos:** Cómo se declaran las entradas, se procesan en memoria y se devuelven al usuario.
3. **Robustez:** Prevención de comportamientos inesperados mediante nombres expresivos y control lógico.

---

## 💻 Ejecución desde la Terminal

Desde la raíz del proyecto, ejecuta:

```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_03_if_el_semaforo_de_decisiones/main.py
```
