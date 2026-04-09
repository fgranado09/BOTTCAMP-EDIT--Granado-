nombres = ["Susana", "Alejandro", "Roberto"]
             #  0         1            2


# Inserta entre Alejandro y Roberto a Paula, y luego
# agrega al final a Silvina. 

nombres.insert(2, "Paula") #Insert se utiliza para agregar un elemento en una posicion especifica de la lista
print(nombres)

nombres.append("Silvina") #Append se utiliza para agregar un elemento al final de la lista
print(nombres)

# Para finalizar, recorre la lista y muestra a todos los
# nombres por pantalla.

for nombre in nombres: #For se utiliza para recorrer cada elemento de la lista
    print(nombre)