# ==========================================================================================================================
# Sistema de gerstion de alumnos
# Descripcion: Permite al administrador registrar alumnos y consultar la lista.
# ==========================================================================================================================

# === Integracion Tkinter para desarrollo de app de escritorio ===

import tkinter as tk

# === Diccionarios ===

# Diccionario Global que almacena alumnos
# Estructura: {nombre_alumno: cantidad_cursos}

alumnos = {}

# === Funciones ===

# Verifica si se ingresa texto en la casilla del Alumno
def verificar (dato):
    if dato == "":
        dato = "error"
    return dato

# Convierte el valor ingresado en caja de texto a un entero, caso de no ingresar un numero arroja error
def convertir (valor):
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = "error"
    return valor

# --- Funcion para agregar alumno ---
# Solicita nombre y cantidad de cursos realizados, y los guarda en el diccionario
def agregar_alumnos():
    nombre_alumno = caja_alumno.get()
    nombre_alumno = verificar(nombre_alumno) # Verificacion
    cursos = caja_cursos.get()
    cursos = convertir(cursos) # Verificacion
    if nombre_alumno == "error":
        print("Error. Nombre Vacio")
    elif cursos == "error":
        print("Error. El ingreso de cursos debe ser solo numeros")
    else:
        alumnos[nombre_alumno] = cursos
        print("El alumno fue añadido a la lista")
        caja_alumno.delete(0, tk.END)
        caja_cursos.delete(0, tk.END)

# --- Funcion para ver lista de alumnos ---
# Recorre e imprime todos los nombres guardados en el diccionario
def ver_alumnos():
    if len(alumnos) == 0:
        print("No hay alumnos en la lista")
    else:
        print("Lista de alumnos:")
        # Al iterar el diccionario, Python devuelve las claves (nombres)
        for alumno in alumnos:
            print(alumno)

# --- Funcion para ver la cantidad de cursos de un alumno ---
# Solicita un nombre y busca su valor (cursos) en el diccionario
def ver_cursos():
    persona = caja_alumno.get()
    # Verifica si el nombre existe como clave en el diccionario
    if persona in alumnos:
        print(persona, "tiene", alumnos[persona], "cursos")
    else: 
        print("Este alumno no existe en la lista")
    caja_alumno.delete(0, tk.END)


# === Ventana ===

ventana = tk.Tk()
ventana.config (width =  500, height =  300)
ventana.title("Proyecto Integrador")

boton_lista = tk.Button(ventana, text= "Ver lista de Alumnos", command= ver_alumnos)
boton_lista.place(x= 15, y= 10)

etiqueta_alumno = tk.Label(ventana, text= "Nombre Alumno:")
etiqueta_alumno.place(x= 15, y= 50)

caja_alumno = tk.Entry()
caja_alumno.place(x= 130, y= 50)

etiqueta_cursos = tk.Label(ventana, text= "Cursos:")
etiqueta_cursos.place(x= 15, y= 86)

caja_cursos = tk.Entry()
caja_cursos.config(width= 7)
caja_cursos.place(x= 130, y= 85)

boton_agregar = tk.Button(ventana, text= "Agregar a la lista", command= agregar_alumnos)
boton_agregar.place(x= 15, y= 130)

boton_visualizacion_cursos = tk.Button(ventana, text= "Ver cantidad de cursos", command= ver_cursos)
boton_visualizacion_cursos.place(x= 130, y= 130)

ventana.mainloop()

