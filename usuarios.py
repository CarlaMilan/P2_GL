"""

Script para la gestión de usuarios(no finalizado)

(previo, luego orientado a obj)
dict y compresión de listas para recorrer
usar expresiones regulares para limitar las contraseñas a letras ASCII y num
con simbolos comunes, y el nombre,
excepciones para controlar no duplicidad usuarios

"""
import csv


def registrar_usuario(nombre, contrasena):
    with open('usuarios.csv', mode='a', newline='') as users_file:
        users_writer = csv.writer(users_file, delimiter=';', quotechar='"')
        with open('usuarios.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            usuarios = [x[0] for x in csv_reader]
        print(f'Los usuarios son: {usuarios}')

        (users_writer.writerow((nombre, contrasena)), print(f'{nombre},Tu usuario ha sido registrado correctamente')) \
            if nombre not in usuarios else print('Ya existe ese usuario, por favor, elige otro nombre.')


def borrar_usuario(nombre):
    pass


registrar_usuario('Jordi', '1234')
