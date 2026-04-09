# Crea un programa que permita ingresar dos
# cadenas vía la consola y las compare. Luego,
# debe imprimir un mensaje en caso de que
# sean iguales y otro en caso de que sean
# diferentes.

# Solicitar al usuario que ingrese dos cadenas
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")  

# Comparar las cadenas
if cadena1 == cadena2:
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son diferentes.")


# Crea un programa que solicite el nombre de
# un alumno a través de la consola, y luego
# chequee que no esté vacío. En caso de estarlo,
# tiene que imprimir un mensaje de error; caso
# contrario, deberá imprimir un mensaje
# indicando que se ingresó correctamente.

# Solicitar al usuario que ingrese el nombre del alumno
nombre_alumno = input("Ingrese el nombre del alumno: ")

# Verificar si el nombre está vacío
if nombre_alumno == "":
    print("Error: El nombre del alumno no puede estar vacío.")
else:
    print("Se ingresó correctamente el nombre del alumno.")


# Pedir la edad por teclado y comparar si es
# mayor o menor de edad. No olvidar de que
# para poder comparar el ingreso, debe ser
# convertido a int, ya que el usuario ingresa un
# número entero.

tu_edad = int(input("Ingrese su edad: "))

if tu_edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")