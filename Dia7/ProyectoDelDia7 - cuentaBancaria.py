class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido) # heredado de class Persona
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: { self.nombre } { self.apellido }\nNumero de Cuenta: { self.numero_cuenta }\nBalance: ${ self.balance }"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
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
