
# http://books.toscrape.com/catalogue/page-2.html

import bs4
import requests

# crear url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'
# print(url_base,format('15'))  # ir a la pagina 15

for n in range(1, 11):
    print(url_base.format(n))

resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print('Cantidad de elementos :', len(sopa.select('.product_pod')))
libros = sopa.select('.product_pod')
# print(libros)

# libro = libros[0].select(('.star-rating.Four'))

# a anchor tag, 1 es la segunda posicion es decir donde esta el titulo, buscar el componenete title
libro = libros[0].select(('a'))[1]['title']
print(libro)

print('---------------------------------------')

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    # seleccionamos la etiqueta objetivo
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # guardar titulo en variable
            # a anchor tag, 1 es la segunda posicion es decir donde esta el titulo, buscar el componenete title
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros de 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)

# toscrape.com
# https://www.udemy.com/course/python-total/learn/lecture/29286038#questions

# identificar condiciones de extraccion
# https://www.udemy.com/course/python-total/learn/lecture/29286880#questions

# extraer el titulo del libro: https://www.udemy.com/course/python-total/learn/lecture/29288006#questions
# combinar items buscados: https://www.udemy.com/course/python-total/learn/lecture/29290674#questions/18247252
