def numeros_perfumeria():

    for n in range(1, 10000): # ninguna farmacia deberia llegar a 10000 turnos en un dia

        yield f"P - { n }" # en espera, solo se generara cuando se le solicite


def numeros_farmacia():

    for n in range(1, 10000):

        yield f"f - { n }"


def numeros_cosmetica():

    for n in range(1, 10000):

        yield f"c - { n }"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(rubro): # usado en principal - proyectoDelDia8.py

    print("\n" + "*" * 23)
    print("Su Numero es:")

    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))

    print("Por Favor Espere en la Fila")
    print("*" * 23 + "\n")
