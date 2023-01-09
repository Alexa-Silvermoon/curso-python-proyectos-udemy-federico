texto = "ALEXANder";
resultado = texto.upper(); # pasar textoa mayuscula
print( resultado );

texto = "alexander";
resultado = texto[3].upper(); # pasar la x a mayuscula
print( resultado );

texto = "ALEXANder";
resultado = texto.lower(); # pasar texto a minuscula
print( resultado );

texto = "ALEXANder millan";
resultado = texto.split(); # pasar a lista, array en JS
print( resultado );

texto = "ALEXANDER MARTINEZ MILLAN";
resultado = texto.split("A"); # crear una lista cortando las "A"
print( resultado );

mensaje = "es pc pertenece a alexander";
resultadoReplace = mensaje.replace( "alexander", "jeronimo"); # viejo, nuevo
resultadoReplaceLetras = mensaje.replace( "e", "X" ); # remplazar todas las "e" por una "X"
print( resultadoReplace );
print(resultadoReplaceLetras);

texto = "ALEXANDER MARTINEZ MILLAN";
resultado = texto.find("L"); # similar a metodo index(), si existe muestra la posicion
resultadoG = texto.find("G"); # si letra no existe, devuelve -1 en vez de error
print( resultado );
print( resultadoG );

nombre1 = "CHRISTIAN";
nombre2 = "ALEXANDER";
apellido1 = "MARTINEZ";
apellido2 = "MILLAN";
nombreUnido2 = [nombre1, nombre2, apellido1, apellido2];
print( " ".join(nombreUnido2) );

nombreUnido = " ".join([nombre1, nombre2, apellido1, apellido2]);
print( nombreUnido );

# metodos de string:
# https://www.udemy.com/course/python-total/learn/lecture/28031382?start=120#questions
# https://www.udemy.com/course/python-total/learn/lecture/28031382?start=600#questions

"""
Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas.
"""
texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(texto);
texto1 = texto.replace("difícil", "fácil");
texto2 = texto1.replace("mala", "buena");
print(texto2);