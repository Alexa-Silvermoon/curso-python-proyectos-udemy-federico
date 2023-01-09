def devolver_distintos(*args):

    suma = 0
    mayor = 0
    menor = 0
    medio = 0
    menorAux = 0
    lista = []

    for item in args:

        suma += item

        if item > mayor:
            mayor = item

    mayorAux = mayor

    for item in args:

        if item < mayor:
            mayor = item
        menor = mayor

    print("mayor: ", mayorAux)
    print("menor: ", menor)
    print("suma: ", suma)

    if suma > 15:
        return f"La suma fue mayor a 15, se devuelve: { mayorAux} "

    if suma < 10:
        return f"La suma fue menor a 10, se devuelve: { menor} "

    # if suma in range(10, 15):
    if suma >= 10 and suma <= 15:
        # medio = ( suma - mayor - menor )
        medio = ( suma - mayorAux - menor )
        print("medio: ", medio)
        return f"La suma estuvo entre 10 y 15, se devuelve: { medio} "


num1 = 7
num2 = 2
num3 = 4
print(num1, num2, num3)
resul = devolver_distintos(num1,num2,num3)
print(resul)