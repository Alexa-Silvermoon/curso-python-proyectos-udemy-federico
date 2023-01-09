n1 = "alexan";
n2 = "der";
print( n1+n2 );
print( n1 * 10 ); # repetir 10 veces n1

# meter cometario con saltos de linea en variable
poema = """la garra
que 
aggara"""
print(poema);
print("existe garra en poema?: ", "garra" in poema ); # true or false
print("NO existe sol en poema?: ", "sol" not in poema ); # true or false, la negacion

# saber longitud de un string
longitud = len(poema);
print(poema, " tiene longitud de: ", longitud);

# propiedades de string
# https://www.udemy.com/course/python-total/learn/lecture/28033266#questions
