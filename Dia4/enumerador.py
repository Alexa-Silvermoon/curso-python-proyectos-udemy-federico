
lista = ["a", "b", "c"];

for item in enumerate(lista): # imprimir elemento e indice al lado
    print(item);

print("------------------------------------");

for i, item in enumerate(lista):
    print(i, item);

print("------------------------------------");

for i, item in enumerate(range(1,11)):
    print("pos: ", i, " item: ", item);

print("------------------------------------");

# lista de tuplas con item y posiciones:

misTuplas = list(enumerate(lista));
print(misTuplas)

# acceder dentro de la tupla:
print( misTuplas[1][0]) # (1, 'b')
print( misTuplas[1][1]) # (1, 'b')

print("------------------------------------");

"""
Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, 
obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

Tip: utiliza loops!
"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
print(lista_nombres)

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

print("------------------------------------");

palabra = "Python"
print(palabra)

lista = list(enumerate(palabra))
lista_indices = lista
print(lista_indices)

print("------------------------------------");

"""
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, 
que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los 
siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
print(lista_nombres)
buscarPorLetra = "M"

for i, item in enumerate(lista_nombres):
    if item[0] == buscarPorLetra:
        print(f"{ item } en pos: { i }")
# enumerador: https://www.udemy.com/course/python-total/learn/lecture/28157004#questions
