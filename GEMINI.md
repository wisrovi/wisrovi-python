# 🏛️ Directrices Oficiales y Estándares de Arquitectura (Wisrovi Standards)

Este archivo establece las reglas universales, directrices pedagógicas, estándares de documentación y políticas de código que **TODO asistente de Inteligencia Artificial o desarrollador** debe cumplir estrictamente al operar en este repositorio.

---

## 👤 1. Autoría Oficial y Perfil del Mentor
- **Nombre:** William Rodríguez (Wisrovi)
- **Cargo:** Principal Software Engineer & AI Solutions Architect
- **Ubicación:** Badajoz, España
- **Sitio Web:** https://wisrovi.dev
- **GitHub:** https://github.com/wisrovi
- **LinkedIn:** https://www.linkedin.com/in/wisrovi-rodriguez/
- **DockerHub:** https://hub.docker.com/u/wisrovi
- **PyPI Suite:** https://pypi.org/user/wisrovi/ (Más de 26 paquetes publicados de optimización, bases de datos y orquestación)

---

## 🌀 2. Pedagogía: Aprendizaje en Espiral & La Regla de la Bicicleta

### Aprendizaje en Espiral (Spiral Learning)
Los conceptos nunca se enseñan de forma aislada ni abstracta, sino en ciclos iterativos de complejidad creciente:
1. **Fase 1 (Visión Holística & Gancho Temprano):** El estudiante ve los componentes clave funcionando juntos desde el primer día (`print`, `variables`, `if/else`, `for`, `def`).
2. **Fase 2 (Profundización Modular & Rigor de Ingeniería):** Se estudian modelos de memoria (heap/stack), tipos inmutables, complejidad Big-O, estructuras avanzadas, gotchas y buenas prácticas (PEP 8).
3. **Fase 3 (Síntesis & Creación de Producto):** Integración en aplicaciones reales, desarrollo de Agentes de IA y proyectos de portafolio Full-Stack.

### La Regla de la Bicicleta
- Más del **70% del tiempo debe ser práctica activa ("pedaleo")**.
- El verdadero aprendizaje ocurre al escribir código por cuenta propia, provocar errores deliberados para entender las trazas y superar pruebas unitarias automatizadas.

### Modelos Mentales Explícitos
Toda clase y módulo debe anclarse en una metáfora del mundo real (*El Megáfono*, *Las Cajas*, *El Semáforo*, *La Cinta Transportadora*, *La Licuadora*, etc.).

---

## 📝 3. Estándar de Documentación y Cobertura de READMEs

1. **README Principal (Raíz):**  
   Debe ser siempre un portal de clase mundial con Hero Section, badges interactivos (`for-the-badge`), resumen ejecutivo, perfil del autor verificado, tabla matriz del currículo con enlaces a libros y PDFs, quickstart en 1 clic (Codespaces) y local, mapa del repositorio y licencia MIT.
2. **Regla de Cero Carpetas sin README:**  
   Absolutamente **toda carpeta y subcarpeta existente** en el repositorio (incluyendo `ejemplos/`, cada ejemplo individual, `ejercicios/`, `notebook/`, `tests/`, `src/`, `scripts/`, `docs/`) debe contener su respectivo `README.md` explicativo y contextual.
3. **Cero Boilerplate Repetitivo:**  
   Prohibido copiar y pegar textos genéricos repetitivos ("Modelo de Aprendizaje Activo") en las subcarpetas. Cada README debe ser específico, directo al grano y describir el código exacto de su carpeta.
4. **Diagramas Mermaid Nativos:**  
   Todo `README.md`, `book.md` y página de documentación debe incluir al menos un diagrama Mermaid (`flowchart LR` o `flowchart TD`) con estilo de alto contraste (`fill:#1e293b,color:#ffffff,stroke:#...`), sin saltos de línea con `\n` (usar `<br/>` o etiquetas limpias) para garantizar renderizado perfecto en GitHub y MkDocs.

---

## 📖 4. Libros Digitales (`book.md`) y Manuales PDF

1. **Libros Digitales (`book.md`):**  
   Cada clase y curso debe disponer de su archivo `book.md` con 6 capítulos obligatorios:
   * **Capítulo 1:** *Fundamentación Teórica & Metáfora Central*
   * **Capítulo 2:** *Arquitectura de Flujo con Diagrama Mermaid*
   * **Capítulo 3:** *Implementación Práctica Comentada*
   * **Capítulo 4:** *Buenas Prácticas, Antipatrones vs Patrones Pythonic y Gotchas*
   * **Capítulo 5:** *Conclusiones, Notas del Mentor y Mensaje de Agradecimiento*
   * **Capítulo 6:** *Bibliografía Canónica y Reto de Autoestudio*
2. **Generación de PDFs con Estética LaTeX:**  
   * Compilados automáticamente mediante Google Chrome Headless (`--headless --disable-gpu --no-sandbox --print-to-pdf=<dest> <temp.html>`).
   * El archivo HTML temporal se genera y procesa en un directorio temporal (`tempfile.mkdtemp()`) y se elimina tras la compilación.
   * Estética tipográfica tipo LaTeX (Computer Modern / Latin Modern / Georgia, 9 páginas por clase, portada elegante con badge de versión, paginación en pie de página y tipografía justificada con márgenes profesionales).

---

## 🌐 5. Plataforma Web Documental (MkDocs Material / GitHub Pages)

- Carpeta `docs/` sincronizada con el portal web interactivo ([`academy_python.wisrovi.dev`](https://academy_python.wisrovi.dev/)).
- `mkdocs.yml` configurado con tema Material, paleta dual claro/oscuro, soporte de Mermaid nativo, tabs de código, admonitions (`!!! note`, `!!! tip`, `!!! warning`, `!!! example`) y búsqueda instantánea.
- Archivo `docs/CNAME` con el subdominio del proyecto (`academy_python.wisrovi.dev`).
- Flujo GitHub Actions en `.github/workflows/docs.yml` con `fetch-depth: 0` y credenciales de bot para despliegue sin fallos.

---

## 🧹 6. Higiene del Repositorio y Arquitectura Limpia

1. **Raíz 100% Limpia:** Ningún script `.py` de mantenimiento o compilación debe residir en la raíz del repositorio. Todo script de soporte debe vivir en `scripts/` con su propio `scripts/README.md`.
2. **Tests Centralizados:** Las suites de pruebas automatizadas (`pytest`) deben residir exclusivamente en `/tests/` para no ensuciar las carpetas de trabajo del estudiante.
3. **Cuadernos Jupyter:** Ubicados en subcarpetas `notebook/` dentro de cada clase con su propio `README.md` y badge interactivo a Google Colab.
