
# match es similar al switch en JS, pero match es mejor ya que permite detectar patrones

serie = "n-02"
print("A buscar: ", serie)

match serie:
    case "n-01":
        print("samsung")
    case "n-02":
        print("nokia")
    case "n-03":
        print("motorola")
    case _: # en caso de no existir lo que buscamos
        print("no existe ese producto")

print("------------------------------------------------")

cliente = {"nombre": "alexander",
           "edad": 26,
           "ocupacion": "estudiante"}
print(cliente)

pelicula = {"titulo": "matrix",
            "ficha_tecnica": {"protagonista": "keanu reeves",
                              "director": "las wachosky"}
            }
print(pelicula)

elementos = [ cliente, pelicula ]

for item in elementos:
    match item:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un cliente")
            print( nombre, edad, ocupacion )

        case {"titulo": titulo,
              "ficha_tecnica": { "protagonista": protagonista,
                                 "director": director}}:
            print("Es una pelicula")
            print( titulo, protagonista, director)

        case _:
            print("No se encontraron coincidencias")

# match: https://www.udemy.com/course/python-total/learn/lecture/30026172#questions
