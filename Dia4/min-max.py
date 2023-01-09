lista = [1,2,3,4,5]
print(lista)

menor = min(lista)
mayor = max(lista)

print("Menor es: ", menor)
print("Mayor es: ", mayor)
print(f"El menor es { min(lista) } y el mayor es { max(lista)}");

print("------------------------------------------------------");

listaNombres = ["christian", "joe", "jeronimo", "profesor charles xavier"]
print(listaNombres)

print( min(listaNombres)) # c, ay que en lestras da prioridad desde la a hasta la z, tener en cuenta mayusculas

print("------------------------------------------------------");

diccionario = { "A":10, "B":20 }
print(diccionario)

print("Minima llave es: ", min(diccionario)) # en los diccionarios por defecto tomas las llaves primero
print("Minimo valor es: ", min(diccionario.values()))
print("Maxima llave es: ", max(diccionario))
print("Maximo valor es: ", max(diccionario.values())) # si queremos los valores, tenemos que especificarlos

print("------------------------------------------------------");

"""
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, 
"Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, 
y almacénalo en una variable llamada ultimo_nombre.
"""

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

ultimo_nombre = max(diccionario_edades)
edad_minima = min(diccionario_edades.values())

print(ultimo_nombre)
print(edad_minima)

# min y max: https://www.udemy.com/course/python-total/learn/lecture/28158350?start=15#questions
