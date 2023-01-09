
# ADVERTENCIA: el nombre del archivo no puede ser el mismo nombre de la importacin

# metodos randint(), uniform(), random(), choice(), shuffle()

from random import * # importar detodo de la libreria random, en JS es al reves

aleatorio = randint(1,50) # del uno al 50 selecciona un numero al azar
print(aleatorio)

print("------------------------------------------")

aleatorio2 = uniform(1,50) # del uno al 50 selecciona un decimal al azar
print(aleatorio2)
print( round(aleatorio2) ) # se puede redondear

print("------------------------------------------")

aleatorio3 = round(uniform(1,50),1) # del uno al 50 selecciona un decimal al azar, agregar un decimal al azar
print(aleatorio3)

print("------------------------------------------")

aleatorio4 = random() # el metodo random asi solo devuelve un valor entre 0 y 1
print(aleatorio4)

print("------------------------------------------")

colores = ["amarillo", "azul", "rojo", "blanco"]
print(colores)
aleatorio5 = choice(colores) # choice() elige un elemento al azar de una lista
print("Aleatorio: ", aleatorio5)

print("------------------------------------------")

numeros = list(range(5,50,5)) # 1 al 50 con paso 5
print(numeros)
shuffle(numeros)
print("Lista aleatoria: ", numeros)

# cosas random: https://www.udemy.com/course/python-total/learn/lecture/28159238?start=15#questions
