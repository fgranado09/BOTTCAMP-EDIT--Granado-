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

