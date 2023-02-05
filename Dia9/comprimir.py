import os
from pathlib import Path
import shutil
import zipfile

# para comprimir archivos uno por uno:
"""
# nombre que tendra el archivo zip que contendra los txt
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# meter los archivos que quiera al archivo zip
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

# cerrar el archivo zip
mi_zip.close()"""

print("------------------------------------------")

# PARA DESCOMPRIMIR ARCHIVO ZIP
"""
# descomprimir el archivo zip con ese nombre
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

# extaer todos los archivos dentro del archivo zip
zip_abierto.extractall()"""

print("------------------------------------------")

# para comprimir archivos dentro de una carpeta:
"""# ruta de la carpeta que quiero comprimir con sus archivos dentro
carpeta_origen = Path(Path.home(), '\Programacion-Cursos-Desarrollador\Python\Python-proyecto1\Dia9\paracomprimir')

# ruta donde se va a guardar el archivo comprimido
archivo_destino = 'todo_comprimido'

# crear el archivo comprimido, poniendo los 3 parametros solicitados
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)"""

print("------------------------------------------")

# para descomprimir archivos que hay dentro de un archivo zip
shutil.unpack_archive('todo_comprimido.zip', 'todo_descomprimido', 'zip')


# comprimir y descomprimir archivos desde python