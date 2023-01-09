
# verificar si un numero es de 3 cifras

def chequear3Cifras(numero):

    return numero in range(100,1000)

suma =  200 + 200
resultado = chequear3Cifras(suma)
print(f"{ suma } es numero de 3 cifras?: { resultado }")

print("---------------------------------------------")

def chequear3CifrasB(lista):

    for n in lista:
        if n in range(100,1000):
            return f"El primer numero encontrado de 3 cifras es: { n }"
        else:
            pass # hace que vuelva a ciclar
    # el pass debe ir en el else, ya que si ninguna condicion se cumplio, se ejecutara el return final:

    return "Esa lista no tenia numeros de 3 cifras"

lista = [99,10,100,6000]
print(lista)
resultado = chequear3CifrasB(lista)
print(resultado)

print("---------------------------------------------")

def chequear3CifrasC(lista):

    lista3Cifras = []

    for n in lista:
        if n in range(100,1000):
            lista3Cifras.append(n)
        else:
            pass # hace que vuelva a ciclar
    # el pass debe ir en el else, ya que si ninguna condicion se cumplio, se ejecutara el return final:

    return lista3Cifras

lista = [99,10,100,6000, 500]
print(lista)
resultado = chequear3CifrasC(lista)
print("Los numeros de 3 cifras son: ", resultado)

print("---------------------------------------------")

"""
Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los 
valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
"""


def todos_positivos(lista_numeros):

    # comprobar si todos los elementos cumplen una condicion
    return all(item > 0 for item in lista_numeros)

lista_numeros = [10, 20, 33, -7]
resultado = todos_positivos(lista_numeros)
print("resultado: ", resultado)

print("---------------------------------------------")

"""
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros)
 siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

"""


def suma_menores(lista):

    total = 0

    for item in lista:

        if item in range(0,1000):
            total += item
    return total

lista_numeros = [1,5,0,500,5000,750]
print(lista_numeros)
resultado = suma_menores(lista_numeros)
print(resultado)

print("---------------------------------------------")

"""
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista 
(lista_numeros), y devuelva el resultado de dicha cuenta.

"""

def cantidad_pares(lista):

    conteoPares = 0

    for item in lista:

        if item % 2 == 0:
            conteoPares += lista.count(item) # contar los pares en la lista
    return conteoPares

lista_numeros = [1, 2, 3, 4, 5, 6]
print(lista_numeros)
resultado = cantidad_pares(lista_numeros)
print("Pares en la lista: ", resultado)


# funciones dinamicas: https://www.udemy.com/course/python-total/learn/lecture/28369108#questions
