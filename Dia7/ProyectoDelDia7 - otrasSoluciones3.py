from os import system
from unicodedata import numeric


class Persona:

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        pass


class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta, balance=0.0) -> None:
        super().__init__(nombre, apellido)
        self.no_cuenta = cuenta
        self.balance = balance
        pass

    def __str__(self) -> str:
        return f"""
        Nombre: {self.nombre + " " + self.apellido}
        Numer de cuenta: {self.no_cuenta}
        Balance: ${self.balance}
        """

    def deposito(self):
        system('cls')
        print("\n")
        print("*" * 30)
        print(f"\nCuentas con ${self.balance} pesos")
        ingreso = validaFloat("Ingresa la cantidad a depositar: ")
        if (ingreso <= 0):
            print(f"\nNo se pueden depositar ${ingreso} pesos")
            salir = input("\nPresione enter para salir: ")

        else:
            system("cls")
            self.balance += ingreso
            print("*" * 10 + "DEPOSITO EXITOSO" + "*" * 10)
            print(f"\n{self.nombre}, usted cuenta con ${self.balance} pesos en su cuenta")
            salir = input("\npresione enter para salir: ")

            return self.balance

        return self.balance

    def retirar(self):
        retiro = 0
        system('cls')
        print(f"Cuentas con ${self.balance} pesos")
        if (self.balance == 0):
            print("\nNo es posible retirar ya que ¿no cuentas con saldo")
            salir = input("\nPresione enter para salir: ")
        else:
            print(f"Puedes retirar un maximo de ${self.balance} pesos")
            print("*" * 30)
            retiro = validaFloat("\nIngrese la cantidad a retirar: ")

            if (retiro < 0):
                system('cls')
                print("\nNo se pueden retirar cantidades negativas")
                salir = input("\nPresione enter para salir: ")

            elif (retiro > self.balance) and (retiro > 0):
                system('cls')
                print(f"\nNo se puede retirar esta cantidad, puede retirar un maximo de ${self.balance} pesos")
                salir = input("\nPresione enter para salir: ")

            elif ((retiro > 0) and (retiro <= self.balance)):
                system('cls')
                self.balance = self.balance - retiro
                print("\n")
                print("*" * 10 + "RETIRO EXITOSO" + "*" * 10)
                print(f"\n{self.nombre}, usted cuenta con ${self.balance} pesos en su cuenta")
                salir = input("\npresione enter para salir: ")

                return self.balance

        return self.balance


def crearCliente():
    nombre = input("Ingrese su nombre (sin apellidos): ")
    apellido = input("\nIngrese su apellido: ")
    no_cuenta = validaInt("\nIngrese su numero de cuenta: ")

    cliente = Cliente(nombre, apellido, no_cuenta)

    return cliente


def pintaMenu(titulo, arr):
    print("=" * 8 + "{}".format(titulo) + "=" * 8)

    for i in range(len(arr)):
        print(f"[{i + 1}] {arr[i]}")

    opc = input("\ningresa una opcion:")

    while not opc.isnumeric() or int(opc) not in range(len(arr) + 1):
        opc = input("Opcion no valida. Intente de nuevo: ")

    return int(opc)


def validaInt(cadena):
    while (True):
        try:
            arg = int(input(cadena))
            break
        except:
            print("Dato no valido. Ingrese un dato correcto (entero)")

    return arg


def validaFloat(cadena):
    while (True):
        try:
            arg = float(input(cadena))
            break
        except:
            print("Dato no valido. Ingrese un dato correcto (float)")

    return arg


def inicio():
    system('cls')
    opc = 0
    arr = ['Deposito', 'Retirar', 'Salir']
    cliente = crearCliente()
    while (opc != len(arr)):
        system('cls')
        print("*" * 10 + "BANCO PYTHON" + "*" * 10)
        print("\n")
        print(cliente)
        print("\n")
        opc = pintaMenu("BANCO", arr)

        match opc:
            case 1:
                cliente.deposito()

            case 2:
                cliente.retirar()

            case 3:
                print("Gracias por usar BANCO PYTHON")


inicio()