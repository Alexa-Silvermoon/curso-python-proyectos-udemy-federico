import re

texto = "si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

# palabra dentro de texto?
palabra = 'ayuda' in texto
print('ayuda se encuentra en el texto?: ', palabra)

# buscar indice de una palabra
patron = 'ayuda'
busqueda = re.search(patron, texto) # re es regular expression
print(busqueda) # span=(13, 18) es decir que ayuda inicia en el indice 13 y termina en el 18
print(busqueda.span()) # (13, 18)
print(busqueda.start()) # 13
print(busqueda.end()) # 18

print("--------------------------------------")

# encontrar todas las coincidencias:
patron2 = 'ayuda'
busqueda2 = re.findall(patron2, texto)
print(busqueda2)

# Encontrar la posicion de cada una de las coincidencias
for hallazgo in re.finditer(patron2, texto):

    print(hallazgo.span()) # (13, 18)(71, 76)

print("--------------------------------------")

# cumplir con la condicion de un formato de nueros
texto2 = "llama al 564-525-6588 ya mismo"
# patron3 = r'\d\d\d-\d\d\d-\d\d\d\d' # d digito, solo numeros
# patron3 = r'\d{3}-\d{3}-\d{4}' # d digito, solo numeros, mas sintetica
patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # d digito, solo numeros, dividir por grupos

resultado = re.search(patron3, texto2)
print(resultado) # <re.Match object; span=(9, 21), match='564-525-6588'>
print(resultado.group()) # 564-525-6588
print(resultado.group(1)) # grupo 1 564
print(resultado.group(2)) # grupo 2 525
print(resultado.group(3)) # grupo 3 6588

print("--------------------------------------")

texto3 = 'no atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto3) # buscar una cosa o la otra
print(buscar) # <re.Match object; span=(17, 22), match='lunes'>

buscar2 = re.search(r'....demos....', texto3) # comodin para ver las letras antes y despues
print(buscar2) # <re.Match object; span=(3, 16), match='atendemos los'>

buscar3 = re.search(r'^\D', texto3) # comodin para saber si texto inicia con un String
print(buscar3) # <re.Match object; span=(0, 1), match='n'>

buscar4 = re.search(r'\D$', texto3) # comodin para saber si texto finaliza con String
print(buscar4) # <re.Match object; span=(0, 1), match='n'>

buscar5 = re.findall(r'[^\s]', texto3) # excluir todos los caracteres en blanco y mostrar letras
print(buscar5) # ['n', 'o', 'a', 't', 'e', 'n', 'd', 'e', 'm', 'o', 's', 'l', 'o', 's', 'l', 'u', 'n', 'e', 's', 'p', 'o', 'r', 'l', 'a', 't', 'a', 'r', 'd', 'e']

buscar6 = re.findall(r'[^\s]+', texto3) # excluir todos los caracteres en blanco y mostrar las palabras
print(buscar6) # ['no', 'atendemos', 'los', 'lunes', 'por', 'la', 'tarde']
print(''.join(buscar6)) # noatendemosloslunesporlatarde

print("--------------------------------------")

"""# crear una contraseña con condiciones
clave = input("Clave: ") # por ejemplo: a123bcde
patron4 = r'\D{1}\w{7}' # D letra, d digito
chequear = re.search(patron4, clave)
print(chequear) # <re.Match object; span=(0, 8), match='a123bcde'>"""

print("--------------------------------------")

"""
Crea una función llamada verificar_saludo para verificar si una frase entregada 
como argumento inicia con la palabra "Hola". 
Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", 
pero si detecta que la frase no contiene "Hola", 
debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
"""
def verificar_saludo(frase):
    patron = r'hola|Hola|HOLA'

    if re.match(patron, frase):
        print("Ok")

    else:
        print("No has saludado")


verificar_saludo('hola')

print("--------------------------------------")

"""
El código postal de una región determinada se forma a partir de dos 
caracteres alfanuméricos y cuatro numéricos a continuación 
(ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar 
si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", 
de lo contrario: "El código postal ingresado no es correcto".
"""


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'

    if re.search(patron, cp):
        print("Ok")

    else:
        print("El código postal ingresado no es correcto")


verificar_cp('221r34')

# modulo RE (regular expression): https://www.udemy.com/course/python-total/learn/lecture/29030152#questions/17870346
# https://parzibyte.me/blog/2018/12/31/posicion-de-subcadena-en-cadena-python/
# https://naps.com.mx/blog/ejemplos-de-for-en-python-usando-listas-split/
# https://www.programarya.com/Cursos/Python/Ciclos/Ciclo-for
# https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/#:~:text=Ejemplos%20del%20m%C3%A9todo%20join()%20en%20Python&text=Ahora%20formar%C3%A1s%20una%20cadena%20usando,son%20todos%20nombres%20de%20frutas.&text=%F0%9F%93%91%20Observa%20que%20el%20separador,ser%20especificado%20como%20una%20cadena.
# https://www.codigopiton.com/funcion-contains-en-string-existe-en-python/#:~:text=En%20Python%2C%20la%20funci%C3%B3n%20contains,a%20est%C3%A1%20contenido%20en%20cadena%20.
# https://help.salesforce.com/s/articleView?id=sf.pardot_emails_allowed_characters.htm&type=5
