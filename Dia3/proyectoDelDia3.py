texto = input("Porfavor ingresa un texto: ");
letra1 = input("Te pedire 3 letras, porfavor ingresa la primera letra: ");
letra2 = input("porfavor ingresa la segunda letra: ");
letra3 = input("porfavor ingresa la tercera letra: ");

# transforma texto y lestras a  minuscula
texto = texto.lower();
letra1 = letra1.lower();
letra2 = letra2.lower();
letra3 = letra3.lower();

conteoLetra1 = texto.count( letra1 );
conteoLetra2 = texto.count( letra2 );
conteoLetra3 = texto.count( letra3 );

conteoPalabras = 1 + texto.count(" "); # +1 para contar la ultima palabra despues del ultimo espacio
conteoEspacios = texto.count(" "); # contar espacios en blanco

longitudLetras = len( texto ); # longitud del texto, inclye espacios en blanco
totalLetras = longitudLetras - conteoEspacios; # sliminar los pescios en blanco y solo quedan letras

textoInvertido = texto[ :: -1 ]; # imprimir texto al revez

aparecePython = "python" in texto; # aparece python en texto? boolean

print("----------------------------------------------------------------------------------------------");
print("Texto ingresado fue: ", texto);
print(f"La letra { letra1 } aparece en el texto { conteoLetra1 } veces");
print(f"La letra { letra2 } aparece en el texto { conteoLetra2 } veces");
print(f"La letra { letra3 } aparece en el texto { conteoLetra3 } veces");
print(f"En el texto hay un total de { conteoPalabras } palabras");
print(f"En el texto hay un total de { totalLetras } letras");
print(f"En el texto hay un total de { conteoEspacios } espacios en blanco");
print(f"La primera letra del texto es: { texto[0] } y la ultima letra del texto es: {  texto[-1]}");
print("El texto en orden inverso es: ", textoInvertido);
print("Aparece la palabra python en el texto?: ", aparecePython );

"""
OUTPUT:
Porfavor ingresa un texto: ALEX MARTT PYTHON
Te pedire 3 letras, porfavor ingresa la primera letra: A
porfavor ingresa la segunda letra: T
porfavor ingresa la tercera letra: J
----------------------------------------------------------------------------------------------
Texto ingresado fue:  alex martt python
La letra a aparece en el texto 2 veces
La letra t aparece en el texto 3 veces
La letra j aparece en el texto 0 veces
En el texto hay un total de 3 palabras
En el texto hay un total de 15 letras
En el texto hay un total de 2 espacios en blanco
La primera letra del texto es: a y la ultima letra del texto es: n
El texto en orden inverso es:  nohtyp ttram xela
Aparece la palabra python en el texto?:  True

Process finished with exit code 0
"""
