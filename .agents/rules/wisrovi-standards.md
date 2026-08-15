# 🏛️ Directrices Oficiales y Estándares de Arquitectura (Wisrovi Standards)

---

## 👤 1. Autoría Oficial
- **Nombre:** William Rodríguez (Wisrovi)
- **Cargo:** Principal Software Engineer & AI Solutions Architect
- **Sitio Web:** https://wisrovi.dev &bull; **GitHub:** https://github.com/wisrovi &bull; **PyPI:** https://pypi.org/user/wisrovi/

---

## 🌀 2. Modelo Pedagógico
- **Aprendizaje en Espiral (Spiral Learning):** Fase 1 (Visión Holística & Gancho Temprano) ➔ Fase 2 (Profundización & Rigor de Ingeniería) ➔ Fase 3 (Síntesis & Creación de Producto).
- **La Regla de la Bicicleta:** Más del 70% del tiempo es práctica activa (pedaleo en código, depuración, tests).
- **Modelos Mentales Explícitos:** Metáforas físicas cotidianas para cada concepto.

---

## 📝 3. Cobertura de Documentación
- **README Principal:** Portal completo con Hero, badges dinámicos, matriz curricular, perfiles y mapa del repositorio.
- **Regla de Cero Carpetas sin README:** Toda carpeta debe tener un `README.md` contextual y específico.
- **Diagramas Mermaid Nativos:** Alto contraste (`fill:#1e293b,color:#ffffff`), iconografía y saltos limpios con `<br/>`.

---

## 📖 4. Libros Digitales y PDFs LaTeX
- `book.md` con 6 capítulos obligatorios.
- Compilación de PDFs de 9 páginas con Google Chrome Headless (`tempfile.mkdtemp()`) y tipografía LaTeX.

---

## 🧹 5. Higiene del Repositorio
- Cero scripts `.py` sueltos en la raíz; todo script de soporte reside en `scripts/`.
- Tests unitarios exclusivamente centralizados en `/tests/`.
- Cuadernos interactivos en `clase-XX/notebook/` con badge a Google Colab.
