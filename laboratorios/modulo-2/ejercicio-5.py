# Crea un programa que solicite una fila y una
# columna e imprima en pantalla el número en
# esa posición según la siguiente matriz:

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

# Un ejemplo de entrada y salida es el siguiente
#(los caracteres en azul son ingresados por el
# usuario):

# Fila: 1
# Columna: 2
# El número en esa posición es: 6.4

# El resultado es 6.4 porque es el valor ubicado en
# matriz[1][2].

# El programa debe chequear que la fila y la
# olumna tengan valores válidos. En este caso, las
# únicas filas válidas son 0 y 1; las columnas, 0, 1 y
# 2. Si alguno de los dos valores es inválido, debe
# mostrar un mensaje de error.

fila = int(input("Fila: "))
columna = int(input("Columna: "))


if fila < 0 or fila > 1:
    print("Hay un error")
elif columna < 0 or columna > 2:  
    print("Hay un error")
else:
    print("El número en esa posición es:", matriz[fila][columna])


# Otra manera de hacerlo

print(len(matriz))

fila = int(input("Fila: "))
columna = int(input("Columna: "))   

if fila < len(matriz):
    if columna < len(matriz[fila]):
        print(matriz[fila][columna])
    else:
        print("Error: Columna inválida.")
else:
    print("Error: Fila inválida.")

