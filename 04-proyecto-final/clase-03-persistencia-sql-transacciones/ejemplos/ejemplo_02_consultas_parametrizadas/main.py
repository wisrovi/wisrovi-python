"""Consultas Parametrizadas Seguras."""
import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE t (v TEXT)')
conn.execute('INSERT INTO t VALUES (?)', ('seguro',))
print('Insert seguro.')
