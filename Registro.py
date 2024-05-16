import pandas as pd
import json


class Libro:
    def __init__(self, titulo, autor, genero, descripcion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.descripcion = descripcion
        self.editorial = editorial


class GestorLecturas:
    def __init__(self, wishlist):
        self.wishlist = [{'Titulo': '', 'Autor': '', 'Genero': '', 'Descripcion': '', 'Editorial': ''}]
        with open('libros.txt', 'r') as archivo:
                self.lista_libros = json.load(archivo)

    def guardar_en_archivo(self):
        # Guarda la lista de libros en el archivo de texto
        with open('libros.txt', 'w') as archivo:
            json.dump(self.wishlist, archivo)

    def registrar_libro(self, libro):
        with open('libros.txt', 'r') as archivo:
            self.lista_libros = json.load(archivo)

        # Agrega el nuevo libro a la lista de libros
        if libro in self.lista_libros:
            self.wishlist.append(self.libro)

        else:
            return f'El libro {libro.titulo} no esta disponible.'

        # Guarda la lista de libros en el archivo de texto
        self.guardar_en_archivo()

        return f"El libro '{libro.titulo}' ha sido registrado correctamente."

    def mostrar_libros(self):
        # convierte la lista de libros en un DataFrame con Pandas para visualizarlo
        df_libros = pd.DataFrame(self.wishlist)
        return df_libros




