# =====================================================
# Modulo Tres
# =====================================================

# Funciones Necesarias:
def separador():
    print("--------------------------------------------------------------")


# Colecciones:

# Diccionarios: Son colecciones de datos que almacenan pares de clave-valor. Permiten acceder a los valores mediante sus claves.

alumnos = {123: "Juan", 456: "Sofia", 789: "Pablo"}

print(alumnos[123])  # Acceder al valor asociado a la clave 123

# Si quiero eliminar un elemento del diccionario, puedo usar la función del:

del alumnos[456]  # Elimina el elemento con la clave 456

print(alumnos)  # Imprime el diccionario actualizado

# Para reemplazar un valor en el diccionario, simplemente asignamos un nuevo valor a la clave:

alumnos[789] = "Maria"  # Reemplaza el valor asociado a la clave 789

print(alumnos)  # Imprime el diccionario actualizado

separador()

# Esta es la manera de crear un diccionario con información de un alumno, es mas legible y fácil de entender que usar listas para almacenar la misma información:

alumno = {
    "nombre": "Juan",
    "dni": 1234,
    "cursos_actuales": ["Python", "Java", "PHP"],
    "cursos_previos": 2
}

print(alumno["cursos_previos"])  # Imprime el número de cursos previos
print(alumno["cursos_actuales"][-1])  # Imprime el último curso actual (PHP)    


separador()

# La instruccion "Range"

# La función range() se utiliza para generar una secuencia de números enteros dentro de un rango determinado.

numeros = range (1,21) # Genera una secuencia de números del 1 al 20 (el 21 no se incluye)

# Otra manera de usar range
for numero in range (1, 21):
    print(numero)  # Imprime cada número en la secuencia del 1 al 20    

separador()

# Para que sirven las funciones? 

# Las funciones son bloques de código reutilizables que realizan una tarea específica. Permiten organizar el código, mejorar la legibilidad y facilitar la reutilización de código en diferentes partes de un programa. Las funciones pueden recibir argumentos, realizar operaciones y devolver resultados, lo que las hace fundamentales para la programación estructurada y modular. 

def imprimir_saludo():
    print("Hola mundo")
    print("desde python")

imprimir_saludo()  # Llama a la función para ejecutar su código

# Argumentos

def imprimir_saludo(destinatario):
    print("Hola, " + destinatario)

# Ejecuto con argumento
imprimir_saludo ("Juan")

# Multiples argumentos

def imprimir_saludos (destinatario, lenguaje, editor):
    print ("Hola " + destinatario)
    print ("desde " + lenguaje)
    print ("y " + editor)

# Ejecucion con multiples argumentos

imprimir_saludos("Juan", "httml", "visual code")

# Se pueden pasar argumentos de una funcion sin respetar el orden solo de esta manera

imprimir_saludos(lenguaje = "httml", editor = "visual code", destinatario = "Juan") # No es la mejor manera

separador()

# Valor de retorno

def aplicar_iva (precio):
    precio_con_iva = precio * 1.21
    return precio_con_iva # La variable que se constituye como resultado de la funcion

print(aplicar_iva (1000)) # Tambien se puede asignar a una variable como "Resultado"

# Ej.
# resultado = aplicar_iva (1000)

# Tambien se pueden utilizar condicionales o bucles dentro de las funciones 

def aplicar_iva (precio):
    if precio < 1000:
        precio_con_iva = precio
    else:
            precio_con_iva = precio * 1.21
    return precio_con_iva 

print (aplicar_iva(800))
print (aplicar_iva (1500))

separador()

# Diferencia entre print y return

# Lo recomendable es no usar print dentro de las funciones

def aplicar_iva (precio):
    precio_con_iva = precio * 1.21
    return precio_con_iva

# Siempre para el resultado de una funcion se usa return

# Print manda mensaje a la consola. El return le dice a python cual de las variables que estan adentro de la funcion 
# tienen que constituir el resultado de esa funcion

# Si estamos desarrollando aplicaciones web o de escritorio, no se usa casi nada el print 

# def aplicar_iva (precio):
#     precio_con_iva = precio * 1.21
#     print (precio_con_iva) --> Se restringue mucho la utilizacion de esa funcion. Solo te va a servir para programas que sean aplicaciones de consola
# Esa funcion solo te sirve cuando queres aplicarle el iva a un precio y mostrarlo en la consola.

precio = 1000

if aplicar_iva (precio) > 1500:
    print("Tenes descuento")
else:
    print("No tenes descuento")

# Evitar poner PRINTS dentro de funciones. Usar siempre RETURN.
# En programacion se distinguen en un programa dos componentes: 1. La presentacion de los datos y 2. la logica de los datos.
# Las funciones pertenecen a la logica de los datos. Reciben datos a traves de los datos, los procesan y devuelven un resultado.
# La visualizacion de los datos va a decidir que hace con esos datos, si los muestra en la consola, si los manda a la base de datos, si los manda en un mail, si lo guarda en un archivo, etc.
# Los componentes no se deben mezclar.

separador()

# Variables y ambitos

# Ambitos = scope --> Alcance
# Es un espacio donde un objeto tiene visibilidad.







