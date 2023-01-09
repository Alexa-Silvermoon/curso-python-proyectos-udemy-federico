def abrir_leer(contenido):
    archivoR = open("textopractica.txt")
    contenido = archivoR.read()
    # print(contenido)
    archivoR.close()
    return contenido

archivoR = open("textopractica.txt")
resul = abrir_leer(archivoR)
print(resul)

archivoR.close()

print("-----------------------------------")

"""
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
"""

def sobrescribir(archivoW):

    archivoW = open("textoremplazado.txt", "w")
    archivoW.write("contenido eliminado")
    archivoW.close()

archivoW = open("textoremplazado.txt", "w")
sobrescribir(archivoW)

archivoW.close()

print("-----------------------------------")

"""
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.
"""

def registro_error():

    archivoA = open("logerrores.txt", "a")
    archivoA.writelines("se ha registrado un error de ejecución\n")
    archivoA.close()

resul = registro_error()
print(resul)
