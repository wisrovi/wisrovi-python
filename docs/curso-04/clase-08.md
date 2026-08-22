# 📘 Clase 08: Despliegue en la Nube, CI/CD y Portafolio Final

<div class="grid cards" markdown>

-   :material-bookmark: **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 08)
-   :material-signal-cellular-outline: **Nivel:** `Nivel 4 - Integrador`
-   :material-lightbulb-on: **Metáfora Central:** *«La Cinta de Ensamblaje Automatizada hacia Producción»*
-   :material-laptop: **Wisrovi Studio (Local):** [🚀 Abrir Reto](http://127.0.0.1:8501/?course=4&class=8) &bull; [👨‍🏫 Modo Tutor](http://127.0.0.1:8501/tutor?course=4&class=8)
-   :material-file-pdf-box: **Manual PDF Oficial:** [Descargar clase-08-despliegue-cicd-portafolio.pdf](https://github.com/wisrovi/wisrovi-python/raw/main/04-proyecto-final/clase-08-despliegue-cicd-portafolio/clase-08-despliegue-cicd-portafolio.pdf)

</div>

<div align="center" style="margin: 1rem 0;" markdown>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-08-despliegue-cicd-portafolio/notebook/clase-08-despliegue-cicd-portafolio.ipynb)
[![Abrir en Studio Local](https://img.shields.io/badge/Wisrovi_Studio-Abrir_en_Local_(127.0.0.1%3A8501)-0284c7?logo=python&logoColor=white)](http://127.0.0.1:8501/?course=4&class=8)
[![Ver en GitHub](https://img.shields.io/badge/GitHub-Ver_Carpeta_de_Clase-181717?logo=github&logoColor=white)](https://github.com/wisrovi/wisrovi-python/tree/main/04-proyecto-final/clase-08-despliegue-cicd-portafolio)

</div>

---

## 1. 💡 Fundamentación Teórica y Modelo Mental

Cierre magistral del programa de 32 semanas:
1. **GitHub Actions CI/CD**: Automatización de linting (`ruff`), testing (`pytest`), build de imágenes y despliegue.
2. **Zero-Downtime Deployment**: Estrategia de despliegue blue/green y validación de endpoints de salud (`/health`).
3. **Acreditación Final & Portafolio**: Generación del Diploma Maestro Oficial de 160 Horas avalado por William Rodríguez (Wisrovi).

!!! note "🌟 Modelo Mental de la Sesión: «La Cinta de Ensamblaje Automatizada hacia Producción»"
    En esta sesión anclamos el aprendizaje en la metáfora del mundo real para visualizar cómo fluyen las estructuras de datos y el flujo de ejecución en la memoria.

---

## 2. 🗺️ Arquitectura de Ejecución y Diagrama de Flujo

```mermaid
flowchart LR
    A["🐙 Git Push (main)"] --> B["🧪 CI Workflow (Pytest & Ruff)"]
    B --> C["🐳 Build Docker & Container Scan"]
    C --> D["🚀 CD Deploy to Cloud (FastAPI + Streamlit)"]
    D --> E["🏆 Master AI Engineer Certified (160h)"]
    style A fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style B fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style C fill:#d97706,color:#ffffff,stroke:#fbbf24,stroke-width:2px
    style D fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style E fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
```

---

## 3. 💻 Código de Implementación Práctica

=== "🚀 Demostración en Vivo"
    ```python
    class PipelineDespliegueDemo:
    def ejecutar(self, etapas: list[str]) -> bool:
        for e in etapas:
            print(f"-> Ejecutando etapa CI/CD: {e}... OK")
        return True

p = PipelineDespliegueDemo()
p.ejecutar(["lint", "test", "security_scan", "build", "deploy"])
    ```

=== "🔬 Arenero de Exploración de Memoria (RAM)"
    ```python
    print("🌟 ¡Has alcanzado la cima del Programa Integral de Formación en Python!")
print("🎓 32 Clases Completadas con Éxito.")
    ```

---

## 4. 🛡️ Buenas Prácticas PEP 8: Antipatrones vs Código Pythonic

!!! warning "⚠️ Cuidado con los Antipatrones"
    

=== "❌ Antipatrón / Código Inadecuado"
    ```python
    # Repositorio con 100 archivos .pyc y credenciales secretas ❌
    ```

=== "✅ Patrón Recomendado / Pythonic"
    ```python
    # Repositorio con .gitignore estándar de Python y variables en secretos de GitHub ✅
    ```

---

## 5. 🏋️ Desafío Práctico de la Clase

!!! example "🎯 Enunciado del Reto"
    **Crea una clase `PipelineDespliegue` con método `ejecutar_fases(self, fases: list[str]) -> dict` que valide que todas las fases requeridas ('lint', 'test', 'build', 'deploy') estén presentes en `fases`, retornando `{'status': 'success', 'fases_ejecutadas': len(fases), 'desplegado': True}` o `{'status': 'failed', 'desplegado': False}` si falta alguna.**

!!! tip "⚡ Resolución Híbrida en 1 Clic (Local + Web)"
    Si tienes ejecutando `wisrovi ui` en tu terminal local, puedes [🚀 Abrir este Reto directamente en tu Studio Local (127.0.0.1:8501)](http://127.0.0.1:8501/?course=4&class=8) para escribir tu código con auto-formateo AST, inspeccionar variables en el Heap/Stack y evaluarlo con pruebas en tiempo real.

=== "💻 Plantilla de Inicio (Starter Code)"
    ```python
    class PipelineDespliegue:
    def ejecutar_fases(self, fases: list[str]) -> dict:
        # ✍️ Valida que contenga lint, test, build y deploy
        requeridas = {"lint", "test", "build", "deploy"}
        if requeridas.issubset(set(fases)):
            return {
                "status": "success",
                "fases_ejecutadas": len(fases),
                "desplegado": True
            }
        return {
            "status": "failed",
            "desplegado": False
        }

    ```

??? info "💡 Pista Socrática 1"
    💡 Pista 1: Define `requeridas = {'lint', 'test', 'build', 'deploy'}`.

??? info "💡 Pista Socrática 2"
    💡 Pista 2: Verifica si `requeridas.issubset(set(fases))`.

??? info "💡 Pista Socrática 3"
    💡 Pista 3: Retorna `status: 'success'` si se cumplen todas las fases.



Para resolver este ejercicio en tu entorno:
1. Abre el archivo `ejercicios/reto.py` de esta clase en Visual Studio Code o utiliza `wisrovi ui` / `wisrovi tutor`.
2. Implementa tu solución cumpliendo los requisitos y contratos de tipado.
3. Valida tus resultados ejecutando las pruebas unitarias:
   ```bash
   pytest tests/curso_04/test_clase_08_despliegue_cicd_portafolio.py
   ```

---


## 6. 📚 Fuentes y Bibliografía Recomendada

*   [📖 Documentación Oficial de Python 3](https://docs.python.org/3/)
*   [📑 Guía de Estilo Oficial PEP 8](https://peps.python.org/pep-0008/)
*   [📦 Ecosistema Open Source wisrovi en PyPI](https://pypi.org/user/wisrovi/)
