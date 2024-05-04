"""

Script para la gestión de usuarios(no finalizado)

(v1, luego orientado a obj)
dict y compresión de listas para recorrer clave(name) : valor(passw)
usar expresiones regulares para limitar las contraseñas a letras ASCII y num
con simbolos comunes, y el nombre,
excepciones para controlar no duplicidad usuarios


aux:

    try:
        with open('usuarios.csv', mode='x'):
            pass
    except FileExistsError:
        with open('usuarios.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                usuarios.append(row[0])

        with open('usuarios.csv', mode='a', newline='') as users_file:
            users_writer = csv.writer(users_file, delimiter=';', quotechar='"')
            if len(usuarios) == 0:
                users_writer.writerow((nombre, contrasena))
                print(f'Usuario inicial creado para {nombre}')
            else:
                for name in usuarios:
                    if name == nombre:
                        print(' Convertir a una excepción (nombre ya existe)')
                        break
                    else:
                        print(name)
                        users_writer.writerow((nombre, contrasena))
                        print(f'{nombre},Tu usuario ha sido registrado correctamente')
"""




import csv


def registrar_usuario(nombre, contrasena):
    usuarios = []
    with open('usuarios.csv', mode='a', newline='') as users_file:
        users_writer = csv.writer(users_file, delimiter=';', quotechar='"')
        with open('usuarios.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                usuarios.append(row[0])
        print(f'Los usuarios son: {usuarios}')
        if nombre not in usuarios:
            users_writer.writerow((nombre, contrasena))
            print(f'{nombre},Tu usuario ha sido registrado correctamente')
        else:
            print('Ya existe ese usuario, por favor, elige otro nombre.')

def borrar_usuario(nombre):
    pass


registrar_usuario('Jordi', '1234')
