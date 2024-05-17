import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('database/database.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Sentencia SQL para eliminar filas de una tabla
sentencia_sql = "DELETE FROM books WHERE book_id=1 OR book_id=2 OR book_id=3 OR book_id=4"

# Ejecutar la sentencia SQL
cursor.execute(sentencia_sql)

# Confirmar la transacción (guardar los cambios)
conexion.commit()

# Cerrar la conexión y el cursor
cursor.close()
conexion.close()