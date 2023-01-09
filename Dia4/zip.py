nombres = ["Gil", "Ofe", "Adri", "Andre", "Jero", "Chris"]
edades = [70, 68, 50, 48, 15, 26]
ciudades = ["La Union", "Pijao", "Cali", "Pereira", "Madrid", "Cali"]

combinados = list(zip( nombres, edades, ciudades ) ); # obligatorio list(zip
print(combinados);

for nombre, edad, ciudad in combinados:
    print(f"{ nombre } tiene { edad } años y vive en { ciudad }")

print("-------------------------------------------------------")

# zip sencillo:
marcas = ["kawasaki", "yamaha"]
productos = ["h2", "r1"]

mi_zip = zip(marcas, productos)
print(mi_zip)
listaZip = list(mi_zip)
print(listaZip)

print("-------------------------------------------------------")

"""
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), 
y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
"""

espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
english = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, english))

print(numeros[0:5])

for numero in numeros:
    print(numero)

# zip: https://www.udemy.com/course/python-total/learn/lecture/28157720#questions
