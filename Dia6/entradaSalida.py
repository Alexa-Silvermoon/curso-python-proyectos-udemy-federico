miArchivo = open('pruebapython.txt')
miArchivo2 = open('pruebapython.txt')
miArchivo3 = open('pruebapython.txt')
# print(miArchivo) # no imprime nada

# print(miArchivo.read()) # aqui si muestra en pantalla

unaLinea = miArchivo.readline() # leer solo la primera linea
print(unaLinea.upper()) # transforma el texto a mayuscula upper()

unaLinea = miArchivo.readline() # tuvo en cuenta la enterior lectura, por eso imprime la linea 2
print(unaLinea.rstrip()) # rstrip() elimina los espacios en blanco

unaLinea = miArchivo.readline() # tuvo en cuenta la enterior lectura, por eso imprime la linea 3
print(unaLinea)

print("-------------------------------------------")

# se puede ciclar y modificar cada linea:
print("ciclo for")
for linea in miArchivo2:
    print("Esta linea dice: ", linea)

print("-------------------------------------------")

print("metodo readlines")
todas = miArchivo3.readlines() # convierte cada linea en un elemento de una lista
print(todas)

ultima = todas.pop()
print("ultima: ", ultima)

# close() libera la memoria que se estaba ocupando
miArchivo.close()
miArchivo2.close()
miArchivo3.close()

print("-------------------------------------------")

"""
Abre el archivo textopractica.txt e imprime únicamente la segunda línea.
"""

miArchivo4 = open('textopractica.txt')

l2 = miArchivo4.readlines()
print(l2[1])

miArchivo4.close()

print("-------------------------------------------")

mi_archivo5 = open('textopractica.txt')

for numero, linea in enumerate(mi_archivo5):
    if numero == 1:
        break
mi_archivo5.close()

print(linea)

# abrir y manipular archivos:
# https://www.udemy.com/course/python-total/learn/lecture/28539061#questions
