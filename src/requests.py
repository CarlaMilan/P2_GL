import pandas as pd
import sqlite3

try:
    conexion = sqlite3.connect('database/database.db') # Establecer conexión con bd
    cursor = conexion.cursor() # Crear cursor
    query = '''
    PRAGMA table_info(comments)
    '''
    cursor.execute(query)
    columns_info = cursor.fetchall()
    conexion.commit()
except Exception as ex:
    print(ex)

finally:
    for column in columns_info:
        print(f'Nombre: {column[1]}, Tipo: {column[2]}, No Nulo: {column[3]}, Default: {column[4]}')
    conexion.close()
