# 📘 Clase 04: Control de Flujo: Bucles (for / while)

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 1: Fundamentos Básicos de Python (CLASE 04)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 1 - Principiante`
-   :material-lightbulb-on: **Metáfora Central:** *«Bucles como una Cinta Transportadora de Fábrica»*
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-04-control-flujo-bucles.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/01-fundamentos-python/clase-04-control-flujo-bucles/clase-04-control-flujo-bucles.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-04-control-flujo-bucles/notebook/clase-04-control-flujo-bucles.ipynb)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/01-fundamentos-python/clase-04-control-flujo-bucles)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental



!!! note "🌟 Modelo Mental de la Sesión: «Bucles como una Cinta Transportadora de Fábrica»"
    El bucle 'for' es como una cinta transportadora donde inspeccionas cada paquete uno a uno hasta terminar.

### Principios Fundamentales de la Sesión


!!! info "⚡ Regla de Oro en Python"
    En bucles while, asegúrate siempre de modificar la variable de control para evitar bucles infinitos.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart TD
    SEQ["📦 Secuencia o Rango<br/>range(1, 10) o lista"] --> ITER["🔄 Iterador del Bucle (for / while)"]
    ITER --> BODY["⚡ Ejecutar Bloque del Bucle"]
    BODY --> CTRL{"¿Instrucción Especial?"}
    CTRL -->|continue| ITER
    CTRL -->|break| EXIT["🛑 Salida Inmediata del Ciclo"]
    CTRL -->|Flujo Normal| NEXT{"¿Fin de Secuencia?"}
    NEXT -->|No| ITER
    NEXT -->|Sí| EXIT

    style SEQ fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style ITER fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style BODY fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style CTRL fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style NEXT fill:#4338ca,color:#ffffff,stroke:#818cf8,stroke-width:2px
    style EXIT fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

```python
ventas = [120.0, 45.5, 300.0, 89.9]
total = 0.0

for venta in ventas:
    if venta  $50: ${total:.2f}")
```

---

## 4. 🛡️ Buenas Prácticas, Gotchas y Prevención de Errores

!!! warning "⚠️ Trampa Frecuente (Gotcha)"
    Hacer .remove() en una lista dentro de un bucle for provoca saltos de elementos.

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    for n in numeros:
    if n % 2 == 0: numeros.remove(n)  # ❌ Muta la colección
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    impares = [n for n in numeros if n % 2 != 0]  # ✅ List comprehension
    ```

!!! tip "🔧 Consejo de Ingeniería"
    

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Escribe un programa que imprima la tabla de multiplicar de un número del 1 al 10.**

Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipo.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_01/test_clase_04_control_flujo_bucles.py
   ```

---

## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
