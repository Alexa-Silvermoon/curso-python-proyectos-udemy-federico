import re

def verificar_email(email):

    stringDividido = re.findall(r'[^\s]', email)
    print(stringDividido)

    longitud = len(stringDividido)
    print("longitud email: ", longitud)

    contarArrobas = 0

    for c in range(0, longitud):

        if stringDividido[c] == '@':

            contarArrobas += 1

    print("@ contadas: ", contarArrobas)

    listaDominio = []
    listaSubDominio = []
    listaCuerpo = []

    posArroba = email.index('@')
    print('posicion @: ', posArroba)

    # print(stringDividido[i])

    for i in range(0, posArroba):

        listaCuerpo.append(stringDividido[i])

    for j in range(posArroba, longitud):

        listaDominio.append(stringDividido[j])

    listaSubDominio.append((listaDominio[-2]))
    listaSubDominio.append((listaDominio[-1]))

    print("Cuerpo Correo: ", listaCuerpo)
    print("Dominio: ", listaDominio)
    print("Sub Dominio: ", listaSubDominio)

    stringCuerpo = ''.join(listaCuerpo)
    print("Cuerpo del Correo: ", stringCuerpo)

    longitudStringCuerpo = len(stringCuerpo)
    print("Longitud Cuerpo del Correo: ", longitudStringCuerpo)

    stringDominio = ''.join(listaDominio)
    print("Dominio: ", stringDominio)

    stringSubDominio = ''.join(listaSubDominio)
    # print("Sub Dominio: ", stringSubDominio)

    if stringSubDominio == 'om':
        stringSubDominio = ''

    print("Sub Dominio: ", stringSubDominio)

    if stringSubDominio == '': # SIN SUB DOMINIO
        isSubDominioValido = True
    elif stringSubDominio == 'co': # colombia
        isSubDominioValido = True
    elif stringSubDominio == 'br': # brasil
        isSubDominioValido = True
    elif stringSubDominio == 'mx': # mexico
        isSubDominioValido = True
    elif stringSubDominio == 'es': # españa
        isSubDominioValido = True
    else:
        isSubDominioValido = False

    print("---------------------------------")

    if '@gmail.com' in stringDominio and contarArrobas == 1 and longitudStringCuerpo >= 1 and isSubDominioValido and longitudStringCuerpo > 7:
        print(email)
        print("SI es un Email Valido")
    elif '@hotmail.com' in stringDominio and contarArrobas == 1 and longitudStringCuerpo >= 1 and isSubDominioValido and longitudStringCuerpo > 7:
        print(email)
        print("SI es un Email Valido")
    elif '@outlook.com' in stringDominio and contarArrobas == 1 and longitudStringCuerpo >= 1 and isSubDominioValido and longitudStringCuerpo > 7:
        print(email)
        print("SI es un Email Valido")
    else:
        print(email)
        print("No es Valido")

def elegir_dominio():
    eleccion_dominio = 'x'

    # mientras sea un numero o eleccion usuario sea un numero entre 1 y 3 (4 no se incluye)
    while not eleccion_dominio.isnumeric() or int(eleccion_dominio) not in range(1, 4):
        print("Elige un Dominio: ")
        print("""
            [1] - @gmail.com
            [2] - @hotmail.com
            [3] - @putlook.com""")

        eleccion_dominio = input()

    return int(eleccion_dominio)

def elegir_sub_dominio():
    eleccion_sub_dominio = 'x'

    # mientras sea un numero o eleccion usuario sea un numero entre 1 y 5 (6 no se incluye)
    while not eleccion_sub_dominio.isnumeric() or int(eleccion_sub_dominio) not in range(1, 6):
        print("Elige un Sub Dominio (es opcional no elegir ninguno): ")
        print("""
            [1] - .co
            [2] - .br
            [3] - .mx
            [4] - .es
            [5] - "Ninguno en Particular" """)

        eleccion_sub_dominio = input()

    return int(eleccion_sub_dominio)

def ensamblar_dominios():

    eleccion_dominio = elegir_dominio()

    if eleccion_dominio == 1:
        dominio = '@gmail.com'
    elif eleccion_dominio == 2:
        dominio = '@hotmail.com'
    elif eleccion_dominio == 3:
        dominio = '@outlook.com'

    eleccion_sub_dominio = elegir_sub_dominio()

    if eleccion_sub_dominio == 1:
        sub_dominio = '.co'
    elif eleccion_sub_dominio == 2:
        sub_dominio = '.br'
    elif eleccion_sub_dominio == 3:
        sub_dominio = '.mx'
    elif eleccion_sub_dominio == 4:
        sub_dominio = '.es'
    elif eleccion_sub_dominio == 5:
        sub_dominio = ''

    dominio_ensamblado = dominio + sub_dominio
    return dominio_ensamblado

dominio_ensamblado = ensamblar_dominios()

nombre_correo = input("Escribe el nombre de tu correo, NO incluyas @: ")

email = nombre_correo + dominio_ensamblado
verificar_email(email)

# modulo RE (regular expression): https://www.udemy.com/course/python-total/learn/lecture/29030152#questions/17870346
# https://parzibyte.me/blog/2018/12/31/posicion-de-subcadena-en-cadena-python/
# https://naps.com.mx/blog/ejemplos-de-for-en-python-usando-listas-split/
# https://www.programarya.com/Cursos/Python/Ciclos/Ciclo-for
# https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/#:~:text=Ejemplos%20del%20m%C3%A9todo%20join()%20en%20Python&text=Ahora%20formar%C3%A1s%20una%20cadena%20usando,son%20todos%20nombres%20de%20frutas.&text=%F0%9F%93%91%20Observa%20que%20el%20separador,ser%20especificado%20como%20una%20cadena.
# https://www.codigopiton.com/funcion-contains-en-string-existe-en-python/#:~:text=En%20Python%2C%20la%20funci%C3%B3n%20contains,a%20est%C3%A1%20contenido%20en%20cadena%20.
# https://help.salesforce.com/s/articleView?id=sf.pardot_emails_allowed_characters.htm&type=5
