
from random import choice

# palabras = ['helicoptero','dinosaurio','otorrinonaringologo','helipuerto']
palabras = ['PERRO','GATO']
letrasCorrectas = []
letrasIncorrectas = []
intentos = 10
aciertos = 0
isJuegoTerminado = False

def elegirPalabra(listaPalabras):

    palabraElegida = choice(listaPalabras) # elegir una palabra al azar
    letrasUnicas = len(set(palabraElegida)) # eliminar letras repetidas y saber longitud sin repetidas

    return palabraElegida, letrasUnicas

def pedirLetra():

    letraElegida = ''
    isValida = False

    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

    while not isValida: # mientras isValida sea False

        letraElegida = input("Escribe una letra: ").upper()

        # letras debe estar en abecedario y solo debe haaberse digitado una letra
        if letraElegida in abecedario and len(letraElegida) == 1:

            isValida = True

        else:

            print("No escribiste una letra")

    return letraElegida


def mostrarTablero(palabraElegida):

    listaOculta = []

    for letrax in palabraElegida:

        if letrax in letrasCorrectas: # si latra elegida esta en letras correctas, agregarla a listaOculta

            listaOculta.append(letrax)

        else:

            listaOculta.append('_') # si letra no esta en letras correctas, se agrega un guion

    print(' '.join(listaOculta))


def chequearLetra(letraElegida, palabraOculta, vidas, coincidencias):

    fin = False

    # letra elegida debe estar en la palabra oculta y no debe haber sido escrita anteriormente por el usuario
    if letraElegida in palabraOculta and letraElegida not in letrasCorrectas:

        letrasCorrectas.append(letraElegida)
        coincidencias += 1 # se pasara a aciertos

    # no restar vidas si usuario vuelve a escribir una letra ya encontrada
    elif letraElegida in palabraOculta and letraElegida in letrasCorrectas:
        print("Ya habias encontrado esa letra")
    else:

        letrasIncorrectas.append(letraElegida)
        vidas -= 1 # si letra no esta en letras correctas, se resta una vida

    if vidas == 0:

        fin = perder()

    elif coincidencias == letrasUnicas:

        fin = ganar(palabraOculta)

    return vidas, fin, coincidencias

def perder(): # al final del juego

    print("Perdiste, fin del juego")
    print("Palabra oculta era: ", palabra)

    return True

def ganar(palabraDescubierta): # al final del juego

    mostrarTablero(palabraDescubierta)
    print("Felicidades, has ganado")

    return True

palabra, letrasUnicas = elegirPalabra(palabras)

while not isJuegoTerminado: # mientras isJuegoTerminado tenga False

    print("*****************************************")

    mostrarTablero(palabra)
    print("*****************************************")

    print('Letras incorrectas: ', '_'.join(letrasIncorrectas))
    print(f"Vidas: { intentos }")
    print("*****************************************")

    letra = pedirLetra()

    # vidas con intentos, coincidencias con aciertos
    intentos, terminado, aciertos = chequearLetra(letra, palabra, intentos, aciertos)
    isJuegoTerminado = terminado

# guia: https://www.udemy.com/course/python-total/learn/lecture/28388424#questions
# guia parte2: https://www.udemy.com/course/python-total/learn/lecture/31780268#questions/17262538

