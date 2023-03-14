# https://escueladirecta-blog.blogspot.com/

import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

#  ver el html de una pagina
# print(resultado.text)
#  print(type(resultado))

#  lxml es el motor de parseo
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
# print(sopa)

#  imprimir la etiqueta deseada en el html
print(sopa.select('title'))
print("sin la etiqueta title: ", sopa.select('title')[0].getText())

print(sopa.select('p'))
print("cantidad de p: ", len(sopa.select('p')))

# print(sopa.select('h1'))
# print(sopa.select('h2'))
print(sopa.select('h3')[0])  # toma la primera h3 que encuentra

print('--------------------------------------------------------------------')

mi_pagina = requests.get('https://www.w3schools.com/html/html_basic.asp')

# busqueda de parrafos
sopa_mi_pagina = bs4.BeautifulSoup(mi_pagina.text, 'lxml')
# print(sopa_mi_pagina)
# print(sopa_mi_pagina.select('p'))
# print(sopa_mi_pagina.select('p')[0].getText())

parrafos = sopa_mi_pagina.select('p')

for p in parrafos:
    print(p.getText())

print('--------------------------------------------------------------------')

mi_pagina2 = requests.get('https://es.wikipedia.org/wiki/Cultura_de_Jap%C3%B3n')

sopa_pagina2 = bs4.BeautifulSoup(mi_pagina2.text, 'lxml')
# print(sopa_pagina2.select('p'))

parrafos2 = sopa_pagina2.select('p')

for p2 in parrafos2:
    print(p2.getText())


#  extraer contenido de etiquetas html
# https://www.udemy.com/course/python-total/learn/lecture/29259628#questions
# extraer elementos de una clase: https://www.udemy.com/course/python-total/learn/lecture/29271406#questions

print('--------------------------------------------------------------------')

# extraer varias imagenes
pagina_de_imagenes = requests.get('https://www.escueladirecta.com/courses')
sopa_imagenes = bs4.BeautifulSoup(pagina_de_imagenes.text, 'lxml')
# imagenes = sopa_imagenes.select('img')
imagenes = sopa_imagenes.select('.course-box-image')  # tomar solo las imagenes que corresponda a los cursos
# print(imagenes)

for i in imagenes:
    print(i['src'])  # taer solo los links de la imagenes


# extraer una sola imagen
imagen = sopa_imagenes.select('.course-box-image')[0]['src']  # tomar el link de la primera imagen
imagen1 = requests.get(imagen)
f = open('mi_imagen.jpg', 'wb')  # wb es write binary
f.write(imagen1.content)
f.close()

# extraer imagendes de: https://www.escueladirecta.com/courses
print('--------------------------------------------------------------------')

