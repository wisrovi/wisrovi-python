"""Capa de Persistencia SQLite segura con consultas parametrizadas."""
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
