# Crea una función rango(desde, hasta,
# intervalo) que retorne una lista de números, tal
# como la función incorporada range(), aunque
# según el intervalo especificado.

# Por ejemplo, el siguiente código:

# lista = rango(1, 10, 2)
# print(lista)

# Debe imprimir: [1, 3, 5, 7, 9], puesto que se
# genera una lista desde 1 hasta 10 con un
# intervalo de 2.


def rango (desde, hasta, intervalo): 
    lista = [] # Hacemos una lista
    numero = desde # Creamos la variable "numero" para poder seguir reasignandole valores cuando el bucle empieza a funcionar sin tocar "desde"
    while numero < hasta: # Mientras que el numero sea menor hasta el numero de llegada se cumple la condicion
        lista.append(numero) # Se agrega el numero a la lista
        numero = numero + intervalo # Nuevo valor de numero + el intervalo asignado
    return lista # Guarda los valores

lista = rango (1,10,2)
print(lista)
