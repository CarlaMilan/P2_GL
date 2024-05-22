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
