# Clase cinco - 18/03/2026

# Repaso

* Entornos Virtuales
* Python
  * Listas
  * Slices
    * Indices (Indices Negativos)
  * Kivy
    * App para celu multiplataforma
   
# Link del Colab del dia
> https://colab.research.google.com/drive/1NrBWseYSDegYAC3ofFoD8ZeIQCfnnWez?usp=sharing

# Python

## Tipos de datos 
* Tipos de datos
 * Basicos
   * int
   * float
   * str
   * complex
   * bool
 * Colecciones
   * List - []
   * tuple - ()
   * range
   * enumerate
   * set >>> proximamente
   * dict >>> proximamente
  
## Tuplas

* Usas la lista cuando los datos cambian
* Usas las tuplas cuando los datos son fijos
* Funcionan como las listas a excepcion que no se pueden modificar

## Rangos

* Revisar para que es mejor las listas y para que los rangos

# Aplicacion Web con Python - APIS

* Las apis son aplicaciones web sin frontend, toman y devuelven texto
* Para hacer APIS usamos la libreria FLASK

## Flask
>https://flask.palletsprojects.com/en/stable/

* Generamos nuestro proyecto con Claude
> https://claude.ai/chat/b0d0e5a8-71c8-4d68-ac2a-c970816b9bf6

# Git

* Creacion de archivo .gitignore
  * Sirve para que un archivo o una carpeta no se suba a github
  * En general todo el entorno virtual no se sube

# Entornos Virtuales
* Cuando un programa tiene muchas librerias estaria bueno informarle al que lo usa que librerias tienne que instalar
* En python la forma tradicional de hacerlo es utilizando un archivo requirements.txt
* Para instalar todas las librerias instaladas en ese archivo --> cmd pip istall -r requirements.txt (Es como un atajo para no instalar libreria por libreria)

* Para ejecutarlo primero creamos un entorno virtual y lo activamos
```cmd
>
>ventorno\Scripts\Activate
```


* Despues creamos un archivo requirements.txt donde dijimos que necesitamos FLASK


# Recapitulando

* Librerias vistas hasta ahora
  * flask: para programar apis
  * pygame: para hacer juegos
  * tkinter: para hacer aplicaciones de escritorio
  * kivy: para hacer aplicaciones multiplataforma (moviles principalmente)
  * panda: de oido todavia no sabemos para que es
  * Ya venian con python
    * random: Para crear numeros al azar
    * date, datetime: Es para fechas y horas
    * sys: para ver informacion del sistema (por ejemplo cuanto espacio en memoria ocupa una variable)
    * os: se usa para interactuar con el sistema operativo, ej: leer archivos
