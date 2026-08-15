# 📚 Clase 04: Control de Flujo: Bucles (for / while)

> **Programa:** Curso 1: Fundamentos Básicos de Python  
> **Nivel:** Nivel 1 - Principiante  
> **Metáfora Central:** *«Bucles como una Cinta Transportadora de Fábrica»*  
> **Documento Oficial PDF:** [clase-04-control-flujo-bucles.pdf](clase-04-control-flujo-bucles.pdf)  
> **Instructor:** **William Rodríguez (Wisrovi)** (AI Solutions Architect & Principal Software Engineer)  

---

## 👤 Perfil del Autor y Mentor

### **William Rodríguez (Wisrovi)**
*AI Solutions Architect & Principal Software Engineer &bull; Badajoz, España*

Ingeniero y arquitecto de software especializado en Inteligencia Artificial Generativa, sistemas multi-agente, Visión por Computador e infraestructuras MLOps de alta disponibilidad. Creador y mantenedor de la suite de software libre wisrovi SUITE en PyPI con más de 26 bibliotecas enfocadas en orquestación de pipelines, caching distribuido y optimización de bases de datos.

*   🐙 **GitHub:** [github.com/wisrovi](https://github.com/wisrovi)
*   💼 **LinkedIn:** [www.linkedin.com/in/wisrovi-rodriguez/](https://www.linkedin.com/in/wisrovi-rodriguez/)
*   🐳 **DockerHub:** [hub.docker.com/u/wisrovi](https://hub.docker.com/u/wisrovi)
*   🌐 **Website:** [wisrovi.dev](https://wisrovi.dev)
*   📦 **PyPI:** [pypi.org/user/wisrovi/](https://pypi.org/user/wisrovi/)

---

### 🚲 La Regla de la Bicicleta

> *"Nadie aprende a montar en bicicleta viendo tutoriales. El verdadero dominio de la programación surge cuando abres tu editor, escribes código con tus propias manos, resuelves errores y construyes proyectos reales."*

---

## 📑 Tabla de Contenidos de la Sesión

1. [💡 Fundamentación Teórica y Modelo Mental](#1--fundamentación-teórica-y-modelo-mental)
2. [🗺️ Arquitectura y Diagrama de Flujo](#2-️-arquitectura-y-diagrama-de-flujo)
3. [💻 Implementación en Python 3.10+](#3--implementación-en-python-310)
4. [🛡️ Buenas Prácticas y Trampas Frecuentes](#4-️-buenas-prácticas-y-trampas-frecuentes)
5. [🏋️ Desafío de Práctica](#5-️-desafío-de-práctica)
6. [📚 Bibliografía y Enlaces Canónicos](#6--bibliografía-y-enlaces-canónicos)

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

Los bucles permiten ejecutar un bloque de código múltiples veces sobre secuencias o hasta cumplir una condición.

> [!NOTE]
> **🌟 Metáfora Didáctica:** El bucle 'for' es como una cinta transportadora donde inspeccionas cada paquete uno a uno hasta terminar.

### Principios Fundamentales

El bucle 'for' en Python itera directamente sobre los elementos de cualquier objeto iterable.

El bucle 'while' evalúa una condición antes de cada ciclo y se detiene cuando la condición es False.

> [!IMPORTANT]
> **⚡ Regla de Oro en Python:** En bucles while, asegúrate siempre de modificar la variable de control para evitar bucles infinitos.

---

## 2. 🗺️ Arquitectura y Diagrama de Flujo

Ciclo de vida de una iteración con range e interrupción controlada.

```mermaid
flowchart LR
    A["📦 Colección / Rango"] --> B["🔄 Iterador (for / while)"]
    B --> C["⚡ Ejecuta Cuerpo del Bucle"]
    C -->|Siguiente Iteración| B
    C -->|break / Fin de Rango| D["🏁 Fin del Ciclo"]

    style A fill:#1e293b,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style B fill:#0369a1,color:#ffffff,stroke:#7dd3fc,stroke-width:2px
    style C fill:#047857,color:#ffffff,stroke:#6ee7b7,stroke-width:2px
    style D fill:#334155,color:#ffffff,stroke:#94a3b8,stroke-width:2px
```

### Desglose Paso a Paso del Flujo

| Fase | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **1. Inicialización** | Instanciación del objeto iterable (range). | `Puntero en el primer índice.` |
| **2. Evaluación** | Extracción del elemento actual (next()). | `Variable de iteración asignada.` |
| **3. Transformación** | Ejecución del cuerpo y evaluación de break/continue. | `Variables actualizadas.` |
| **4. Retorno / Salida** | Fin de colección o StopIteration. | `Liberación del iterador.` |

> [!TIP]
> **🔍 Visualización Mental:** Visualiza a 'continue' como saltar al siguiente turno y a 'break' como parar la máquina.

---

## 3. 💻 Implementación en Python 3.10+

```python
# CLASE 04 - Código de Demostración
ventas = [120.0, 45.5, 300.0, 89.9]
total = 0.0

for venta in ventas:
    if venta < 50.0:
        continue
    total += venta

print(f"Total de ventas > $50: ${total:.2f}")
```

*Uso idiomático de continue para filtrar elementos sin anidar estructuras if.*

---

## 4. 🛡️ Buenas Prácticas y Trampas Frecuentes

> [!WARNING]
> **⚠️ Gotcha Frecuente (Trampa de Principiante):** Hacer .remove() en una lista dentro de un bucle for provoca saltos de elementos.

*   **❌ Antipatrón:**
    ```python
for n in numeros:
    if n % 2 == 0: numeros.remove(n)  # ❌ Muta la colección
    ```

*   **✅ Patrón Correcto:**
    ```python
impares = [n for n in numeros if n % 2 != 0]  # ✅ List comprehension
    ```

> [!TIP]
> **💡 Consejo Profesional:** Prefiere List Comprehensions para filtrar y transformar datos.

---

## 5. 🏋️ Desafío de Práctica

> **Desafío:** Escribe un programa que imprima la tabla de multiplicar de un número del 1 al 10.

Para ejecutar la verificación automática con pytest:
```bash
pytest ejercicios/
```

---

## 6. 📚 Bibliografía y Enlaces Canónicos

| Fuente / Recurso | Descripción | Enlace |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Especificación y biblioteca estándar | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Estándar oficial de formateo y estilo | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Patrones de ingeniería y desarrollo | [realpython.com](https://realpython.com/) |
| **Suite Open Source wisrovi** | Librerías de alto rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |
