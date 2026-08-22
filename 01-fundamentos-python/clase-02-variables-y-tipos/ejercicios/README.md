# 🏋️ Reto Práctico: Clase 02: Variables, Tipos de Datos y Funciones Modulares

<div align="center">

**Curso 1: Fundamentos Básicos de Python** &bull; **Semana CLASE 02**  
*Archivo de Trabajo:* [`reto.py`](reto.py) &bull; *Suite de Validación:* [`tests/curso_01/test_clase_02.py`](../../../tests/curso_01/test_clase_02.py)

</div>

---

## 🎯 Enunciado del Desafío

> **Construye una calculadora de propinas y facturación modular implementando 3 funciones con Type Hints (PEP 484):**
> 1. `calcular_propina(total_cuenta: float, porcentaje: float) -> float`
> 2. `calcular_total_por_persona(total_cuenta: float, porcentaje: float, num_personas: int) -> float`
> 3. `formatear_factura(total_cuenta: float, propina: float, total_por_persona: float) -> str`

---

## 🗺️ Ciclo de Resolución y Feedback Automatizado

```mermaid
flowchart LR
    A["📖 1. Leer reto.py<br/>Firmas de función y Type Hints"] --> B["💻 2. Implementar Funciones<br/>Escribe tu lógica tipada"]
    B --> C["🧪 3. Ejecutar Pytest<br/>pytest tests/curso_01/test_clase_02.py"]
    C -->|Fallo ❌| D["🔍 4. Depuración<br/>Revisa tipos y redondeo"]
    D --> B
    C -->|Pasa 100% ✅| E["🏆 5. ¡Hito Superado!<br/>Avanza a la siguiente clase"]

    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 🚀 Pasos para Resolver el Reto

1. Abre [`reto.py`](reto.py) en tu editor.
2. Lee las firmas de función, docstrings y anotaciones de tipo.
3. Escribe tu solución implementando los cálculos aritméticos y el formateo con f-strings.
4. Valida tu solución en cualquier momento ejecutando en la terminal:
   ```bash
   pytest tests/curso_01/test_clase_02.py
   ```

