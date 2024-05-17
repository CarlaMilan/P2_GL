import tkinter as tk
from tkinter import messagebox
import requests

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def registrar_usuario(self):
        data = {'username': self.nombre, 'password': self.contrasena}
        response = requests.post('http://localhost:5000/register', json=data)

        if response.status_code == 201:
            messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente.")
        elif response.status_code == 409:
            messagebox.showerror("Usuario existente", "Ya existe el usuario. Por favor inicia sesión o cambia de usuario")
        else:
            messagebox.showerror(f"Error {response.status_code}", "Error al registrar usuario. Por favor intenta nuevamente.")

    def iniciar_sesion(self):
        data = {'username': self.nombre, 'password': self.contrasena}
        response = requests.post('http://localhost:5000/login', json=data)

        if response.status_code == 200:
            access_token = response.json()['access_token']
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {self.nombre}!")
            # Aquí podrías abrir la ventana principal o realizar cualquier otra acción
        else:
            messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas. Por favor intenta nuevamente.")

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    user = Usuario(usuario, contraseña)
    user.iniciar_sesion()

def registrar_usuario():
    ventana_registro = tk.Toplevel(ventana_login)
    ventana_registro.title("Registro de usuario")

    etiqueta_usuario_registro = tk.Label(ventana_registro, text="Nuevo Usuario:")
    etiqueta_usuario_registro.grid(row=0, column=0, padx=10, pady=5)
    entrada_usuario_registro = tk.Entry(ventana_registro)
    entrada_usuario_registro.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_contraseña_registro = tk.Label(ventana_registro, text="Nueva Contraseña:")
    etiqueta_contraseña_registro.grid(row=1, column=0, padx=10, pady=5)
    entrada_contraseña_registro = tk.Entry(ventana_registro, show='*')
    entrada_contraseña_registro.grid(row=1, column=1, padx=10, pady=5)

    boton_registro = tk.Button(ventana_registro, text="Registrar",
                               command=lambda: Usuario(entrada_usuario_registro.get(), entrada_contraseña_registro.get()).registrar_usuario())
    boton_registro.grid(row=2, columnspan=2, padx=10, pady=5)

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