
# archivo de prueba para cambiaTexto.py

import unittest
import cambiaTexto # se importa el archivo

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self): # funcion de prueba debe iniciar con test

        palabra = 'Buen dia'
        resultado = cambiaTexto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA') # verifica si son exactamente iguales

if __name__ == '__main__': # clase main del lenguaje de programacion python

    unittest.main()

# probar codigo con unitest: https://www.udemy.com/course/python-total/learn/lecture/28851486#questions
