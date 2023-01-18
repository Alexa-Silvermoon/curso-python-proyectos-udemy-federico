class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) # super() es para tomar el __init__() de la clase padre Animal(), smilar a JS
        self.altura_vuelo = altura_vuelo

    def hablar(self): # modificacion del metodo del padre
        print("Pio")

    def volar(self, metros): # volar() es esclusivo de Pajaro(), asi que Animal() no lo podra usar
        print(f"El pajaro vuela { metros } metros")

print(Pajaro.__bases__) # me indica de quien hereda esta clase (<class '__main__.Animal'>,)
print(Animal.__subclasses__()) # me indica quien esta heredando [<class '__main__.Pajaro'>]

piolin = Pajaro(1, 'amarillo', 50)
piolin.nacer() # tiene parentesis porque es un metodo
print("Color: ", piolin.color) # no tiene parentesis porque no es un metodo
print("Edad: ", piolin.edad) # no tiene parentesis porque no es un metodo

piolin.hablar() # Pio
piolin.volar(100)
print("Altura de vuelo: ", piolin.altura_vuelo)

print("----------------------------")

# herencia multiple

class Padre:

    def hablar(self):
        print("Hola")

class Madre:

    def reir(self):
        print("ha ha ha")

    def hablar(self):
        print("Que tal")

class Hijo(Padre, Madre): # en el caso del metodo hablar() toma primero el del padre ya que (Padre, Madre)
    pass

class Nieto(Hijo):
    pass


nieto1 = Nieto()
nieto1.hablar() # Hola, heredado de Padre()
nieto1.reir() # reir, heredado de Madre()

# method order resolution
print(Nieto.__mro__) # nos muetra el orden en que se resuelve las cosas



print("----------------------------")

"""
Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() 
(puedes dejar el código de los métodos en blanco con pass). 
Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
"""

class Vehiculo:

    def acelerar(self):
        print("El vehiculo esta acelerando")
        # pass

    def frenar(self):
        print("El vehiculo esta frenando")
        # pass

class Automovil(Vehiculo):
    pass

carro = Automovil()
carro.acelerar()
carro.frenar()

print("----------------------------")
"""
Práctica Herencia Extendida 2
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; 
y amamanta a sus crías pero no tienen mamas." (National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
tal que "construyas" un animal que tiene los siguientes métodos y atributos:

- poner_huevos()

- tiene_pico = True

- vertebrado = True

- venenoso = True

- nadar()

- caminar()

- amamantar()
"""
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Ave, Reptil, Mamifero, Vertebrado ):
    pass

ornito = Ornitorrinco()

ornito.poner_huevos()
print(ornito.tiene_pico)
print(ornito.vertebrado)
print(ornito.venenoso)
ornito.nadar()
ornito.caminar()
ornito.amamantar()

print(Ornitorrinco.__mro__)

print("----------------------------")

"""
Un hijo ha heredado de su padre todas sus características, 
sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos 
y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: 
"Juego videojuegos en mi tiempo libre"

[1]: asegúrate de utilizar return seguido de una cadena de texto
"""


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):

    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

hijo1 = Hijo()

print(hijo1.hobby())


# herencia: https://www.udemy.com/course/python-total/learn/lecture/28728888#questions
# herencia extendida: https://www.udemy.com/course/python-total/learn/lecture/28733770#questions
