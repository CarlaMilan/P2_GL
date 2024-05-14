from usuarios import Usuario
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

    # Botón para registrar usuario
    boton_registro = tk.Button(ventana_registro, text="Registrar",
                               command=lambda: registro(entrada_usuario_registro.get(),
                                                        entrada_contraseña_registro.get()))
    boton_registro.grid(row=2, columnspan=2, padx=10, pady=5)


def registro(usuario, contraseña):
    # Por ahora, simplemente muestra un mensaje indicando que el usuario ha sido registrado
    user = Usuario(usuario, contraseña)
    comprobacion = user.registrar_usuario()
    if comprobacion == 0:
        messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente.")
    elif comprobacion == 1:
        messagebox.showinfo("Usuario existente", "Ya existe el usuario. Por favor inicia sesión o cambia de usuario")
    else:
        messagebox.showinfo("Usuario existente", "Las contraseñas están limitadas a carácteres unicode")

def validación(usuario, contraseña):
    user = Usuario(usuario, contraseña)
    comp = user.iniciar_sesion(usuario, contraseña)
    if comp:
        return True
    else:
        return False

# Función mostrar ventana principal
def ventana_principal(usuario):
    ventana_login.destroy()
    ventana_principal = tk.Tk()
    ventana_principal.title(f"Gestor de libros de {usuario}")
    ventana_principal.configure(bg='#f0f0f0')
    ventana_principal.geometry("400x300")
    et_bienvenida = tk.Label(ventana_principal, text=f'BookTrail de {usuario}')
    et_bienvenida.pack()
    ventana_principal.mainloop()

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

b_inicio_sesion = tk.Button(ventana_login, text='Iniciar sesión', command=iniciar_sesión)
b_inicio_sesion.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

b_registro = tk.Button(ventana_login, text='Registrarse', command=registrar_usuario)
b_registro.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

ventana_login.mainloop()