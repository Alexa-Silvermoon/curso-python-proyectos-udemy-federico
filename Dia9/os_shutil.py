import os
import shutil
import send2trash

print(os.getcwd()) # get current directory

# crear archivo txt
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba Dia9')
archivo.close()

print(os.listdir()) # muestra los archivos que tengo en ese directorio
# shutil.move('curso.txt', "C:\\Users\\USER\\Desktop") # mover el archivo a mi escritorio


# metodo para eliminar carpetas vacias
# os.rmdir()

# metodo para eliminar archivos dentro de una carpeta
# shutil.rmtree() # MUCHO CUIDADO AL USARLO

# pip install send2trash - enviar archivos a la papelera
send2trash.send2trash('curso.txt')

print("-------------------------------")

# walk() almacena la ruta, sus sub carpetas y los archivos que hayan en la carpeta y las sub carpetas
rutaDia9 = 'C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia9'
print(rutaDia9)

criterioBusqueda = '2015' # si quiero buscar un archivo que comienze con ese nombre

for carpeta, subcarpeta, archivo in os.walk(rutaDia9):

    print(f"Buscando En La Carpeta: { carpeta }")
    print("Las Sub Carpetas Son: ")

    for sub in subcarpeta:

        print(f'\t{sub}')
    print("Los Archivos Son: ")

    for arch in archivo:
        if arch.startswith(criterioBusqueda):
            print(f"\tLos archivos que empiezan con el criterio { criterioBusqueda} son: ")
            print(f'\t{arch}')
        else:
            print(f"\tNo tienen el criterio de busqueda: ")
            print(f'\t{arch}')
    print('\n')

# modulos OS, shutil, walk: https://www.udemy.com/course/python-total/learn/lecture/28999432#questions
