import collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

# Counter() sirve para saber cuantas veces re repite un numero
numeros = [2,1,1,3,4,4,4,5,5,5]
print(Counter(numeros)) # Counter({4: 3, 5: 3, 1: 2, 2: 1, 3: 1})

# Counter tambien funciona con letras
print(Counter('ALEXAN')) # Counter({'A': 2, 'L': 1, 'E': 1, 'X': 1, 'N': 1})

# Counter tambien funciona con frases,  se puede dividir en conteo de palabras agregando metodo split()
frase = 'ANITA LAVA LA TINA CHIQUI TINA'
print(Counter(frase.split())) # Counter({'TINA': 2, 'ANITA': 1, 'LAVA': 1, 'LA': 1, 'CHIQUI': 1})

print("---------------------------------------------")

# Similar a Counter(), el metodo most_common() sirve para saber cuantas veces re repite un numero,
# lo que devuelve lo ordena en TUPLA
serie = Counter([2,1,1,3,4,4,4,5,5,5])
print(serie.most_common()) # [(4, 3), (5, 3), (1, 2), (2, 1), (3, 1)]
print(serie.most_common(2)) # saber cuales son los dos numeros que mas repiten
print(list(serie)) # mostrar los numeros de serie pero sin repetidos

print("---------------------------------------------")

# crear un diccionario que si no se le asigna algo, por defecto contendra le string 'nada'
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos']) # llave 'dos' no contiene ningun valor, por defecto aparece 'nada'
print(mi_dic) # muestra mi_dic en memoria

print("---------------------------------------------")

mi_tupla = (500, 18, 65)
print(mi_tupla[1])

# acceder a valores de la tupla usando nombres
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
Ariel = Persona('Ariel', 1.76, 79)
print(Ariel.nombre)
print(Ariel.altura)
print(Ariel.peso)

# tambien se puede acceder con las llaves
print(Ariel[0])
print(Ariel[1])
print(Ariel[2])

print("---------------------------------------------")

# los deque permite agregar o eliminar valores ya sea por delante o por detras de una lista
"""
Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal 
que permite insertar y eliminar elementos por ambos extremos.

Investiga más al respecto en cualquier sitio de documentación, 
y a continuación implementa una deque a partir del módulo collections. 
Los elementos iniciales de la lista se brindan a continuación.

["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

La lista debe tener la capacidad de incorporar elementos por la izquierda, 
y recibir el nombre lista_ciudades.
"""

# complemento:
ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)
listaCasteadaCiudades = list(lista_ciudades)
print(listaCasteadaCiudades)

# insertar por la derecha
lista_ciudades.append("Bogota")
dequeCasteadoDerecha = list(lista_ciudades)
print(dequeCasteadoDerecha)

# insertar por la izquierda
lista_ciudades.appendleft("Tokyo")
dequeCasteadoIzquierda = list(lista_ciudades)
print(dequeCasteadoIzquierda)

"""
# con casteo:
lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
dequeCiudades = deque(lista_ciudades)
listaCasteadaCiudades = list(lista_ciudades)
# print("deque: ", dequeCiudades)
print(listaCasteadaCiudades)

# insertar por la derecha
dequeCiudades.append("Bogota")
dequeCasteadoDerecha = list(dequeCiudades)
print(dequeCasteadoDerecha)

# insertar por la izquierda
dequeCiudades.appendleft("Tokyo")
dequeCasteadoIzquierda = list(dequeCiudades)
print(dequeCasteadoIzquierda)
"""

"""
# sin casteo

dequeCiudades = collections.deque["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
print("deque: ", dequeCiudades)

# insertar por la derecha
dequeCiudades.append("Bogota")
print(dequeCiudades)

# insertar por la izquierda
dequeCiudades.appendleft("Tokyo")
print(dequeCiudades)
"""

# modulo collections: https://www.udemy.com/course/python-total/learn/lecture/28998004?start=0#questions
# deque: https://www.geeksforgeeks.org/deque-in-python/
# deque: https://stackoverflow.com/questions/5888680/how-do-you-add-a-string-to-a-deque-without-breaking-the-string-up-into-character
