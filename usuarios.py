"""

Script para la gestión de usuarios

"""
import csv
import re


class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def registrar_usuario(self):
        with open('usuarios.csv', mode='a', newline='') as users_file:
            fieldnames = ['Nombre', 'Contraseña']
            writer = csv.DictWriter(users_file, fieldnames=fieldnames, delimiter=';')
            with open('usuarios.csv', newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=';', fieldnames=fieldnames)
                dict_1 = {}

                for nombres in csv_reader:
                    v = list(nombres.values())
                    dict_1[v[0]] = v[1]

                match = re.search('^[\\w]+$', self.contrasena)
                match = re.search('^[\\w]+$', self.contrasena)
                if match:
                    if self.nombre not in dict_1.keys():
                        writer.writerow({'Nombre': self.nombre, 'Contraseña': self.contrasena})
                        return 0
                    else:
                        return 1
                else:
                    return 2

    @staticmethod
    def iniciar_sesion(nombre, contrasena):
        with open('usuarios.csv') as csv_file:
            fieldnames = ['Nombre', 'Contraseña']
            csv_reader = csv.DictReader(csv_file, delimiter=';', fieldnames=fieldnames)
            credenciales = []
            for usuario in csv_reader:
                credenciales = list(usuario.values())
                if nombre == credenciales[0] and contrasena == credenciales[1]:
                    return True # Si las credenciales son correctas
                    break
            else:
                return False # Si las credenciales son incorrectas



# Nota, si el archivo csv no tiene una linea nueva vacia, habrá errores. No debe ocurrir ningún error si no se modifica manualmente.

if __name__ == '__main__':
    Usuario('Jordi','ijy3')