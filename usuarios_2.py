"""

Script para la gestión de usuarios

"""
import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
import sqlite3
from passlib.hash import argon2

# Conexión a la base de datos
conn = sqlite3.connect('src/database/database.db')
cursor = conn.cursor()


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        # Verificar si el usuario ya existe
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return False

        # Generar el hash de la contraseña
        password_hash = argon2.hash(self.password)

        # Insertar el nuevo usuario en la base de datos
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (self.username, password_hash))
        conn.commit()
        return True

    # Función para iniciar sesión
    def login_user(self):
        # Obtener el usuario de la base de datos
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = cursor.fetchone()
        if not user:
            return 0
        elif not argon2.verify(self.password, user[2]):
            return 1
        return 2
