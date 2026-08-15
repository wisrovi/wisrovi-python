# Clase 04: Control de Flujo - Bucles

<div class="grid cards" markdown>

-   :material-school: __Nivel:__ Principiante Absoluto
-   :material-book-open-page-variant: __Curso:__ Curso 1: Fundamentos Básicos de Python
-   :material-lightbulb-on: __Metáfora:__ *«Las Vueltas a la Pista y el Termostato»*
-   :material-file-pdf-box: __Descargar PDF:__ [clase-04-control-flujo-bucles.pdf](https://github.com/wisrovi/wisrovi-python/blob/main/01-fundamentos-python/clase-04-control-flujo-bucles/clase-04-control-flujo-bucles.pdf)

</div>

---

## 🎯 Objetivos de Aprendizaje

!!! abstract "Competencias Clave de la Sesión"
    *   **Competencia Conceptual:** Diferenciar con claridad cuándo emplear una iteración acotada (for) vs una iteración gobernada por estado (while).
    *   **Competencia Práctica:** Construir bucles eficientes con acumuladores, validaciones con reintentos y control de salida.

---

## 1. 💡 Fundamentos Teóricos y Modelo Mental

La mayor fortaleza de una computadora es su capacidad para ejecutar una misma tarea millones de veces sin cansarse ni cometer errores.

!!! note "🌟 Metáfora Central: Las Vueltas a la Pista y el Termostato"
    El bucle for es como un atleta que da un número exacto de vueltas a la pista de carreras (5 vueltas definidas). El bucle while es como el termostato de un calentador: funciona continuamente mientras la temperatura esté por debajo de 22 grados, y se detiene automáticamente cuando se alcanza la meta.

### Principios Fundamentales

Bucle for: Ideal cuando conoces de antemano el número de repeticiones o cuando recorres una colección finita.

Bucle while: Ideal cuando la repetición depende de una condición externa que puede cambiar dinámicamente durante la ejecución.

!!! tip "⚡ Regla de Oro en Python"
    Todo bucle while debe modificar en su cuerpo la variable de control; de lo contrario, se convierte en un bucle infinito que congela el programa.

---

## 2. 🗺️ Diagrama de Arquitectura y Flujo de Control

Estructura del flujo de control iterativo y mecanismos de interrupción anticipada.

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

| Fase del Flujo | Acción del Intérprete | Estado en Memoria |
| :--- | :--- | :--- |
| **1. Inicialización** | Inicializa el índice o evalúa la condición de entrada del bucle. | `Variable de control lista` |
| **2. Evaluación** | Ejecuta las instrucciones del bloque interno. | `Cálculo en la iteración actual` |
| **3. Transformación** | Si encuentra 'continue', salta directamente a la siguiente iteración. | `Bypass de código restante` |
| **4. Retorno / Salida** | Si encuentra 'break', aborta el bucle inmediatamente hacia la siguiente línea externa. | `Salida forzada del ciclo` |

!!! info "🔍 Visualización Mental"
    Visualiza el bucle como una rueda que gira; cada vuelta procesa un dato individual hasta que se agota el combustible de la condición.

---

## 3. 💻 Implementación Práctica en Python

Implementación que combina bucles while, banderas booleanas y control de intentos:

```python title="main.py - Python 3.10+ (PEP 8)" linenums="1"
PASSWORD_SECRETA = "python2026"
intentos_maximos = 3
intentos_realizados = 0
acceso_concedido = False

while intentos_realizados < intentos_maximos:
    intento = input(f"Intento [{intentos_realizados + 1}/{intentos_maximos}] - Contraseña: ")
    if intento == PASSWORD_SECRETA:
        acceso_concedido = True
        print("¡Acceso exitoso al sistema! 🔓")
        break
    else:
        print("❌ Contraseña incorrecta.")
        intentos_realizados += 1

if not acceso_concedido:
    print("🚫 Sistema bloqueado por demasiados intentos fallidos.")
```

### Análisis Detallado del Código

Demuestra el uso de contadores incrementales, la instrucción break para salida inmediata y la bandera booleana de estado.

---

## 4. 🛡️ Buenas Prácticas, Gotchas y Depuración

Errores habituales que provocan fallos de rendimiento o bucles congelados:

!!! warning "⚠️ Gotcha Frecuente (Trampa de Principiante)"
    Olvidar incrementar el contador en un bucle while, resultando en un bucle infinito que consume el 100% de la CPU.

### Comparativa: Patrón Recomendado vs Antipatrón

=== "✅ Patrón Pythonic Recomendado"
    ```python
for i in range(5):
    print(i) # Seguro, limpio e idiomático
    ```

=== "❌ Antipatrón / Mal Código"
    ```python
i = 0
while i < 5:
    print(i) # Olvido de i += 1 -> Bucle infinito
    ```

!!! success "🛡️ Consejo de Resiliencia en Producción"
    Prefiere siempre for sobre while cuando conozcas el número de iteraciones o trabajes sobre secuencias.

---

## 5. 🏋️ Ejercicios y Desafío de Autoestudio

!!! example "Desafío Práctico Recomendado"
    Escribe un programa que utilice bucles anidados para generar la tabla de multiplicar completa del 1 al 10 con formato tabular.

???+ tip "🧪 Cómo validar tu solución con Pytest"
    Abre tu terminal en VS Code y ejecuta:
    ```bash
    pytest 01-fundamentos-python/clase-04-control-flujo-bucles/ejercicios/
    ```

---

## 6. 📚 Fuentes y Referencias Oficiales

| Fuente / Recurso | Descripción Temática | Enlace Oficial |
| :--- | :--- | :--- |
| **Documentación Oficial de Python** | Referencia canónica del lenguaje y librería estándar | [docs.python.org/3/](https://docs.python.org/3/) |
| **PEP 8 — Style Guide for Python** | Guía oficial de estilo, formato e indentación | [peps.python.org/pep-0008/](https://peps.python.org/pep-0008/) |
| **Real Python Tutorials** | Artículos técnicos y patrones de desarrollo moderno | [realpython.com](https://realpython.com/) |
| **Suite Open Source wisrovi** | Paquetes Python para orquestación y rendimiento | [github.com/wisrovi](https://github.com/wisrovi) |
