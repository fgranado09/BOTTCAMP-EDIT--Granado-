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

separador() 

# Listas

# Una lista es una coleccion de elementos, es un tipo de dato que permite almacenar varios valores en una sola variable. Se pueden modificar, agregar o eliminar elementos de la lista.

alumnos = ["Juan", "Sofia", "Matias"]
print(alumnos) # Imprime la lista completa
print(alumnos[0]) # Imprime el primer elemento de la lista, que es "Juan". Esto es un indice, que empieza desde 0.
print(alumnos[1]) # Imprime el segundo elemento de la lista, que es "Sofia" 
print(alumnos[2]) # Imprime el tercer elemento de la lista, que es "Matias" 

separador()

# Operaciones sobre listas

alumnos = ["Juan", "Sofia", "Matias"]

# Agregar un elemento a la lista
alumnos.append("Lucia") # Agrega el elemento "Lucia" al final de la lista

print(alumnos) # Imprime la lista completa, que ahora es ["Juan", "Sofia", "Matias", "Lucia"]

# Para insertar un elemento en una posicion especifica, se puede usar el metodo insert
alumnos.insert(1, "Pedro") # Inserta el elemento "Pedro" en la posicion 1 de la lista, desplazando los demas elementos hacia la derecha

print(alumnos) # Imprime la lista completa, que ahora es ["Juan", "Pedro", "Sofia", "Matias", "Lucia"]

# Para reemplazar un elemento de la lista, se puede usar el indice para asignar un nuevo valor
alumnos[2] = "Maria" # Reemplaza el elemento en la posicion 2 de la lista, que es "Matias", por "Maria" 

print(alumnos) # Imprime la lista completa, que ahora es ["Juan", "Pedro", "Maria", "Matias", "Lucia"]

# Para eliminar un elemento de la lista, se puede usar el metodo remove
del alumnos[3] # Elimina el elemento en la posicion 3 de la lista, que es "Lucia"

print(alumnos) # Imprime la lista completa, que ahora es ["Juan", "Pedro", "Maria"]

separador()

# Bucle For

# El bucle for es una estructura de control que permite repetir un bloque de codigo un numero determinado de veces, o iterar sobre los elementos de una coleccion (como una lista).
alumnos = ["Juan", "Sofia", "Matias"]

for alumno in alumnos: # Para cada elemento x en la lista alumnos, se va a ejecutar el bloque de codigo del for
    print("Hola mundo") # Imprime "Hola mundo" para cada elemento de la lista alumnos
    print(alumno) # Imprime el valor de x, que es cada elemento de la lista alumnos

print("Fin del programa")

# Ejemplo con mails

for alumno in alumnos:
  #  enviar_mail(alumno) # Envia un mail a cada alumno de la lista alumnos, usando la funcion enviar_mail (que no esta definida en este codigo, pero se asume que existe)
  print("Enviando mail a:", alumno)


separador()

# Las instrucciones "Continue" y "Break"

# Continue: Permite saltar el bloque de codigo del for y pasar al siguiente elemento de la lista, sin ejecutar el bloque de codigo del for para ese elemento.

primos = [1, 2, 3, 5, 7, 11, 13]

for numero in primos: 
    if numero == 5:
        continue # Si el numero es 5, se salta el bloque de codigo del for y se pasa al siguiente numero de la lista primos
    print(numero) # Imprime el numero, excepto el numero 5

# Break: Permite salir del bucle for, sin importar si se han iterado todos los elementos de la lista o no.

for numero in primos :
    if numero == 5:
        break # Si el numero es 5, se sale del bucle for y no se iteran los siguientes numeros de la lista primos
    print(numero) # Imprime el numero, pero se detiene cuando llega al numero 5


# Matrices

# Una matriz es una lista de listas, es decir, una coleccion de listas que a su vez son elementos de otra lista. Se pueden usar para representar tablas de datos, como una hoja de calculo o una base de datos.

# Con cantidad de cursos realizados por cada alumno

alumnos = [
    ["Juan", 2], 
    ["Matias", 5], 
    ["Sofia", 5]
]

print(alumnos[1]) # Imprime la lista del segundo alumno, que es ["Matias", 5]
print (alumnos[1][0]) # Imprime el nombre del segundo alumno, que es "Matias"
print (alumnos[1][1]) # Imprime la cantidad de cursos realizados por el

