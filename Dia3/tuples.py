# las tuplas son como las listas, pero las tuplas usan () y son inalterables

miTupla = (1,2,(10,20),3,4,"q","w","e");
print( miTupla, type( miTupla ) );
print(( miTupla[4])); # 4

# miTupla[1] = "esto deberia dar error"; # INALTERABLES
print( miTupla[2][0] ); # 10

# se puede convertir una tuple a list de la siguiente forma:
miLista = list( miTupla );
print( miLista, type( miLista) );

# e igualmente se puede convertir una lista en tuple:
miNuevaTuple = tuple( miLista );
print( miNuevaTuple, type( miNuevaTuple ) );

# similar a la desestructuracion en JS, se puede extraer cosas de la tupla
tupla2 = ("A","B","C");
x,y,z = tupla2;
print( "tupla desestructurada: ", x,y,z );

"""
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla,
 y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
"""
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print( "repeticiones del 2: ", mi_tupla.count(2));

# tuples: https://www.udemy.com/course/python-total/learn/lecture/28045614?start=0#questions
