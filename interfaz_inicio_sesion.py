import tkinter as tk
from tkinter import messagebox

def iniciar_sesión():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    # Verificar credenciales
    validez = validación(usuario,contraseña) # Conseguir validación
    if validez:
        ventana_principal(usuario)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")
def validación(usuario, contraseña):
    if usuario == 'Carla' and contraseña == '1':
        return True
    else:
        return False

# Función mostrar ventana principal
def ventana_principal(usuario):
    # Cerrar ventana inicio sesión
    ventana_login.destroy()

    # Crear ventana principal del gestor de libros
    ventana_principal = tk.Tk()
    ventana_principal.title(f"Gestor de libros de {usuario}")
    ventana_principal.mainloop() # Ejecutar el bucle principal de la ventana

    # Personalizar apariencia de la ventana
    ventana_principal.configure(bg='#f0f0f0')
    ventana_principal.geometry("400x300")

    # Etiqueta bienvenida
    et_bienvenida = tk.Label(ventana_principal, text=f'BookTrail de {usuario}')

# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de sesión")

# Etiqueta y entrada para el nombre de usuario
etiqueta_usuario = tk.Label(ventana_login, text="Usuario:")
etiqueta_usuario.grid(row = 0, column = 0, padx = 10, pady = 5)
entrada_usuario = tk.Entry(ventana_login)
entrada_usuario.grid(row = 0, column = 1, padx = 10, pady = 5)

# Etiqueta y entrada para la contraseña
etiqueta_contraseña = tk.Label(ventana_login, text="Contraseña:")
etiqueta_contraseña.grid(row = 1, column = 0, padx = 10, pady = 5)
entrada_contraseña = tk.Entry(ventana_login, show = '*')
entrada_contraseña.grid(row = 1, column = 1, padx = 10, pady = 5)

# Crear botón iniciar sesión
b_inicio_sesion = tk.Button(ventana_login, text = 'Iniciar sesión', command = iniciar_sesión)
b_inicio_sesion.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady =5)

ventana_login.mainloop() # Ejecutar bucle principal


