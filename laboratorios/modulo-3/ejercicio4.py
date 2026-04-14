# Definimos la lista
l1 = ["m", 2, 1, 2, "m"]
#      0   1  2  3   4

# Comienza la funcion
def es_palindromo(lista):
    # === Definimos Puntas ===
    pos_izq = 0
    pos_der = len(lista) - 1 # La lista tiene 5 elementos, nos interesa pararnos sobre el indice 4 (Que es el ultimo). Remember las posiciones arrancan siempre en 0
    # === Comienza el bucle ===
    while pos_der >= pos_izq: #  4 >= 0 --> True
        # == Condicional ===
        if lista[pos_izq] != lista[pos_der]: # Si la posicion izquierda difiere de la posicion derecha --> Falso . Ej. lista[0] != lista [4] o "m" != "m" -> Falso, no entra.
            return False
    pos_izq = pos_izq + 1 # Se mueve una posicion a la derecha
    pos_der = pos_der - 1 # Se mueve una posicion a la izquierda
    return True


print(es_palindromo(l1))