# 📖 05 Funcion La Licuadora

<div align="center">

**Clase:** Clase 01: Primer Vistazo Práctico (print, variables, if, for)  
*Script de Ejecución:* [`main.py`](main.py)

</div>

---

## 🎯 Propósito del Ejemplo
Ejemplo 05: La Licuadora (Funciones con def).

---

## 🗺️ Diagrama de Flujo del Script

```mermaid
flowchart LR
    IN1["🍓 Fresa (fruta1)"] --> BLENDER["🍹 def licuadora(fruta1, fruta2):<br/>Procesa y mezcla ingredientes"]
    IN2["🍌 Plátano (fruta2)"] --> BLENDER
    BLENDER --> OUT["🥤 return 'Batido refrescante de Fresa con Plátano'"]

    style IN1 fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style IN2 fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style BLENDER fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style OUT fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
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
python 01-fundamentos-python/clase-01-panorama-general/ejemplos/ejemplo_05_funcion_la_licuadora/main.py
```
