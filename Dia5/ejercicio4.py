def contar_primos(num):

    contadorPrimos = 0

    for item in range(1, num):

        if item > 1:

            contador = 0
            i = 2
            while i<item and contador == 0:

                aux = item % i

                if aux == 0:
                    contador += 1

                i += 1

            if contador == 0:
                print("Es primo: ", item)
                contadorPrimos += 1
    print("Primos contados: ", contadorPrimos)

numero = int(input("Ingrese un numero: "))
print("Numero digitado: ", numero)
contar_primos(numero)

# https://www.youtube.com/watch?v=kcabccq1nRg
# https://miniwebtool.com/es/list-of-prime-numbers/?to=100
