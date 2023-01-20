import os
import shutil
from pathlib import Path
from os import system
from shutil import rmtree
import shutil

mi_ruta = Path(Path.home(), '\Programacion-Cursos-Desarrollador\Python\Python-proyecto1\Dia7\Banco')

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido) # heredado de class Persona
        self.numero_cuenta = numero_cuenta
        self.balance = balance

        ruta_balance = Path(mi_ruta, 'BalanceCuenta.txt')
        BalanceCuentaLeer = open(ruta_balance)
        contenidoBalanceCuentaLeer = BalanceCuentaLeer.read()
        # print("Prueba balance print: ", contenidoBalanceCuentaLeer)
        # print("Tipo de dato: ", type(contenidoBalanceCuentaLeer))
        balance_int = int(contenidoBalanceCuentaLeer)
        # print("Tipo de dato 2: ", type(contenidoBalanceCuentaLeer))
        self.balance = balance_int
        # print(type(self.balance))
        BalanceCuentaLeer.close()

    def __str__(self):
        return f"Cliente: { self.nombre } { self.apellido }\nNumero de Cuenta: { self.numero_cuenta }\nBalance: ${ self.balance }"

    def depositar(self, monto_deposito):

        self.balance += monto_deposito

        ruta_depositar = Path(mi_ruta, 'RegistroTransacciones.txt')
        ruta_balance = Path(mi_ruta, 'BalanceCuenta.txt')

        archivoRegistroTransacciones = open(ruta_depositar, "a")
        archivoRegistroTransacciones.write(f"{ monto_deposito } - INGRESO\n")
        archivoRegistroTransacciones.close()

        # Path.write_text(ruta_depositar, str(monto_deposito)) error, ya que no haria salto de linea \n
        Path.write_text(ruta_balance, str(self.balance))
        print("Deposito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:

            self.balance -= monto_retiro

            ruta_depositar = Path(mi_ruta, 'RegistroTransacciones.txt')
            ruta_balance = Path(mi_ruta, 'BalanceCuenta.txt')

            archivoRegistroTransacciones = open(ruta_depositar, "a")
            archivoRegistroTransacciones.write(f"{monto_retiro} - RETIRO\n")
            archivoRegistroTransacciones.close()

            Path.write_text(ruta_balance, str(self.balance))

            print("Retiro Realizado")
        else:
            print("Fondos Insuficientes Para el Retiro")


def crear_cliente():
    nombre_cl = input("Ingrese su Nombre: ")
    apellido_cl = input("Ingrese su Apellido: ")
    numero_cuenta = input("Ingrese Su Numero de Cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta) # class Cliente

    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente) # f"Cliente: { self.nombre } { self.apellido }\nNumero de Cuenta: { self.numero_cuenta }\nBalance: { self.balance }"
    opcion = 0

    while opcion != 'S': # 'S' salir
        print('Elija: Depositar (D), Retirar (R), Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a Depositar: $"))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_dep = int(input("Monto a Retirar: $"))
            mi_cliente.retirar(monto_dep)
        print(mi_cliente) # mostrar como queda cliente despues de esas operaciones

    print("Gracias Por Su Visita - Hasta Luego")

inicio()

# proyecto: https://www.udemy.com/course/python-total/learn/lecture/28747292#questions
# convertir str a int: https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=To%20convert%2C%20or%20cast%2C%20a,int(%22str%22)%20.
# convertir int a str: https://es.stackoverflow.com/questions/364966/como-convertir-un-dato-int-a-string-en-python

