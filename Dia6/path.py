from pathlib import Path

base = Path.home() # toma la ruta del usuario donde se esta ejecutando python
# guia = Path("valle","familia_millan.txt") # convierte esto en una ruta
guia = Path(base, "valle","familia_millan.txt") # convierte esto en una ruta

print(base) # C:\Users\USER
print(guia) # valle\familia_millan.txt

print("---------------------------------")

base = Path.home()
guia = Path(base, "america", "colombia", Path("valle","cali.txt"))

print(base) # C:\Users\USER
print(guia) # america\colombia\valle\cali.txt

print("---------------------------------")

base = Path.home()
guia = Path(base, "america", "colombia", Path("valle","cali.txt"))
guia2 = guia.with_name("palmira.txt") # cambiar el archivo final por otro

print(guia)
print(guia2)

print("---------------------------------")

base = Path.home()
guia = Path(base, "america", "colombia", Path("valle","cali.txt"))

print(guia.parent) # devuelve solo la ruta donde esta el archivo, se puede hacer varios parent

print("---------------------------------")

# mostrar todos los txt de una carpeta
# C:\Programacion-Cursos-Desarrollador\Python\Python-proyecto1\Dia6\rutaalternativa
# base = Path(Path.home(),"rutaalternativa")
guia = Path("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa")

for txt in Path(guia).glob("*.txt"): # todos los txt de una carpeta
    print(txt)

print("---------------------------------")

# mostrar todos los txt de una carpeta y sus sub carpetas
guia = Path("C:\\Programacion-Cursos-Desarrollador\\Python\\Python-proyecto1\\Dia6\\rutaalternativa")

for txt in Path(guia).glob("**/*.txt"): # todos los txt de una carpeta y sus sub carpetas
    print(txt)

# Path: https://www.udemy.com/course/python-total/learn/lecture/28600874?start=45#questions
