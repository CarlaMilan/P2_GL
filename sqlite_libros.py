import sqlite3

# Conectar a la base de datos
con = sqlite3.connect('libros.db')
cursor = con.cursor()

# Crear tabla de libros
cursor.execute('''CREATE TABLE IF NOT EXISTS biblioteca (
               id INTEGER PRIMARY KEY,
               titulo TEXT,
               notas TEXT,
               valoracion REAL,
               imagen BLOB
               )''')

libro1 = ('El señor de los anillos', 'kkkk', 4.5, b'\x89PNG\r\n\x1a\n\x00\x00...')
libro2 = ('Cien años de soledad', 'nota', 4.8, b'\x89PNG\r\n\x1a\n\x00\x00...')

cursor.execute('INSERT INTO biblioteca (titulo, notas, valoracion, imagen) VALUES (?, ?, ?, ?)', libro1)
cursor.execute('INSERT INTO biblioteca (titulo, notas, valoracion, imagen) VALUES (?, ?, ?, ?)', libro2)

con.commit()
con.close()


