texto = "ALEXANDER";
fragmento = texto[ 0 : 6 ]; # extraer desde A hastan N, es decir ALEXAN
print(( fragmento ) );

texto = "ALEXANDER";
fragmento = texto[ 0 : 6 : 2]; # extraer desde A hastan N y salteando de 2 en 2
print(( fragmento ) );

texto = "ALEXANDER";
fragmento = texto[ :: -1 ]; # imprimir cadena al revez
print(( fragmento ) );

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
longitud = len(frase); # len() medir longitudes de cadenas en python, en este caso 66
print( "longitud es: ", longitud );
print( frase[ 8 : longitud : 3 ] ); # 8 es de 0 a 8 hay 9, 3 porque asi lo pide el ejercicio

# extraer sub-strings
# https://www.udemy.com/course/python-total/learn/lecture/28006052#questions
