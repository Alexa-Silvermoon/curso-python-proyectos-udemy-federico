
from random import * # importar detodo de la libreria random, en JS es al reves

print("Hola soy Jigsaw, juguemos un poco ")

nombre = input("Por favor dime tu nombre: ")
print(f"Bienvenido { nombre }, el juego consiste en lo siguiente:")
print("Tú tienes que adivinar un número y escribirlo en la consola, "
      "recuerda que solo tienes 8 intentos, que empiece el juego, "
      "PISTA: el numero esta entre 0 y 100")

intentos = 8

aleatorio = int(randint(1,100))
print("respuesta: ", aleatorio)

numero = int(input("Escribe el numero: "))
# print(numero)

if numero < 0 or numero >= 100:
      print("Incorrecto, los numeros deben estar entre 0 y 100")

if numero != aleatorio:
      intentos -= 1
      print("Equivocado prueba otro numero")
      print("Numero de intentos restantes: ", intentos)

if numero != aleatorio:

      while intentos > 0:

            intentos -= 1

            numero = int(input("Escribe de nuevo un numero: "))

            if numero < 0 or numero >= 100:
                  print("Incorrecto, los numeros deben estar entre 0 y 100")

            if numero == aleatorio:
                  print("Ganaste Felicidades 1")
                  break

            if numero < aleatorio:
                  print("Equivocado prueba otro numero")
                  print("Numero de intentos restantes: ", intentos)
                  print("Prueba con numeros mayores a: ", numero)

            if numero > aleatorio:
                  print("Equivocado prueba otro numero")
                  print("Numero de intentos restantes: ", intentos)
                  print("Prueba con numeros menores a: ", numero)

            if intentos == 4:
                  print(f"Te dare una pista, el numero esta entre { aleatorio + 10 } y { aleatorio - 10 } ")

      else:
            print(f"Fin Del Juego {nombre}")

else:
      print("Ganaste Felicidades 2")

# solucion del profe: https://www.udemy.com/course/python-total/learn/lecture/28162240#questions


"""
SI GANA:

Hola soy Jigsaw, juguemos un poco 
Por favor dime tu nombre: ALEXANDER
Bienvenido ALEXANDER, el juego consiste en lo siguiente:
Tú tienes que adivinar un número y escribirlo en la consola, recuerda que solo tienes 8 intentos, que empiece el juego, PISTA: el numero esta entre 0 y 100
respuesta:  79
Escribe el numero: -999
Incorrecto, los numeros deben estar entre 0 y 100
Equivocado prueba otro numero
Numero de intentos restantes:  7
Escribe de nuevo un numero: 999
Incorrecto, los numeros deben estar entre 0 y 100
Equivocado prueba otro numero
Numero de intentos restantes:  6
Prueba con numeros menores a:  999
Escribe de nuevo un numero: 99
Equivocado prueba otro numero
Numero de intentos restantes:  5
Prueba con numeros menores a:  99
Escribe de nuevo un numero: 99
Equivocado prueba otro numero
Numero de intentos restantes:  4
Prueba con numeros menores a:  99
Te dare una pista, el numero esta entre 89 y 69 
Escribe de nuevo un numero: 99
Equivocado prueba otro numero
Numero de intentos restantes:  3
Prueba con numeros menores a:  99
Escribe de nuevo un numero: 99
Equivocado prueba otro numero
Numero de intentos restantes:  2
Prueba con numeros menores a:  99
Escribe de nuevo un numero: 99
Equivocado prueba otro numero
Numero de intentos restantes:  1
Prueba con numeros menores a:  99
Escribe de nuevo un numero: 79
Ganaste Felicidades 1

Process finished with exit code 0

SI PIERDE:
Hola soy Jigsaw, juguemos un poco 
Por favor dime tu nombre: ALEXANDER
Bienvenido ALEXANDER, el juego consiste en lo siguiente:
Tú tienes que adivinar un número y escribirlo en la consola, recuerda que solo tienes 8 intentos, que empiece el juego, PISTA: el numero esta entre 0 y 100
respuesta:  99
Escribe el numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  7
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  6
Prueba con numeros mayores a:  55
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  5
Prueba con numeros mayores a:  55
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  4
Prueba con numeros mayores a:  55
Te dare una pista, el numero esta entre 109 y 89 
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  3
Prueba con numeros mayores a:  55
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  2
Prueba con numeros mayores a:  55
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  1
Prueba con numeros mayores a:  55
Escribe de nuevo un numero: 55
Equivocado prueba otro numero
Numero de intentos restantes:  0
Prueba con numeros mayores a:  55
Fin Del Juego ALEXANDER

Process finished with exit code 0

"""