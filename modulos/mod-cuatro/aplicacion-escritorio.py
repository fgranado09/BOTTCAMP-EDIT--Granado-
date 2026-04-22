import tkinter as tk

# Funcion para un boton
def saludar():
    nombre = caja.get() # Asigno funcion a variable "nombre". get() retorna la cadena ingresada por el usuario al igual que input
    etiqueta_saludo.config(text= "Hola " + nombre ) # Esto es para mostrar el mensaje en alguna parte de la ventana

ventana = tk.Tk() # Se crea una ventana
ventana.config(width = 400, height = 300) # Establece medidas de ancho y alto a la ventana, los valores estan expresados en pixeles
ventana.title("Primera aplicacion de escritorio") # Establece un titulo a la ventana

boton = tk.Button(ventana, text="Hola mundo", command= saludar) # Creo un boton, en los argumentos tengo que aclarar dentro de donde va a ir ubicado y que texto va a tener
boton.place(x= 20, y=20) # Las coordenadas de la posicion del boton

caja = tk.Entry() # Es el espacio donde el usuario puede escribir
caja.place(x= 20, y= 120, width= 200, height= 25) # Hay que definir las coordenadas de donde va ubicado, tambien como proximo argumento se le puede agregar el ancho y la altura a la caja

etiqueta = tk.Label(ventana, text = "Ingresa tu nombre:", bg= "Green") # Muestra un texto
etiqueta.place (x=20, y=90) # Coordenadas

etiqueta_saludo = tk.Label()
etiqueta_saludo.place (x= 20, y= 200)

ventana.mainloop() # Esto hace que la ventana se vuelva visible y no se detenga hasta que el usuario la cierre. Siempre debe ir al final


# Aplicaciones de Escritorio

# Tk, wxWidgets, Qt, GTK, etc.

# Controles = Widgets ... Es cualquier componente grafico con el que yo puedo interactuar en una aplicacion de escritorio. 
# Ej botones, etiquetas, etc.

# Progamacion orientada a eventos: El programador puede asociar varios eventos con funciones
