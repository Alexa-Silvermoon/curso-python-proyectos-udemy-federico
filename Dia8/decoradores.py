
def cambiar_letras(tipo):

    def mayuscula(texto):

        print(texto.upper())

    def minuscula(texto):

        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula

# operacion = cambiar_letras('may') # convertir a mayuscula
operacion = cambiar_letras('min') # convertir a minuscula
operacion('pAlAbRa')

print('------------------------------------------------')

# El decorardor es una funcion que envuelve a otra funcion
# en este caso el decorador es decorar_saludo() y envuelve a mayuscula() y minuscula()

def decorar_saludo(funcion):

    # esta funcion opera a las funciones envueltas por el decorador
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra) # funcion ya sea mayuscula() o minuscula()
        print('adios')
    return otra_funcion

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())

minusculas('PyThON')
mayuscula('PyThON')

print('------------------------------------------------')

def decorar_saludo2(funcion2):

    # esta funcion opera a las funciones envueltas por el decorador
    def otra_funcion2(palabra2):
        print('hola')
        funcion2(palabra2) # funcion ya sea mayuscula() o minuscula()
        print('adios')
    return otra_funcion2

def mayuscula2(texto2):
    print(texto2.upper())

def minusculas2(texto2):
    print(texto2.lower())

mayuscula_decorada = decorar_saludo2(mayuscula2)
mayuscula_decorada('AlExAnDeR')

# decoradores: https://www.udemy.com/course/python-total/learn/lecture/28854194#questions
