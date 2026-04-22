# Desarrolla una función que reciba una lista con
# números enteros y devuelva en una matriz:
# ● Como primer elemento, una lista con los
# números pares.
# ● Como segundo elemento, una lista de los
# números impares de la lista recibida.

def par_impar (numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return [pares, impares] # Esta es la manera de generar matrices desde un return

valores = [10, 22, 55, 29, 44, 3, 19]

print(par_impar(valores))
