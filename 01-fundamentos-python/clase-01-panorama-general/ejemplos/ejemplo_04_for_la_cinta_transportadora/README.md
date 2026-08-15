# 📖 04 For La Cinta Transportadora

<div align="center">

**Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
*Script de Ejecución:* [`main.py`](main.py)

</div>

---

## 🎯 Propósito del Ejemplo
Ejemplo 04: La Cinta Transportadora (Bucle for).

---

## 🗺️ Diagrama de Flujo del Script

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

## 🔍 Aspectos Clave a Observar en el Código

1. **Claridad Sintáctica:** Estructura modular, tipado explícito y apego a la guía de estilo oficial PEP 8.
2. **Transformación de Datos:** Cómo se declaran las entradas, se procesan en memoria y se devuelven al usuario.
3. **Robustez:** Prevención de comportamientos inesperados mediante nombres expresivos y control lógico.

---

## 💻 Ejecución desde la Terminal

Desde la raíz del proyecto, ejecuta:

```bash
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_04_for_la_cinta_transportadora/main.py
```
