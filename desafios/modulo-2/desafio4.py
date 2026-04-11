# A la derecha, vemos un diagrama de flujo de
# cómo se hace para calcular un año bisiesto. La
# idea es llevar este algoritmo a código Python.

año = int(input("Ingrese un año a analizar: "))

if año % 400 == 0:
    print("El año " + str(año) + " es bisiesto.")
elif año % 4 == 0 and año % 100 != 0:
    print("El año " + str(año) + " es bisiesto.")
else:
    print("El año " + str(año) + " no es bisiesto.")

print("Fin")
