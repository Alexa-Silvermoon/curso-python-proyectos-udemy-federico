
# los diccionarios son similares a los objetos en JS
diccionarioPersona = {
    "apellido": "martinez",
    "nombre": "alexander",
    "edad": 10
}
print( diccionarioPersona, type( diccionarioPersona ) );

apellido = diccionarioPersona["apellido"];
print( "apellido: ", apellido );
nombre = diccionarioPersona["nombre"];
print( "nombre: ", nombre );
edad = diccionarioPersona["edad"];
print( "edad: ", edad );

print("---------------------------------------");

diccionarioMix = {

    "llave1": 55,
    "llave2": [10,20,30],
    "llave3": {

        "subllave1": 100,
        "subllave2": 200,
        "subllave3": ["a","l","e","x"]
    }
}
print( "llave2: ", diccionarioMix["llave2"]); # [10, 20, 30]
print( "llave2 solo posicion 1: ", diccionarioMix["llave2"][1]); # 20
print( "llave3 subllave2: ", diccionarioMix["llave3"]["subllave2"]); # 200
print( "llave3 subllave3: ", diccionarioMix["llave3"]["subllave3"]); # ["a","l","e","x"]
print( "llave3 subllave3 pos1 solo la l en mayuscula: ", diccionarioMix["llave3"]["subllave3"][1].upper() );

print("---------------------------------------");

diccionarioNumeros = { 1: "a", 2: "b" }

diccionarioNumeros[3] = "c";
print( diccionarioNumeros );

diccionarioNumeros[2] = "z"; # remplazar valor en la llave 2
print( diccionarioNumeros );

print( "llaves: ", diccionarioNumeros.keys() );
print( "valores: ", diccionarioNumeros.values() );

"""
Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver 
el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los 
nombres de las claves y/o índices según corresponda.
"""
mi_dict = {

    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9,
               "points2": [10, 300, 15]
               }
}

print(mi_dict["puntos"]["points2"][1]);

print("---------------------------------------");

"""
Actualiza la información de nuestro diccionario llamado mi_dic  
(reasignando nuevos valores a las claves según corresponda), 
y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Karen

apellido: Jurgens

edad: 36

ocupacion: Editora

pais: Colombia

para ello, no debes cambiar la línea de código ya escrita, 
sino actualizar los valores mediante métodos de diccionarios.
"""
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
print("original: ", mi_dic);
mi_dic["edad"] = 36;
mi_dic["ocupacion"] = "Editora";
mi_dic["pais"] = "Colombia";
print( "despues: ", mi_dic );

# diccionarios: https://www.udemy.com/course/python-total/learn/lecture/28043634#questions
