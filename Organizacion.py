#permite organizar y buscar los libros según el género, id y título

import sqlite3
import os

class BooksRepository:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    @staticmethod
    def connect():
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(BooksRepository.db_path)

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
            books = cursor.fetchall  # Seleccionar todos los libros
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
