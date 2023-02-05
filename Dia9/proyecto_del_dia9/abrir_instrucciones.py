from pathlib import Path
import shutil

# EXTRAER LO QUE NO PIDE EL EJERCICIO

# mi_ruta = Path(Path.home(), '/Programacion-Cursos-Desarrollador/Python/Python-proyecto1/Dia6/Recetas')
ruta_destino = Path(Path.home(), '\Programacion-Cursos-Desarrollador\Python\Python-proyecto1\Dia9\proyecto_del_dia9')

shutil.unpack_archive('Proyecto+Dia+9.zip', ruta_destino, 'zip')