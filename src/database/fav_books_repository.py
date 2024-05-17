import sqlite3
import os

class FavBooksRepository:
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')

    @staticmethod
    def connect():
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(FavBooksRepository.db_path)

    @staticmethod
    def add_fav(user_id, book_id):
        """
        Añade una relación favoritos a la base de datos.
        :param user_id: int - Usuario existente.
        :param book_id: int - Libro existente.
        :return: bool - True si el favorito se añadió correctamente, False en caso contrario.
        """
        conn = FavBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO fav_books (user_id, book_id) 
                VALUES (?, ?)
            ''', (user_id, book_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Error al añadir favorito:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def del_fav(user_id, book_id):
        """
        Elimina una relación favoritos de la base de datos.
        :param user_id: int - Usuario existente.
        :param book_id: int - Libro existente.
        :return: bool - True si el favorito se eliminó correctamente, False en caso contrario.
        """
        conn = FavBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                DELETE FROM fav_books WHERE user_id = ? AND book_id = 
                ''', (user_id, book_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Error al eliminar favorito:", e)
            return False
        finally:
            conn.close()

    @staticmethod
    def get_user_favs(user_id):
        """
        Obtiene los id de los libros favoritos de un usuario.
        :param user_id: int - ID del usuario.
        :return: list of tuples - Lista de IDs de libros favoritos del usuario.
        """
        conn = FavBooksRepository.connect()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT book_id FROM fav_books WHERE user_id=?', (user_id,))
            books = cursor.fetchall()
            return books
        finally:
            conn.close()


