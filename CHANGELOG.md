# 📋 Registro de Cambios (CHANGELOG)

Todos los cambios notables en el proyecto **`wisrovi-python`** serán documentados cronológicamente en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y este proyecto se adhiere al estándar de [Versionado Semántico (SemVer)](https://semver.org/lang/es/).

---

## [2.5.1] - 2026-08-23 (Universal LinkedIn Sharing Hub & Enhanced Master Modal)

### 🌟 Añadido (New Features)
- **Centro Universal de Publicación en LinkedIn en el Modal Master (`#cert-modal`):**
  - Incorporación del panel completo de publicación con texto enriquecido dinámico para el Master Diploma de 160h y certificados de curso individuales.
  - Botón de 1-clic `[🚀 PUBLICAR EN LINKEDIN (Texto + Imagen)]` con descarga automática del diploma PNG y copia al portapapeles.
  - Barra de compartición directa en redes sociales con LinkedIn destacado junto a WhatsApp y 𝕏 (Twitter).

---

## [2.5.0] - 2026-08-23 (Master-Class UI Studio, Dual-Column Memory Inspector & CLI Suite)

### 🌟 Añadido (New Features)
- **Inspector de Memoria Dual (Stack vs Heap con IDs Criptográficos y Tamaños en Bytes):**
  - Separación arquitectónica visual entre variables primitivas inmutables (Stack) y estructuras de datos/objetos (Heap).
  - Inspección de direcciones en memoria hexadecimales y consumo exacto en bytes (`sys.getsizeof`).
- **Persistencia Continua en LocalStorage (`Auto-Save Drafts`):**
  - Guardado en segundo plano de borradores de código para Demo, Sandbox y Retos por cada una de las 32 clases, evitando cualquier pérdida accidental de código.
- **Suite Avanzada de Comandos en CLI (`wisrovi`):**
  - `wisrovi profile` / `wisrovi stats`: Matriz interactiva de progreso curricular, barra de XP, nivel y vitrina de insignias en la terminal.
  - `wisrovi cert`: Generación y exportación de micro-diplomas y master diploma en PDF/PNG directamente por línea de comandos.
  - `wisrovi book <curso> <clase>`: Visor en consola del libro digital canónico con renderizado Markdown.
- **Suite de Pruebas Centralizada (55 Tests Pytest):**
  - Cobertura completa de endpoints, contratos de tipado, motor de gamificación, CLI y generador de certificados.

---

## [2.4.0] - 2026-08-23 (32 Micro-Class Credentials, 1-Click LinkedIn Publishing & Navigation Engine)

### 🌟 Añadido (New Features)
- **Motor de Micro-Acreditaciones Oficiales por Clase (32 Diplomas de Clase):**
  - Generación de diplomas individuales para cada una de las 32 clases del programa con competencias técnicas personalizadas, evidencia de ingeniería, código de verificación criptográfica hash SHA-256 y firma del mentor William Rodríguez (Wisrovi).
  - Exportación automática a **PDF estilo LaTeX** y captura en **PNG de alta resolución (1200x850)** mediante Chrome Headless.
- **Suite de Publicación en 1-Clic para LinkedIn (`🚀 Publicar en LinkedIn`):**
  - Botón permanente en Navbar, Modal de Celebración de Retos y Modal de Certificados.
  - Copia automática de publicación enriquecida al portapapeles, descarga automática del diploma en formato PNG para adjuntar como imagen, apertura directa de LinkedIn Feed y banner interactivo de guía paso a paso.
  - Atribución oficial y enlace al perfil del mentor William Rodríguez (Wisrovi).

### 🛠️ Correcciones y Mejoras (Bug Fixes & Improvements)
- **Desacoplamiento de Estado en la Transición de Lecciones:** Corregida la mutación en `fetchProfile()` que calculaba saltos erróneos de clase tras superar un reto.
- **Optimización de Calidad y Linter en CI Matrix:** Reglas de `ruff` y `pytest` ajustadas para garantizar 100% de éxito en GitHub Actions en Python 3.10, 3.11 y 3.12.

---

## [2.3.0] - 2026-08-22 (Presentation Slide Deck, Drag Resizer & Local Disk Sync)

### 🌟 Añadido (New Features)
- **Motor de Diapositivas en Pantalla Completa (Slide Deck Presentation Engine):**
  - Nuevo botón `📽️ Diapositivas` y atajo rápido <kbd>F</kbd> en Modo Tutor para proyectar conferencias y clases magistrales con tarjetas dinámicas de gran formato:
    - *Slide 1:* Portada, nivel, título y narrativa de la Metáfora Central.
    - *Slide 2:* Flujo arquitectónico renderizado en Diagrama Mermaid nativo de alto contraste.
    - *Slide 3:* Demostración en vivo con tipado estricto Python 3.12+.
    - *Slide 4:* Comparativa de ingeniería: Antipatrón vs Solución Idiomática Pythonic (PEP 8).
    - *Slide 5:* Reto práctico del estudiante (*La Regla de la Bicicleta*) y botón de salto al editor.
  - Navegación fluida por teclado con <kbd>←</kbd>, <kbd>→</kbd> y <kbd>Espacio</kbd>, además de soporte para modo pantalla completa nativo (`F11` / botón ⛶).
- **Divisor Ajustable y Redimensionable en Pantalla Dividida (Drag Resizer Divider):**
  - Pestaña de arrastre interactiva (`#docs-resize-handle`) en el panel de documentación web para ajustar horizontalmente el ancho entre el 25% y el 75% del visor.
- **Sincronización y Guardado Directo a Disco Local (`💾 Guardar en Disco`):**
  - Nuevo endpoint `@app.post("/api/save-solution")` y botón en el editor del Paso 4 que escribe directamente la solución del estudiante en `ejercicios/reto.py` dentro de la carpeta correspondiente del workspace.
- **Nuevos Atajos Globales de Teclado:**
  - <kbd>Alt + LeftArrow</kbd> y <kbd>Alt + RightArrow</kbd> para alternar instantáneamente entre clases previas y siguientes.
- **Ampliación de Pruebas Automatizadas:** 50 pruebas unitarias con 100% de éxito en Pytest.

---

## [2.2.1] - 2026-08-22 (JS Runtime & Presentation Navigation Fix)

### 🐛 Corregido (Bug Fixes)
- **Eliminación de saltos de línea sin escapar en literales JavaScript:** Se corrigieron cadenas multilinea en la función `renderPythonicTip()`, snippets del arenero y mensajes de alerta (`alert`) migrándolos a *Template Literals* (backticks `` `...` ``), eliminando el error fatal `SyntaxError: Invalid or unexpected token` que detenía la ejecución del script en el navegador.
- **Enlace Inmediato de Eventos (`setupEvents`):** Se reorganizó el ciclo de inicio (`initApp`) para registrar todos los escuchadores de eventos (botones de diplomas, panel de documentación dividida, atajos y modales) de forma síncrona e inmediata al cargar el DOM.
- **Navegación Desbloqueada para el Docente en Modo Tutor:** Se corrigió el botón *Siguiente Clase* (`dom.nextBtn`) en `updateStepperUI()` para garantizar que permanezca habilitado y permita al mentor recorrer libremente las 32 lecciones sin requerir la resolución de retos previos.

---

## [2.2.0] - 2026-08-22 (Teacher Lecture Deck & Hybrid Web Bridge Edition)

### 🌟 Añadido
- **Redefinición de `wisrovi tutor` como Consola Docente y Modo Presentador en Vivo (Lecture Deck):**
  - **Acceso Maestro Desbloqueado (Master Mode):** Acceso libre e inmediato a las 32 clases de los 4 cursos sin restricciones de gamificación estudiantil, permitiendo al mentor impartir cualquier lección a demanda.
  - **Modo Proyector de Gran Formato (📺):** Escala tipográfica ampliada (20px-28px) de alto contraste optimizada para proyectores de aula y transmisiones en vivo (Zoom, Meet, YouTube).
  - **Live Coding Canvas en Directo:** Editor interactivo integrado para ejecutar, modificar parámetros, demostrar *edge cases* y formatear código PEP 8 ante los alumnos sin necesidad de salir a VS Code.
  - **Panel de Notas Pedagógicas del Mentor (Speaker Notes):** Guión didáctico con la historia de la metáfora central, preguntas socráticas para dinamizar la sesión y advertencias sobre los errores y trampas más frecuentes.
  - **Temporizador de Reto para el Aula (Classroom Timer):** Cronómetro digital gigante proyectable con presets (3m, 5m, 10m, 15m, 20m), controles de reproducción/pausa/reinicio, efectos sonoros de alarma y lluvia de confeti al concluir el tiempo.
- **Integración Híbrida Web-to-Local (Deep Linking & CORS Bridge):**
  - Botones de enlace directo en cada página de la documentación en GitHub Pages (`academy_python.wisrovi.dev`):
    - `🚀 Abrir Reto en Wisrovi Studio (127.0.0.1:8501)` -> `http://127.0.0.1:8501/?course=X&class=Y`.
    - `👨‍🏫 Presentar en Modo Tutor` -> `http://127.0.0.1:8501/tutor?course=X&class=Y`.
  - Soporte de enrutamiento por parámetros de URL (`?course=X&class=Y` y `?mode=tutor`) en la SPA embebida para auto-cargar lecciones directamente.
  - Habilitación de `CORSMiddleware` en el servidor FastAPI para comunicación entre la web estática y el backend local.
  - Conmutador en el encabezado global para alternar al instante entre `👨‍🏫 Modo Presentador` y `👨‍💻 Modo Estudiante`.
- **Suite de Pruebas Automatizadas:**
  - 48 pruebas unitarias en `pytest` pasando al 100% en `0.81s`, incluyendo la validación de endpoints del Modo Maestro y la entrega de Speaker Notes.

---

## [2.1.0] - 2026-08-22 (Master Diamond Edition)

### 🌟 Añadido
- **Currículo Completo de 32 Clases en 4 Cursos Oficiales:**
  - **Curso 1 (Fundamentos Básicos):** 8 clases completas con metáforas, teoría, diagramas Mermaid, demos y retos evaluados.
  - **Curso 2 (Algoritmos Avanzados & Big-O):** Pilas/Colas con `deque`, Hash Sets O(1), Búsqueda Binaria, QuickSort, Árboles BST, Grafos BFS/DFS y Programación Dinámica (Memoización `@lru_cache`).
  - **Curso 3 (Agentes de Inteligencia Artificial):** Modelos LLM, Prompt Engineering, validación Pydantic V2, Tool Calling, Embeddings vectoriales y similitud coseno, RAG semántico, Agentes ReAct y Sistemas Multi-Agente con orquestación.
  - **Curso 4 (Taller Práctico & Proyecto Integrador Full-Stack):** Clean Architecture, Backend FastAPI REST, SQLite ACID con transacciones, Frontend reactivo Streamlit, Integración de Agentes, Testing Pytest con Mocks, Docker Multi-Stage y CI/CD Pipeline.
- **Sistema de Progresión Secuencial Lineal (*Linear Progression Gate*):**
  - Restricción estricta anti-saltos: El alumno no puede acceder a lecciones avanzadas sin haber superado previamente las clases anteriores en orden lineal.
  - Bloqueo secuencial de cursos completos (el Curso 2 requiere completar las 8 clases del Curso 1; el Curso 3 requiere el Curso 2; el Curso 4 requiere el Curso 3).
- **Modo Repaso y Práctica Libre Permanente:**
  - Todas las lecciones previamente completadas quedan marcadas como accesibles (`✓ Repasar`), permitiendo re-ejecutar demostraciones, explorar el arenero de memoria y reevaluar retos cuantas veces se desee sin alterar la progresión.
  - Badge visual dinámico en la Hero Card (`🔄 Modo Repaso y Práctica Libre`).
- **Sistema Dinámico de Experiencia (XP) con Bonificación por Velocidad (*Speed Bonus*):**
  - **⚡ Rápido (< 5 min):** +50 XP bonus (Total: 200 XP) + Insignia `speedster`.
  - **🎯 Óptimo (5 - 15 min):** +25 XP bonus (Total: 175 XP).
  - **⏳ Estándar (15 - 30 min):** Base 150 XP.
  - **🐢 Exploración Lenta (> 30 min):** 120 XP (penalización pedagógica por tiempo excesivo).
- **Auto-Formateador de Código PEP 8 en 1 Clic (`/api/format-code`):**
  - Normalización sintáctica instantánea vía Python AST (`ast.parse` y `ast.unparse`) en el Arenero y en el Editor de Retos.
- **Micro-Quizzes Conceptuales Interactivos (`/api/quiz/evaluate`):**
  - Evaluaciones breves de opción múltiple en el Paso 1 con retroalimentación explicativa inmediata y recompensa de **+25 XP**.
- **Comparador Visual de Patrones Pythonic vs Antipatrones:**
  - Comparativa lado a lado en el Paso 2 entre estilos C-like/antipatrones y código canónico limpio según directrices PEP 8.
- **RAM Memory Inspector 3.0 (Heap vs Stack):**
  - Visualizador en vivo con desglose de direcciones hexadecimales (`id(obj)`), tamaño exacto en bytes (`sys.getsizeof`), etiquetas de inmutabilidad y conteo de referencias.
- **Suite de Pruebas Automatizadas para los 32 Retos:**
  - 46 pruebas unitarias e integrales en `pytest` cubriendo los 4 cursos, motores de gamificación, certificados criptográficos y lógica de progresión.

### 🔄 Cambiado
- **Interfaz de Usuario (`wisrovi ui` / `wisrovi tutor`):**
  - Barra de pestañas superiores con navegación directa entre los 4 cursos.
  - Alertas pedagógicas contextuales al hacer clic sobre lecciones o módulos bloqueados indicando la lección exacta requerida.
  - Selector de 4 temas visuales (*Midnight Cyber*, *Obsidian OLED*, *Matrix Emerald*, *Solar Gold*).
  - Paleta de comandos interactiva con <kbd>Ctrl+K</kbd> y modal de atajos de teclado.
- **Comandos CLI (`wisrovi start` y `wisrovi list`):**
  - Soporte global para los cursos 1, 2, 3 y 4.
  - Verificación del estado de desbloqueo en `~/.wisrovi/student_profile.json` antes de iniciar la sesión de trabajo.

---

## [2.0.0] - 2026-08-20

### 🌟 Añadido
- **Wisrovi Interactive Studio v10.0:** Interfaz SPA sin dependencias externas compilada en un único archivo HTML servido por FastAPI.
- **Gamificación RPG:** Sistema de niveles (1-4), títulos de maestría, rachas diarias, insignias desbloqueables y persistencia JSON.
- **Generador de Certificados Oficiales en PDF:** Diplomas profesionales apaisados con hash de verificación criptográfica SHA-256 compilados mediante Google Chrome Headless.
- **Tutor Virtual Socrático:** Diálogo didáctico contextual basado en metáforas del mundo real (*El Megáfono*, *Las Cajas*, *El Semáforo*, *La Cinta Transportadora*).

---

## [1.0.0] - 2026-08-15

### 🌟 Añadido
- Lanzamiento inicial del paquete **`wisrovi-python`** en PyPI.
- Estructura curricular de 32 semanas basada en la pedagogía de **Aprendizaje en Espiral** y **La Regla de la Bicicleta**.
- CLI oficial `wisrovi` con comandos `start`, `test`, `list`, `help`.
- Suites de pruebas unitarias con `pytest`.
- Documentación técnica y plataforma web desplegada en MkDocs Material.
