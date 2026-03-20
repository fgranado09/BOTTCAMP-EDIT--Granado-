## Clase Seis - 20/03/26

# Repaso

* Python
  * Tuplas: Son inmutables, unan vez que las creas no se puede sacar ni agregar elementos
  * Desempaquetar v1, v2 = (v1, v2)
  * Silicing tambien en tuplas
  * Rangos
  * Funciones built-in
    * enumerate
  * Funciones
    * Declarar funciones con def
    * Esta curiosidad que una funcion puede devolver varios valores en python y el resultado lo recibo como tupla y lo puedo         desempaquetar
  * Tipos de aplicaciones
    * Aplicaciones Web/APIS
      * Flask
  * Repasamos entornos virtuales

# Colab del dia
> https://colab.research.google.com/drive/1ylSzFeRYPsqaGpEnLx7J2x_go7hUJq_s?usp=sharing


# Tipos de datos que vamos a ver hoy...

* Diccionarios
* Sets / conjuntos

# Javascripts

* El lenguaje de programacion utizado dentro de los navegadores para la parte de front
* Si estoy en el navegador y apreto F12 puedo abrir la consola del navegador de Javascript
* Fue un lenguaje trascendental en el mundo Dev. Todos en alguna manera lidia con el.
* Javascript puso de moda un lenguaje que se usa para representar informacion, almacennar informacion, comuinicar informacion

# JSON (Javascript Object Notation)
* En la consola de javascript (F12 en cualquier pagina) puedo declarar un objeto json

```javascript

let persona = {
  nombre: "Esteban",
  apellido: "Calabria",
  edad: 45
}


// Tambien puedo escribir las claves entre comillas (Esto es mas estandar)
```
* Luego cuando tengo un objeto en json le puedo consultar en forma separada por cada uno de sus atributos

```javascript

persona.nombre

o

persona["nombre"]
```


* Si hago un paralelismo con la programacion orienta a objetos, un objeto json se centra mas en la parte de datos que la de comportamiento
* En python vimos que las variables son objetos. Y a los objetos le podes pedir cosas ejecutando metodos sobre ellos


# Noticias
* Ahora hay un lenguaje que sale como alternativa al json que se llama toon (token object notations) (Gastar menos token cuando usamos modelos de lenguaje) - Tenes menos longitud, es mas compacto.

# Python 

## Tipos de datos
* Basicos
  * int
  * float
  * str
  * complex
  * bool
* Especiales
  * None
* Enumerables
  * list
  * tuple
  * dict
  * set << todavia no lo vimos
  * range
  * enumerate

## Diccionarios

* Los diccionarios en python representan una estructura que almacena una lista de elementos (clave, valor) donde la clave es unica
* Los diccionarios son casi lo mismo que un json en javascript

* Ejemplo -- Declarar y acceder

```python

persona = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 30,
}

print(persona)

# Esto no funciona en python como en javascript
# print (persona.nombre)

# Hay que usar la sintaxis de indice como si fuera el indice de una lista
# Con los corchetes

print (persona["nombre"])
print (persona["apellido"])
print (persona["edad"])

try:
  print (persona["sarasa"]) # Falla si haces referencia a un atributo que no existe
except KeyError:
  print ("La llave no existe")


# Tambien puedo usar el get
print (persona.get("nombre"))
print (persona.get("apellido"))
print (persona.get("edad"))
print (persona.get("algo")) # No tiene informacion el objeto 

sarasa = persona.get("sarasa")
print(sarasa)
print (type(sarasa))
# Les presento al tipo de dato "Especial" None en python

nada = None
```

## Modificiar diccionario

```python
# A los diccionarios se les puede agregar elementos dinamicamente y modificar elementos existentes

persona ["dni"] = 40903870
persona ["edad"] = 28
print(persona)

# Se van agregando 

```

## Diccionarios Anidados y listas de diccionarios

```python

alumnos = [
    {"nombre" : "Majo", "Apellido" : "Pisseta"},
    {"nombre" : "Lucas", "Apellido" : "Santiago"},
]

for alumno in alumnos:
  print(alumno["nombre"], alumno["Apellido"])

  datos_persona = {
      "Nombre" : "Juan",
      "Apellido": "Perez",
      "hijos" : ["Julieta", "Amadeo"],
      "direccion" : {
          "calle": "Calle Falsa",
          "numero" : 123,
          "ciudad" : "Springfield",
      }
  }

  print(datos_persona["direccion"]["calle"])
  print(datos_persona["hijos"][1])

```

## Recorrer un diccionario


```python

automovil = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964,
    "color": "rojo"
}
#Recorrer las claves
print("Recorro las claves del Diccionario")
for clave in automovil.keys():
    print(clave)
#Recorrer los valores
print("Recorro los valores del Diccionario")
for valor in automovil.values():
    print(valor)
#Recorrer ambos al mismo tiempo
print("Recorro ambos al mismo tiempo")
for clave, valor in automovil.items():
    print(f"{clave} : {valor}")

```











