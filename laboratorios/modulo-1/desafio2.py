# Ejercicio 2 

# Calcula los minutos que hay en una semana declarando variables

minuto = 60
hora = minuto * 60
dia = hora * 24
semana = dia * 7

resultado = semana / minuto
print(resultado)

# Dada esta situacion: 

# Una juguetería tiene mucho éxito en la venta de
# dos de sus productos: payasos y muñecas. Suele
# hacer ventas por correo y la empresa de logística
# les cobra por el peso de cada paquete, por lo que
# necesitan calcular el peso de los payasos y
# muñecas que saldrán en cada paquete a
# demanda. Cada payaso pesa 112 g y cada
# muñeca, 75 g.

# Escribe un programa que:

# Solicite al usuario el número de payasos y muñecas vendidos en el último pedido.

# Calcule el peso total del paquete que será enviado

peso_payaso = 112
peso_muñeca = 75

compra_payasos = input("Ingrese cuantos payasos desea comprar: ")
compra_muñecas = input("Igrese cuantas muñecas desea comprar: ")

total_compra_payasos = int(compra_payasos) * peso_payaso
total_compra_muñecas = int(compra_muñecas) * peso_muñeca

peso_total_paquete = total_compra_payasos + total_compra_muñecas

print(peso_total_paquete)