import tkinter as tk
import time
import os
import random
from PIL import Image, ImageTk

class FavBooksApp:
    def __init__(self, usuario):
        self.usuario = usuario

        self.ventana_principal = tk.Tk()
        self.ventana_principal.title(f"FavBook de {self.usuario}")

        # Dimensiones y posición para centrar la ventana en la pantalla
        ancho_ventana = 1000
        alto_ventana = 800
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (alto_ventana // 2)
        self.ventana_principal.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Configuración del color de fondo
        self.ventana_principal.configure(bg='#D19AFF')

        # Etiqueta de bienvenida
        self.et_bienvenida = tk.Label(self.ventana_principal, text=f'FavBook de {self.usuario}', font=('Trebuchet MS', 18), bg='#D19AFF')
        self.et_bienvenida.pack(pady=10)

        # Etiqueta para mostrar la hora
        self.et_hora = tk.Label(self.ventana_principal, text=self.obtener_hora())
        self.et_hora.pack()

        # Sección de libro del día
        self.seccion_libro_dia = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE)
        self.seccion_libro_dia.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.et_libro_dia = tk.Label(self.seccion_libro_dia, text="Libro del Día", font=('Trebuchet MS', 14))
        self.et_libro_dia.pack(pady=5)

        # Widget Label para mostrar la imagen del libro del día
        self.label_imagen_libro_dia = tk.Label(self.seccion_libro_dia)
        self.label_imagen_libro_dia.pack()

        # Sección de libros recomendados
        self.seccion_recomendados = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE)
        self.seccion_recomendados.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.et_recomendados = tk.Label(self.seccion_recomendados, text="Libros Recomendados", font=('Trebuchet MS', 14))
        self.et_recomendados.pack(pady=5)

        # Sección de lista de favoritos
        self.seccion_favoritos = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE)
        self.seccion_favoritos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.et_favoritos = tk.Label(self.seccion_favoritos, text="Lista de Favoritos", font=('Trebuchet MS', 14))
        self.et_favoritos.pack(pady=5)

        # Sección de lista de leídos
        self.seccion_leidos = tk.Frame(self.ventana_principal, bg='#FFFFFF', bd=1, relief=tk.GROOVE)
        self.seccion_leidos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.et_leidos = tk.Label(self.seccion_leidos, text="Lista de Leídos", font=('Trebuchet MS', 14))
        self.et_leidos.pack(pady=5)

        self.actualizar_hora()
        self.mostrar_libro_del_dia()  # Llamada para mostrar el libro del día al iniciar la aplicación

        self.ventana_principal.mainloop()
        self.imagen_libro_dia = None

        def mostrar_libro_del_dia(self):
            # código para obtener y mostrar la imagen del libro del día
            # al final, actualiza la referencia a la imagen
            self.imagen_libro_dia = imagen_tk
            self.label_imagen_libro_dia.config(image=self.imagen_libro_dia)
            self.label_imagen_libro_dia.image = self.imagen_libro_dia  # mantener una referencia

    def obtener_hora(self):
        hora_actual = time.strftime("%H:%M:%S")
        return hora_actual

    def actualizar_hora(self):
        # Actualizar la hora cada segundo
        self.et_hora.config(text=self.obtener_hora())
        self.ventana_principal.after(1000, self.actualizar_hora)

    def obtener_imagen_aleatoria(self, carpeta_imagenes):
        # Obtener la lista de nombres de archivos de la carpeta de imágenes
        nombres_archivos = os.listdir(carpeta_imagenes)
        # Filtrar solo los archivos de imagen (se pueden agregar más extensiones según sea necesario)
        imagenes = [archivo for archivo in nombres_archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        # Seleccionar una imagen aleatoria de la lista
        imagen_aleatoria = random.choice(imagenes)
        # Devolver la ruta completa de la imagen aleatoria
        return os.path.join(carpeta_imagenes, imagen_aleatoria)

    def mostrar_libro_del_dia(self):
        # Carpeta donde se encuentran las imágenes de los libros
        carpeta_imagenes = 'images/'  # Cambia esto a la ruta de tu carpeta de imágenes
        # Obtener una imagen aleatoria de la carpeta
        ruta_imagen_libro_dia = self.obtener_imagen_aleatoria(carpeta_imagenes)

        # Cargar la imagen del libro del día
        imagen_pil = Image.open(ruta_imagen_libro_dia)
        # Redimensionar la imagen si es necesario para que se ajuste al widget Label
        imagen_pil = self.redimensionar_imagen(imagen_pil, 400, 400)
        # Convertir la imagen PIL a un objeto que Tkinter pueda mostrar
        imagen_tk = ImageTk.PhotoImage(imagen_pil)

        # Mostrar la imagen del libro del día en el widget Label correspondiente
        self.label_imagen_libro_dia.config(image=imagen_tk)
        self.label_imagen_libro_dia.image = imagen_tk  # Se debe mantener una referencia para evitar que la imagen se elimine por el recolector de basura

        # Programar la llamada para mostrar el siguiente libro del día después de un cierto período de tiempo (por ejemplo, cada día)
        # Esto se puede hacer usando el método `after` de Tkinter, proporcionando el tiempo en milisegundos
        # Por ejemplo, para mostrar un nuevo libro del día después de 24 horas (86400000 milisegundos):
        self.ventana_principal.after(86400000, self.mostrar_libro_del_dia)

    def redimensionar_imagen(self, imagen, max_width, max_height):
        # Redimensionar la imagen manteniendo la proporción
        width, height = imagen.size
        if width > max_width or height > max_height:
            ratio = min(max_width / width, max_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            return imagen.resize((new_width, new_height))
        return imagen

