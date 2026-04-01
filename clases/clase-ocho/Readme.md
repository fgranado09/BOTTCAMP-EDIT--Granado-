## Clase 8 - 27/03/26

# Repaso

* Python
  * Estructuras de control
    * For
      * break
      * continue
      * else del for 
  * Funciones
    * Cantidad variable de parametros
      * (*Args) y (**kwargs)
        * *args ---> Recibo los parametros como una tupla
        * (**kwargs) ---> Recibo los parametros como un diccionario
        * Operador de desempaquetamiento ----> Diccionario o tupla ----> Convierte en parametros
      * pass (Para funciones vacias)
      * Parametros con nombre
        * saludar(nombre = "Florencia" , apellido = "Granado")
      * Parametros por defecto
      * Funciones que reciben funciones como parametro
  * Tipos de Aplicaciones
    * Gradio
      * interfaz = gr.Interface(fn = saludar, inputs = "text", outputs = "text") ---> Aca le paso por parametro la funcionn que se ejecuta cuando apretan "Submit"
  * Hugging Face
    * Crear usuario

# Modelo de lenguajes

* Open Source
  * Qwen
    * Es la copia china CHATGPT
    * Tiene personalizacion
    * No tiene limite de tokens
  * Deepseek (El que invento el modo razonamiento)
 
# IDES especializadas en IA
* Cursor
  * Esta pensado para desarrollar proyectos grandes
  * Mantiene mucho mejor el contexto de toda la estructura del proyecto
  * CTA (Call to action)
 

# Python

## Modulos de Python

* Proyectos Grandes
 * El junior tiende a meter todo en un solo archivo ---> El senior sabe organizar su codigo en forma eficiente dividiendolo en varios archivos. (Averiguar de que manera) 


* Hoy trabajamos local. Abrimos una carpeta con Visual Studio Code desde la terminal

```cmd
> code .
```

* Con cursor

```cmd
> cursor .
```

* Crear un archivo calculadora.py
* Ya sea en cursor o en vscode con github copilot en el chat de IA pedirle que cree 4 metodos

Crear 4 funciones (sumar, restar, multiplicar y dividir), tambien una constante que se llame PI. Programar los metodos para que sean seguros realizando todas las validaciones y controles pertinentes de tipo de rangos de entrada, tipos de datos. Quiero una version de las funciones que sea profesional


* La IA genero lo siguiente

```python
"""
Operaciones aritméticas básicas con validación estricta de operandos.
"""

from __future__ import annotations

import math
from numbers import Real
__all__ = ["PI", "sumar", "restar", "multiplicar", "dividir"]

# Constante π definida en términos de la biblioteca estándar (doble precisión IEEE 754).
PI: float = math.pi


def _validar_operando(nombre: str, valor: object) -> float:
    """
    Convierte el operando a float y rechaza tipos y valores no permitidos.

    No se aceptan ``bool`` (subclase de ``int`` en Python), ``complex``, cadenas
    ni ``None``. Solo ``int`` y ``float`` finitos (sin ``nan`` ni ``inf``).
    """
    if isinstance(valor, bool):
        raise TypeError(
            f"{nombre}: no se aceptan valores booleanos; use int o float explícitos."
        )
    if valor is None:
        raise TypeError(f"{nombre}: no se admite None.")
    if isinstance(valor, complex):
        raise TypeError(f"{nombre}: no se admiten números complejos.")
    if not isinstance(valor, Real):
        raise TypeError(
            f"{nombre}: se esperaba int o float, se obtuvo {type(valor).__name__}."
        )
    # Real incluye algunos tipos raros; restringimos a int/float explícitos.
    if not isinstance(valor, (int, float)):
        raise TypeError(
            f"{nombre}: se esperaba int o float, se obtuvo {type(valor).__name__}."
        )
    x = float(valor)
    if math.isnan(x):
        raise ValueError(f"{nombre}: NaN no es un valor válido.")
    if math.isinf(x):
        raise ValueError(f"{nombre}: infinito no es un valor válido.")
    return x


def _resultado_finito(nombre: str, resultado: float) -> float:
    if math.isnan(resultado):
        raise OverflowError(f"{nombre}: el resultado es NaN (operación no definida o inestable).")
    if math.isinf(resultado):
        raise OverflowError(
            f"{nombre}: el resultado excede el rango representable (desbordamiento)."
        )
    return resultado


def _es_int_seguro(a: float, b: float, r: float) -> bool:
    if not a.is_integer() or not b.is_integer() or not r.is_integer():
        return False
    ia, ib, ir = int(a), int(b), int(r)
    return float(ia) == a and float(ib) == b and float(ir) == r


def sumar(a: int | float, b: int | float) -> int | float:
    """
    Suma dos números. Devuelve ``int`` si ambos operandos y el resultado son enteros
    exactos; en caso contrario, ``float``.
    """
    x = _validar_operando("sumar: primer operando (a)", a)
    y = _validar_operando("sumar: segundo operando (b)", b)
    r = _resultado_finito("sumar", x + y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def restar(a: int | float, b: int | float) -> int | float:
    """Resta ``b`` de ``a``. Misma convención de tipo de retorno que ``sumar``."""
    x = _validar_operando("restar: primer operando (a)", a)
    y = _validar_operando("restar: segundo operando (b)", b)
    r = _resultado_finito("restar", x - y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def multiplicar(a: int | float, b: int | float) -> int | float:
    """Producto de ``a`` y ``b``. Misma convención de tipo de retorno que ``sumar``."""
    x = _validar_operando("multiplicar: primer operando (a)", a)
    y = _validar_operando("multiplicar: segundo operando (b)", b)
    r = _resultado_finito("multiplicar", x * y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def dividir(a: int | float, b: int | float) -> float:
    """
    Cociente ``a / b``. Siempre retorna ``float``.

    El divisor no puede ser cero. Se validan ambos operandos como en las demás funciones.
    """
    x = _validar_operando("dividir: dividendo (a)", a)
    y = _validar_operando("dividir: divisor (b)", b)
    if y == 0.0:
        raise ZeroDivisionError("dividir: división por cero no está definida.")
    r = x / y
    return _resultado_finito("dividir", r)

```

* Observaciones:
  * Usa TypeHints: A los parametros de las funciones les documenta los  tipos de datos que el programador esperaria usar
  * Es documentacion profesional
    * NO VA A TIRAR ERROR SI HAGO SUMAR("CADENA","CADENA") pero el que ve el codigo como tiene los type hints sabe que esta mal

 (Junior no le pone type hints al codigo, no aclara que tipos espera trabajar) --> El senior genera codigo autodocumentado con los tipos de datos como si python fuera fuertemente tipado.

 * Al profesor le llamo la atencion que la IA utilizara Object como tipo de dato de entrada en las funciones. Entonces le pregunto el porque del accionar.

* Nunca me quedo con lo primero que hace la IA . Nuestro rol como devs es cuestionar a la IA. Aprender de ella y adaptar su solucion.
  * Miro lo que hace la IA --> Lo entiendo --> Hago preguntas --> Lo cuestiono y lo mejoro
  * Segun mi criterio no tiene mucho sentido poner como parametro un "object", no aporta nada
  * Revisar el README del profe.
 


Un modulo en numpy es practicamente un "archivo" 

* Si queremos usar todos los metodos de un archivo usamos este import (archivo importar-modulo-completo.py)

```python
import calculadora 

# Varios Ejemplos   (2)
print(calculadora.sumar(1, 2))
print(calculadora.restar(1, 2))
print(calculadora.multiplicar(1, 2))
print(calculadora.dividir(1, 2))

# Un Ejemplo   (1)
print(calculadora.PI)

# Un Ejemplo   (1)
print(calculadora.sumar(1, 2))

# Parece como si el modulo calculadora fuere un objeto 
# Tiene un monton de metodos que podemos usar para realizar operaciones aritmeticas.
```
* Lo ejecuto y me da

```python
3
-1
2
0.5
3.141592653589793
3
```

* Importar partes especificas
* 


* Me quede en la hora 49 y me falta ver librerias. En esta clase Django






