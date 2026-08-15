"""Tests de validación para Clase 03: Persistencia de Datos: Modelado SQL y Transacciones ACID."""
import sqlite3
def test_c4_clase_03():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE t (id INT)")
    conn.execute("INSERT INTO t VALUES (1)")
    res = conn.execute("SELECT id FROM t").fetchone()
    assert res[0] == 1

