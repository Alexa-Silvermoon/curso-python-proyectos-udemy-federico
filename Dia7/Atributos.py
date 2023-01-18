class Pajaro:

    alas = True # atributo de clase

    def __init__(self, color, especie): # equivale a constructor en JS
        self.color = color # equivale en JS a this.color = color
        self.especie = especie

mi_pajaro = Pajaro("azul", "carpintero")
print("Color: ", mi_pajaro.color)
print("Especie: ", mi_pajaro.especie)
print(f"El pajaro loco es un { mi_pajaro.especie } y es de color { mi_pajaro.color}")

print(Pajaro.alas)
print(mi_pajaro.alas)

print("---------------------------------")


class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanco", 4)
print("color: ", casa_blanca.color, " Pisos: ", casa_blanca.cantidad_pisos)

print("---------------------------------")


class Cubo:

    caras = 6 # atributo de clase

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")
print(cubo_rojo.color)

print("---------------------------------")

"""
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

especie = "Humano"

magico = True

edad = 17
"""


class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("Humano", True, 17)

# Atributos: https://www.udemy.com/course/python-total/learn/lecture/28707250#questions/17650490
