"""

Script para la gestión de usuarios

"""

import sqlite3
from passlib.hash import argon2
import os


class UsersRepository:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    @staticmethod
    def connect():
        """Establece la conexión con la base de datos."""
        return sqlite3.connect(UsersRepository.db_path)

    def register_user(self):
        con = UsersRepository.connect()
        cursor = con.cursor()
        # Verificar si el usuario ya existe
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return False

        # Generar el hash de la contraseña
        password_hash = argon2.hash(self.password)

        # Insertar el nuevo usuario en la base de datos
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (self.username, password_hash))
        con.commit()
        return True

    # Función para iniciar sesión
    def login_user(self):
        con = UsersRepository.connect()
        cursor = con.cursor()
        # Obtener el usuario de la base de datos
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = cursor.fetchone()
        if not user:
            return 0
        elif not argon2.verify(self.password, user[2]):
            return 1
        return 2
    @staticmethod
    def search_user(username):
        con = UsersRepository.connect()
        cursor = con.cursor()
        # Obtener el usuario de la base de datos
        cursor.execute("SELECT user_id FROM users WHERE username=?", (username,))
        id = cursor.fetchone()
        return id
