monedas = 5;

while monedas > 0:
    print(f"Tengo { monedas } monedas");
    monedas -= 1;

print("---------------------------------------------");

respuesta = "s";

while respuesta == "s":
    respuesta = input("Quieres seguir? 's' o 'n'");
else:
    print("Decidiste no seguir");

print("---------------------------------------------");

"""respuesta2 = "s";
while respuesta2 == "s":
    pass # no le veo utilidad :v
print("le he hecho un pass al while");
"""

print("---------------------------------------------");

print("El objetivo es ingresar su nombre y si detecta una letra en especifico, el programa se detendra");
nombre = input("Ingrese su nombre: ");
letraDetener = input("Ingrese la letra: ");
print(f"El programa se detuvo porque encontro la letra { letraDetener }");

for letra in nombre:

    if letra == letraDetener:
        break
    print(letra);

print("---------------------------------------------");

print("El objetivo es ingresar su nombre y si detecta una letra en especifico, el programa se saltara esa letra");
nombre2 = input("Ingrese su nombre: ");
letraDetener2 = input("Ingrese la letra: ");
print(f"El programa se salto la letra { letraDetener }");

for letra2 in nombre2:

    if letra2 == letraDetener2:
        continue
    print(letra2);


print("---------------------------------------------");

"""
Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) 
con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla 
(¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla 
(no te olvides de seguir restando para que el programa no corra infinitamente).
"""

print("Saber si un numero es divisible por otro")
numero = int(input("Favor ingrese un numero entero para dividir: "))
divisiblePor = int(input("Favor ingrese el numero que dividira al anterior numero: "))

while numero >= 0:
    if numero % divisiblePor == 0:
        print(f"El numero {numero} SI es divisible por {divisiblePor}")
        numero -= 1
    elif numero % divisiblePor == 1:
        print(f"El numero {numero} NO es divisible por {divisiblePor}")
        numero -= 1
    else:
        print(numero, " es neutral")
        numero -= 1

"""
Crea un loop For a lo largo de la siguiente lista de números, 
imprimiendo en pantalla cada uno de sus elementos, 
e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

No debes cambiar el orden de la lista.
"""
print("---------------------------------------------");

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for num in lista_numeros:
    if num > 0:
        print(num)
        continue
    else:
        break
# loop while
