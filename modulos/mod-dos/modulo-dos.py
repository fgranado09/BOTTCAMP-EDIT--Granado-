def separador():
    print("--------------------------------------------------")

# Condicionales Simples

 # Permiten ejecutar un codigo en funcion de si se cumple o no una condicion

edad = 30

if edad >= 16: # Solo se va a ejecutar esta condicion si se cumple la condicion de que edad sea mayor o igual a 16
    print("Esta persona puede votar")
    print("Hola mundo") # Puede tener mas de una condicion dentro del bloque de codigo      

separador()

# Caso inverso
edad = 10

if edad < 16: # Solo se va a ejecutar esta condicion si se cumple la condicion de que edad sea menor a 16       
    print("Esta persona no puede votar")

# Otra manera de escribirlo

if not edad >= 16: 
    print("Esta persona no puede votar")

separador() 

# Utilidad de Else

edad = 10
if edad >= 16:
    print("Esta persona puede votar")
else: # Si no se cumple la condicion del if, se ejecuta el bloque de codigo del else
    print("Esta persona no puede votar")


separador()

# Condicionales multiples

# En un mismo condicional quiero chequear mas de una condicion

edad = 2
if edad >= 65:
    print("Votacion Opcional")
elif edad >= 16: # Si no se cumple la condicion del if, se chequea esta condicion
    print("Puede votar")
elif edad < 3: # Otra condicion
    print("Sos demasiado chico para votar")
else: # Si no se cumple ninguna de las condiciones anteriores, se ejecuta el bloque de codigo del else
    print("No puede votar")

# Siempre lo primero debe ser un if, luego pueden haber varios elif y por ultimo un else (opcional)
# Todas estas cosas se van dando en orden.
# Una vez que encuentra el valor verdadero, no chequea las siguientes condiciones, por eso es importante el orden de las condiciones.

separador()

# Condicionales Anidados

# Es un condicional dentro de otro condicional

edad = 2

if edad >= 16:
    # Aca ya se que la edad es mayor o igual a 16, entonces puedo chequear si es mayor o igual a 65
    if edad >= 65:
        print("Votacion Opcional")
    else:
        print ("Puede votar")
else: 
    if edad < 3:
        print("Sos demasiado chico para votar")
    else:
        print("No puede votar")

separador()

