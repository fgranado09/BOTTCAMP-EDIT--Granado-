# Escribe una función que sirva para multiplicar
# cada elemento de una lista numérica por un
# valor (ambos deben ser parámetros de función);
# y devuelva la nueva lista con cada elemento en
# su respectiva posición, pero ya multiplicado

def multiplicar (lista, valor):
    nueva = []
    for numeros in lista:
        resultado = numeros * valor
        nueva.append (resultado)
    return nueva

numeros = [2, 4, 6, 8]


print(multiplicar(numeros, 2))