import sqlite3
import os

# Conectar a la base de datos SQLite (creará el archivo si no existe)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Leer el archivo SQL convertido
with open('bd mindsofi/sqlite_schema.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

# Ejecutar el script SQL
cursor.executescript(sql_script)

# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()

print("Esquema SQLite creado exitosamente en db.sqlite3")
