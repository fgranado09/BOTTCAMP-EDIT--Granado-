# ==========================================================================================================================
# Sistema de gerstion de alumnos
# Descripcion: Permite al administrador registrar alumnos y consultar la lista.
# ==========================================================================================================================

# Autenticacion del usuario: Solicitud de credencial.
usuario = input("Ingrese su usuario: ")

# Estructura de datos principal: Diccionario de alumnos (Cada elemento es {nombre, cursos})
alumnos = {}

# --- Validacion de usuario ---
if usuario == "admin":
    # --- Solicitud y validacion de contraseña ---
    contraseña = (input("Ingrese su contraseña: ")) 
    if contraseña == "uni123":
        # --- Bucle principal del menu: Se ejecuta hasta que el usuario elija salir --- 
        while True: 
            # --- Menu de opciones disponibles ---
            print("Ingrese el numero de la operacion que desea ejecutar:")
            print("1 - Añadir un alumno a la lista")
            print("2 - Ver la lista de alumnos")
            print("3 - Ver cantidad de cursos")
            print("4 - Salir")
            # --- Captura y conversion de la opcion ingresada ---
            opcion = input("Opcion: ")
            # --- Opcion 1: Registro de nuevo alumno ---
            if opcion == "1": 
                nombre_alumno = input("Ingrese nombre del alumno: ")
                cursos = int(input("Ingrese la cantidad de cursos: "))
                # Se almacena el alumno como sublista [nombre, cusos]
                alumnos.update({nombre_alumno: cursos})    
                print("El alumno fue añadido a la lista")   
            # --- Opcion 2: Visualizacion del registro de alumnos ---       
            elif opcion == "2": 
                if len(alumnos) == 0:
                    print("No hay alumnos en la lista")
                else:
                    print("Lista de alumnos:")
                    # Iteracionn sobre cada registro e impresion de sus datos
                    for alumno in alumnos: 
                        print(alumno)
            # --- Opcion 3: Revisa cuantos cursos tiene el alumno ---
            elif opcion == "3":
                persona = input("Ingrese el nombre del alumno: ")
                # Si la persona se encuentra entre los alumnos hace print de los datos
                if persona in alumnos:
                    print(persona, "tiene", alumnos[persona], "cursos")
                else:
                    print("Ese alumno no existe en la lista")
            # --- Opcion 4: Salida del programa ---
            elif opcion == "4":
                print("Gracias por utilizar el programa")
                break # Salida del bucle principal
            # --- Entrada invalida ---
            else:
                print("La opcion ingresada no es correcta, vuelva a intentarlo")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")
