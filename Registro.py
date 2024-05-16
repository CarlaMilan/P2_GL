import pandas as pd
import json

'''class Libro:
    def __init__(self, titulo, autor, genero, descripcion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.descripcion = descripcion
        self.editorial = editorial


class GestorLecturas:
    def __init__(self, data):
        # Crear diccionadrio
        self.data = [{'Titulo': '', 'Autor': '', 'Genero': '', 'Descripcion': '', 'Editorial': ''}]

        # Crear dataframe desde el diccionario
        self.df = pd.DataFrame(self.data)

    def registrar_libro(self, libro):
        libro_nuevo = {'Titulo': libro.titulo,
                       'Autor': libro.autor,
                       'Genero': libro.genero,
                       'Descripcion': libro.descripcion,
                       'Editorial': libro.editorial}

        self.df = self.df.append(libro_nuevo)

        with open('libros.txt', 'w') as archivo_libros:
            archivo_libros.write(self.df)

        return f"El libro '{libro.titulo}' ha sido registrado exitosamente."'''


class Libro:
    def __init__(self, titulo, autor, genero, descripcion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.descripcion = descripcion
        self.editorial = editorial


class GestorLecturas:
    def __init__(self):
        # carga los libros desde el archivo, pero si no existe se crea una lista vacía
        try:
            with open('libros.txt', 'r') as archivo:
                self.lista_libros = json.load(archivo)
        except FileNotFoundError:
            self.lista_libros = []

    def guardar_en_archivo(self):
        # Guarda la lista de libros en el archivo de texto
        with open('libros.txt', 'w') as archivo:
            json.dump(self.lista_libros, archivo)

    def registrar_libro(self, libro):
        # Agrega el nuevo libro a la lista de libros
        self.lista_libros.append({
            'Titulo': libro.titulo,
            'Autor': libro.autor,
            'Genero': libro.genero,
            'Descripcion': libro.descripcion,
            'Editorial': libro.editorial
        })

        # Guarda la lista de libros en el archivo de texto
        self.guardar_en_archivo()

        return f"El libro '{libro.titulo}' ha sido registrado correctamente."

    def mostrar_libros(self):
        # convierte la lista de libros en un DataFrame con Pandas para visualizarlo
        df_libros = pd.DataFrame(self.lista_libros)
        return df_libros


