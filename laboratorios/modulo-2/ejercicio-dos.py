# Con un bucle while, incrementar una
# variable entera de uno en uno (desde 0 a 10
# sin incluir). Mostrar por pantalla el resultado
# por vuelta

a = 0
while a <= 10:
    print(a)
    a += 1

# Pedir por teclado el nombre de usuario. Si
# está vacío, volver a pedirlo hasta que ingrese
# un nombre. Luego, saludar al usuario.

nombre_usuario = ""

while nombre_usuario == "":
    nombre_usuario = input("Ingrese su nombre de usuario: ")
print("Hola", nombre_usuario, "!")

