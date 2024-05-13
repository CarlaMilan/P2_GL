import pandas as pd

class Libro:
    def __init__(self, titulo, autor, genero, descripcion, editorial):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.descripcion = descripcion
        self.editorial = editorial


class GestorLecturas:
    def __init__(self, data):
        # Crear diccionadrio
        self.data = [{'Titulo': '', 'Autor': '', 'Genero': '', 'Descripcion': '', 'Editorial': ''},
                     {'Titulo': '', 'Autor': '', 'Genero': '', 'Descripcion': '', 'Editorial': ''}]

        # Crear dataframe desde el diccionario
        self.df = pd.DataFrame(self.data)

    def registrar_libro(self, libro):
        libro_nuevo = {'Titulo': libro.titulo,
                       'Autor': libro.autor,
                       'Genero': libro.genero,
                       'Descripcion': libro.descripcion,
                       'Editorial': libro.editorial}

        self.df = self.df.append(libro_nuevo)
        return f"El libro '{libro.titulo}' ha sido registrado exitosamente."

