# 🧪 Suite de Pruebas Automatizadas (Pytest)

> **Módulo:** `README.md`  
> **Ubicación:** `tests`  

---

## 🌀 Pirámide y Flujo de Verificación de Calidad

```mermaid
flowchart TD
    DEV["💻 Código del Estudiante<br/>(reto.py / funciones)"] --> PYTEST["🧪 Pytest Test Suite<br/>(tests/README.md)"]
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
pytest tests/

# Ejecutar con reporte detallado
pytest -v tests/
```
