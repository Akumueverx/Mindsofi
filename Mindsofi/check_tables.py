import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Obtener todas las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print('Tablas en la base de datos:')
for table in tables:
    print(table[0])

# Cerrar conexión
conn.close()
