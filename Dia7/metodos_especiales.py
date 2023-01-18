class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # desde la clase puede convertir los atributos a un string y enviarlo
    def __str__(self):
        return f"Album: { self.titulo } de { self.autor}"

    # en caso de necesitar el numero de canciones, puedo hacerlo con len()
    def __len__(self):
        return self.canciones

    """
        def __del__(self):
        print("Se ha eliminado el CD")
    """

mi_CD = CD('Pink Floyd', 'The Wall', 24)
print(mi_CD)

# ambas formas funcionan
print("Numero de Canciones: ", mi_CD.canciones)
print("Numero de Canciones: ", len(mi_CD))

# BORRAR la instancia mi_CD
# del mi_CD
# print(mi_CD)

print("---------------------------------------")

"""
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, 
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
"""


class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        return print("Libro eliminado")


libro1 = Libro('La Casa del Dragon', 'George RR Martin', 883)
print(libro1, " Paginas: ", len(libro1))
del libro1

# metodos especiales: https://www.udemy.com/course/python-total/learn/lecture/28744840#questions
