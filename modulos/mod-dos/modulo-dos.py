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

# Entrada de Datos

nombre = input("Ingrese su nombre: ") # El input siempre devuelve un string, por eso no es necesario poner comillas 
cursos = input("Cuantos cursos realizaste?")

print("Hola", nombre) # El input le asigna un valor a la variable nombre, que luego se puede usar en el programa
print("Hiciste", cursos, "cursos") # El input le asigna un valor a la variable cursos, que luego se puede usar en el programa

separador()

# Mala practica

# edad = input("Ingresa tu edad: ") # No permite hacer operaciones matematicas con esta variable, porque el input devuelve un string, por eso es necesario convertirlo a un entero

# Buena Practica

edad = int(input("Ingresa tu edad: ")) # Convertimos el string a un entero, para poder hacer operaciones matematicas con esta variable
if edad >= 16: 
    print("Puede votar")
else:
    print("No puede votar")


separador()

# Conversiones entre tipos de datos

# Agregar prefijo a un numero de celular
celular = "1124557307"
celular_con_prefijo = "+54" + celular
print(celular_con_prefijo)
print(type(celular_con_prefijo))

# Calcular el siguiente numero de celular
celular_siguiente = int(celular) + 1
print(celular_siguiente)       
print(type(celular_siguiente))

# Agregar prefijo al siguiente numero de celular
celular_siguiente_con_prefijo = "+54" + str(celular_siguiente)
print(celular_siguiente_con_prefijo)
print(type(celular_siguiente_con_prefijo))

separador() 

# Bucle While

a = 1
while a < 5: # Mientras a sea menor o igual a 5, se va a ejecutar el bloque de codigo del while hasta que el booleano sea false.
    print("Hola mundo")
    print("Desde python")
    a = a + 1 # Incrementamos el valor de a en 1, para evitar un bucle infinito
print("Fin del programa")