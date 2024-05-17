import sqlite3
import io

def convertir_imagen_a_blob(ruta_imagen):
    with open(ruta_imagen, 'rb') as file:
        blob = file.read()
    return blob

def actualizar_imagen_libro(conexion, titulo, ruta_imagen):
    imagen_blob = convertir_imagen_a_blob(ruta_imagen)
    cursor = conexion.cursor()
    cursor.execute("UPDATE books SET cover_image = ? WHERE title = ?", (imagen_blob, titulo))
    conexion.commit()

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('database/database.db')

# Actualizar la imagen de un libro existente
actualizar_imagen_libro(conexion, "Hábitos atómicos", "images/hatomicos.jpg")

# Cerrar la conexión
conexion.close()