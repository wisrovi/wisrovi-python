# 🏋️ Reto Práctico: Clase 02: Prompt Engineering Avanzado y Few-Shot Learning

<div align="center">

**Curso 3: Creación y Desarrollo de Agentes de IA** &bull; **Semana CLASE 02**  
*Archivo de Trabajo:* [`reto.py`](reto.py) &bull; *Suite de Validación:* [`tests/curso_03/test_clase_02_prompt_engineering_avanzado.py`](../../tests/curso_03/test_clase_02_prompt_engineering_avanzado.py)

</div>

---

## 🎯 Enunciado del Desafío

> **Diseña un prompt que evalúe y extraiga la información de un CV en formato JSON sin alucinar datos ausentes.**

---

## 🗺️ Ciclo de Resolución y Feedback Automatizado

```mermaid
flowchart LR
    A["📖 1. Leer reto.py<br/>Comprende los requisitos y tipos"] --> B["💻 2. Implementar Solución<br/>Escribe tu lógica en VS Code"]
    B --> C["🧪 3. Ejecutar Pytest<br/>pytest tests/curso_03/"]
    C -->|Fallo ❌| D["🔍 4. Depuración<br/>Analiza el mensaje de error"]
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
2. Lee las firmas de función, docstrings y restricciones.
3. Escribe tu solución reemplazando los comentarios `TODO`.
4. Valida tu solución en cualquier momento ejecutando en la terminal:
   ```bash
   pytest tests/curso_03/
   ```
