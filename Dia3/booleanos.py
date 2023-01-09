
# en los booleanos siempre el True o False debe iniciar con mayuscla

var1 = True;
print( var1, type( var1));

numero1 = 5;
numero2 = 3 + 2;

comparacion = numero1 > numero2;
print( f"{ numero1 } mayor que { numero2 } ?: ", comparacion, type( comparacion ) );

comparacion2 = numero1 >= numero2;
print( f"{ numero1 } mayor o igual que { numero2 } ?: ", comparacion2, type( comparacion2 ) );

comparacion3 = numero1 != numero2;
print( f"{ numero1 } es diferente que { numero2 } ?: ", comparacion3, type( comparacion3 ) );

# lo mismo pero poniendo directamente el metodo bool()
comparacion4 = bool( numero1 < numero2 );
print( f"{ numero1 } menor que { numero2 } ?: ", comparacion4, type( comparacion4 ) );

lista = [1,2,3];
control = 5 in lista;
print( "5 dentro de lista?: ", control );


"""
Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) 
en pantalla utilizando print()

"""
prueba = 25 ** 0.5 == 5
print(prueba)

# booleanos: https://www.udemy.com/course/python-total/learn/lecture/28052134#questions

redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"];
listaOrdenada = redes.sort()
print( listaOrdenada )
# redes.sort()