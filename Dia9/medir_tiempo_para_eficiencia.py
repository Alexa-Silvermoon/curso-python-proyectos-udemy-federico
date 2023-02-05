import time # para cronometrar

# El objetivo de esta prueba es demostrar cual de las siguiente 2 funciones que hacen lo mismo,
# trabaja mas rapido

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#print(prueba_for(10))
#print(prueba_while(10))

inicio = time.time()
prueba_for(1000000)
final = time.time()
print(f"Tiempo For Fue: { final - inicio }")
# PRUEBA FOR TUVO MEJOR RENDIMIENTO

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(f"Tiempo While Fue: { final - inicio }")


print("----------------------------------------------")

import timeit # para cronometrar tiempos MUY pequeños

declaracion = """
prueba_for(10)
"""

setup = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

# declaracion  de la funcion, la funcion o codigo a probar, numero de veces que quiero que se repita la prueba
duracion = timeit.timeit(declaracion, setup, number = 1000000)
print("Prueba For con timeit: ", duracion)

declaracion2 = """
prueba_while(10)
"""

setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

# declaracion  de la funcion, la funcion o codigo a probar, numero de veces que quiero que se repita la prueba
duracion2 = timeit.timeit(declaracion2, setup2, number = 1000000)
print("Prueba For con timeit: ", duracion2)

# modulos para medir el tiempo: https://www.udemy.com/course/python-total/learn/lecture/29024830#questions
