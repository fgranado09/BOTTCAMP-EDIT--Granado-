# 1. Lee la siguiente situación problemática:
# Un empleado cobró 300 dólares por mes desde
# enero a junio, 500 dólares de julio a octubre, y
# 700 dólares por mes en noviembre y en
# diciembre.

# 2. Crea un programa que calcule el sueldo
# promedio y que indique si este empleado está
# cobrando un sueldo bajo, normal o mejor de lo
# normal.
# ● Sueldo bajo: por debajo de 300 dólares.
# ● Sueldo normal: entre 300 a 900.
# ● Sueldo mejor de lo normal: más de 900
# dólares.

sueldo_enero_junio = 300 * 6
sueldo_julio_octubre = 500 * 4      
sueldo_noviembre_diciembre = 700 * 2

sueldo_total = sueldo_enero_junio + sueldo_julio_octubre + sueldo_noviembre_diciembre
sueldo_promedio = sueldo_total / 12     

print("El sueldo promedio es: " + str(sueldo_promedio))     

if sueldo_promedio < 300:
    print("El sueldo es bajo.")
elif sueldo_promedio <= 900:
    print("El sueldo es normal.")
else:
    print("El sueldo es mejor de lo normal.")