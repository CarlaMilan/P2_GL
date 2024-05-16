import sqlite3

def insertar_libros():
    # Datos de libros de ejemplo
    libros = [
        ("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960-07-11"),
        ("1984", "George Orwell", "Dystopian", "1949-06-08"),
        ("Pride and Prejudice", "Jane Austen", "Romance", "1813-01-28"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1925-04-10"),
        ("Moby-Dick", "Herman Melville", "Adventure", "1851-10-18")
    ]

    try:
        # Establecer conexión con la base de datos
        conexion = sqlite3.connect('database/database.db')
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
        # Cerrar la conexión
        conexion.close()

# Llamar a la función para insertar los libros
insertar_libros()