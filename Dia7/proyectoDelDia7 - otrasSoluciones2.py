from os import system
import sys


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        print("==" * 20)
        print("\nBanco Python\n")
        return f"Cliente: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: ${self.balance}\n\n==========================================="

    def deposito(self, monto_deposito):
        self.balance += monto_deposito
        print("==" * 20)
        print("\nBanco Python\n")
        print(f"\nEl deposito de ${monto_deposito} ha sido exitoso\n")
        print("==" * 20)
        system("pause")
        system("cls")

    def retiro(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("==" * 20)
            print("\nBanco Python\n")
            print(f"\nEl retiro de ${monto_retiro} ha sido exitoso\n")
            print("==" * 20)
            system("pause")
            system("cls")
        else:
            print("==" * 20)
            print("\nBanco Python\n")
            print("Fondos insuficientes\n")
            print("==" * 20)


def crear_cliente():
    print("==" * 20)
    print("\nBanco Python\n")
    nombre_cliente = input("\nIngrese el nombre del cliente: ")
    while nombre_cliente.isalpha() == False:
        print("\n[Error] Solo puede ingresar letras para el nombre del cliente.")
        nombre_cliente = input("\nIngrese el nombre del cliente: ")
    apellido_cliente = input("\nIngrese el apellido del cliente: ")
    while apellido_cliente.isalpha() == False:
        print("\n[Error] Solo puede ingresar letras para el apellido del cliente.")
        apellido_cliente = input("\nIngrese el apellido del cliente: ")
    numero_cuenta = input("\nIngrese el numero de cuenta del cliente: ")
    while numero_cuenta.isnumeric() == False:
        print("\n[Error] Solo puede ingresar numeros para el numero de cuenta del cliente.")
        numero_cuenta = input("\nIngrese el numero de cuenta del cliente: ")
    system("cls")
    cuenta = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cuenta


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 3:
        print("\nEliga la operacion que desea realizar: \n1- Depositar \n2- Retirar \n3- Salir\n")
        opcion = int(input())
        if opcion > 3:
            system("cls")
            print("[Error] Solo puedes escojer un numero del 1 al 3.")
        else:
            system("cls")

        if opcion == 1:
            print("==" * 20)
            print("\nBanco Python\n")
            validacion_deposito = False
            while not validacion_deposito == True:
                monto_deposito = float(input("Ingrese el monto a depositar: "))
                if monto_deposito > 0:
                    validacion_deposito = True
                else:
                    print("[Error] Ingrese un monto valido.")
                    monto_deposito = float(input("Ingrese el monto a depositar: "))
            system("cls")
            mi_cliente.deposito(monto_deposito)
        elif opcion == 2:
            print("==" * 20)
            print("\nBanco Python\n")
            validacion_retiro = False
            while not validacion_retiro == True:
                monto_retiro = float(input("Ingrese el monto a retirar: "))
                if monto_retiro > 0:
                    validacion_retiro = True
                else:
                    print("[Error] Ingrese un monto valido.")
                    monto_retiro = float(input("Ingrese el monto a retirar: "))
            system("cls")
            mi_cliente.retiro(monto_retiro)
        print(mi_cliente)
    system("cls")
    print("==" * 20)
    print("\nBanco Python\n")
    print("Gracias por usar nuestro sistema.\n")
    print("==" * 20)


inicio()