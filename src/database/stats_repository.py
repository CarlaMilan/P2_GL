import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LibraryDataVisualizer:
    def __init__(self, db_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener ruta absoluta archivo actual
        db_path = os.path.join(script_dir, '..', 'database', 'database.db')
        self.conn = sqlite3.connect(db_path)

    def generos_mas_leidos(self, user_id):
        query = '''
           SELECT books.genre AS genre, COUNT(*) as count
           FROM read_books
           JOIN books ON read_books.book_id = books.book_id
           WHERE read_books.user_id = ?
           GROUP BY books.genre
           ORDER BY count DESC
           LIMIT 1;
           '''
        result = pd.read_sql_query(query, self.conn, params=(user_id,))
        return result

    def grafico_generos_mas_leidos(self, user_id, frame):
        # Obtener los datos para el gráfico
        data = self.generos_mas_leidos(user_id)

        # Crear el gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(data['genre'], data['count'], color='skyblue')
        ax.set_xlabel('Género')
        ax.set_ylabel('Número de libros leídos')
        ax.set_title('Géneros más leídos por la persona')

        # Integrar el gráfico con Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Agregar botón para cerrar el gráfico
        boton_cerrar = ttk.Button(frame, text="Cerrar Gráfico", command=lambda: self.cerrar_grafico(canvas, frame))
        boton_cerrar.pack(side=tk.BOTTOM, pady=10)

    def cerrar_grafico(self, canvas, frame):
        # Destruir el widget del gráfico
        canvas.get_tk_widget().destroy()
        # Olvidar el contenedor que contiene el gráfico y el botón de cerrar
        frame.pack_forget()

    def close_connection(self):
        self.conn.close()

    @staticmethod
    def visualizer():
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener ruta absoluta archivo actual
        db_path = os.path.join(script_dir, '..', 'database', 'database.db')
        visualizer = LibraryDataVisualizer(db_path)
        return visualizer
