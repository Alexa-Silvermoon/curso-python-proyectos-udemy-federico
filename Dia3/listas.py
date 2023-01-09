
# las listas son similares a los arrays en JS

lista1 = ["a", "b", "c"];
lista2 = ["x", "y", "z"];
lista3 = lista1 + lista2;
lista4 = lista1 + lista2;
print("antes: ", lista3);

lista3[0] = "alfa"; # remplaza la posicion 0 anterior
print( "despues: ", lista3 );

lista3.append("p"); # inserta el elemento al final de la lista array
print( lista3);

lista3.pop() # .pop() por defecto elimina el ultimo elemento de la lista array, en este caso la p
print("eliminar lo que inserto el append() anterior: ", lista3 );

eliminado = lista4.pop(1); # eliminar la "b" en este caso y extraerla en una nueva variable
print( lista4 );
print("elemento eliminado fue: ", eliminado );

listaDesOrdenada = ["b", "c", "a", "d"];
listaDesOrdenada.sort();
listaOrdenada = listaDesOrdenada # parece tonteria, pero solo asi funciona xD
print( listaOrdenada );

nombre = ["A","L","E","X","A","N","D","E","R"];
nombre.reverse();
nombreRevez = nombre; # parece tonteria, pero solo asi funciona xD
print( nombreRevez );

# listas: https://www.udemy.com/course/python-total/learn/lecture/28034636#questions
