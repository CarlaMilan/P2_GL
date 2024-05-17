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
        ("Sapiens: De animales a dioses", "Yuval Noah Harari", "No ficción", "2011-09-04"),
        ("El guardián entre el centeno", "J.D. Salinger", "Ficción", "1951-07-16"),
        ("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "1954-07-29"),
        ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "1997-06-26"),
        ("El hobbit", "J.R.R. Tolkien", "Fantasía", "1937-09-21"),
        ("Fahrenheit 451", "Ray Bradbury", "Distopía", "1953-10-19"),
        ("El poder de los hábitos", "Charles Duhigg", "Autoayuda", "2012-02-28"),
        ("Mi historia", "Michelle Obama", "Memorias", "2018-11-13"),
        ("El alquimista", "Paulo Coelho", "Aventura", "1988-01-01"),
        ("El código Da Vinci", "Dan Brown", "Suspenso", "2003-03-18"),
        ("La ladrona de libros", "Markus Zusak", "Ficción histórica", "2005-03-14"),
        ("La carretera", "Cormac McCarthy", "Post-apocalíptico", "2006-09-26"),
        ("Pensar rápido, pensar despacio", "Daniel Kahneman", "No ficción", "2011-10-25"),
        ("Una educación", "Tara Westover", "Memorias", "2018-02-20")
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