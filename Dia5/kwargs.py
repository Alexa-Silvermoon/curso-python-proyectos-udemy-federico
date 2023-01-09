
# kwargs hace que los valores ingresados a la funciones, se vuelvan diccionarios

def suma(**kwargs):

    print(type(kwargs))

    total = 0

    for clave, valor in kwargs.items(): # similar a for( let LV of arreglo.entries() ) en JS
        print(f"clave es: { clave }, valor es: { valor }")

        total += valor

    return total

resultado = suma(x=3, y=5, z=2)
print("La suma es: ", resultado)

print("--------------------------------------")

def prueba(num1, num2, *args, **kwargs):

    print("num1: ", num1)
    print("num2: ", num2)
    print("args: ", args)
    print("kwards: ", kwargs)

    total = 0

    for arg in args:
        print(f"arg: ", arg)


    for clave, valor in kwargs.items(): # similar a for( let LV of arreglo.entries() ) en JS
        print(f"clave es: { clave }, valor es: { valor }")

resultado2 = prueba(10,20,100,200,300,x="uno",y="dos",z="tres")


print("--------------------------------------")

def prueba2(num1, num2, *args, **kwargs):

    print("num1: ", num1)
    print("num2: ", num2)

    for arg in args:
        print(f"arg: ", arg)


    for clave, valor in kwargs.items(): # similar a for( let LV of arreglo.entries() ) en JS
        print(f"clave es: { clave }, valor es: { valor }")

lista = [ 100,200,300 ]
kwargs = { "x":"uno","y":"dos","z":"tres" }

resultado2 = prueba2(10,20, lista, kwargs)

print("--------------------------------------")

"""
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, 
y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):

    conteo = 0

    for kwar in kwargs:
        conteo += 1

    return conteo

resul = cantidad_atributos(x="uno",y="dos")
print("Cantidad de atributos: " ,resul)

print("--------------------------------------")

"""
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los 
atributos entregados en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""

def lista_atributos(**kwargs):

    lista = []

    for llave, valor in kwargs.items():

        lista.append(valor)
        # print(valor)

    return lista

resul = lista_atributos(x=3, y=5, z=2)
print(resul)

print("--------------------------------------")

"""
Crea una función llamada describir_persona, que tome como parámetros su nombre 
y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
  

"""
def describir_persona(nombre, **kwargs):

    print(f"Características de {nombre}:")

    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{ nombre_argumento }: { valor_argumento }")

describir_persona("tomás", color_ojos="azules", color_pelo="rubio")

# argumentos indefinidos kwargs: https://www.udemy.com/course/python-total/learn/lecture/28373768?start=45#questions
