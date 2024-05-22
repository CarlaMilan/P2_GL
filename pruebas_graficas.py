import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


class LibraryDataVisualizer:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def generos_mas_leidos(self, user_id):
        query = f'''
        SELECT books.genre AS genre, COUNT(*) as count
        FROM read_books
        JOIN books ON read_books.book_id = books.book_id
        WHERE read_books.user_id = {user_id}
        GROUP BY books.genre
        ORDER BY count DESC
        LIMIT 1;
        '''
        result = pd.read_sql_query(query, self.conn)
        print("Generos más leídos:", result)
        return result

    def libros_leidos_mes(self, user_id):
        query = f'''
        SELECT strftime('%Y-%m', read_books.started_at) as month, COUNT(*) as count
        FROM read_books
        WHERE read_books.user_id = {user_id}
        GROUP BY month
        ORDER BY month;
        '''
        result = pd.read_sql_query(query, self.conn)
        print("Libros leídos por mes:", result)
        return result

    def ranking_valoracion(self):
        query = '''
        SELECT read_books.rating, COUNT(*) as count
        FROM read_books
        GROUP BY read_books.rating
        ORDER BY read_books.rating;
        '''
        result = pd.read_sql_query(query, self.conn)
        print("Ranking de valoración:", result)
        return result

    def grafico_generos_mas_leido(self, user_id):
        genre_data = self.generos_mas_leidos(user_id)
        plt.figure(figsize=(10, 6))
        plt.bar(genre_data['genre'], genre_data['count'], color='skyblue')
        plt.xlabel('Género')
        plt.ylabel('Número de libros leídos')
        plt.title('Género más leído por la persona')
        plt.show()

    def grafico_libros_leidos_mes(self, user_id):
        monthly_data = self.libros_leidos_mes(user_id)
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_data['month'], monthly_data['count'], marker='o', linestyle='-', color='skyblue')
        plt.xlabel('Mes')
        plt.ylabel('Número de libros leídos')
        plt.title('Número de libros leídos por mes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def grafico_ranking_valoracion(self):
        rating_data = self.ranking_valoracion()
        plt.figure(figsize=(10, 6))
        plt.bar(rating_data['rating'], rating_data['count'], color='skyblue')
        plt.xlabel('Valoración')
        plt.ylabel('Número de libros')
        plt.title('Distribución de las valoraciones de los libros')
        plt.show()

    def close_connection(self):
        self.conn.close()


# Uso de la clase LibraryDataVisualizer
visualizer = LibraryDataVisualizer('src/database/database.db')

# ID del usuario para el que queremos generar las gráficas
user_id = 3

# Generar las gráficas
visualizer.grafico_generos_mas_leido(user_id)
# visualizer.grafico_libros_leidos_mes(user_id)
# visualizer.grafico_ranking_valoracion()

# Cerrar la conexión a la base de datos
visualizer.close_connection()


