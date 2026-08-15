# 🏋️ Reto Práctico: Clase 06: Testing Riguroso con Pytest, Mocks y Calidad

> **Curso:** 04-proyecto-final &bull; **Semana:** CLASE 06  
> **Archivo del Reto:** [`reto.py`](reto.py)  

---

## 🎯 Enunciado del Desafío
> **Escribe un test parametrizado con @pytest.mark.parametrize para validar 5 casos de cálculo de IVA.**

---

## 🗺️ Flujo de Resolución

```mermaid
flowchart LR
    A["📖 1. Leer reto.py"] --> B["💻 2. Escribir Solución"]
    B --> C["🧪 3. Validar con Pytest<br/>pytest tests/curso_04/"]
    C -->|Falla ❌| B
    C -->|Pasa ✅| D["🏆 4. Reto Completado"]

    style A fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style D fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
```

---

## 🚀 Cómo Validar tu Código
```bash
pytest tests/curso_04/
```
