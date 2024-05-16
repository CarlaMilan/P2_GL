import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


class LibraryDataVisualizer:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get_genre_most_read_by_user(self, user_id):
        query = f'''
        SELECT books.genre, COUNT(*) as count
        FROM readings
        JOIN books ON readings.book_id = books.id
        WHERE readings.user_id = {user_id}
        GROUP BY books.genre
        ORDER BY count DESC
        LIMIT 1;
        '''
        return pd.read_sql_query(query, self.conn)

    def get_books_read_per_month(self, user_id):
        query = f'''
        SELECT strftime('%Y-%m', readings.date) as month, COUNT(*) as count
        FROM readings
        WHERE readings.user_id = {user_id}
        GROUP BY month
        ORDER BY month;
        '''
        return pd.read_sql_query(query, self.conn)

    def get_book_ratings_distribution(self):
        query = '''
        SELECT books.rating, COUNT(*) as count
        FROM books
        GROUP BY books.rating
        ORDER BY books.rating;
        '''
        return pd.read_sql_query(query, self.conn)

    def plot_genre_most_read_by_user(self, user_id):
        genre_data = self.get_genre_most_read_by_user(user_id)
        plt.figure(figsize=(10, 6))
        plt.bar(genre_data['genre'], genre_data['count'], color='skyblue')
        plt.xlabel('Género')
        plt.ylabel('Número de libros leídos')
        plt.title('Género más leído por la persona')
        plt.show()

    def plot_books_read_per_month(self, user_id):
        monthly_data = self.get_books_read_per_month(user_id)
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_data['month'], monthly_data['count'], marker='o', linestyle='-', color='skyblue')
        plt.xlabel('Mes')
        plt.ylabel('Número de libros leídos')
        plt.title('Número de libros leídos por mes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_book_ratings_distribution(self):
        rating_data = self.get_book_ratings_distribution()
        plt.figure(figsize=(10, 6))
        plt.bar(rating_data['rating'], rating_data['count'], color='skyblue')
        plt.xlabel('Valoración')
        plt.ylabel('Número de libros')
        plt.title('Distribución de las valoraciones de los libros')
        plt.show()

    def close_connection(self):
        self.conn.close()


# Uso de la clase LibraryDataVisualizer
visualizer = LibraryDataVisualizer('biblioteca.db')

# ID del usuario para el que queremos generar las gráficas
user_id = 1

# Generar las gráficas
visualizer.plot_genre_most_read_by_user(user_id)
visualizer.plot_books_read_per_month(user_id)
visualizer.plot_book_ratings_distribution()

# Cerrar la conexión a la base de datos
visualizer.close_connection()

