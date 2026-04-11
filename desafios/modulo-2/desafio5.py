# Escribe un programa que permita crear una lista
# de nombres.
# Para ello, el programa debe pedir un número y
# luego solicitar esa cantidad de nombres para
# crear la lista. Por último, el programa tiene que
# mostrar la lista creada.


nombres = []

cantidad = int(input("¿Cuántos nombres desea ingresar? "))

for i in range(cantidad):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

print("Los nombres ingresados son:")
for nombre in nombres:
    print(nombre)
