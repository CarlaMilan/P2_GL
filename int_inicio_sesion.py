import tkinter as tk
from tkinter import messagebox
import sqlite3
from passlib.hash import argon2
from usuarios_2 import Usuario
import time
from int_app_principal import FavBooksApp


def registrar_usuario():
    ventana_registro = tk.Toplevel(ventana_login)
    ventana_registro.title("Registro de usuario")

    # Etiqueta y entrada para el nombre de usuario
    etiqueta_usuario_registro = tk.Label(ventana_registro, text="Nuevo Usuario:")
    etiqueta_usuario_registro.grid(row=0, column=0, padx=10, pady=5)
    entrada_usuario_registro = tk.Entry(ventana_registro)
    entrada_usuario_registro.grid(row=0, column=1, padx=10, pady=5)

    # Etiqueta y entrada para la contraseña
    etiqueta_contraseña_registro = tk.Label(ventana_registro, text="Nueva Contraseña:")
    etiqueta_contraseña_registro.grid(row=1, column=0, padx=10, pady=5)
    entrada_contraseña_registro = tk.Entry(ventana_registro, show='*')
    entrada_contraseña_registro.grid(row=1, column=1, padx=10, pady=5)

    def registrar():
        username = entrada_usuario_registro.get()
        password = entrada_contraseña_registro.get()
        p = Usuario(username, password)
        if p.register_user():
            messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    # Botón para registrar usuario
    boton_registro = tk.Button(ventana_registro, text="Registrar", command=registrar)
    boton_registro.grid(row=2, columnspan=2, padx=10, pady=5)


def iniciar_sesion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    user = Usuario(usuario, contraseña)
    comprobacion = user.login_user()
    if comprobacion == 0:
        messagebox.showinfo("Usuario Inválido", "El usuario no existe")
    elif comprobacion == 1:
        messagebox.showinfo("Credenciales inválidas", "La contraseña no es válida")
    else:
        ventana_principal(usuario)
        ventana_login.destroy()


def obtener_hora():
    hora_actual = time.strftime("%H:%M:%S")
    return hora_actual

def ventana_principal(usuario):
    FavBooksApp(usuario)

ventana_login = tk.Tk()
ventana_login.title("Inicio de sesión")

etiqueta_usuario = tk.Label(ventana_login, text="Usuario:")
etiqueta_usuario.grid(row=0, column=0, padx=10, pady=5)
entrada_usuario = tk.Entry(ventana_login)
entrada_usuario.grid(row=0, column=1, padx=10, pady=5)

etiqueta_contraseña = tk.Label(ventana_login, text="Contraseña:")
etiqueta_contraseña.grid(row=1, column=0, padx=10, pady=5)
entrada_contraseña = tk.Entry(ventana_login, show='*')
entrada_contraseña.grid(row=1, column=1, padx=10, pady=5)

b_inicio_sesion = tk.Button(ventana_login, text='Iniciar sesión', command=iniciar_sesion)
b_inicio_sesion.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

b_registro = tk.Button(ventana_login, text='Registrarse', command=registrar_usuario)
b_registro.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

ventana_login.mainloop()