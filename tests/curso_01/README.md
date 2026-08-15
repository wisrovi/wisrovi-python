# 🧪 Suite de Pruebas Automatizadas (Pytest)

> **Módulo:** `curso_01`  
> **Ubicación:** `tests/curso_01`  

---

## 🌀 Pirámide y Flujo de Verificación de Calidad

```mermaid
flowchart TD
    DEV["💻 Código del Estudiante<br/>(reto.py / funciones)"] --> PYTEST["🧪 Pytest Test Suite<br/>(tests/curso_01)"]
    PYTEST --> CI["⚙️ GitHub Actions CI<br/>Validación en cada Commit"]
    CI --> PASS["✅ 100% Tests Pasados<br/>Calidad Garantizada"]

    style DEV fill:#eff6ff,stroke:#3b82f6,stroke-width:2px
    style PYTEST fill:#f5f3ff,stroke:#8b5cf6,stroke-width:2px
    style CI fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style PASS fill:#ecfdf5,stroke:#10b981,stroke-width:2px
```

---

## 💻 Comandos de Ejecución

```bash
# Ejecutar todas las pruebas de este módulo
pytest tests/curso_01/

# Ejecutar con reporte detallado
pytest -v tests/curso_01/
```
