import os # metodo para trabjar en sistemas operativos, no importa cual
from pathlib import Path, PureWindowsPath # para las rutas en cualquier OS y manipulacion de rutas y archivos

# metodo getcwd() current working directory
ruta = os.getcwd()
print(ruta) # trae la ruta actual donde estamos trabajando este archivo de python

print("-----------------------------------")

# metodo chdir() metodo para cambiar de directorio
ruta2 = os.chdir("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa")
archivo2 = open('otro_archivo.txt', 'r')
print(archivo2.read()) # ostras chaval

print("-----------------------------------")

# metodo makedirs() para crear carpetas, es decir directorios
# ruta3 = os.makedirs("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutamakedirs")

print("-----------------------------------")

# ver el primer archivo que hay en una ruta
ruta3 = "C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt"
elemento = os.path.basename(ruta3)
print(elemento) # otro_archivo.txt

print("-----------------------------------")

# ver la ruta donde se encuentra un archivo
ruta4 = "C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt"
elemento = os.path.dirname(ruta4)
print(elemento) # ruta

print("-----------------------------------")

# ver la ruta donde se encuentra un archivo y al archivo, (lo trae a modo de tupla)
ruta5 = "C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt"
elemento = os.path.split(ruta5)
print(elemento) # ruta y archivo

print("-----------------------------------")

# eliminar una carpeta
# os.rmdir("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\carpetaaeliminar")

print("-----------------------------------")

# para abrir directorios en cualquier OS es asi

# carpeta = Path("C:/Programacion-Cursos-Desarrollador/Python/Python-proyecto1/Dia6/rutaalternativa")
carpeta = Path("/Programacion-Cursos-Desarrollador/Python/Python-proyecto1/Dia6/rutaalternativa")
archivo3 = carpeta / 'otro_archivo.txt' # se concatena de esta forma

mi_archivo = open(archivo3)
print(mi_archivo.read())

print("-----------------------------------")

# leer contenido archivo facilmente
carpeta = Path("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt")
print(carpeta.read_text())

# saber el nombre del archivo
print(carpeta.name)

# saber la extension del archivo
print(carpeta.suffix)

# saber el nombre del archivo pero sin la extension
print(carpeta.stem)

print("-----------------------------------")

# verificar si un archivo existe o no
carpeta2 = Path("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt")
if not carpeta2.exists():
    print("El archivo no existe")
else:
    print("El archivo si existe")

print("-----------------------------------")

# PureWindowsPath transforma cualquier ruta, en una ruta solo para windows
carpeta3 = Path("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa\\otro_archivo.txt")
rutaWindows = PureWindowsPath(carpeta3)
print(rutaWindows)

# directorios https://www.udemy.com/course/python-total/learn/lecture/28541365#questions
# Pathlib https://www.udemy.com/course/python-total/learn/lecture/28541653?start=15#questions

