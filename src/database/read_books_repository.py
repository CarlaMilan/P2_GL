import sqlite3
from datetime import datetime
import os

class ReadBooksRepository:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    @staticmethod
    def connect():
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(ReadBooksRepository.db_path)

    @staticmethod
    def add_read(user_id, book_id, started_at, finished_at, rating):
        """
        Añade una relación favoritos a la base de datos.
        :param user_id: int - Usuario existente.
        :param book_id: int - Libro existente.
        :param started_at: date - Fecha de comienzo de lectura
        :param finished_at: date - Fecha de final de lectura
        :param rating: int
        :return: bool - True si el favorito se añadió correctamente, False en caso contrario.
        """
        conn = ReadBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO read_books (user_id, book_id, started_at, finished_at, rating) 
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, book_id, started_at, finished_at, rating))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Error al añadir libro:", e)
            return False
        finally:
            conn.close()
    @staticmethod
    def start_reading(user_id,book_id):
        conn = ReadBooksRepository.connect()
        cursor = conn.cursor()
        started_at = datetime.now()
        try:
            cursor.execute('''
                INSERT INTO read_books (user_id, book_id, started_at) 
                VALUES (?, ?, ?)
            ''', (user_id, book_id, started_at))
            conn.commit()
            print(' Leyendo... fncsql')
            return True
        except sqlite3.IntegrityError as e:
            print("Error al leer libro:", e)
            return False
        finally:
            conn.close()
    @staticmethod
    def get_user_reading(user_id):
        """
        Obtiene los id de los libros sin terminar de un usuario.
        :param user_id: int - ID del usuario.
        :return: list of tuples - Lista de IDs de libros no terminados del usuario.
        """
        conn = ReadBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT book_id FROM read_books WHERE user_id=?', (user_id,))
            books = cursor.fetchall()
            return books
        finally:
            conn.close()

    @staticmethod
    def get_user_read(user_id):
        """
        Obtiene los id de los libros leídos de un usuario.
        :param user_id: int - ID del usuario.
        :return: list of tuples - Lista de IDs de libros no terminados del usuario.
        """
        conn = ReadBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM read_books WHERE user_id=?AND finished_at IS NOT NULL', (user_id,))
            books = cursor.fetchall()
            return books
        finally:
            conn.close()




