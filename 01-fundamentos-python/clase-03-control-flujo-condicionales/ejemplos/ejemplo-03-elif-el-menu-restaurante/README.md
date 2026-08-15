# 📑 Ejemplo 03: El Menú del Restaurante (elif múltiple)

> **Concepto Clave:** Múltiples opciones alternativas con elif.  
> **Metáfora:** Menú del restaurante: Opción 1, Opción 2, Opción 3 o plato por defecto.

---

## 📊 Diagrama de Flujo del Ejemplo

```mermaid
flowchart TD
    A["Opción escogida: 2"] --> B{"¿Opción == 1?"}
    B -- No --> C{"¿Opción == 2?"}
    C -- Sí --> D["🍔 Sirviendo Hamburguesa"]
    B -- Sí --> E["🍕 Sirviendo Pizza"]
    C -- No --> F["❓ Plato por defecto"]

    style A fill:#2b5c8f,color:#fff
    style B fill:#d69e2e,color:#fff
    style C fill:#d69e2e,color:#fff
    style D fill:#3b7a57,color:#fff
    style E fill:#3b7a57,color:#fff
    style F fill:#805ad5,color:#fff
```

---

## 🏃‍♂️ ¿Cómo ejecutar este ejemplo?

Abre tu terminal en VS Code y ejecuta:

```bash
python 01-fundamentos-python/clase-03-control-flujo-condicionales/ejemplos/ejemplo-03-elif-el-menu-restaurante/03_elif_el_menu_restaurante.py
```

---

## 📄 Explicación Paso a Paso

1. Lee detenidamente los comentarios dentro del archivo [`03_elif_el_menu_restaurante.py`](03_elif_el_menu_restaurante.py).
2. Ejecuta el código y observa la salida en consola.
3. Revisa la sección final del archivo para ver el resumen conceptual explicativo.
