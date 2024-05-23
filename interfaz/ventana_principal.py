import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from functools import partial  # Para pasar argumentos a funciones de callback
from src.database.books_repository import BooksRepository
from src.database.fav_books_repository import FavBooksRepository
from dominio.favbooks import FavBooks
from src.database.read_books_repository import ReadBooksRepository
from src.database.users_repository import UsersRepository
from src.database.stats_repository import LibraryDataVisualizer
import time


class FavBooksApp:

    def __init__(self, usuario):
        self.usuario = usuario

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title(f"FavBook de {self.usuario}")
        self.ventana_principal.iconbitmap('logo.ico')
        # Dimensiones y posición para centrar la ventana en la pantalla
        ancho_ventana = 1000
        alto_ventana = 800
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (alto_ventana // 2)
        self.ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Configuración del color de fondo
        self.ventana_principal.configure(bg='#D19AFF')


        # Botón para abrir el buscador de libros
        boton_buscador = tk.Button(self.ventana_principal, text="Buscar Libro", command=self.abrir_buscador)
        boton_buscador.pack(pady=10)

        # Etiqueta de bienvenida
        self.et_bienvenida = tk.Label(self.ventana_principal, text=f'FavBook de {self.usuario}',
                                      font=('Trebuchet MS', 18), bg='#D19AFF')
        self.et_bienvenida.pack(pady=10)

        # Etiqueta para mostrar la hora
        self.et_hora = tk.Label(self.ventana_principal, text=self.obtener_hora())
        self.et_hora.pack()

        self.boton_frame = tk.Frame(self.ventana_principal)
        self.boton_frame.pack(fill=tk.BOTH, expand=True)

        # Crear un botón para mostrar el gráfico
        self.boton_mostrar_grafico = tk.Button(self.boton_frame, text="Libros leídos por género",
                                                command=self.mostrar_grafico)
        self.boton_mostrar_grafico.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        # Crear un frame para el gráfico
        self.frame_grafico = tk.Frame(self.ventana_principal)
        self.frame_grafico.pack(fill=tk.BOTH, expand=True)

        # Crear instancia de LibraryDataVisualizer
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener ruta absoluta archivo actual
        db_path = os.path.join(script_dir, '..', 'database', 'database.db')
        self.visualizer = LibraryDataVisualizer('db_path')

        # Sección de libros recomendados
        self.seccion_recomendados = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE, height=180)
        self.seccion_recomendados.pack_propagate(False)
        self.seccion_recomendados.pack(fill=tk.BOTH, padx=10, pady=10)

        libros = self.recomendar_libros()
        for librorec in libros:
            self.librrec = tk.Label(self.seccion_recomendados, text=f"{librorec}", font=('Trebuchet MS', 14))
            self.librrec.pack(padx=5, pady=5)

        self.et_recomendados = tk.Label(self.seccion_recomendados, text="Libros Recomendados", font=('Trebuchet MS', 14))

        self.et_recomendados.pack(pady=5)

        # Sección de lista de favoritos
        self.seccion_favoritos = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE, height=190)
        self.seccion_favoritos.pack_propagate(False)
        self.seccion_favoritos.pack(fill=tk.BOTH, padx=10, pady=5)

        self.et_favoritos = tk.Label(self.seccion_favoritos, text="Lista de Favoritos", font=('Trebuchet MS', 14))
        self.et_favoritos.pack(pady=5)
        us = UsersRepository.search_user(self.usuario)
        favs = FavBooksRepository.get_user_favs(us[0])
        libro = BooksRepository.get_random_book_cover()
        ids = []
        for id in favs:
            ids.append(id[0])
        librosfavs = BooksRepository.get_books_by_ids(ids)  # Tenemos los libros favoritos del usuario
        counter = 0
        varpos = 0
        varps = 0
        for librofav in librosfavs:
            if counter < 4:
                self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
                self.librofav.pack(pady=1)
            elif 4 <= counter < 8:
                self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
                self.librofav.place(x=10, y=33 + varpos)
                varpos += 40
            elif counter >= 8:
                self.librofav = tk.Label(self.seccion_favoritos, text=f"{librofav[0]}", font=('Trebuchet MS', 14))
                self.librofav.place(x=800, y=33 + varps)
                varps += 40

            counter += 1

        # Sección de lista de leídos
        self.seccion_leidos = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE, height=180)
        self.seccion_leidos.pack_propagate(False)
        self.seccion_leidos.pack(fill=tk.BOTH, padx=10, pady=10)

        self.et_leidos = tk.Label(self.seccion_leidos, text="Estás leyendo: ", font=('Trebuchet MS', 14))
        self.et_leidos.pack(pady=5)

        bdleidos = ReadBooksRepository.get_user_reading(us[0])
        librosids = []
        for idlibro in bdleidos:
            librosids.append(idlibro[0])
        librosleidos = BooksRepository.get_books_by_ids(librosids) # Obtenemos los libros leidos por el usuario
        counter0 = 0
        varpos0 = 0
        varps0 = 0
        for libroleido in librosleidos:
            if counter0 < 4:
                self.libroleido = tk.Label(self.seccion_leidos, text=f"{libroleido[0]}", font=('Trebuchet MS', 14))
                self.libroleido.pack(pady=1)
            elif 4 <= counter0 < 8:
                self.libroleido = tk.Label(self.seccion_leidos, text=f"{libroleido[0]}", font=('Trebuchet MS', 14))
                self.libroleido.place(x=10, y=33 + varpos0)
                varpos0 += 37
            elif counter0 >= 8:
                self.libroleido = tk.Label(self.seccion_leidos, text=f"{libroleido[0]}", font=('Trebuchet MS', 14))
                self.libroleido.place(x=800, y=33 + varps0)
                varps0 += 37
            counter0 += 1



        self.actualizar_hora()

        self.ventana_principal.mainloop()

    def obtener_hora(self):
        hora_actual = time.strftime("%H:%M:%S")
        return hora_actual

    def actualizar_hora(self):
        # Actualizar la hora cada segundo
        self.et_hora.config(text=self.obtener_hora())
        self.ventana_principal.after(1000, self.actualizar_hora)

    def abrir_buscador(self):
        # Crear una nueva ventana para el buscador
        ventana_buscador = tk.Toplevel(self.ventana_principal)
        ventana_buscador.title("Buscar Libro")
        ventana_buscador.iconbitmap('logo.ico')
        # Campo de entrada para el título del libro
        label_titulo = tk.Label(ventana_buscador, text="Título del libro:")
        label_titulo.pack()
        entry_titulo = tk.Entry(ventana_buscador)
        entry_titulo.pack()

        # Función de búsqueda
        buscar_libro = partial(self.buscar_libro, entry_titulo, ventana_buscador)

        # Botón de búsqueda
        boton_buscar = tk.Button(ventana_buscador, text="Buscar", command=buscar_libro)
        boton_buscar.pack()

    def mostrar_grafico(self):
        user_id = UsersRepository.search_user(self.usuario)
        user_id = user_id[0]
        v = LibraryDataVisualizer.visualizer()
        # Llamar a la función para mostrar el gráfico
        v.grafico_generos_mas_leidos(user_id=user_id, frame=self.frame_grafico)

    def buscar_libro(self, entry_titulo, ventana_buscador):
        # Obtener el título ingresado por el usuario
        titulo = entry_titulo.get()
        if titulo:
            # Llamar a la función para buscar el libro en la base de datos
            resultados = BooksRepository.find_book_by_title(titulo)

            # Mostrar los resultados en una ventana emergente
            if resultados:
                ventana_resultados = tk.Toplevel(ventana_buscador)
                ventana_resultados.title("Resultados de la búsqueda")
                ventana_resultados.iconbitmap('logo.ico')

                # Crear una etiqueta para mostrar los resultados
                etiqueta_resultados = tk.Label(ventana_resultados, text="Resultados de la búsqueda:")
                etiqueta_resultados.pack()

                # Mostrar cada resultado en una nueva línea
                for libro in resultados:
                    # Crear una etiqueta para mostrar el resultado
                    etiqueta_libro = tk.Label(ventana_resultados, text=libro)
                    etiqueta_libro.pack()
                    # Botón para marcar como favorito
                    boton_favorito = tk.Button(ventana_resultados, text="Marcar como Favorito",
                                               command=lambda libro=libro: self.marcar_favorito(libro))
                    boton_favorito.pack()
                    global bookid
                    bookid = libro[0]
                    global userid
                    userid = UsersRepository.search_user(self.usuario)[0]
                    boton_empezarlibro = tk.Button(ventana_resultados, text="Leer",
                                                   command=lambda userid=userid, bookid=bookid: self.empezar_lectura(userid, bookid))
                    boton_empezarlibro.pack()

            else:
                messagebox.showinfo("Búsqueda", "No se encontraron resultados para el título proporcionado.")

    def redimensionar_imagen(self, file, size1, size2):
        imagen_original = Image.open(file)

        # Redimensiona la imagen a un tamaño específico
        nuevo_ancho = size1  # Ancho deseado
        nuevo_alto = size2  # Alto deseado
        imagen_original.thumbnail((nuevo_ancho, nuevo_alto))

        # Convierte la imagen redimensionada a un objeto PhotoImage de tkinter
        icono_redimensionado = ImageTk.PhotoImage(imagen_original)
        return icono_redimensionado

    def marcar_favorito(self, libro):
        libro = list(libro)
        us = UsersRepository.search_user(self.usuario) # Obtener id usuario actual
        ins = FavBooks(us[0], libro[0])
        try:
            ins.save() # Guardar en favoritos
            messagebox.showinfo("Añadido a favorito")
        except Exception as e:
            messagebox.showerror("Error")



    def recomendar_libros(self):
        libros = []
        for i in range(0,3):
            libro = BooksRepository.get_random_book_cover()
            libros.append(libro[0])
        return list(libros)

    def empezar_lectura(self, userid, bookid):
        try:
            ReadBooksRepository.start_reading(userid, bookid)
            messagebox.showinfo("Leyendo...")
        except Exception as e:
            messagebox.showerror("Error")
