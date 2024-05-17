import sqlite3
from PIL import Image, ImageTk
import io
import tkinter as tk

# Función para redimensionar la imagen manteniendo la proporción
def redimensionar_imagen(imagen, max_width, max_height):
    width, height = imagen.size
    ratio = min(max_width / width, max_height / height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    return imagen.resize((new_width, new_height))

def obtener_blob_desde_bd(conexion, titulo):
    cursor = conexion.cursor()
    cursor.execute("SELECT cover_image FROM books WHERE title = ?", (titulo,))
    blob = cursor.fetchone()[0]
    return blob

def convertir_blob_a_imagen(blob):
    return Image.open(io.BytesIO(blob))

# Crear la ventana principal de Tkinter
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Mostrar Imagen desde BLOB en SQLite")

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('src/database/database.db')

# Obtener el BLOB desde la base de datos
titulo_libro = "Hábitos atómicos"  # Título del libro cuya imagen deseas mostrar
blob = obtener_blob_desde_bd(conexion, titulo_libro)

# Convertir el BLOB a una imagen PIL
imagen_pil = convertir_blob_a_imagen(blob)

# Redimensionar la imagen
imagen_redimensionada = redimensionar_imagen(imagen_pil, 400, 400)

# Convertir la imagen PIL a un formato que Tkinter pueda usar
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen_tk)
label_imagen.pack()

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()

# Cerrar la conexión
conexion.close()