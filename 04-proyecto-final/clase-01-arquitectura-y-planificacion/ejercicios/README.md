# 🏋️ Reto Práctico: Clase 01: Arquitectura de Software y Planificación del Proyecto

> **Curso:** 04-proyecto-final &bull; **Semana:** CLASE 01  
> **Ubicación:** `04-proyecto-final/clase-01-arquitectura-y-planificacion/ejercicios`  

---

## 🌀 Ciclo de Resolución y Validación

```mermaid
flowchart LR
    A["📖 1. Lee el Reto<br/>ejercicios/reto.py"] --> B["💻 2. Escribe tu Código<br/>Implementa tu solución"]
    B --> C["🧪 3. Ejecuta Pytest<br/>pytest tests/curso_04/"]
    C -->|Fallo ❌| B
    C -->|Éxito ✅| D["🏆 4. Concepto Consolidado<br/>Avanza a la siguiente clase"]

    style A fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style B fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style C fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style D fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 🎯 Desafío de la Sesión
> **Enunciado:** Dibuja el diagrama de arquitectura y redacta las 5 rutas principales de tu API.

---

## 🚀 Pasos para Resolverlo
1. Abre el archivo [`reto.py`](reto.py).
2. Escribe tu lógica de solución.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_04/
   ```
