class Pajaro:

    alas = True # atributo de clase

    def __init__(self, color, especie): # equivale a constructor en JS
        self.color = color # equivale en JS a this.color = color
        self.especie = especie

    def piar(self): # metodo
        print(f"pio mi color es { self.color}")

    def volar(self, metros): # metodo
        print(f"El pajaro a volado { metros } metros")

piolin = Pajaro("amarillo", "canario")

piolin.piar()
piolin.volar(10)

print("------------------------------------------------")

"""
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


posponer = Alarma()

posponer.postergar(5)

# metodos: https://www.udemy.com/course/python-total/learn/lecture/28722636#questions
