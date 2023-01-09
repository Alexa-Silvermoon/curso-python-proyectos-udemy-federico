from random import shuffle, randint

# juego de sacar el palito mas largo, o mas corto
# si el palito es el mas corto, pierde, SINO gana

# lista inicial
palitos = ['-', '--', '---', '----']


# mezclar lista
def mezclar(lista):
    shuffle(lista)
    return lista


# pedir intento
def probar_suerte():

    intento = ''

    while intento not in ['1','2','3','4']: # mientras inteto no esta dentro del 1 y el 4
        intento = input("Ingrese un numero del 1 al 4: ")

    return int(intento) # esto se llama castear


# comprobar intento
def chequeo(lista, intento):

    if lista[intento - 1] == '-':
        print("Perdiste")
    else:
        print("Ganaste")

    print("Palito que te salio fue: ", lista[intento-1])


listaMezclada = mezclar(palitos)
print(listaMezclada)

intentoUsuario = probar_suerte()
print("Palito que escogiste fue: ", intentoUsuario)

chequeo(listaMezclada, intentoUsuario)

print("--------------------------------------------")

"""
Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente 
los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- 
un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar 
entre 1 y 6.
"""
print("lanzar dados")

def lanzar_dados():

    valDado1 = randint(1,6)
    valDado2 = randint(1,6)

    # print(valDado1, valDado2)

    return (valDado1, valDado2)


valDado1, valDado2 = lanzar_dados()
print(valDado1, valDado2)


def evaluar_jugada(valDado1, valDado2):

    suma_dados = valDado1 + valDado2
    msg = ''

    if suma_dados <= 6:
        msg = f"La suma de tus dados es {suma_dados}. Lamentable"

    if suma_dados > 6 and suma_dados < 10:
        msg = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"

    if suma_dados >= 10:
        msg = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

    return msg


mensaje = evaluar_jugada(valDado1, valDado2)
print(mensaje)

print("--------------------------------------------")

"""
Crea una función llamada reducir_lista() que tome una lista como argumento 
(crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados 
(dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. 
El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por 
la anterior función, y que calcule el promedio de los valores de la misma. 
Debe devolver el resultado, sin imprimirlo.
"""

import statistics

def reducir_lista(lista_numeros):

    mayor = 0
    listaMayorEliminado = []
    listaSinDuplicados = []

    listaSinDuplicados = list(set(lista_numeros)) # set() elimina duplicados
    # print(listaSinDuplicados)

    for item in listaSinDuplicados:

        if item > mayor:
            mayor = item
            # print(mayor)
    listaSinDuplicados.remove(mayor)
    listaMayorEliminado = listaSinDuplicados

    # print(listaMayorEliminado)
    return listaMayorEliminado


lista_numeros = [1,2,15,7,2,8]
print("Lista original: ", lista_numeros)
listaFiltrada = reducir_lista(lista_numeros)
print("Lista filtrada: ", listaFiltrada)

def promedio(llistaFiltradas):

    valPromedio = statistics.mean(listaFiltrada)
    # print(promedio)

    return valPromedio

valPromedio = promedio(listaFiltrada)
print("Promedio es: ", valPromedio)

print("--------------------------------------------")

"""
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos 
para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, 
debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de 
números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", 
y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" 
y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de 
una secuencia.
"""

from random import choice

def lanzar_moneda():

    moneda = ["Cara", "Cruz"]
    seleccion = choice(moneda)
    # print(seleccion)

    return seleccion

res_lanzar_moneda = lanzar_moneda()
print(res_lanzar_moneda)

def probar_suerte(res_lanzar_moneda, lista_numeros):

    if res_lanzar_moneda == "Cara":
        lista_numeros.clear() # eliminar todos los elementos de una lista
        print("La lista se autodestruirá: ", lista_numeros)

        return lista_numeros

    if res_lanzar_moneda == "Cruz":
        print("La lista fue salvada: ", lista_numeros)

        return lista_numeros



lista_numeros = [1,2,3,4,5,6,7,8,9,10]

res_probar_suerte = probar_suerte(res_lanzar_moneda, lista_numeros)
print(res_probar_suerte)

# https://geekflare.com/es/remove-duplicate-items-from-python-lists/
# https://lineadecodigo.com/python/eliminar-elementos-de-una-lista-con-python/
# https://naps.com.mx/blog/hallar-el-valor-maximo-y-minimo-de-una-lista-en-python/
# https://www.delftstack.com/es/howto/python/get-average-of-list-python/
# https://www.techiedelight.com/es/remove-all-items-from-list-python/
# https://www.udemy.com/course/python-total/learn/lecture/28372490#questions
