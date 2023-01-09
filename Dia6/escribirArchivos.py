# archivo = open('textoeditable.txt', 'r') # modo solo lectura, viene por defecto
archivo = open('textoeditable.txt', 'w') # modo para editar el archivo

# OJO, la informacion anterior se borrara para siempre y sera remplazada por el nuevo texto
# archivo.write('texto nuevo desde python')
archivo.write('''texto nuevo desde python
linea 2 nueva
linea 3 nueva''')
# usar triple ''' equivale a hacer salto de linea \n
archivo.close()

archivoNuevo = open('textoeditable.txt', 'r')
lineas = archivoNuevo.readlines()
print(lineas)
archivoNuevo.close()

print('--------------------------------------------')

archivoMultiLineas = open('textoeditable2.txt', 'w')
archivoMultiLineas.writelines(['christian','alexander','martinez','millan'])
archivoMultiLineas.close()

archivoMultiLineasRead = open('textoeditable2.txt', 'r')
print(archivoMultiLineasRead.readlines())
archivoMultiLineasRead.close()

print('--------------------------------------------')

archivoForW = open('textoeditable3ciclofor.txt', 'w')

lista = ['christian','alexander','martinez','millan']

for linea in lista:
    archivoForW.writelines(linea + '\n')

archivoForW.close()

archivoForR = open('textoeditable3ciclofor.txt', 'r')
print(archivoForR.readlines())
archivoForR.close()

print('--------------------------------------------')

archivoa = open('textoeditable4a.txt', 'a')
archivoa.write('nuevo y ultimo registro a')
archivoa.close()

archivoAR = open('textoeditable4a.txt')
print(archivoAR.readlines())
archivoAR.close()

print('--------------------------------------------')

"""
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: 
"Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""

archivoA = open("mi_archivo.txt", "a")
archivoA.write("Nuevo inicio de sesión\n")
archivoA.close()

archivoR = open("mi_archivo.txt", "r")
for linea in archivoR:
    print(linea.rstrip())

print('--------------------------------------------')

"""
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo 
"registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. 
También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura 
para poder imprimir su contenido.
"""
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga\t"]

archivoA = open("registro.txt", "a")
archivoA.writelines(registro_ultima_sesion)
archivoA.close()

archivoR = open("registro.txt", "r")
for linea in archivoR:
    print(linea.rstrip())

# crear y escribir archivos
# https://www.udemy.com/course/python-total/learn/lecture/28540623#questions
# https://www.freecodecamp.org/espanol/news/python-creacion-de-archivos/

