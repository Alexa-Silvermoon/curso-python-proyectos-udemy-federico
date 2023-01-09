def zeroConsecutivos(lista):

    indice = lista.index(0)
    print("0 en indice: ", indice)

    if lista[indice] == 0:

        while lista[indice] == 0 and lista[indice + 1] == 0:
            print("Lista SI tenia dos 0 consecutivos", True)
            break
        else:
            print("Lista NO tenia dos 0 consecutivos", False)

lista = [5,6,1,0,0,9,3,5]
print("Lista: ", lista)
zeroConsecutivos(lista)

# https://pythonconejemplos.xyz/python/obtener-el-indice-o-la-posicion-de-un-elemento-en-una-lista-de-python/
