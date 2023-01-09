def ordenAlfabetico(palabra):

    palabraSinRepetidos = []
    palabraOrdenadaLIST = []
    # palabraOrdenadaSTR = ''

    for pal in palabra:

        if pal not in palabraSinRepetidos:

            palabraSinRepetidos.append(pal)

    # print(palabraSinRepetidos)

    # palabraOrdenadaSTR = ''.join(sorted(palabraSinRepetidos)) # lo devuelve como string
    # print(type(palabraOrdenadaSTR))
    # return palabraOrdenadaSTR

    palabraSinRepetidos.sort() # lo devuelve como list
    palabraOrdenadaLIST = palabraSinRepetidos

    return palabraOrdenadaLIST

palabraOriginal = "entretenido"
print("Palabra original: ", palabraOriginal)
resul = ordenAlfabetico(palabraOriginal)
print(resul)

# https://www.techiedelight.com/es/sort-string-python/
# https://geekflare.com/es/remove-duplicate-items-from-python-lists/
# https://j2logo.com/python/ordenar-una-lista-en-python/
