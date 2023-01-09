
lista = ["A", "B", "C"];
print( lista );

for elemento in lista:
    posicion = lista.index(elemento)
    print( "Letra: ", elemento, " en posicion: ", posicion );

lista2 = ["Anastasia", "Benjamin", "Carmela", "Christian", "Daniela"];
letraAbuscar = "C";

print("-------------------------------------------------------------");

for nombre in lista2:

    if nombre.startswith( letraAbuscar ): # en JS seria nombre[0]

        print( f"Nombres que SI inicia con { letraAbuscar } es: { nombre }");

    else:

        print(f"Nombre que NO inicia por la letra: { letraAbuscar } es: { nombre }");

print("-------------------------------------------------------------");

numeros = [1,2,3];
print( numeros );
acumulador = 0;

for numero in numeros:

    acumulador = acumulador + numero;

print("Los elementos de esa lista sumados dan: ",  acumulador );

print("-------------------------------------------------------------");
# GVR855
nombre = "ALEX";

for nom in nombre:
    print( nom );

print("-------------------------------------------------------------");

listaDePares = [ [1,2], ["a","b"], [3,4]];
print( "Lista original: ", listaDePares );

for par in listaDePares:
    print( par );

print("-------------------------------------------------------------");

listaDePares = [[1, 2], ["a", "b"], [3, 4]];
print("Lista original: ", listaDePares);

for a,b in listaDePares:
    print( "Por separado: ", a);
    print( "Por separado: ", b);

print("-------------------------------------------------------------");

dic = { "llave1":"valor1", "llave2":"valor2", "llave3":"valor3"};
print( dic );

for itemLlave in dic:
    print( "solo llaves: ", itemLlave );

for itemValor in dic.values():
    print( "solo valores: ", itemValor );

for item in dic.items():
    print( "Llave y valor pegados: ", item );

for x,y in dic.items():
    print( "Llave y valor separados: ", x,y );

print("-------------------------------------------------------------");

"""
Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* 
por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero 
cuando dicho valor es par, y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)
"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4];
print(lista_numeros);
suma_pares = 0;
suma_impares = 0;

for num in lista_numeros:

    if num % 2 == 0:
        suma_pares = suma_pares + num;

    if num % 2 == 1:
        suma_impares = suma_impares + num;

print("La suma de pares es: ", suma_pares);
print("La suma de impares es: ", suma_impares);


# loop for: https://www.udemy.com/course/python-total/learn/lecture/28147012#questions
