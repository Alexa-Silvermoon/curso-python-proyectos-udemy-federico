preciosCafe = [{"capuccino", 1.5}, ("expreso", 1.2), ("moka", 1.9)]
print(preciosCafe)

for cafe, precio in preciosCafe:
    print(f"cafe: { cafe }, precio: { precio }")

print("-----------------------------------------")

# saber cual es el cafe mas caro:

def cafeMasCaro(listaPrecios):

    precioMayor = 0
    CafeMasCaro = ''

    for cafe,precio in listaPrecios:

        if precio > precioMayor:
            precioMayor = precio
            CafeMasCaro = cafe
        else:
            pass

    return (CafeMasCaro, precioMayor)

preciosCafe2 = [{'capuccino', 1.5}, ('expreso', 3.0), ('moka', 1.9)]
cafe, precio = cafeMasCaro(preciosCafe2)
print(f"El cafe { cafe } tiene un precio de { precio }")

# ejemplo de funciones: https://www.udemy.com/course/python-total/learn/lecture/28370608#questions
