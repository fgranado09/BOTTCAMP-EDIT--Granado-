# Crea una función que fuerce el ingreso de solo
# números.
# ● Debe recibir un número por argumento y
# verificar que este sea un número posible de
# convertir a int.
# ● En caso contrario, volver a pedir el ingreso
# dentro de la función.
# ● Deber de retornar el valor convertido a int.

def convertir(valor):
    valor = str(valor) # Convierte el argumento en str porque .isdecimal() solo funciona para str
    while valor.isdecimal() == False: # .isdecimal() verifica si el string contiene solo digitos y no letras.
        print("Error") 
        valor = input("Ingrese nuevamente: ") # Pide un nuevo ingreso 
    valor = int(valor) # Tranforma los digitos a int
    return valor # Guarda el valor 

print(convertir("hola que tal"))