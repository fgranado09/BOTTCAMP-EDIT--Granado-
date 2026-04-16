def separador():
    print("---------------------------------------------------")

# Multiples valores de retorno

def aplicar_iva(precio):
    if precio < 1000:
        precio_con_iva = precio
    else:
        precio_con_iva = precio * 1.21
    return precio_con_iva
    print (precio_con_iva) # El codigo no avanza y no lee esta instruccion porque en las funciones cuando aparece un "return" la funcion termina ahi

# Esto es por lo general, porque cuando hay condicionales puede que no termine ahi, pero si va a ser posible un unico "return"

# Ejemplo

# Queremos crear la siguiente funcion

def min_y_max (lista):
    a = min(lista) # Min es un valor reservado de Python -- Ubica el numero de menor valor dentro de una lista
    b = max(lista) # Max es un valor reservado de Python -- Ubica el numero de mayor valor dentro de una lista
    # return a
    # return b No funciona porque solo se puede devolver un solo "return"
    return [a , b] # El valor de retorno puede ser de cualquier tipo de dato, los 4 basicos y tambien las listas

# Se crea una lista dentro de una funcion y se establece como valor de retorno

print (min_y_max([4, 7, 9, 1, 13, 2]))

separador()

# Funciones sentido matematico 

# El concepto funcion dentro de la programacion es muy similar a la funcion matematica

# En matematica esta la funcion lineal f(x) = a.x + b

# Como aplicar la funcion f(x) = 5x + 3 a un programa de Python

def f(x):
    return 5 * x + 3

y = f(10)
print (y)

# Como aplicar la cuadratica --> ax² + bx + c = 0
#                               x = -b ± √(b² - 4ac) /// 2a


def raices(a, b, c):
    d = (b ** 2 - 4 * a * c) ** 0.5
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return [x1, x2]

print(raices(1, 1, -6))  # [2.0, -3.0] # Las dos raices de la ecuacion de segundo grado

separador()


 