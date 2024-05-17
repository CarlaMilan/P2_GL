import sqlite3
import os

class BooksRepository:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    @staticmethod
    def connect():
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(BooksRepository.db_path)

    @staticmethod
    def add_book(title, author, genre, publication_date):
        """
        Añade un nuevo libro a la base de datos.
        :param title: str - Título del libro.
        :param author: str - Autor del libro.
        :param genre: str - Género del libro.
        :param publication_date: str - Fecha de publicación del libro.
        :return: bool - True si el libro se añadió correctamente, False en caso contrario.
        """
        conn = BooksRepository.connect()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                    INSERT INTO books (title, author, genre, publication_date) 
                    VALUES (?, ?, ?, ?)
                ''', (title, author, genre, publication_date))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Error al añadir el libro:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def get_all_books():
        """
        Recupera todos los libros de la base de datos.
        :return: list of tuples - Lista de libros.
        """
        conn = BooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT title, author, genre, publication_date FROM books')
            books = cursor.fetchall()
            return books
        finally:
            conn.close()

    @staticmethod
    def find_book_by_title(title_prefix):
        """
        Busca un libro por su título o prefijo del título
        :param title: str - Título del libro.
        :return: tuple or None - Datos del libro si se encuentra, None si no se encuentra.
        """
        conn = BooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM books WHERE title LIKE ?', (title_prefix + '%',))
            books = cursor.fetchall()
            return books
        finally:
            conn.close()

    @staticmethod
    def find_book_by_genre(genre):
        """
        Busca un libro por su género.
        :param genre: str - Nombre del género.
        :return: tuple or None - Datos del libro si se encuentra, None si no se encuentra.
        """
        conn = BooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                            SELECT * from books WHERE genre = ?
                        ''', (genre,))
            books = cursor.fetchall # Seleccionar todos los libros
            return books
        finally:
            conn.close()

    @staticmethod
    def get_books_by_ids(book_ids):
        """
        Obtiene la información de los libros correspondientes a los IDs proporcionados.
        :param book_ids: list of int - Lista de IDs de libros.
        :return: list of tuples - Información de los libros.
        """
        conn = BooksRepository.connect()
        cursor = conn.cursor()
        try:
            query = '''
                SELECT title, author, genre
                FROM books
                WHERE book_id IN ({})
            '''.format(', '.join(['?'] * len(book_ids)))
            cursor.execute(query, book_ids)
            books = cursor.fetchall()
            return books

        finally:
            conn.close()

    @staticmethod
    def get_random_book_cover():
        conn = BooksRepository.connect()
        cursor = conn.cursor()

        # Consulta SQL para seleccionar un libro aleatorio
        cursor.execute("SELECT book_cover FROM libros ORDER BY RANDOM() LIMIT 1")

        # Obtener el resultado de la consulta
        libro_aleatorio = cursor.fetchone()

        # Cerrar la conexión a la base de datos
        conn.close()
        return libro_aleatorio







