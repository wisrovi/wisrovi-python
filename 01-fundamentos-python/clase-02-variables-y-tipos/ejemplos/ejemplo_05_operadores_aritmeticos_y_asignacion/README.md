# 📖 Ejemplo 05: Operadores Aritméticos y Asignación Aumentada

<div align="center">

**Clase:** Clase 02: Variables, Tipos de Datos y Operadores  
*Script de Ejecución:* [`main.py`](main.py)

</div>

---

## 🎯 Propósito del Ejemplo
Dominar los operadores aritméticos fundamentales de Python:
* División decimal (`/`) vs División entera (`//`)
* Módulo / Residuo (`%`)
* Potenciación (`**`)
* Asignación aumentada (`+=`, `-=`, `*=`, `/=`)
Todo estructurado dentro de funciones tipadas bajo el estándar **PEP 484**.

---

## 🗺️ Diagrama de Flujo del Script

```mermaid
flowchart LR
    A["📥 Entradas Numéricas<br/>dividendo = 17, divisor = 5"] --> B["⚙️ Función: calcular_estadisticas_division()<br/>Operadores: /, //, %, **"]
    B --> C["📤 Diccionario Tipado Dict[str, float]<br/>División real, entera, residuo y potencia"]
    C --> D["📊 Función: calcular_interes_compuesto()<br/>Cálculo con potenciación (1 + r)^t"]
    D --> E["💳 Función: simular_caja_registradora()<br/>Acumulador con operador +="]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style D fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
```

---

## 🔍 Aspectos Clave a Observar en el Código

1. **Diferencia entre `/` y `//`:** `/` siempre devuelve un `float` (ej. `17 / 5 = 3.4`), mientras que `//` trunca al entero inferior (ej. `17 // 5 = 3`).
2. **Utilidad del Módulo (`%`):** `17 % 5 = 2` obtiene el residuo, fundamental para determinar paridad (`x % 2 == 0`) o ciclos periódicos.
3. **Operadores de Asignación (`+=`):** `saldo += monto` es equivalente a `saldo = saldo + monto`, pero más conciso y Pythonic.

---

## 💻 Ejecución desde la Terminal

Desde la raíz del proyecto, ejecuta:

```bash
python 01-fundamentos-python/clase-02-variables-y-tipos/ejemplos/ejemplo_05_operadores_aritmeticos_y_asignacion/main.py
```
