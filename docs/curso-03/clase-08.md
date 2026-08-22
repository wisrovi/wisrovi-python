# 📘 Clase 08: Sistemas Multi-Agente, Supervisión y Guardrails

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 3: Creación y Desarrollo de Agentes de IA (CLASE 08)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 3 - Avanzado`
-   :material-lightbulb-on: **Metáfora Central:** *«La Agencia de Expertos Especializados con Supervisor de Calidad»*
-   :material-laptop: **Wisrovi Studio (Local):** [🚀 Abrir Reto](http://127.0.0.1:8501/?course=3&class=8) &bull; [👨‍🏫 Modo Tutor](http://127.0.0.1:8501/tutor?course=3&class=8)
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-08-sistemas-multi-agente.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/03-agentes-ia/clase-08-sistemas-multi-agente/clase-08-sistemas-multi-agente.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/03-agentes-ia/clase-08-sistemas-multi-agente/notebook/clase-08-sistemas-multi-agente.ipynb)
[![Abrir en Studio Local](https://img.shields.io/badge/Wisrovi_Studio-Abrir_en_Local_(127.0.0.1%3A8501)-0284c7?logo=python&logoColor=white)](http://127.0.0.1:8501/?course=3&class=8)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/03-agentes-ia/clase-08-sistemas-multi-agente)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

Orquestación de equipos de agentes con roles especializados y políticas de seguridad:
1. **Roles Especializados**: Agente Investigador -> Agente Redactor -> Agente Revisor / Crítico.
2. **Supervisor Central**: Enruta las tareas y valida que ningún agente viole restricciones de seguridad.
3. **Guardrails**: Reglas deterministas que bloquean salidas tóxicas o con alucinaciones antes de entregarlas al usuario.

!!! note "🌟 Modelo Mental de la Sesión: «La Agencia de Expertos Especializados con Supervisor de Calidad»"
    En esta sesión anclamos el aprendizaje en la metáfora del mundo real para visualizar cómo fluyen las estructuras de datos y el flujo de ejecución en la memoria.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart LR
    A["👤 Solicitud"] --> B["🕵️ 1. Investigador (Recupera datos)"]
    B --> C["✍️ 2. Redactor (Genera borrador)"]
    C --> D["🛡️ 3. Supervisor & Guardrails (Auditoría)"]
    D --> E["🎯 Respuesta Certificada de Calidad"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style D fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

=== "🚀 Demostración en Vivo"
    ```python
    class SupervisorMultiAgenteDemo:
    def ejecutar_pipeline(self, texto: str) -> dict:
        investigacion = f"Datos sobre: {texto}"
        redaccion = f"Artículo: {investigacion}"
        aprobado = len(redaccion) > 10
        return {"resultado": redaccion, "guardrail_pass": aprobado}

s = SupervisorMultiAgenteDemo()
print(s.ejecutar_pipeline("Arquitectura de Agentes"))
    ```

=== "🔬 Arenero de Exploración de Memoria (RAM)"
    ```python
    roles = ["Researcher", "Coder", "Reviewer"]
print("Equipo de Agentes:", " -> ".join(roles))
    ```

---

## 4. 🛡️ Buenas Prácticas PEP 8: Antipatrones vs Código Pythonic

!!! warning "⚠️ Cuidado con los Antipatrones"
    

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    msg_agente_2 = call_llm(f'El otro dijo: {texto_libre_caotico}')  # ❌ Degradación
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    # Usa esquemas Pydantic para el paso de mensajes entre agentes ✅
    ```

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Crea una clase `OrquestadorMultiAgente` con método `procesar_flujo(self, entrada: str) -> dict` que simule el paso por un Investigador (añade '[INVESTIGADO]'), un Redactor (añade '[REDACTADO]') y un Guardrail (verifica que contenga ambas marcas y retorne dict con 'final_output' y 'valid: bool').**

!!! tip "⚡ Resolución Híbrida en 1 Clic (Local + Web)"
    Si tienes ejecutando `wisrovi ui` en tu terminal local, puedes [🚀 Abrir este Reto directamente en tu Studio Local (127.0.0.1:8501)](http://127.0.0.1:8501/?course=3&class=8) para escribir tu código con auto-formateo AST, inspeccionar variables en el Heap/Stack y evaluarlo con pruebas en tiempo real.

=== "💻 Plantilla de Inicio (Starter Code)"
    ```python
    class OrquestadorMultiAgente:
    def procesar_flujo(self, entrada: str) -> dict:
        # ✍️ Pipeline: Investigador -> Redactor -> Guardrail
        paso1 = f"[INVESTIGADO] {entrada}"
        paso2 = f"[REDACTADO] {paso1}"
        es_valido = "[INVESTIGADO]" in paso2 and "[REDACTADO]" in paso2
        return {
            "final_output": paso2,
            "valid": es_valido
        }

    ```

??? info "💡 Pista Socrática 1"
    💡 Pista 1: Añade `[INVESTIGADO]` a la entrada original.

??? info "💡 Pista Socrática 2"
    💡 Pista 2: Añade `[REDACTADO]` al resultado de la investigación.

??? info "💡 Pista Socrática 3"
    💡 Pista 3: Retorna el diccionario con `final_output` y `valid: True`.



Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code o utiliza `wisrovi ui` / `wisrovi tutor`.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipado.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_03/test_clase_08_sistemas_multi_agente.py
   ```

---


## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
