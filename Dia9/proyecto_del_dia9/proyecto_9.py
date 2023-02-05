import re
import os
import time
import datetime
from pathlib import Path
import math
import shutil

inicio = time.time()

ruta = Path(Path.home(), '\Programacion-Cursos-Desarrollador\Python\Python-proyecto1\Dia9\proyecto_del_dia9\Mi_Gran_Directorio')

# r de regular expression
mi_patron = r'N\D{3}-\d{5}' # D= 3 caracteres no numericos almenos, d = 5 caracteres numericos
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):

    este_archivo = open(archivo, 'r') # r de modo lectura
    texto = este_archivo.read()

    if re.search(patron, texto):

        return re.search(patron, texto)
    else:
        return '' # si no encuentra un patron, enviar string vacio


def crear_listas():

    for carpeta, subcarpeta, archivo in os.walk(ruta):

        for a in archivo: # a es el archivo

            # carpeta contiene la ruta, a contiene el archivo
            resultado = buscar_numero(Path(carpeta, a), mi_patron)

            # al ser resultado diferente de un string vacio, me quedo solo con los patrones encontrados
            if resultado != '':
                numeros_encontrados.append((resultado.group())) # agregar grupo de archivos encontrados a la lista
                archivos_encontrados.append(a.title()) # agregar el archivo donde encontro el resultado exacto a la lista


def mostrar_todo():

    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print("\n")
    print('Archivo\t\t\tNro.SERIE')
    print('--------\t\t\t--------')

    for a in archivos_encontrados:

        # imprimir los archivos donde se encontro el patron
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1

    print('\n')
    print(f'Numeros Encontrados: {len(numeros_encontrados)}')

    fin = time.time()

    duracion = fin - inicio
    print(f'Duracion de la Busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()

# proyecto buscado numeros de serie:
# https://www.udemy.com/course/python-total/learn/lecture/29034622#questions/18812856
