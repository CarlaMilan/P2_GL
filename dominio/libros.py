# domain/libros.py
from src.database.books_repository import BooksRepository

class Libro:
    def __init__(self, title, author, genre, publication_date):
        self._title = title
        self._author = author
        self._genre = genre
        self._publication_date = publication_date

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def publication_date(self):
        return self._publication_date

    @publication_date.setter
    def publication_date(self, value):
        self._publication_date = value


    def __str__(self):
        cad=f"Título: {self._title}\n"
        cad += f"Autor: {self._author}\n"
        cad += +f"Género: {self._genre}\n"
        cad += f"Fecha de publicación: {self._publication_date}\n"
        return cad

    def save(self):
        return BooksRepository.add_book(self._title, self._author, self._genre, self._publication_date)

    @classmethod
    def get_all(cls):
        books_data = BooksRepository.get_all_books()
        print(books_data)
        return [cls(title, author, genre, publication_date) for title, author, genre, publication_date in books_data]

    def get_random_book(self):
        return BooksRepository.get_random_book_cover()
