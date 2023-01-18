import os
import time


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, no_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.no_cuenta = no_cuenta
        self.balance = balance

    def __str__(self):
        return f'{self.nombre} {self.apellido} con numero de cuenta {self.no_cuenta}, su balance es de: ${self.balance}'

    def depositar(self):
        while True:
            try:
                deposito = float(input('¿Cuanto deseas depositar?: '))
                if deposito > 0:
                    print(f'Has depositado ${deposito}')
                    print(f'Tu saldo ahora es de: ${self.balance + deposito}')
                    self.balance += deposito
                    time.sleep(10)
                else:
                    print('No se puede depositar menos de $0')
                    time.sleep(5)
            except ValueError:
                print('Unicamente numeros')
                time.sleep(10)
                os.system('cls')
            else:
                break

    def retirar(self):
        while True:
            try:
                retiro = float(input('Cuanto deseas retirar?: '))
                if retiro > 0:
                    if retiro <= self.balance:
                        print(f'Has retirado ${retiro}')
                        print(f'Tu saldo ahora es de: ${self.balance - retiro}')
                        self.balance -= retiro
                        time.sleep(10)
                    else:
                        print('No cuentas con ese saldo para retirar')
                        print(f'Lo maximo que puedes retirar son: ${self.balance}')
                        time.sleep(10)
                else:
                    print('No puedes retirar menos de $0')
                    time.sleep(5)
            except ValueError:
                print('Unicamente numeros')
                time.sleep(1)
                os.system('cls')
            else:
                break

    def ver(self):
        print(f'Tú saldo es: ${self.balance}')
        time.sleep(2)


def crear_cliente():
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    no_cuenta = input('Ingresa un numero de cuenta: ')
    cliente = Cliente(nombre, apellido, no_cuenta)
    return cliente


def menu():
    persona = crear_cliente()
    print(persona)
    opcion = 'x'
    while opcion != 4:
        print('*' * 30)
        print('Bienvenido al cajero')
        print('*' * 30)
        print("""Seleciona una opcion:
        1-Depositar
        2-Retirar
        3-Ver saldo
        4-Salir""")
        while True:
            try:
                opcion = int(input('Ingresa tu opcion (1-4): '))
                if opcion == 1:
                    persona.depositar()
                elif opcion == 2:
                    persona.retirar()
                elif opcion == 3:
                    persona.ver()
                elif opcion == 4:
                    print('*' * 30)
                    print('Gracias por utilizar nuestro banco! Adios!')
                    print('*' * 30)
                    break
                else:
                    print('Opcion invalida')
                    time.sleep(1)
                    os.system('cls')
            except ValueError:
                print('Unicamente numeros')
            else:
                break


menu()