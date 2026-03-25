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



# Distintos lenguajes

# Tipos de Apps en Python
