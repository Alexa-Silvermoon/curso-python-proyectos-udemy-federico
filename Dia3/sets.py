
# los set eliminan los repetidos

miSet = set((1,2,3,3,1,1,1)); # debe tener doble parentesis
print( miSet, type( miSet ) );
print("longitud de set: ", len(miSet));
print(" 2 esta dentro de set?: ", 2 in miSet);

miOtroSet = {"a","b","b","c"};
print( miOtroSet, type( miOtroSet));

# print( miSet[0] ); # error, no se pueden leer los set asi
# miSet[0] = 10; #error, no se le puede asignar asi un valor a un set

# no pueden haber listas dentro de set
# no pueden haber diccionarios dentro de sets

# los set si admiten tuple, ya que los tuple son inmutables
miSet2 = set((1, 2, 3, 3, (9, 8), 1, 1, 1));
print(miSet2, type(miSet2));

# unir un set con otro
miSet3 = {1,2,3}
miSet4 = {3,4,5}
miSet5 = miSet3.union( miSet4 ); # el nuevo set elimina los repetidos
print( miSet5, type(miSet5 ) );

# set con metodos add, remove, discard, pop
miSet6 = {9,8,7,11,12};
miSet6.add(10); # de esta forma si se puede agregar un elemento al set
print( miSet6 );
miSet6.remove(11); # de esta forma si se puede eliminar un elemento de un set
miSet6.discard(11); # discard NO da error si el elemento dentro del set no existe, remove si
sorteo = miSet6.pop(); # cuidado al dejar pop vacio en un set ya que elimina un elemento de forma aleatoria
print(miSet6);
print("elemento aleatorio tomado por pop(): ", sorteo );

# vacia el set con metodo clear()
miSet7 = {11,12,13,14};
miSet7.clear()
print("vaciar el set con clear(): ", miSet7 );

# sets: https://www.udemy.com/course/python-total/learn/lecture/28047634#questions
