# ==========================================================================================================================
# Sistema de gerstion de alumnos
# Descripcion: Permite al administrador registrar alumnos y consultar la lista.
# ==========================================================================================================================

# === Diccionarios ===

# Diccionario Global que almacena alumnos
# Estructura: {nombre_alumno: cantidad_cursos}

alumnos = {}

# === Funciones ===

# --- Funcion de autenticacion ---
# Solicita usuario y contraseña, returna True si son correctos, False si no.
def autenticar():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    return usuario == "admin" and contraseña == "uni123"

# --- Funcion para agregar alumno ---
# Solicita nombre y cantidad de cursos realizados, y los guarda en el diccionario
def agregar_alumnos(alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    cursos = int(input("Ingrese la cantidad de cursos: "))
    alumnos[nombre] = cursos
    print("El alumno fue añadido a la lista")

# --- Funcion para ver lista de alumnos ---
# Recorre e imprime todos los nombres guardados en el diccionario
def ver_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos en la lista")
    else:
        print("Lista de alumnos:")
        # Al iterar el diccionario, Python devuelve las claves (nombres)
        for alumno in alumnos:
            print(alumno)

# --- Funcion para ver la cantidad de cursos de un alumno ---
# Solicita un nombre y busca su valor (cursos) en el diccionario
def ver_cursos(alumnos):
    persona = input("Ingrese el nombre del alumno: ")
    # Verifica si el nombre existe como clave en el diccionario
    if persona in alumnos:
        print(persona, "tiene", alumnos[persona], "cursos")
    else: 
        print("Este alumno no existe en la lista")

# === Codigo Principal ===

if autenticar():
    # Bucle infito que muestra el menu hasta que el usuario decida salir
    while True:
        print("Menú")
        print("1 - Añadir un alumno")
        print("2 - Ver lista de alumnos")
        print("3 - Ver cantidad de cursos")
        print("4 - Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            agregar_alumnos(alumnos)
        elif opcion == "2":
            ver_alumnos(alumnos)
        elif opcion == "3":
            ver_cursos(alumnos)
        elif opcion == "4":
            print("Gracias por utilizar el programa")
            break # Rompe el bucle y termina el programa
        else:
            print("La opcion seleccionada es invalida")
else:
    print("Usuario o contraseña incorrectos")