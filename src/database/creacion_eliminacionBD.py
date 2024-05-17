import sqlite3
import os

'''
Este es el archivo que se encarga de crear la base de 
datos del proyecto empleando la biblioteca sqite3,
así como de eliminarla del proyecto y realizar consultas
básicas en la base de datos
'''
def creaDB(nombreBD="database.db"):
    try:
        # Crea o abre el archivo database.db con SQLite3
        db = sqlite3.connect(nombreBD)
        # Get a cursor object
        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR NOT NULL,
            password_hash VARCHAR NOT NULL,
            UNIQUE(username)
            )
            ''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            genre VARCHAR,
            publication_date DATE,
            cover_image BLOB,
            UNIQUE(title, author),
            FOREIGN KEY(genre) REFERENCES categories(category_id)
            )
            ''')


        cursor.execute('''CREATE TABLE IF NOT EXISTS fav_books(
            fav_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id VARCHAR,
            book_id VARCHAR,
            UNIQUE(user_id, book_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
            )
            ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS read_books(
            read_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            started_at DATE,
            finished_at DATE,
            RATING INT,
            UNIQUE(user_id, book_id)
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)  
            )
            ''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS comments(
            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            content TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
            )
            ''')

    except Exception as ex:
        db.rollback()
        print(ex)

    finally:
        # Cerrar conexión siempre
        db.close()

def eliminaDB(nombreBD="database.db"):
    try:
        db = sqlite3.connect(nombreBD)
        cursor = db.cursor()
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM books")
        cursor.execute("DELETE FROM fav_books")
        cursor.execute("DELETE FROM read_books")
        cursor.execute("DELETE FROM categories")
        cursor.execute("DELETE FROM comments")
        db.commit()
    except Exception as ex:
        # Roll back los cambios si devuelve algún error
        db.rollback()
        print(ex)
    finally:
        # Cerrar conexión siempre
        db.close()

def eliminaBD_total(nombreBD="database.db"):
    """
    Elimina la base de datos del sistema.
    """
    db_path = os.path.join(os.path.dirname(__file__), nombreBD)

    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"La base de datos '{nombreBD}' ha sido eliminada exitosamente.")
        except Exception as e:
            print(f"Error al intentar eliminar la base de datos '{nombreBD}': {e}")
    else:
        print(f"La base de datos '{nombreBD}' no existe.")


def introduceCategorías(nombreBD="database.db"):
    try:
        db = sqlite3.connect(nombreBD)
        cursor=db.cursor()
        cursor.execute("DELETE FROM categories")
        categorias = [
            (1, 'Ciencia Ficción'),
            (2, 'Fantasía'),
            (3, 'Romance'),
            (4, 'Misterio'),
            (5, 'Terror'),
            (6, 'Aventura'),
            (7, 'Historia'),
            (8, 'Poesía'),
            (9, 'Biografía'),
            (10, 'Autoayuda'),
            (11, 'Negocios'),
            (12, 'Arte'),
            (13, 'Cocina'),
            (14, 'Viajes'),
            (15, 'Humor'),
            (16, 'Religión'),
            (17, 'Ciencia'),
            (18, 'Educación'),
            (19, 'Deportes'),
            (20, 'Política'),
            (21, 'Distopía'),
            (22, 'Ficción'),
            (23, 'Ensayo'),
            (24, 'Memorias'),
            (25, 'Ficción histórica'),
            (26, 'Suspense'),
            (27, 'Post-apocalíptico')
        ]
        cursor.executemany(''' INSERT INTO categories(category_id, name) VALUES(?,?)''', categorias)
        db.commit()
    except Exception as ex:
        # Roll back any change if something goes wrong
        db.rollback()
        print(ex)
    finally:
        # Close the db connection
        db.close

import sqlite3

def insertar_libros():
    # Datos de libros de ejemplo
    libros = [
        ("Matar a un ruiseñor", "Harper Lee", "Ficción", "1960-07-11"),
        ("1984", "George Orwell", "Distopía", "1949-06-08"),
        ("Orgullo y prejuicio", "Jane Austen", "Romance", "1813-01-28"),
        ("El gran Gatsby", "F. Scott Fitzgerald", "Ficción", "1925-04-10"),
        ("Moby-Dick", "Herman Melville", "Aventura", "1851-10-18"),
        ("Hábitos atómicos", "James Clear", "Autoayuda", "2018-10-16"),
        ("Sapiens: De animales a dioses", "Yuval Noah Harari", "Ensayo", "2011-09-04"),
        ("El guardián entre el centeno", "J.D. Salinger", "Ficción", "1951-07-16"),
        ("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "1954-07-29"),
        ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "1997-06-26"),
        ("El hobbit", "J.R.R. Tolkien", "Fantasía", "1937-09-21"),
        ("Fahrenheit 451", "Ray Bradbury", "Distopía", "1953-10-19"),
        ("El poder de los hábitos", "Charles Duhigg", "Autoayuda", "2012-02-28"),
        ("Mi historia", "Michelle Obama", "Memorias", "2018-11-13"),
        ("El alquimista", "Paulo Coelho", "Aventura", "1988-01-01"),
        ("El código Da Vinci", "Dan Brown", "Suspense", "2003-03-18"),
        ("La ladrona de libros", "Markus Zusak", "Ficción histórica", "2005-03-14"),
        ("La carretera", "Cormac McCarthy", "Post-apocalíptico", "2006-09-26"),
        ("Pensar rápido, pensar despacio", "Daniel Kahneman", "Ensayo", "2011-10-25"),
        ("Una educación", "Tara Westover", "Memorias", "2018-02-20")
    ]

    try:
        # Establecer conexión con la base de datos
        conexion = sqlite3.connect('database.db')
        cursor = conexion.cursor()

        # Insertar libros en la tabla books
        cursor.executemany('''
        INSERT INTO books (title, author, genre, publication_date)
        VALUES (?, ?, ?, ?)
        ''', libros)

        # Confirmar los cambios
        conexion.commit()
        print("Libros insertados correctamente.")

    except Exception as ex:
        print(ex)

    finally:
        conexion.close()

