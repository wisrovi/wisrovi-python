"""Creación de Tablas DDL."""
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE t (id INT)')
print('Tabla creada.')
