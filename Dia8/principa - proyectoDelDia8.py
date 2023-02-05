import numerosProyectoDelDia8

def preguntar():

    print("Bienvenido a Farmacia")

    while True:

        print("P - Perfumeria\nF - Farmacia\nC - Cosmeticos")

        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)

        except ValueError:

            print("Esa no es una opcion valida")

        else:
            break

    numerosProyectoDelDia8.decorador(mi_rubro) # le paso mi_rubro a la funcion decorar() en numerosProyectoDelDia8.py


def inicio():

    while True:

        preguntar()

        try:
            otro_turno = input("Desea Sacar Otro Turno?  [S] Si - [N] No ").upper()
            ["S", "N"].index(otro_turno)

        except ValueError:

            print("Esa no es una opcion valida")

        else:

            if otro_turno == "N": # en caso de ser [S] se activara de nuevo preguntar()
                print("Gracias Por Su Visita")
                break

inicio()

# proyecto: https://www.udemy.com/course/python-total/learn/lecture/28867924?start=15#questions
