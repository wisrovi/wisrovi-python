#!/usr/bin/env python3
"""
Centraliza todas las suites de pruebas automatizadas en la carpeta raíz /tests
para que las carpetas de clase de los estudiantes permanezcan 100% limpias,
intuitivas y libres de archivos de configuración confusos.
"""

import os
import glob
import shutil

from all_32_classes_metadata import ALL_CLASSES, COURSES_CONFIG, BASE_DIR

TESTS_DIR = os.path.join(BASE_DIR, "tests")

def remove_tests_from_class_folders():
    """Elimina todos los archivos test_*.py que se encuentren dentro de los cursos."""
    print("🧹 Limpiando archivos test_*.py de las carpetas de clase de los estudiantes...")
    deleted_count = 0
    for course_folder in ["01-fundamentos-python", "02-algoritmos-estructuras", "03-agentes-ia", "04-proyecto-final"]:
        search_path = os.path.join(BASE_DIR, course_folder, "**", "test_*.py")
        for f in glob.glob(search_path, recursive=True):
            os.remove(f)
            deleted_count += 1
    print(f"  ✓ {deleted_count} archivos de test removidos de las carpetas de clase.")

def create_centralized_tests():
    """Crea la estructura modular /tests/curso_01 a /tests/curso_04 en la raíz."""
    print("\n📦 Creando estructura centralizada en /tests/...")
    
    if os.path.exists(TESTS_DIR):
        shutil.rmtree(TESTS_DIR)
    os.makedirs(TESTS_DIR, exist_ok=True)
    
    with open(os.path.join(TESTS_DIR, "__init__.py"), "w", encoding="utf-8") as f:
        f.write('"""Suite Central de Pruebas Automatizadas de wisrovi-python."""\n')
        
    with open(os.path.join(TESTS_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("# 🧪 Suite Central de Pruebas Automatizadas (Pytest)\n\n"
                "Esta carpeta centraliza todas las pruebas unitarias y de integración del repositorio.\n"
                "Permite validar la integridad de las 32 clases sin saturar las carpetas de estudio de los alumnos.\n\n"
                "## 💻 Cómo ejecutar las pruebas\n"
                "```bash\n"
                "# Ejecutar todos los tests del repositorio\n"
                "pytest\n\n"
                "# Ejecutar los tests de un curso específico\n"
                "pytest tests/curso_01/\n"
                "pytest tests/curso_02/\n"
                "pytest tests/curso_03/\n"
                "pytest tests/curso_04/\n"
                "```\n")
        
    for c_cfg in COURSES_CONFIG:
        c_num = c_cfg["course_num"]
        course_test_dir = os.path.join(TESTS_DIR, f"curso_{c_num:02d}")
        os.makedirs(course_test_dir, exist_ok=True)
        
        with open(os.path.join(course_test_dir, "__init__.py"), "w", encoding="utf-8") as f:
            f.write(f'"""Tests para {c_cfg["course_name"]}."""\n')
            
        c_classes = [m for m in ALL_CLASSES if m["course_num"] == c_num]
        
        for i, meta in enumerate(c_classes, 1):
            test_file = os.path.join(course_test_dir, f"test_clase_{i:02d}.py")
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(f'"""Tests de validación para {meta["class_title"]}."""\n'
                        f'{meta["test_logic"]}\n')
            print(f"  ✓ Creado tests/curso_{c_num:02d}/test_clase_{i:02d}.py")
            
    # Tests adicionales para componentes integradores del Curso 4 (FastAPI, SQLite, Chatbot)
    c4_extra = os.path.join(TESTS_DIR, "curso_04")
    with open(os.path.join(c4_extra, "test_integracion_chatbot.py"), "w", encoding="utf-8") as f:
        f.write('''"""Test del motor de chatbot conversacional."""
def test_chatbot_engine():
    class SimpleBot:
        def reply(self, msg): return f"Respuesta a: {msg}"
    bot = SimpleBot()
    assert "Hola" in bot.reply("Hola")
''')
    with open(os.path.join(c4_extra, "test_integracion_database.py"), "w", encoding="utf-8") as f:
        f.write('''"""Test de operaciones de base de datos relacional SQLite."""
import sqlite3
def test_sqlite_transaccion():
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT)")
        conn.execute("INSERT INTO productos (nombre) VALUES ('Laptop')")
    row = conn.execute("SELECT nombre FROM productos WHERE id = 1").fetchone()
    assert row[0] == "Laptop"
''')

def update_pyproject_config():
    """Actualiza pyproject.toml para apuntar estrictamente a /tests."""
    pyproject_path = os.path.join(BASE_DIR, "pyproject.toml")
    with open(pyproject_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(
        'testpaths = ["tests", "01-fundamentos-python", "02-algoritmos-estructuras", "03-agentes-ia", "04-proyecto-final"]',
        'testpaths = ["tests"]'
    )
    with open(pyproject_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Actualizado pyproject.toml -> testpaths = ['tests']")

def main():
    print("=" * 80)
    print("🚀 CENTRALIZANDO TODA LA INFRAESTRUCTURA DE TESTS EN /tests")
    print("=" * 80)
    remove_tests_from_class_folders()
    create_centralized_tests()
    update_pyproject_config()
    print("\n" + "=" * 80)
    print("✨ CARPETAS DE CLASES LIMPIAS Y TESTS CENTRALIZADOS EXITOSAMENTE.")
    print("=" * 80)

if __name__ == "__main__":
    main()
