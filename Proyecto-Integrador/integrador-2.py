
# ==========================================================================================================================
# Sistema de gerstion de alumnos
# Descripcion: Permite al administrador registrar alumnos y consultar la lista.
# ==========================================================================================================================

# Autenticacion del usuario: Solicitud de credencial.
usuario = input("Ingrese su usuario: ")

# Estructura de datos principal: Lista de alumnos (Cada elemento es [nombre, cursos])
alumnos = []

# --- Validacion de usuario ---
if usuario == "admin":
    # --- Solicitud y validacion de contraseña ---
    contraseña = str(input("Ingrese su contraseña: ")) 
    if contraseña == "uni123":
        # --- Bucle principal del menu: Se ejecuta hasta que el usuario elija salir --- 
        while True: 
            # --- Menu de opciones disponibles ---
            print("Ingrese el numero de la operacion que desea ejecutar:")
            print("1 - Añadir un alumno a la lista")
            print("2 - Ver la lista de alumnos")
            print("3- Salir")
            # --- Captura y conversion de la opcion ingresada ---
            opcion = int(input("Opcion: "))
            # --- Opcion 1: Registro de nuevo alumno ---
            if opcion == 1: 
                nombre_alumno = input("Ingrese nombre del alumno: ")
                cursos = int(input("Ingrese la cantidad de cursos: "))
                # Se almacena el alumno como sublista [nombre, cusos]
                alumnos.append([nombre_alumno, cursos])    
                print("El alumno fue añadido a la lista")   
            # --- Opcion 2: Visualizacion del registro de alumnos ---       
            elif opcion == 2: 
                if len(alumnos) == 0:
                    print("No hay alumnos en la lista")
                else:
                    print("Lista de alumnos:")
                    # Iteracionn sobre cada registro e impresion de sus datos
                    for alumno in alumnos: 
                        print(alumno[0], "-", alumno[1], "cursos")
            # --- Opcion 3: Salida del programa ---
            elif opcion == 3:
                print("Gracias por utilizar el programa")
                break # Salida del bucle principal
            # --- Entrada invalida ---
            else:
                print("La opcion ingresada no es correcta, vuelva a intentarlo")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")