# 📘 Clase 04: Algoritmos de Búsqueda: Lineal vs Binaria O(log n)

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 2: Algoritmos Avanzados y Estructuras de Datos (CLASE 04)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 2 - Intermedio`
-   :material-lightbulb-on: **Metáfora Central:** *«El Diccionario Abierto por la Mitad»*
-   :material-laptop: **Wisrovi Studio (Local):** [🚀 Abrir Reto](http://127.0.0.1:8501/?course=2&class=4) &bull; [👨‍🏫 Modo Tutor](http://127.0.0.1:8501/tutor?course=2&class=4)
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-04-algoritmos-busqueda.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/02-algoritmos-estructuras/clase-04-algoritmos-busqueda/clase-04-algoritmos-busqueda.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/02-algoritmos-estructuras/clase-04-algoritmos-busqueda/notebook/clase-04-algoritmos-busqueda.ipynb)
[![Abrir en Studio Local](https://img.shields.io/badge/Wisrovi_Studio-Abrir_en_Local_(127.0.0.1%3A8501)-0284c7?logo=python&logoColor=white)](http://127.0.0.1:8501/?course=2&class=4)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/02-algoritmos-estructuras/clase-04-algoritmos-busqueda)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

Estrategias de búsqueda y división logarítmica:
1. **Búsqueda Lineal**: $O(N)$ explorando elemento por elemento.
2. **Búsqueda Binaria**: $O(\log N)$ descartando la mitad del espacio de búsqueda en cada paso sobre colecciones ordenadas.
3. **Punteros `left`, `right`, `mid`**: Evitar desbordamientos y manejar correctamente condiciones de parada (`left <= right`).

!!! note "🌟 Modelo Mental de la Sesión: «El Diccionario Abierto por la Mitad»"
    En esta sesión anclamos el aprendizaje en la metáfora del mundo real para visualizar cómo fluyen las estructuras de datos y el flujo de ejecución en la memoria.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart TD
    A["📥 Lista Ordenada [10, 20, 30, 40, 50], target=30"] --> B["📍 mid = (0 + 4)//2 -> arr[2]=30"]
    B -->|arr[mid] == target| C["🎯 ¡Encontrado en índice 2!"]
    B -->|arr[mid] < target| D["👉 left = mid + 1"]
    B -->|arr[mid] > target| E["👈 right = mid - 1"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

=== "🚀 Demostración en Vivo"
    ```python
    def busqueda_binaria_demo(arr: list[int], x: int) -> int:
    izq, der = 0, len(arr) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if arr[medio] == x: return medio
        elif arr[medio] < x: izq = medio + 1
        else: der = medio - 1
    return -1

datos = [10, 20, 30, 40, 50, 60, 70]
print("Buscar 40:", busqueda_binaria_demo(datos, 40))
    ```

=== "🔬 Arenero de Exploración de Memoria (RAM)"
    ```python
    import bisect
ordenados = [5, 15, 25, 35, 45]
idx = bisect.bisect_left(ordenados, 25)
print("Índice con módulo bisect:", idx)
    ```

---

## 4. 🛡️ Buenas Prácticas PEP 8: Antipatrones vs Código Pythonic

!!! warning "⚠️ Cuidado con los Antipatrones"
    

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    while left < right:  # ❌ Puede fallar si el target está en el último elemento
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    while left <= right:  # ✅ Evalúa todos los casos correctamente
    ```

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Crea una función `busqueda_binaria(ordenados: list[int], objetivo: int) -> int` que retorne el índice del elemento `objetivo` en la lista ordenada, o `-1` si no existe.**

!!! tip "⚡ Resolución Híbrida en 1 Clic (Local + Web)"
    Si tienes ejecutando `wisrovi ui` en tu terminal local, puedes [🚀 Abrir este Reto directamente en tu Studio Local (127.0.0.1:8501)](http://127.0.0.1:8501/?course=2&class=4) para escribir tu código con auto-formateo AST, inspeccionar variables en el Heap/Stack y evaluarlo con pruebas en tiempo real.

=== "💻 Plantilla de Inicio (Starter Code)"
    ```python
    def busqueda_binaria(ordenados: list[int], objetivo: int) -> int:
    # ✍️ Implementa búsqueda binaria iterativa
    left, right = 0, len(ordenados) - 1
    while left <= right:
        mid = (left + right) // 2
        if ordenados[mid] == objetivo:
            return mid
        elif ordenados[mid] < objetivo:
            left = mid + 1
        else:
            right = mid - 1
    return -1

    ```

??? info "💡 Pista Socrática 1"
    💡 Pista 1: Inicializa `left = 0` y `right = len(ordenados) - 1`.

??? info "💡 Pista Socrática 2"
    💡 Pista 2: En cada iteración calcula `mid = (left + right) // 2`.

??? info "💡 Pista Socrática 3"
    💡 Pista 3: Si `ordenados[mid] < objetivo`, avanza `left = mid + 1`; en caso contrario `right = mid - 1`.



Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code o utiliza `wisrovi ui` / `wisrovi tutor`.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipado.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_02/test_clase_04_algoritmos_busqueda.py
   ```

---


## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
