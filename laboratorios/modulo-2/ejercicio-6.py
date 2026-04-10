# Realiza un programa que, ingresando la edad de
# una persona, determine si es menor, mayor con
# edad laboral o jubilado (contemplando jubilado
# para ambos sexos a los 65 años).


edad = int(input("Ingrese su edad: "))

if edad < 18: 
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad")
elif edad >= 65:
    print("Sos jubilado")

# Recórrela con 2 sentencias for para mostrar cada uno
# de los elementos que la componen.

matriz = [[10, 50, 5], [20, 30, 70], [15, 45, 80]]

for matrices in matriz:
    for numero in matrices:
        print(numero)