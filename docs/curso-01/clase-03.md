# 📘 Clase 03: Control de Flujo: Condicionales (if / elif / else)

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 03)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 1 - Principiante`
-   :material-lightbulb-on: **Metáfora Central:** *«Condicionales como Semáforos y Bifurcaciones en un Tren»*
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-03-control-flujo-condicionales.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/01-fundamentos-python/clase-03-control-flujo-condicionales/clase-03-control-flujo-condicionales.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-03-control-flujo-condicionales/notebook/clase-03-control-flujo-condicionales.ipynb)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/01-fundamentos-python/clase-03-control-flujo-condicionales)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental



!!! note "🌟 Modelo Mental de la Sesión: «Condicionales como Semáforos y Bifurcaciones en un Tren»"
    Un condicional es como una aguja ferroviaria que desvía el tren según el color del semáforo.

### Principios Fundamentales de la Sesión


!!! info "⚡ Regla de Oro en Python"
    Mantén las condiciones planas: evita anidar más de 3 niveles de if.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart TD
    COND["⚖️ Evaluación de Expresión Booleana"] --> IF{"¿Condición Principal<br/>if edad >= 18?"}
    IF -->|True (Verdadero)| B1["🟢 Semáforo Verde<br/>Acceso Autorizado al Sistema"]
    IF -->|False (Falso)| ELIF{"¿Condición Secundaria<br/>elif tiene_permiso?"}
    ELIF -->|True (Verdadero)| B2["🟡 Semáforo Amarillo<br/>Acceso con Supervisión"]
    ELIF -->|False (Falso)| ELSE["🔴 Semáforo Rojo<br/>Acceso Denegado por Defecto"]

    style COND fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style IF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B1 fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style ELIF fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style B2 fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style ELSE fill:#991b1b,color:#ffffff,stroke:#f87171,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

```python
puntaje = 85

if puntaje >= 90:
    calificacion = "A - Excelente"
elif puntaje >= 80:
    calificacion = "B - Notable"
elif puntaje >= 70:
    calificacion = "C - Aprobado"
else:
    calificacion = "D - Refuerzo"

print(f"Resultado final: {calificacion}")
```

---

## 4. 🛡️ Buenas Prácticas, Gotchas y Prevención de Errores

!!! warning "⚠️ Trampa Frecuente (Gotcha)"
    Usar 'is' para comparar números o strings; 'is' compara direcciones de memoria.

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    if nombre is 'Juan':  # ❌ SyntaxWarning
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    if nombre == 'Juan':  # ✅ Comparación correcta
    ```

!!! tip "🔧 Consejo de Ingeniería"
    

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Diseña un clasificador de acceso por edad y membresía VIP.**

Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipo.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_01/test_clase_03_control_flujo_condicionales.py
   ```

---

## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
