# 📘 Clase 03: Salidas Estructuradas y Validación Tipada con Pydantic V2

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 03)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 3 - Avanzado`
-   :material-lightbulb-on: **Metáfora Central:** *«El Inspector de Aduanas y el Formulario Rígido (Validación Estricta)»*
-   :material-laptop: **Wisrovi Studio (Local):** [🚀 Abrir Reto](http://127.0.0.1:8501/?course=3&class=3) &bull; [👨‍🏫 Modo Tutor](http://127.0.0.1:8501/tutor?course=3&class=3)
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-03-salidas-estructuradas-pydantic.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/03-agentes-ia/clase-03-salidas-estructuradas-pydantic/clase-03-salidas-estructuradas-pydantic.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-03-salidas-estructuradas-pydantic/notebook/clase-03-salidas-estructuradas-pydantic.ipynb)
[![Abrir en Studio Local](https://img.shields.io/badge/Wisrovi_Studio-Abrir_en_Local_(127.0.0.1%3A8501)-0284c7?logo=python&logoColor=white)](http://127.0.0.1:8501/?course=3&class=3)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/03-agentes-ia/clase-03-salidas-estructuradas-pydantic)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

Garantizar que las respuestas del LLM cumplan con contratos de software sin alucinaciones:
1. **Esquemas Pydantic (`BaseModel`)**: Tipado estático con `Field(ge=..., le=...)` y validadores.
2. **Extracción JSON Forzada**: Conversión de texto no estructurado en objetos fuertemente tipados.
3. **Manejo de Errores de Validación**: `ValidationError` para reintentar prompts automáticamente.

!!! note "🌟 Modelo Mental de la Sesión: «El Inspector de Aduanas y el Formulario Rígido (Validación Estricta)»"
    En esta sesión anclamos el aprendizaje en la metáfora del mundo real para visualizar cómo fluyen las estructuras de datos y el flujo de ejecución en la memoria.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart LR
    A["📝 JSON LLM: '{"entidad": "Python", "confianza": 0.95}'"] --> B["🛂 Pydantic BaseModel Validator"]
    B -->|Válido| C["📦 Objeto Python Seguro ExtractionSchema"]
    B -->|Inválido| D["💥 ValidationError & Retry"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style D fill:#881337,color:#ffffff,stroke:#fb7185,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

=== "🚀 Demostración en Vivo"
    ```python
    from pydantic import BaseModel, Field

class UsuarioIA(BaseModel):
    nombre: str
    edad: int = Field(ge=0, le=120)
    habilidades: list[str]

u = UsuarioIA(nombre="Wisrovi", edad=30, habilidades=["FastAPI", "Agentes"])
print("Modelo validado:", u.model_dump_json())
    ```

=== "🔬 Arenero de Exploración de Memoria (RAM)"
    ```python
    import json
raw_json = '{"nombre": "Agent-01", "score": 98.5}'
parsed = json.loads(raw_json)
print("JSON cargado:", parsed)
    ```

---

## 4. 🛡️ Buenas Prácticas PEP 8: Antipatrones vs Código Pythonic

!!! warning "⚠️ Cuidado con los Antipatrones"
    

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    data = json.loads(respuesta_llm)
total = data['precio'] * 2  # ❌ Falla si 'precio' vino como None o string
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    data = FacturaModel.model_validate_json(respuesta_llm)
total = data.precio * 2    # ✅ Garantizado float tipado
    ```

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Crea una clase `ExtractionSchema(BaseModel)` con campos: `entidad: str`, `confianza: float = Field(ge=0.0, le=1.0)` y `etiquetas: list[str]`, y una función `validar_extraccion_json(payload_json: str) -> ExtractionSchema` que valide y retorne la instancia.**

!!! tip "⚡ Resolución Híbrida en 1 Clic (Local + Web)"
    Si tienes ejecutando `wisrovi ui` en tu terminal local, puedes [🚀 Abrir este Reto directamente en tu Studio Local (127.0.0.1:8501)](http://127.0.0.1:8501/?course=3&class=3) para escribir tu código con auto-formateo AST, inspeccionar variables en el Heap/Stack y evaluarlo con pruebas en tiempo real.

=== "💻 Plantilla de Inicio (Starter Code)"
    ```python
    import json
from pydantic import BaseModel, Field

class ExtractionSchema(BaseModel):
    entidad: str
    confianza: float = Field(ge=0.0, le=1.0)
    etiquetas: list[str]

def validar_extraccion_json(payload_json: str) -> ExtractionSchema:
    # ✍️ Deserializa y valida con Pydantic
    datos = json.loads(payload_json)
    return ExtractionSchema(**datos)

    ```

??? info "💡 Pista Socrática 1"
    💡 Pista 1: Define `confianza: float = Field(ge=0.0, le=1.0)`.

??? info "💡 Pista Socrática 2"
    💡 Pista 2: Usa `json.loads(payload_json)` para obtener el diccionario.

??? info "💡 Pista Socrática 3"
    💡 Pista 3: Retorna `ExtractionSchema(**datos)`.



Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code o utiliza `wisrovi ui` / `wisrovi tutor`.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipado.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_03/test_clase_03_salidas_estructuradas_pydantic.py
   ```

---


## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
