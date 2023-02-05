def suma():

    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))

    print(n1 + n2)
    print("gracias por sumar")

# suma()

try:
    # codigo aqui
    suma()

except:
    print("Error except") # codigo a ejecutar si hay un error

else:
    # codigo que se ejecutara si no hay ningun error
    print("todo salio bien, else")

finally:
    # codigo que se ejecutara de todos modos
    print("fin del proceso, finally")

print("----------------------------------")

def suma2():

    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))

    print(n1 + n2)
    print("gracias por sumar" + n1) # TypeError

# suma()

try:
    # codigo aqui
    suma2()

except TypeError:
    print("Error, estas intentando concatenar tipos distintos") # codigo a ejecutar si hay un error

except ValueError:
    # aparece si alguien ingresa una letra donde se supone debe ingresar un numero
    print("Error, ese no es un numero")

else:
    # codigo que se ejecutara si no hay ningun error
    print("todo salio bien, else")

finally:
    # codigo que se ejecutara de todos modos
    print("fin del proceso, finally")

print("----------------------------------")

def pedir_numero():

    while True:

        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no era un numero")
        else:
            print(f"El { numero } si era un numero")
            break # salir del ciclo

    print("Gracias")

pedir_numero()

print("----------------------------------")

"""
Implementa para la siguiente función cociente(), un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: 
"Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: 
"El segundo argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) 
entre los dos números entregados como argumento.
"""


def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


cociente(6, 2)

print("----------------------------------")

"""
Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), 
mostrar en pantalla el mensaje: "El archivo no fue encontrado"

En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"

Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
"""


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")


abrir_archivo("arhivo.txt")
