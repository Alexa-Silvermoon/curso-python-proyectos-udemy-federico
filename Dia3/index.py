miTexto = "esta es una prueba";
# resultado = miTexto[-2];
# resultado = miTexto[9];
# resultado = miTexto.index("n");
resultado = miTexto.index("prueba");
resultado = miTexto.index("a", 5 ); # buscar la a despues del indice 5
resultado = miTexto.index("a", 10, 12 ); # buscar la a despues del indice 5 hasta el indice 12
print(resultado);

resultadoRevez = miTexto.rindex("b"); # .rindex() es para buscar de derecha a izquierda
print( resultadoRevez );

# metodo index() y rindex()
# https://www.udemy.com/course/python-total/learn/lecture/27999642#questions

palabra = "ordenador";
resultado = palabra[4];
print(resultado);

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print( frase.rindex("práctica"));
