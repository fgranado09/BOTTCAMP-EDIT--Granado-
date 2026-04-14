# Escribe una función mostrar_estrellas(cantidad)
# que muestre tantos * como indica cantidad,
# comenzando con un *.

def mostrar_estrellas (cantidad):
    for i in range (1, cantidad + 1): # Se agrega + 1 porque si no terminaria en 4 # Recorre del 1 al 2, del 2 al 3, del 3 al 4 y del 4 al 5 = Osea, 4 tramos
        print ("*" * i)
    
mostrar_estrellas(5)
    

