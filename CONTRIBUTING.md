# 🤝 Guía de Contribución para Estudiantes y Desarrolladores

¡Te damos la bienvenida al proyecto **`wisrovi-python`**! Tu participación y contribuciones son el motor de esta comunidad de aprendizaje.

---

## 🚴‍♂️ Cómo Contribuir (Flujo de Trabajo Git)

1. **Haz un Fork del repositorio:**
   Haz clic en el botón `Fork` en la esquina superior derecha de GitHub.

2. **Clona tu copia localmente:**
   ```bash
   git clone https://github.com/TU-USUARIO/wisrovi-python.git
   cd wisrovi-python
   ```

3. **Crea una rama descriptiva para tu tarea:**
   ```bash
   git checkout -b solucion/curso-01-clase-03-mi-nombre
   ```

4. **Instala el entorno de desarrollo:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev,all]"
   ```

5. **Escribe tu solución y ejecuta las pruebas:**
   ```bash
   pytest
   ```

6. **Haz commit con mensajes claros (Conventional Commits):**
   ```bash
   git add .
   git commit -m "feat(c1): implementada solucion para evaluador de notas"
   ```

7. **Sube tu rama y abre un Pull Request:**
   ```bash
   git push origin solucion/curso-01-clase-03-mi-nombre
   ```
   Entra a GitHub y presiona **«Compare & pull request»**.

---

## 📜 Reglas de Estilo de Código

*   Todo el código debe cumplir con **PEP 8**.
*   Usa **type hints** en todas las funciones (`def func(x: int) -> str:`).
*   Documenta con **docstrings** claros el propósito de las funciones.
*   Asegúrate de que `pytest` pase al 100% antes de solicitar revisión.
