#!/usr/bin/env python3
"""
Genera ejemplos de código ejecutables y suites de tests con pytest con nombres únicos y modulares.
"""

import os
import glob

BASE_DIR = "/home/wisrovi/Documents/wisrovi-python"

def clean_old_tests():
    for f in glob.glob(f"{BASE_DIR}/**/test_*.py", recursive=True):
        os.remove(f)

def populate_course_1_tests():
    """Crea tests pytest para los ejercicios del Curso 1."""
    
    # Clase 1
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-01-panorama-general/ejercicios/test_c1_ejercicio_01.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_01():
    res = subprocess.run([sys.executable, '01-fundamentos-python/clase-01-panorama-general/ejercicios/ejercicio_01_mi_primer_vistazo.py'], capture_output=True, text=True)
    assert res.returncode == 0
    assert "¡Hola!" in res.stdout
""")

    # Clase 2
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-02-variables-y-tipos/ejercicios/test_c1_ejercicio_02.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_02():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-02-variables-y-tipos/ejercicios/ejercicio_02_perfil_usuario.py'],
        input="Madrid\\n4.50\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Ciudad: Madrid" in res.stdout
    assert "Total por 5 bebidas: $22.50" in res.stdout
""")

    # Clase 3
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-03-control-flujo-condicionales/ejercicios/test_c1_ejercicio_03.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_03():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-03-control-flujo-condicionales/ejercicios/ejercicio_03_evaluador_notas.py'],
        input="95\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Excelente (A)" in res.stdout
""")

    # Clase 4
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-04-control-flujo-bucles/ejercicios/test_c1_ejercicio_04.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_04():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-04-control-flujo-bucles/ejercicios/ejercicio_04_tabla_multiplicar.py'],
        input="7\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "7 x 10 = 70" in res.stdout
""")

    # Clase 5
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-05-listas-y-colecciones/ejercicios/test_c1_ejercicio_05.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_05():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-05-listas-y-colecciones/ejercicios/ejercicio_05_gestion_inventario.py'],
        input="Zapatos\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Zapatos" in res.stdout
""")

    # Clase 6
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-06-diccionarios/ejercicios/test_c1_ejercicio_06.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_06():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-06-diccionarios/ejercicios/ejercicio_06_agenda_contactos.py'],
        input="Carlos\\n987654\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Carlos: 987654" in res.stdout
""")

    # Clase 7
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-07-funciones/ejercicios/test_c1_ejercicio_07.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_07():
    res = subprocess.run(
        [sys.executable, '01-fundamentos-python/clase-07-funciones/ejercicios/ejercicio_07_calculadora.py'],
        input="100\\n20\\n",
        capture_output=True,
        text=True
    )
    assert res.returncode == 0
    assert "Final: $80.00" in res.stdout
""")

    # Clase 8
    with open(f"{BASE_DIR}/01-fundamentos-python/clase-08-proyecto-integrador-basico/ejercicios/test_c1_ejercicio_08.py", "w") as f:
        f.write("""import subprocess, sys

def test_ejercicio_08():
    res = subprocess.run([sys.executable, '01-fundamentos-python/clase-08-proyecto-integrador-basico/ejercicios/ejercicio_08_reto_final.py'], capture_output=True, text=True)
    assert res.returncode == 0
    assert "FELICIDADES" in res.stdout
""")

def populate_course_2():
    c2 = f"{BASE_DIR}/02-algoritmos-estructuras"
    
    # 01
    with open(f"{c2}/01-estructuras-datos-avanzadas/ejercicios/test_c2_m01_parentesis.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_01_validador_parentesis import son_parentesis_validos

def test_parentesis_validos():
    assert son_parentesis_validos("()") is True
    assert son_parentesis_validos("()[]{}") is True
    assert son_parentesis_validos("{[()]}") is True
    assert son_parentesis_validos("(]") is False
    assert son_parentesis_validos("([)]") is False
""")

    # 02
    with open(f"{c2}/02-algoritmos-ordenamiento-busqueda/ejercicios/test_c2_m02_quicksort.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_02_quicksort import quicksort

def test_quicksort():
    assert quicksort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 3, 3]) == [3, 3, 3]
""")

    # 03
    with open(f"{c2}/03-recursividad-optimizacion/ejercicios/test_c2_m03_caminos.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_03_caminos_cuadricula import caminos_unicos

def test_caminos_unicos():
    assert caminos_unicos(3, 7) == 28
    assert caminos_unicos(3, 2) == 3
    assert caminos_unicos(1, 1) == 1
""")

def populate_course_3():
    c3 = f"{BASE_DIR}/03-agentes-ia"
    
    # 01
    with open(f"{c3}/01-fundamentos-ia-llm/ejercicios/test_c3_m01_pydantic.py", "w") as f:
        f.write("""import sys, os, pytest
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_01_extractor_contacto import validar_contacto
from pydantic import ValidationError

def test_contacto_valido():
    json_data = '{"nombre_completo": "Carlos Ruiz", "email": "carlos@test.com"}'
    c = validar_contacto(json_data)
    assert c.nombre_completo == "Carlos Ruiz"
    assert c.empresa == "Independiente"

def test_contacto_invalido():
    with pytest.raises(ValidationError):
        validar_contacto('{"nombre_completo": 123}')
""")

    # 02
    with open(f"{c3}/02-herramientas-y-memoria/ejercicios/test_c3_m02_similitud.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_02_similitud_coseno import similitud_coseno

def test_similitud_identica():
    assert round(similitud_coseno([1.0, 0.0], [1.0, 0.0]), 2) == 1.0

def test_similitud_ortogonal():
    assert round(similitud_coseno([1.0, 0.0], [0.0, 1.0]), 2) == 0.0
""")

    # 03
    with open(f"{c3}/03-construccion-de-agentes/ejercicios/test_c3_m03_agente.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from ejercicio_03_agente_validador import AgentePresupuesto

def test_agente_aprobado():
    ag = AgentePresupuesto(1000.0)
    res = ag.evaluar_gasto([{"nombre": "A", "monto": 200.0}])
    assert res["aprobado"] is True

def test_agente_rechazado():
    ag = AgentePresupuesto(500.0)
    res = ag.evaluar_gasto([{"nombre": "A", "monto": 600.0}])
    assert res["aprobado"] is False
""")

def populate_course_4():
    c4 = f"{BASE_DIR}/04-proyecto-final/plantillas"
    
    with open(f"{c4}/02-chatbot-inteligente/test_c4_chatbot.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from bot_engine import ChatEngine

def test_chatbot_respuestas():
    bot = ChatEngine("Asistente")
    r1 = bot.get_response("u1", "Quiero saber el precio")
    assert "$19/mes" in r1
    r2 = bot.get_response("u1", "Necesito soporte")
    assert "soporte@empresa.com" in r2
""")

    p3 = f"{c4}/03-sistema-gestion-bd"
    with open(f"{p3}/database.py", "w") as f:
        f.write('''"""Capa de Persistencia SQLite segura con consultas parametrizadas."""
import sqlite3

class BaseDeDatos:
    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    stock INTEGER NOT NULL,
                    precio REAL NOT NULL
                )
            """)

    def insertar(self, nombre: str, stock: int, precio: float) -> int:
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
                (nombre, stock, precio)
            )
            return cursor.lastrowid

    def listar(self) -> list[tuple]:
        cursor = self.conn.cursor()
        return cursor.execute("SELECT id, nombre, stock, precio FROM productos").fetchall()

    def cerrar(self):
        self.conn.close()
''')

    with open(f"{p3}/test_c4_database.py", "w") as f:
        f.write("""import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from database import BaseDeDatos

def test_database_crud():
    db = BaseDeDatos(":memory:")
    prod_id = db.insertar("Monitor", 10, 199.99)
    assert prod_id == 1
    items = db.listar()
    assert len(items) == 1
    assert items[0][1] == "Monitor"
""")

def main():
    clean_old_tests()
    populate_course_1_tests()
    populate_course_2()
    populate_course_3()
    populate_course_4()
    print("✓ Tests reorganizados con nombres de módulo únicos.")

if __name__ == "__main__":
    main()
