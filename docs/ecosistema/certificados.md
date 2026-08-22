# 📜 Certificación Oficial y Diplomas Verificables

Al completar los cursos del programa formativo, los estudiantes obtienen diplomas oficiales de graduación con validez técnica y respaldo de **Wisrovi Academy**.

---

## 🏛️ Características del Diploma Oficial

```mermaid
flowchart TD
    STUDENT["👨‍💻 Estudiante"] --> COMPLETE["🏆 32 Clases Completadas"]
    COMPLETE --> GEN["📜 Motor de Certificación (certificate.py)"]
    GEN --> HASH["🔒 Hash Criptográfico SHA-256"]
    GEN --> PDF["📄 Compilación PDF (Chrome Headless A4 Landscape)"]
    PDF --> DIPLOMA["🎓 Diploma Oficial de 160 Horas"]

    style STUDENT fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#ffffff
    style COMPLETE fill:#059669,stroke:#34d399,stroke-width:2px,color:#ffffff
    style GEN fill:#581c87,stroke:#c084fc,stroke-width:2px,color:#ffffff
    style HASH fill:#78350f,stroke:#f59e0b,stroke-width:2px,color:#ffffff
    style PDF fill:#0f766e,stroke:#2dd4bf,stroke-width:2px,color:#ffffff
    style DIPLOMA fill:#b45309,stroke:#fbbf24,stroke-width:2px,color:#ffffff
```

- **Acreditación Horaria:** Diploma maestro de **160 horas de ingeniería práctica** o diplomas modulares por curso (40 horas cada uno).
- **Verificación Criptográfica:** Cada diploma incluye un identificador único generado mediante hash SHA-256 basado en el nombre del estudiante, el título del curso y la fecha de expedición.
- **Compilación de Alta Calidad:** Generado directamente en formato PDF apaisado (*Landscape*) con tipografía institucional, sellos dorados y estética LaTeX.
- **Badge Markdown para LinkedIn y GitHub:** Insignia interactiva lista para insertar en el perfil o README del alumno:
  ```markdown
  [![Wisrovi Certified](https://img.shields.io/badge/Wisrovi%20Academy-Certified%20AI%20Engineer-gold.svg)](https://academy_python.wisrovi.dev)
  ```

---

## 🚀 Emisión del Certificado

### Vía Interfaz Web (`wisrovi ui`)
1. Pulsa en el botón **`📜 Certificado`** en la barra superior.
2. Ingresa tu nombre completo.
3. Selecciona el curso o el **Programa Integral de 160 Horas**.
4. Haz clic en **`Descargar Certificado (PDF Oficial)`**.

### Vía Línea de Comandos (CLI)
```bash
wisrovi certificate --name "Alejandro Martínez" --output "mi_certificado.pdf"
```
