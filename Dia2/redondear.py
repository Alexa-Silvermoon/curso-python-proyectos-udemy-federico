z = 90;
x = 7;
print( f" { z } dividido entre { x } es: { z / x }");

q = float( input("Ingrese un numero con decimales para redondearlo: ") );
w = float( input("Ingrese un numero para dividir al anterior: ") );
e = q / w;
print( "Redondear como entero: ", round( e ) );
# el redondedo se hace hacia arriba o hacia abajo dependiendo del entero que este mas cerca
print( "Redondear con dos decimales: ", round( e, 2 ) ); # el 2 siginifica la cantidad de decimales que quiero en el resultado

# redondeo:
# https://www.udemy.com/course/python-total/learn/lecture/27921002#questions

num = round( 10/3, 2  );
print( num );

# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
num1 = 5 ** 0.5;
num2 = round( num1, 4 );
print( num2 );