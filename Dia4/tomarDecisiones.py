if 10 > 9:
    print("correcto");

if 5 == 2:
    print("error");
else:
    print(" 5 no es 2 ");

mascota = "perro";
if mascota == "gato":
    print("tienes un gato");
else:
    print("ni idea de tu mascota");

# los : equivalen a las {} en JS
mascota = "perro";
if mascota == "gato":
    print("tienes un gato");
elif mascota == "perro":
    print("tienes un perro");
else:
    print("ni idea que mascota tienes");


edad = 15;
calificacion = 7;
if edad < 18:
    print( edad, "eres menor de edad");
    if calificacion >= 7:
        print(calificacion, "Aprobado");
    else:
        print(calificacion, "Reprobado")
else:
    print(edad, "eres mayor de edad");

# control de flujo: https://www.udemy.com/course/python-total/learn/lecture/28141856#questions

"""
Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"

"num2 es mayor que num1"

"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
"""
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

"""
output:
Ingresa un número:9
Ingresa otro número:5
9 es mayor que 5
"""

"""
Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, 
y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, 
y muestra el resultado que corresponda en pantalla:

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.
"""

print("-------------------------------------------");
edad = int(input("Ingrese edad: "));

if edad >= 18:

    tieneLicencia = input("tiene licencia? responda solo si o no: ").lower();

    if tieneLicencia == "si":

        print("Puedes conducir");

    elif tieneLicencia == "no":

        print("No puedes conducir. Necesitas contar con una licencia");

    else:

        print("Ingrese solo 'si' o 'no'")

else:
    print("Eres menor de edad para conducir");

"""
output:
Ingrese edad: 7
Eres menor de edad para conducir

Ingrese edad: 18
tiene licencia? responda solo si o no: no
No puedes conducir. Necesitas contar con una licencia

Ingrese edad: 18
tiene licencia? responda solo si o no: si
Puedes conducir

Ingrese edad: 18
tiene licencia? responda solo si o no: xd
Ingrese solo 'si' o 'no'
"""

"""
Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python 
y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, 
y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada 
y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.
"""

print("-------------------------------------------------------");
print("En las siguiente dos preguntas responda solo 'si' o 'no");
hablaIngles = input("Usted habla ingles?: ").lower();
sabePython = input("Usted sabe python?: ").lower();

if hablaIngles == "si" and sabePython == "si":

    print("Cumples con los requisitos para postularte");

elif hablaIngles == "no" and sabePython == "si":

    print("Para postularte, necesitas tener conocimientos de inglés");

elif hablaIngles == "si" and sabePython == "no":

    print("Para postularte, necesitas saber programar en Python");

elif hablaIngles == "no" and sabePython == "no":

    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés");

else:
    print("Responda solo 'si' o 'no'");

"""
OUTPUT:
Usted habla ingles?: SI
Usted sabe python?: SI
Cumples con los requisitos para postularte

Usted habla ingles?: NO
Usted sabe python?: NO
Para postularte, necesitas saber programar en Python y tener conocimientos de inglés

Usted habla ingles?: SI
Usted sabe python?: NO
Para postularte, necesitas saber programar en Python

Usted habla ingles?: NO
Usted sabe python?: SI
Para postularte, necesitas tener conocimientos de inglés

Usted habla ingles?: XD
Usted sabe python?: XD
Responda solo 'si' o 'no'

Usted habla ingles?: SI
Usted sabe python?: XD
Responda solo 'si' o 'no'

Usted habla ingles?: NO
Usted sabe python?: XD
Responda solo 'si' o 'no'

Usted habla ingles?: XD
Usted sabe python?: SI
Responda solo 'si' o 'no'

Usted habla ingles?: XD
Usted sabe python?: NO
Responda solo 'si' o 'no'
"""

# Control de flujo: https://www.udemy.com/course/python-total/learn/lecture/28141856#questions
