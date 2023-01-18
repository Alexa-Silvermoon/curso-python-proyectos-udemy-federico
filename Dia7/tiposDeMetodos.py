class Pajaro:

    alas = True # atributo de clase

    def __init__(self, color, especie): # equivale a constructor en JS
        self.color = color # equivale en JS a this.color = color
        self.especie = especie

    def piar(self): # metodo
        print(f"pio mi color es { self.color}")

    def volar(self, metros): # metodo
        print(f"El pajaro a volado { metros } metros")
        self.piar() # un metodo puede llamar otro metodo desde adentro

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es color { self.color}")

    @classmethod # este metodo no esta relacionado a las instancias, sino a la clase en si
    def poner_huevos(cls, cantidad):
        print(f"Puso { cantidad } huevos")
        cls.alas = False
        print("Alas desde poner_huevos(): ", Pajaro.alas)

    @staticmethod # este metodo no accede ni a metodos de clase o metodos de instancia
    def mirar():
        print("El pajaro mira")

piolin = Pajaro("amarillo", "canario")

piolin.piar()
piolin.volar(10)
piolin.pintar_negro()
piolin.volar(20)

# piolin.alas = False # modificar el estado de la clase
# print("Alas: ", piolin.alas)

Pajaro.poner_huevos(2) # @classmethod, se pone directamente la clase y el metodo, no necesita instancias

Pajaro.mirar() # @staticmethod, se pone directamente la clase y el metodo, no necesita instancias

print("-------------------------------------")

"""
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
estableciéndolo en True cada vez que es invocado. 
El valor predeterminado del atributo vivo, debe ser False.
"""


class Jugador:

    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("Pajaro vivo?: ", cls.vivo)

Jugador.revivir()

print("-------------------------------------")

"""
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una 
instancia de Personaje, que cuenta con un atributo de instancia de tipo número,
 llamado cantidad_flechas.
"""


class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(f"Cantidad de flechas = {self.cantidad_flechas}")


flecha = Personaje(10)
flecha.lanzar_flecha()
# flecha.lanzar_flecha()

# tipos de metodos: https://www.udemy.com/course/python-total/learn/lecture/28726342#questions
# https://careerkarma.com/blog/python-typeerror-object-takes-no-arguments/#:~:text=The%20%E2%80%9CTypeError%3A%20object()%20takes%20no%20arguments%E2%80%9D%20error%20is,of%20the%20word%20%E2%80%9Cinit%E2%80%9D.

