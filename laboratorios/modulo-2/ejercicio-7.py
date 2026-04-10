# Una agencia de viajes tiene un sistema de información
# para paquetes turísticos. Realiza un programa que, al
# ingresar el paquete (solo la letra), genere una
# descripción de lo que contiene cada “combo”.

a = "Cancun 7 noches + aereos: u$s 1200 por persona."
b = "Miami 8 noches + aereos + alquiler de auto: u$s 1500 por persona."
c = "Bariloche 10 noches + aereos + excursiones: u$s 1300 por persona."
d = "Rio de janeiro 10 noches + aereos + excursiones: u$s 1400 por persona."

combo = input("Ingrese el combo del cual necesita informacion:")

if combo == "a":
    print(a)
elif combo == "b":
    print(b)
elif combo == "c":
    print(c)
elif combo == "d":
    print(d)
