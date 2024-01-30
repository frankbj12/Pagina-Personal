"""
r = (20 + 20) * 13
a = (17 / 15) + 30
b = 17 / 15 * 30
e = (17 / 15) * 30 
print(r,a,b,e)"""

"""
r = (x / y) + 1
a = (x + y) / (x - y)
b = (x + (y / z)) / (x - (y / z))
e = [(x + y)**2]**2
"""


"""
num_1 = int(input("ingrese un  numero: "))
num_2 = int(input("ingrese otro numero: "))

resultado_1 = num_1 /2
resultado_2 = num_2 /2

print(resultado_1,resultado_2)
"""

"""
print("mi primer programa en python.")
"""


"""print("v\ne\nr\nt\ni\nc\na\nl")
"""

"""
print("*****\n*   *\n*   *\n*   *\n*****")
"""

"""print("*\n***\n*****\n*******\n*********")
"""

"""dato = int(input("ingrese un dato: "))
print(f"su dato es {dato}")
"""

"""valor = int(input("ingrese un valor: "))

print(f"***************\n* su valor es: {valor} *\n***************")
"""

"""dinero = float(input("cuanto dinero desea invertir?: "))
cant = int(input("por cuantos meses desea invertir?: "))

incremento = 0.06
gxm = dinero * incremento
ganancia = gxm * cant
gtotal = dinero + ganancia

print(f"su retiro luego de  {cant} sera en total de $ {gtotal}")
"""
"""
cant_de_llam = int(input("cuantas llamadas realizo?: "))
minutos_de_llam = int(input("cuantos minutos llamo?: "))

costoxcom = cant_de_llam * 12
cada_seg = minutos_de_llam * 1.5
precio_a_cobrar = costoxcom + cada_seg

print(f"su cantidad de llamadas son {cant_de_llam} y su precio a cobrar es {precio_a_cobrar}")
"""

"""
venta1 = int(input("cual fue el valor de la venta?: "))
venta2 = int(input("cual fue el valor de la venta?: "))
venta3 = int(input("cual fue el valor de la venta?: "))

sueldo_base = 42000
comicion = (venta1 + venta2 + venta3) * 0.1
total_del_mes = comicion + sueldo_base
print("su sueldo sera de" ,total_del_mes)
"""

"""
cantidaddeseg = float(input("ingrese la cantidad de segundos: "))
segxhora = 3600
segxdia = 86400

miniutos = cantidaddeseg // 60
hora = cantidaddeseg // 3600
dia = cantidaddeseg // 86400


print(f"los segundos ingresados son {cantidaddeseg} segundos, en miniutos seria {miniutos} minutos, en horas seria {hora} horas y en dias seria {dia} dias")
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






