def mi_funcion():

    lista = []

    for x in range(1,5):

        lista.append(x * 10)

    return lista


def mi_generador():

    for x in range(1,5):

        yield x * 10 # devuelve algo solo cuando lo necesitemos en un momento exacto
        # de esta forma ahorramos espacio en memoria


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g)) # 10
print(next(g)) # 20
print(next(g)) # 30
print(next(g)) # 40

print("-----------------------------------------")

def mi_generador2():

    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g2 = mi_generador2()
print(next(g2)) # 1
print(next(g2)) # 2
print("hola aqui puede ir cualquier codigo extra")
print(next(g2)) # 3

print("-----------------------------------------")

"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia 
infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que 
sea llamada mediante next.
"""

print("Incrementar infinitamente")
def generador():
    x = 0

    while True:
        x += 1
        yield x

g3 = generador()
print(next(g3))
print(next(g3))
print(next(g3))

print("-----------------------------------------")

"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida 
múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente 
múltiplo (7, 14, 21, 28...).
"""

print("multiplos de 7")
def fun_generador():
    numero = 7
    multiplo = 0

    while True:
        multiplo += 1
        resul = numero * multiplo
        yield resul


g4 = fun_generador()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))

print("-----------------------------------------")

"""
Crea un generador que reste una a una las vidas de un personaje de videojuego, 
y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida
"""


def fun_generador2():
    vidas = 4

    while True:

        if vidas > 2:
            vidas -= 1
            yield f"Te quedan {vidas} vidas"
        elif vidas > 1:
            vidas -= 1
            yield f"Te queda {vidas} vida"
        else:
            yield f"Game Over"


perder_vida = fun_generador2()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

# generadores: https://www.udemy.com/course/python-total/learn/lecture/28863404?start=0#questions
