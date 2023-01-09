from os import system

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

system('cls') # para limpiar consola en windows
# system('clear') # para limpiar consola en otros os

print(f"Su nombre es { nombre } y tienes { edad } años")

"""
Para emular la cosola de windows:
1 - ir a pestaña run, click en debug
2 - click en Edit Configurations...
3 - ir a la parte de abajo y activar la casilla Emulate terminal in output console
4 - click en boton Apply y cerrar esa ventanita

warning: en caso de comportamiento extraño en la consola, revertir el proceso
"""