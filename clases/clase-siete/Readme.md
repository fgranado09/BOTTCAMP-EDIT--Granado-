# Clase 7 - 27/03/26

# Repaso

* Cultura General
  * JSON
  * API
    * HTTP
* Python
  * Diccionarios
    * Una lista de elementos clave, valor...
    * Para representar datos concretos relacionados
    * Una lista de diccionarios para pensarse como una base de datos no relacional de nuestro sistema
  * Conjuntos
  * Tipos de aplicaciones
    * Flask


# Conocimiento General
* Antes 90 : Un sistema era una caja y diseñar un sistema era definir la estructura interna del mismo  y los sistemas eran grandes. Cada vez mas complejo
* Hoy 2026 : El diseño de un sistema no es tanto una caja grande sino varias cajitas chicas que se comunican entre si.
  * Hoy muchas cuestiones de arquitectura de sistemas se resuelven a nivel infraestructura.


# Funciones en Python

* Link de Colab
> https://colab.research.google.com/drive/1As6cDwldTeZq7jNTnllSsR0V7RQvgYQx?usp=sharing

```python
def separador():
  print("-----------------")

def saludar ():
  print("Hola Mundo")

resultado = saludar()
print(f"La funcion saludar devolvio {resultado}") # Devuelve None 

separador()

def saludar_con_parametros (nombre,apellido):
  print(f"Hola {nombre} {apellido}")

# Invoco una funcion especificando paramentros por nombre
saludar_con_parametros("Juan","Perez") # Es obligatorio pasar todos los parametros sino arroja error

separador()
# Pasar parametros segun nombre

saludar_con_parametros(apellido="Granado",nombre="Florencia")

separador()
```

* Cantidad variable de parametros con tuplas

```python
# Funciones que reciben una cantidad variable de paramertros

# Basicamente estamos recibiendo una tupla
def sumar (*numeros): # El asterisco representa una cantidad variable de elementos
  suma = 0
  for numero in numeros:
    suma += numero
  return suma

resultado = sumar (1,2,3,4,5,6,7,8,9,10)
print(resultado);

resultado = sumar (1,2,3)
print (resultado)

separador()

# Inspeccionar Parametros

def inspeccionar_parametros (*args):
  print("Recibi ", args);
  print("De tipo ", type(args));
  print("Cantidad de parametros recibidos, ", len(args));

inspeccionar_parametros(1,2,3,4,5)

separador()

tupla = (1,2,3,4,5)
inspeccionar_parametros(tupla)

separador()

# Si quiero convertir cada elemento de una tupla en un parametro separado al tengo que "desempaquetar"
inspeccionar_parametros(*tupla)  # Se hace con un asterisco adelante

```

# Parametros opcionnales o por defecto

```python
def saludo_formal (nombre = "Desconocido"):
  print(f"Hola {nombre}")

# Se puede invocar de dos maneras distintas
saludo_formal()
saludo_formal("Juan")

separador()

# Siempre el parametro opcional va al final

def saludo_completo (nombre , apellido = "Snow"):
  print (f"Hola {nombre} {apellido}")

saludo_completo("Jhon")
saludo_completo(nombre = "Jhon")
saludo_completo(apellido = "Snow", nombre = "John")
saludo_completo ("John", apellido = "Stark")
saludo_completo("Jhon", "Snow")

# Tira error si hago 
try:
  saludo_completo(apellido = "Stark")
except Exception as e:
  print("Si no le pongo el nombre me tira error")
```

* Parametros diccionario (Cantidad Variable de parametros con nombre)

```python
def mostrar_datos (**datos):
  print(datos)
  print(type(datos))

mostrar_datos(nombre = "Juan", apellido = "Perez")

separador()

# Para que muestre solo valores

def mostrar_solo_valores (**datos):
  for valor in datos.values():
    print(valor)

mostrar_solo_valores(nombre = "Florencia", apellido = "Granado")
```
* Funciones aun sin implementar

```python
def funcion_aun_no_implementada():
  return NotImplemented

# Se usa cuando queres declarar que en el futuro vas a implementar esta funcion pero por ahora no llegaste
resultado = funcion_aun_no_implementada()
print(resultado)

# Otra opcion es que si llaman a esta funcion sale un error
def funcion_aun_no_implementada_con_error():
  raise NotImplementedError #Si invocas esta funcion se aborta todo

print(funcion_aun_no_implementada_con_error)

```

* Funciones como parametro de funciones

```python
# Todas las funciones tienen que tener un cuerpo
# Si quiero declarar una funcion vacia en el cuerpo tengo que poner "pass"
def funcion_ejemplo():
  pass

def mostrar_tipo_parametro(parametro):
  print(type(parametro))

mostrar_tipo_parametro(5) # Numero (Int)
mostrar_tipo_parametro(funcion_ejemplo) # Funcion

variable_tipo_funcion = funcion_ejemplo
mostrar_tipo_parametro(variable_tipo_funcion) # Funcion

def sumar(a,b):
  return a+b

def restar(a,b):
  return a-b

def operar(fn,a,b):
  return fn(a,b)


resultado = operar(sumar,1,2)
print(resultado)

resultado = operar(restar,1,2)
print(resultado)

```

# Inteligencia Artificial

* Repositorio de Modelos Open Source de IA
> https://huggingface.co/

* Tarea: Crear un usaurio de HuggingFace
* En IA los modelos se dividen en dos categorias
  * Los propietarios
    * GPT
    * Claude
  * Modelos Open Source
    * Familia Llama (Los que puedan usar en wp)
  * Todos los modelos open source se suben a hugging face
  * Es como el github de los modelos open source
  * Tienen una seccion que se llama Spaces que te permite probar online los modelos open source
    * Ejemplo: Flux --> Para generar imagenes
      > https://huggingface.co/spaces/black-forest-labs/FLUX.1-dev
  * La interfaz grafica de todos los spaces se programa con una libreria que se llama Gradio
  * Gradio es una libreria por excelencia para hacer y compartir interfaces visuales de prueba para cosas de IA
    * Las interfaces de Gradio se pueden ejecutar en el Colab


# Distintos lenguajes

# Tipos de Apps en Python

* Ya vimos
  * Apps de escritorio --> tkinter
  * Multiplataforma --> kivy
  * Juegos --> pygame
  * Apis --> flask

## Interfaces Gradio

* Para propotipos de IA --> Gradio

```python
import gradio as gr

def saludar(nombre):
  return f"Hola {nombre}"

interfaz = gr.Interface(fn = saludar, inputs = "text", outputs = "text")
interfaz.launch()
```

* Gradio facilita la generacion de interfaces graficas para prototipos IA
* Genera uns utl publica para que cualquier persona pueda probar mi codigo
* Por defecto las interfaces gradio tienen un boton de submit

# Ejercicio 
* El programa va a determinar un numero al azar entre 1 y 100. El usuario debe adivinar ese numero y para ello tiene 5 oportunidades. El sistema le pregunta al usuario cual piensa que es el numero secreto. Si el usuario acierta, gana. Sino la maquina le informa si el numero secreto es mayor o menor al que el usuario pensaba. Si se le terminan las oportunidades para adivinar pierde. Usar Print e input.

```python
import random
 
numero_secreto = random.randint(1, 100)
oportunidades = 5
 
print("=== ADIVINA EL NÚMERO ===")
print(f"Tenés {oportunidades} oportunidades para adivinar un número entre 1 y 100.")
print()
 
for intento in range(1, oportunidades + 1):
    print(f"Oportunidad {intento} de {oportunidades}")
    respuesta = input("¿Cuál creés que es el número secreto? ")
 
    if not respuesta.isdigit():
        print("Por favor ingresá un número válido.\n")
        continue
 
    numero_usuario = int(respuesta)
 
    if numero_usuario == numero_secreto:
        print(f"\n¡Felicitaciones! ¡Adivinaste! El número secreto era {numero_secreto}. 🎉")
        break
    elif numero_usuario < numero_secreto:
        print("El número secreto es MAYOR al que dijiste.\n")
    else:
        print("El número secreto es MENOR al que dijiste.\n")
else:
    print(f"\n¡Se te acabaron las oportunidades! El número secreto era {numero_secreto}. 😔")
```

* Prompt copado para usar para la misma actividad

Ahora voy a hacer una aplicacion en gradio para correrlo en google colab , este es mi promt , primero mejoralo para que sea con mucha interacion visual , que tenga easter eggs y quiero que tenga trampas y sorpresas
El programa va a determinar un numero al azar entre 1 y 100. El usuario debe adivinar ese numero y para ello tiene 5 oportunidades. El sistema le pregunta al usuario cual piensa que es el numero secreto. Si el usuario acierta, gana. Sino la maquina le informa si el numero secreto es mayor o menor al que el usuario pensaba. Si se le terminan las oportunidades para adivinar pierde. Usar Print e input.

* Revisar codigo que paso compañero para analizar
