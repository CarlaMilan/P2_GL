import sqlite3

try:
    conexion = sqlite3.connect('database/database.db') # Establecer conexión con bd
    cursor = conexion.cursor() # Crear cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments(
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    book_id INTEGER,
    content TEXT,
    created_at DATETIME,
    UNIQUE(user_id, book_id),  
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) 
    )
    ''')
    conexion.commit()
except Exception as ex:
    print(ex)

finally:
    conexion.close()