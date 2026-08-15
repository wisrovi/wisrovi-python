# 🏋️ Reto Práctico: Clase 01: Análisis de Complejidad y Notación Big-O

> **Curso:** 02-algoritmos-estructuras &bull; **Semana:** CLASE 01  
> **Ubicación:** `02-algoritmos-estructuras/clase-01-analisis-complejidad-big-o/ejercicios`  

---

## 🌀 Ciclo de Resolución y Validación

```mermaid
flowchart LR
    A["📖 1. Lee el Reto<br/>ejercicios/reto.py"] --> B["💻 2. Escribe tu Código<br/>Implementa tu solución"]
    B --> C["🧪 3. Ejecuta Pytest<br/>pytest tests/curso_02/"]
    C -->|Fallo ❌| B
    C -->|Éxito ✅| D["🏆 4. Concepto Consolidado<br/>Avanza a la siguiente clase"]

    style A fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style B fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style C fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style D fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🎯 Desafío de la Sesión
> **Enunciado:** Escribe un script que compare el tiempo real de buscar un elemento en una lista vs un set de 500.000 elementos.

---

## 🚀 Pasos para Resolverlo
1. Abre el archivo [`reto.py`](reto.py).
2. Escribe tu lógica de solución.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_02/
   ```
