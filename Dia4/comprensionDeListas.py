palabra = "ALEXANDER"
print(palabra)

lista = []

for letra in palabra:
    lista.append(letra) # similar al split en JS

print(lista)

print("-------------------------------------------")

lista2 = [letra for letra in palabra] # compresion de listas
print(lista2)

print("-------------------------------------------")

lista3 = [num for num in range(0,20,2)] # de 0 a 21 con paso 2
print(lista3)

print("-------------------------------------------")

lista4 = [num2 / 2 for num2 in range(0,21)] # salta de 0.5 en 0.5 en 21 decimales
print(lista4)

print("-------------------------------------------")

lista5 = [num3 / 2 for num3 in range(0,21,2)] # salta de 0.5 en 0.5 per con paso 2, es decir salta de 1 en 1
print(lista5)

print("-------------------------------------------")

# para aclarar: 6*2 = 12, por ello supera la condicion de >10
lista6 = [num4 for num4 in range(0,21,2) if num4 * 2 > 10] # poco legible
print(lista6)

print("-------------------------------------------")

# para aclarar: 6*2 = 12, por ello supera la condicion de >10
lista7 = [num5 if num5 * 2 > 10 else 'no' for num5 in range(0,21,2)] # poco legible
print(lista7)

print("-------------------------------------------")

print("pasar de medida pies a metros")
pies = [10,20,30,40]
print(pies)
medicion = 3.281
print(medicion)
metros = []

for medida in pies:
    medida *= medicion
    metros.append(medida) # .append() en python equivale a .push() en JS

print(metros)

print("-------------------------------------------")

print("pasar de medida pies a metros forma simplificada")
pies = [10,20,30,40]
print(pies)
medicion = 3.281
print(medicion)

metros = [ medida * medicion for medida in pies]

print(metros)

print("-------------------------------------------")

"""
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a 
afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
"""

valores = [1, 2, 3, 4, 5, 6, 9.5]
print(valores)
valores_cuadrado = [ val ** 2 for val in valores]
print(valores_cuadrado)

print("-------------------------------------------")

"""
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a 
afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]
"""
valores = [1, 2, 3, 4, 5, 6, 9.5]
print(valores)
valores_pares = [ val for val in valores if val % 2 == 0 ]
print(valores_pares)

print("-------------------------------------------")

"""
Para la siguiente lista de temperaturas en grados Fahrenheit, 
expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. 
La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius
"""
temperatura_fahrenheit = [32, 212, 275]
print(temperatura_fahrenheit)
grados_celsius = [ (val - 32) * ( 5 / 9 ) for val in temperatura_fahrenheit ]
print(grados_celsius)

# compresion de listas: https://www.udemy.com/course/python-total/learn/lecture/28161730?start=240#questions
