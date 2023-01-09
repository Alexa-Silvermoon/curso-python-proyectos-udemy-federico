nombre = input("Escriba su nombre: ");
ventas = round( float( input("Cual fue el valor total de sus ventas?: ") ), 2 ); # 2 decimales a ventas
comision = 13;
# comision2 = comision / 100; # comision2 es 0.13
#print( comision2, type( comision2));;
pago = round( ventas * comision / 100, 2 ); # 2 decimales al pago

print(f"Hola { nombre } tus ventas fueron ${ ventas } con comision al { comision }% y tu pago sera ${ pago }");

"""
Escriba su nombre: alexander
Cual fue el valor total de sus ventas?: 5000.59
Hola alexander tus ventas fueron $5000.59 con comision al 13% y tu pago sera $650.08

Process finished with exit code 0
"""