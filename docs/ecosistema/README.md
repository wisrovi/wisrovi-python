# 🖥️ Ecosistema Interactivo & Tutor Virtual (`wisrovi_lib`)

El ecosistema de **`wisrovi-python`** incluye una plataforma integral de aprendizaje activo con interfaz gráfica local, motor de tutoría socrática con IA, inspector de memoria RAM Heap/Stack en tiempo real, gamificación RPG y generación de diplomas oficiales en PDF.

---

## 🗺️ Arquitectura del Ecosistema

```mermaid
flowchart TD
    CLI["🖥️ Comandos CLI<br/>(wisrovi ui / wisrovi tutor)"] --> API["🌐 Servidor Web FastAPI (Local: 8501)"]
    API --> UI["💻 Wisrovi Studio Diamond Edition (SPA)"]
    
    UI --> SPLIT["📖 Split Screen (Doc Web Embebida Alt+D)"]
    UI --> S1["1️⃣ Concepto & Micro-Quiz (+25 XP)"]
    UI --> S2["2️⃣ Demo & Patrones Pythonic PEP 8"]
    UI --> S3["3️⃣ Arenero & Inspector RAM Heap/Stack"]
    UI --> S4["4️⃣ Reto Evaluado en Vivo & Speed Bonus"]
    UI --> TUT["👨‍🏫 Consola Docente (Speaker Notes & Timer)"]
    
    API --> GAM["🎮 Motor de Gamificación<br/>(XP Dinámica, Niveles 1-4, Insignias)"]
    API --> CERT["📜 Certificados Oficiales PDF<br/>(Hash SHA-256 & Chrome Headless)"]

    style CLI fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
    style API fill:#0f766e,stroke:#2dd4bf,stroke-width:2px,color:#ffffff
    style UI fill:#1e1e2e,stroke:#a855f7,stroke-width:2px,color:#ffffff
    style SPLIT fill:#0284c7,stroke:#38bdf8,stroke-width:1px,color:#ffffff
    style S1 fill:#0369a1,stroke:#38bdf8,stroke-width:1px,color:#ffffff
    style S2 fill:#047857,stroke:#34d399,stroke-width:1px,color:#ffffff
    style S3 fill:#1d4ed8,stroke:#60a5fa,stroke-width:1px,color:#ffffff
    style S4 fill:#b45309,stroke:#f59e0b,stroke-width:1px,color:#ffffff
    style TUT fill:#581c87,stroke:#c084fc,stroke-width:1px,color:#ffffff
    style GAM fill:#581c87,stroke:#c084fc,stroke-width:2px,color:#ffffff
    style CERT fill:#78350f,stroke:#fbbf24,stroke-width:2px,color:#ffffff
```

---

## 📑 Secciones del Ecosistema

| Documento | Descripción |
| :--- | :--- |
| [🎓 Tutor Virtual & Wisrovi Studio](tutor-virtual.md) | Diferencias entre `wisrovi ui` y `wisrovi tutor`, modo proyector, split view web y flujo de 4 pasos. |
| [🎮 Gamificación, XP y Progresión](gamificacion.md) | Sistema de XP dinámico por velocidad, niveles 1 a 4, insignias, bloqueo secuencial y modo repaso. |
| [📜 Certificación Oficial en PDF](certificados.md) | Emisión de diplomas apaisados de 160 horas con verificación criptográfica SHA-256. |
