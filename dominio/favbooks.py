# domain/libros.py
from src.database.fav_books_repository import FavBooksRepository

class FavBooks:
    def __init__(self, user_id, book_id):
        self._user_id = user_id
        self._book_id = book_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def book_id(self):
        return self._book_id

    def __str__(self):
        cad = f"LIBRO FAVORITO\n"
        cad += f"ID usuario: {self._user_id}\n"
        cad += f"ID libro: {self._book_id}\n"
        return cad

    def save(self):
        return FavBooksRepository.add_fav(self.user_id, self.book_id)

    def delete(self):
        return FavBooksRepository.del_fav(self.user_id, self.book_id)
    @classmethod
    def get_filtered(cls, user_id):
        favs_data = FavBooksRepository.get_user_favs(user_id)
        print(favs_data)
        return [cls(user_id, book_id) for user_id, book_id in favs_data]
