"""Transacciones con Commit / Rollback."""
import sqlite3
conn = sqlite3.connect(':memory:')
with conn: conn.execute('CREATE TABLE x (id INT)')
print('Transacción completada.')
