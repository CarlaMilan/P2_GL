from passlib.hash import argon2

# Generar hash de una contraseña
contrasena = "password123"
hash_contrasena = argon2.hash(contrasena)

print("Contraseña original:", contrasena)
print("Hash de contraseña:", hash_contrasena)

# Verificar una contraseña
contrasena_ingresada = "password123"
es_valido = argon2.verify(contrasena_ingresada, hash_contrasena)

print("Contraseña ingresada es válida:", es_valido)
