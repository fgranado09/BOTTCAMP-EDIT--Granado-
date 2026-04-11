usuario = input("Ingrese su usuario: ")

alumnos = []

if usuario == "admin":
    contraseña = str(input("Ingrese su contraseña: "))
    if contraseña == "uni123":
        while True:
            print("Ingrese el numero de la operacion que desea ejecutar:")
            print("1 - Añadir un alumno a la lista")
            print("2 - Ver la lista de alumnos")
            print("3- Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                nombre_alumno = input("Ingrese nombre del alumno: ")
                cursos = int(input("Ingrese la cantidad de cursos: "))
                alumnos.append([nombre_alumno, cursos])    
                print("El alumno fue añadido a la lista")          
            elif opcion == 2:
                if len(alumnos) == 0:
                    print("No hay alumnos en la lista")
                else:
                    print("Lista de alumnos:")
                    for alumno in alumnos:
                        print(alumno[0], "-", alumno[1], "cursos")
            elif opcion == 3:
                print("Gracias por utilizar el programa")
                break
            else:
                print("La opcion ingresada no es correcta, vuelva a intentarlo")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")