miBool = 4 < 5 < 6;
print( miBool ); # True

miBool2 = 4 < 5 > 6;
print( miBool2 ); # False

miBool3 = 4 < 5 and 5 > 6
print( miBool3 ); # False

miBool4 = ( 4 < 5 ) and ( 5 == 2 + 3 ); # ambas condiciones deben ser verdaderas para el true
print( miBool4 ); # True

miBool5 = ( 55 == 55 ) and ( "perro" == "perro" );
print( miBool5 ); # True

miBool6 = 1 == 10 or 30 == 30; # basta con que una de las condiciones sea verdadera para el true
print( miBool6 ); # True

texto = "christian alexander martinez millan";
miBool7 = ( "frase" in texto ) and ( "christian" in texto );
print( miBool7 ); # False

miBool8 = ( "alexander" in texto ) and ( "christian" in texto );
print( miBool8 ); # True

miBool9 = ( "nope" in texto ) or ( "christian" in texto );
print( miBool9 ); # True

miBool10 = not ( "a" == "a" ); # verdadero choca con falso
print( miBool10 ); # false

miBool11 = not ( "a" != "a" ); # falso igual a falso
print( miBool11 ); # true

"""
Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y

palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

Elon Musk
"""

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_boolFINAL = ( palabra1 not in frase ) and ( palabra2 not in frase );
print( mi_boolFINAL ); # true

# operadores logicos: https://www.udemy.com/course/python-total/learn/lecture/28139872#questions
