dic = {"clave1": 100, "clave2": 500}

a = dic.popitem() # ultimo en entrar, primero en salir
print("a: ", a)
print("dic: ", dic)

# metodos ayuda y documentacion: https://www.udemy.com/course/python-total/learn/lecture/28344286?start=30#questions
print("-----------------------------------------")

stringFeo = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
result = stringFeo.lstrip(",:_#%,:# ") # este metodo elimina algunos caracteres
print(result)

print("-----------------------------------------")

"""
Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa 
y cómo es su funcionamiento.
"""
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

# frutas.insert("naranja") # forma 1
# frutas.append("naranja") # forma 2
print(frutas)

print("-----------------------------------------")

"""
Agregar un elemento al final de la lista
Método: append("nuevo elemento")
"""
nombres_masculinos = ["Edgardo", "David"]
print(nombres_masculinos)
nombres_masculinos.append("Jose")
print(nombres_masculinos)
# ['Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose']

print("-----------------------------------------")

"""
Agregar varios elementos al final de la lista
Método: extend(otra_lista)
"""
nombres2 = ['Alvaro', 'David', 'Edgardo']
print(nombres2)
nombres_masculinos.extend(["Jose", "Gerardo"])
print(nombres_masculinos)

print("-----------------------------------------")

"""
Agregar un elemento en una posición determinada
Método: insert(posición, "nuevo elemento") # meter en la posicion que yo quiera
"""
nombres3 = ["antony", "benjamin", "clay"]
print(nombres3)
nombres3.insert(0, "Ricky")
print(nombres3)

# https://uniwebsidad.com/libros/python/capitulo-7/metodos-de-agregado

print("-----------------------------------------")

"""
Verifica si los sets a continuación forman conjuntos aislados 
(es decir, que no tienen elementos en común), utilizando el método isdisjoint(). 
Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y 
cómo es su funcionamiento.
"""
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
print(marcas_smartphones)
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_tv)
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados) # false

# da false porque hay elementos en comun en ambos sets
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
