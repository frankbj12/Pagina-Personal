#Resolver el siguiente ejercicio de programación
""""
Resolver el siguiente ejercicio de programación
El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. 



En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa que calcule el sueldo promedio del empleado Juan. Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:



a. Sueldo bajo: por debajo de 300 dólares.

b. Sueldo normal:  entre 300 a 900.

c. Sueldo mejor de lo normal: más de 900 dólares.



Tip: se debe utilizar estructuras condicionales.
"""



"""
# Definir los montos de sueldo para cada período
sueldos = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Calcular el sueldo promedio
sueldo_promedio = sum(sueldos) / len(sueldos)

# Determinar la categoría del sueldo
if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif sueldo_promedio >= 300 and sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"

# Imprimir resultados
print(f"El sueldo promedio de Juan es: {sueldo_promedio} dólares.")
print(f"Categoría del sueldo: {categoria}")
"""

x=0
int(input("ingrese un numero: "))
print(x)