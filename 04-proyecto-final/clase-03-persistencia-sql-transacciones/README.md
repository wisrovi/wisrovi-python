# 📘 Clase 03: Persistencia de Datos: Modelado SQL y Transacciones ACID

> **Curso:** Curso 4: Taller Práctico & Proyecto Final Integrador (CLASE 03)  
> **Nivel:** Nivel 4 - Integrador &bull; **Metáfora:** *«La Base de Datos como una Bóveda Acorazada para la Información»*  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wisrovi/wisrovi-python/blob/main/04-proyecto-final/clase-03-persistencia-sql-transacciones/notebook/clase-03-persistencia-sql-transacciones.ipynb)

---

## 🗺️ Diagrama de Arquitectura y Flujo de la Clase

```mermaid
flowchart TD
    TX["Inicio: with conn: (Transacción ACID)"] --> DDL["CREATE TABLE / Migración"]
    DDL --> SEC["Consultas Parametrizadas Seguras (?)"]
    SEC -->|Sin errores| CMT["Commit Automático a Disco"]
    SEC -->|Excepción| RBK["Rollback Automático (Consistencia Protegida)"]

    style TX fill:#1e293b,color:#fff,stroke:#3b82f6,stroke-width:2px
    style DDL fill:#0f766e,color:#fff,stroke:#2dd4bf,stroke-width:2px
    style SEC fill:#b45309,color:#fff,stroke:#f59e0b,stroke-width:2px
    style CMT fill:#065f46,color:#fff,stroke:#34d399,stroke-width:2px
    style RBK fill:#881337,color:#fff,stroke:#fb7185,stroke-width:2px
```

---

## 📑 Recursos Disponibles en esta Clase

*   📄 [`clase-03-persistencia-sql-transacciones.pdf`](clase-03-persistencia-sql-transacciones.pdf): Manual técnico oficial en PDF (9 páginas).
*   📖 [`book.md`](book.md): Libro de estudio digital con teoría profunda y diagramas Mermaid.
*   📁 [`notebook/`](notebook/): Cuaderno interactivo Jupyter ejecutable en local y en Google Colab.
*   📁 [`ejemplos/`](ejemplos/): Carpetas de código funcional con casos prácticos comentados.
*   📁 [`ejercicios/`](ejercicios/): Reto práctico para afianzar conceptos.
