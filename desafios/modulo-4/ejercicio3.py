# Crea una aplicación de escritorio que simule un
# dado, es decir, debe arrojar número aleatorio de
# 1 al 6.
# ● La vista de la aplicación debería ser similar a
# la imagen de la derecha.
# ● En la caja, deberían de aparecer los resultados
# aleatorios cada vez que se presiona el botón.
# ● Antes de mostrar los resultados se limpia la
# caja, dejando el mismo resultado hasta que se
# vuelve a pulsar

import tkinter as tk
import random

def dado():
    caja_resultado.delete(0,tk.END)
    valor = random.randint(1,6)
    caja_resultado.insert(0, valor)

ventana = tk.Tk()
ventana.config(width= 300, height= 300)
ventana.title("Dado 2.0")

boton = tk.Button(ventana, text= "Arroja el dado", command= dado)
boton.config(width= 15, height= 3)
boton.place(relx= 0.5, rely= 0.3, anchor= "center")

etiqueta = tk.Label(ventana, text= "Valor:")
etiqueta.place(relx= 0.5, rely= 0.5, anchor= "center")

caja_resultado = tk.Entry()
caja_resultado.place(relx= 0.5, rely= 0.6, anchor= "center")

ventana.mainloop()
