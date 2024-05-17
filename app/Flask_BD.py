from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from passlib.hash import argon2
import os

app = Flask(__name__) # Crear instancia Flask

# Ruta absoluta a la carpeta del proyecto
project_dir = os.path.dirname(os.path.abspath(__file__))

# Configuración de la base de datos y JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(project_dir, "src/database/database.db") # Establecer fichero bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Impedir modificaciones
app.config['JWT_SECRET_KEY'] = 'SK8997oA'
db = SQLAlchemy(app) # Establecer entorno a SQAlchemy
jwt = JWTManager(app) # Establecer entorno a JWTManager

# RUTAS PARA REGISTRO Y ATUENTIFICACIÓN USUARIOS
@app.route('/register', methods=['POST']) # Responde solo a solicitudes http post
def register():
    data = request.get_json() # Obtener datos enviados en la solicitud
    username = data.get('username') # Extraer nombre de la solicitud
    password = data.get('password') # Extraer contraseña de la solicitud
    if not username or not password: # Comprobar entrada completa de usuario y contraseña
        return jsonify({'message': 'Username and password are required'}), 400

    existing_user = db.engine.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if existing_user: # Buscar si existe un usuario con el nombre de usuario
        return jsonify({'message': 'User already exists'}), 409 # 409: Conflict

    password_hash = argon2.hash(password) # Generar hash seguro contraseña

    # Insertar nuevo usuario en users directamente con engine.execute
    db.engine.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    db.session.commit() # Confirmar cambios

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/login', methods=['POST']) # Responde solo a solicitudes http post
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Ejecutar consulta SQL para obtener el usuario por nombre de usuario
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.engine.execute(query)
    user = result.fetchone()

    if not user or not argon2.verify(password, user.password_hash):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Si las credenciales son válidas, se crea un token de acceso JWT
    access_token = create_access_token(identity=user.user_id)
    return jsonify(access_token=access_token), 200


@app.route('/books', methods=['GET'])
@jwt_required()
def get_books():
    # Ejecutar una consulta SQL para obtener todos los libros
    books = db.engine.execute("SELECT * FROM books") #

    # Convertir los resultados de la consulta en una lista de diccionarios
    books_data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]

    # Devolver la lista de libros en formato JSON
    return jsonify(books_data), 200


@app.route('/books/<int:book_id>', methods=['GET'])
@jwt_required()
def get_book(book_id):
    # Ejecutar una consulta SQL para obtener el libro con el ID proporcionado
    book = db.engine.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()

    # Verificar si el libro existe
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    # Convertir el resultado de la consulta en un diccionario
    book_data = {'id': book.id, 'title': book.title, 'author': book.author}

    # Devolver los datos del libro en formato JSON
    return jsonify(book_data), 200

@app.route('/books', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    genre = data.get('genre')

    if not title or not author: # Comprobar entrada título y autor
        return jsonify({'message': 'Title and author are required'}), 400

    # Ejecutar consulta SQL para insertar un nuevo libro
    query = "INSERT INTO books (title, author, genre) VALUES (?, ?, ?)"
    db.engine.execute(query, (title, author, genre))
    db.session.commit()

    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/books/<int:book_id>/read', methods=['POST'])
@jwt_required()
def mark_book_as_read(book_id):
    current_user_id = get_jwt_identity()
    # Verificar si el usuario existe en la base de datos
    user = db.engine.execute("SELECT * FROM users WHERE id = ?", (current_user_id,)).fetchone()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Verificar si el libro existe en la base de datos
    book = db.engine.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    # Insertar la relación de libro leído en la tabla read_books
    db.engine.execute("INSERT INTO read_books (user_id, book_id) VALUES (?, ?)", (current_user_id, book_id))

    # Devolver una respuesta exitosa
    return jsonify({'message': 'Book marked as read successfully'}), 200


@app.route('/books/<int:book_id>/favorite', methods=['POST'])
@jwt_required()
def mark_book_as_favorite(book_id):
    # Obtener el ID del usuario actualmente autenticado
    current_user_id = get_jwt_identity()

    # Verificar si el usuario existe en la base de datos
    user = db.engine.execute("SELECT * FROM users WHERE id = ?", (current_user_id,)).fetchone()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Verificar si el libro existe en la base de datos
    book = db.engine.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    # Verificar si el libro ya está marcado como favorito por el usuario
    existing_favorite = db.engine.execute("SELECT * FROM fav_books WHERE user_id = ? AND book_id = ?", (current_user_id, book_id)).fetchone()
    if existing_favorite:
        return jsonify({'message': 'Book already marked as favorite'}), 409

    # Insertar la relación de libro favorito en la tabla fav_books
    db.engine.execute("INSERT INTO fav_books (user_id, book_id) VALUES (?, ?)", (current_user_id, book_id))

    # Devolver una respuesta exitosa
    return jsonify({'message': f'Book {book.title} marked as favorite'}), 201

# Ejecutar código
if __name__ == '__main__':
    app.run(host='localhost', port=5000)