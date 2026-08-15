# 🏛️ Wisrovi Academy Core Library (`wisrovi_lib`)

El paquete **`wisrovi_lib`** es el motor central que impulsa el **Tutor Virtual Interactivo**, el sistema de **Gamificación RPG**, el **Inspector de Memoria Heap/Stack** y el **Generador Oficial de Certificados en PDF**.

---

## 🗺️ Arquitectura de la Librería

```mermaid
flowchart TD
    CLI["🖥️ CLI: wisrovi ui / tutor"] --> SRV["🌐 Servidor Web FastAPI (server.py)"]
    
    SRV --> GAM["🎮 GamificationEngine (gamification.py)<br/>• XP, Niveles 1-4, Insignias & Rachas<br/>• Persistencia en ~/.wisrovi/student_profile.json"]
    SRV --> TUT["📚 TutorEngine (tutor_engine.py)<br/>• Currículo de 32 Clases y 4 Cursos<br/>• Metáforas del Mundo Real & Diagramas"]
    SRV --> MEM["🔬 MemoryInspector (memory_inspector.py)<br/>• Inspección de Memoria Heap en tiempo real<br/>• Direcciones Hex, Tipos e Inmutabilidad"]
    SRV --> RUN["🧪 CodeRunner (code_runner.py)<br/>• Ejecución Segura & Pytest Evaluator<br/>• Pistas Socráticas del Mentor"]
    SRV --> CERT["📜 CertificateGenerator (certificate.py)<br/>• Diplomas Oficiales en PDF (Landscape)<br/>• Hash de Verificación Criptográfica"]

    style CLI fill:#1e293b,color:#ffffff,stroke:#3b82f6,stroke-width:2px
    style SRV fill:#0f766e,color:#ffffff,stroke:#2dd4bf,stroke-width:2px
    style GAM fill:#581c87,color:#ffffff,stroke:#c084fc,stroke-width:2px
    style TUT fill:#0284c7,color:#ffffff,stroke:#38bdf8,stroke-width:2px
    style MEM fill:#1e3a8a,color:#ffffff,stroke:#60a5fa,stroke-width:2px
    style RUN fill:#059669,color:#ffffff,stroke:#34d399,stroke-width:2px
    style CERT fill:#78350f,color:#ffffff,stroke:#f59e0b,stroke-width:2px
```

---

## 📦 Módulos Principales

| Módulo | Archivo | Responsabilidad |
| :--- | :--- | :--- |
| **Gamificación** | [`gamification.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/gamification.py) | Administra los perfiles de usuario, XP, desbloqueo de insignias y niveles. |
| **Currículo & Pedagogía** | [`tutor_engine.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/tutor_engine.py) | Proveedor estructurado de conceptos, código, metáforas y retos de las 32 clases. |
| **Inspector de Memoria** | [`memory_inspector.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/memory_inspector.py) | Mapea variables, direcciones hexadecimales (`id`), tamaños en RAM y mutabilidad. |
| **Ejecutor & Evaluador** | [`code_runner.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/code_runner.py) | Evalúa retos en vivo contra la suite de Pytest y genera sugerencias socráticas. |
| **Certificación PDF** | [`certificate.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/certificate.py) | Compila diplomas oficiales apaisados de alta resolución vía Chrome Headless. |
| **Servidor & Frontend** | [`server.py`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/server.py) & [`static/`](file:///home/wisrovi/Documents/wisrovi-python/src/wisrovi_lib/static/) | API REST y aplicación web Single-Page Application (SPA) para el estudiante. |

---

## 🚀 Uso Programático (`import wisrovi_lib`)

```python
from wisrovi_lib import MemoryInspector, CertificateGenerator, GamificationEngine

# 1. Inspeccionar objetos en memoria RAM
res = MemoryInspector.execute_and_inspect("x = 42; y = 'Wisrovi'")
print(res["memory_variables"])

# 2. Generar un certificado de graduación
CertificateGenerator.generate_pdf(
    student_name="Alejandro Martínez",
    output_pdf_path="mi_certificado.pdf",
    hours=160
)
```
