
# los *args son usados en la funciones cuando no sabemos la cantidad exacta de argumentos que
# van a entrar en la funcion

# funciona parecido a  ... en JS

def suma(*args):
    total = 0
    for item in args:
        total += item
    return total

resultado = suma(2,2,2,4)
print("suma es: ", resultado)

# argumentos indefinidos: https://www.udemy.com/course/python-total/learn/lecture/28373272?start=15#questions

print("-----------------------------------")

"""
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, 
y que retorne la suma de sus valores al cuadrado.



Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""
def suma_cuadrados(*args):
    total = 0
    aux = 0

    for item in args:
        aux += item ** 2
        total = aux


    return total

lista = [2,3,5,-7]
print(lista)
result = suma_cuadrados(2,3,5,-7)
print("Sumados y al cuadrado: ", result)

print("-----------------------------------")

"""
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, 
y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, 
o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
"""


def suma_absolutos(*args):

    suma = 0

    for item in args:

        positivo = abs(item) # abs convierte valores a positivo sin necesidad de multiplicar * -1
        suma += positivo
        suma

    return suma


result = suma_absolutos(2,3,5,-7)
print(result)

print("-----------------------------------")

"""
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, 
y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

def numeros_persona(nombre, *args):

    suma_numeros = 0

    for item in args:
        suma_numeros += item


    return f"{nombre}, la suma de tus números es {suma_numeros}"

result = numeros_persona("Alexanderr", 3,3,3,1)
print(result)