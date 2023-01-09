
# funciones, palabra clave: def, en JS seria function o funcion de flecha

# crear funciones: https://www.udemy.com/course/python-total/learn/lecture/28367124#questions

def saludarPersona(nom):
    """
    Hola a todos
    espero esten bien
    """
    print("Hola ", nom)

nombre = "Alexander"
saludarPersona(nombre)

def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

nombre_persona = "chris"
bienvenida(nombre_persona)

print("----------------------------------")

def cuadrado(un_numero):
    un_numero = un_numero ** 2
    print("Al cuadrado: ", un_numero)

un_numero = 5
print(un_numero)
cuadrado(un_numero)

print("----------------------------------")

def multiplicar(num1,num2):
    result = num1 * num2
    print("resultado dentro de la funcion: ", result)
    return result

numero1 = 3
numero2 = 2

resultado = multiplicar( numero1, numero2)
print(f"{ numero1 } X { numero2 } = { resultado }")

print("----------------------------------")

"""
Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
Deberá devolver el número que resulte de resolver una potencia, 
utilizando el primer número como base, y el segundo como exponente:
"""


def potencia(num, pot):
    result = num ** pot
    return result


resultado = potencia(3, 4)
print("Potenciado es: ", resultado)

print("----------------------------------")

"""
Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico 
(un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. 
A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu 
función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en 
dólares por 0.90 para obtener el monto equivalente en euros.
"""


def usd_a_eur(val):
    resul = val * 0.90
    return resul


dolares = 1
resultado = usd_a_eur(dolares)
print(f" { dolares } dolares en euros son: { resultado }")

print("----------------------------------")

"""
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, 
invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, 
para sumisitrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.
"""


def invertir_palabra(pal):
    resul = pal[ :: -1].upper()
    return resul


palabra = "Python"
resultado = invertir_palabra(palabra)
print(resultado)