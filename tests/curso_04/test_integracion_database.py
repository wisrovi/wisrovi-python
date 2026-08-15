"""Test de operaciones de base de datos relacional SQLite."""
import sqlite3
def test_sqlite_transaccion():
    conn = sqlite3.connect(":memory:")
    with conn:
        conn.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT)")
        conn.execute("INSERT INTO productos (nombre) VALUES ('Laptop')")
    row = conn.execute("SELECT nombre FROM productos WHERE id = 1").fetchone()
    assert row[0] == "Laptop"
