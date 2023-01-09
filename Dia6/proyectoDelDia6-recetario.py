import os
import pathlib
from os import system

def count_recetas():
    recetas = [txt for txt in raiz.glob("**/*.txt")]
    counter = len(recetas)
    return counter


def get_categoria():
    categorias = []
    ruta_recetas_raiz = raiz
    for categoria in ruta_recetas_raiz.iterdir():
        categorias.append(categoria)
    dic_categoria = {"categorias": categorias, "raiz": ruta_recetas_raiz}
    return dic_categoria


def which_categoria():
    categorias_rutas = get_categoria()
    categorias = [categoria.stem.title() for categoria in categorias_rutas['categorias']]
    print('Categorias:', *categorias, sep='\n- ')
    categoria = input(f"\nElige una categoria por favor:\n").title()
    while categoria not in categorias:
        # system('clear')
        system('cls')
        print('Categorias:', *categorias, sep='\n- ')
        categoria = input(f'Error: "{categoria}" no es una categoria valida, por favor elige una '
                          f'disponible:\n').title()
    else:
        id_categoria = categorias.index(categoria)
        categoria = categorias_rutas['categorias'][id_categoria]
        return categoria


def get_recetas():
    recetas = []
    categoria = which_categoria()
    ruta_recetas_raiz = get_categoria()
    ruta_de_categoria = ruta_recetas_raiz['raiz'] / categoria
    for receta in ruta_de_categoria.iterdir():
        recetas.append(receta)
        recetas.sort()
    return recetas, ruta_de_categoria


def which_receta():
    receta_rutas, ruta_de_categoria = get_recetas()
    recetas = [receta.stem.title() for receta in receta_rutas]
    print(f'\nRecetas de {ruta_de_categoria.stem}:', *recetas, sep='\n- ')
    receta = input(f"\nElige una receta por favor:\n").title()
    while receta not in recetas:
        # system('clear')
        system('cls')
        print(f'Recetas de {ruta_de_categoria.stem}:', *recetas, sep='\n- ')
        receta = input(
            f'Error: "{receta}" no es una receta valida, por favor elige una disponible:\n').title()
    else:
        id_receta = recetas.index(receta)
        receta = receta_rutas[id_receta]
    return receta


# [1] Leer receta
def read_receta():
    receta = which_receta()
    print(f"\nReceta de {receta.stem}:")
    print(receta.read_text())


# [2] Crear Receta
def create_receta():
    receta_rutas, categoria = get_recetas()
    recetas = [receta.stem.title() for receta in receta_rutas]
    nueva_receta_nombre = input(f"Proporciona el nombre de la nueva receta sin extension (i.e. '.txt') "
                                f"para la categoria {categoria.stem.capitalize()} por favor:\n").title()
    while nueva_receta_nombre in recetas or '.' in nueva_receta_nombre:
        # system('clear')
        system('cls')
        print(f'Recetas de {categoria.stem.capitalize()}:', *recetas, sep='\n- ')
        print(f'Error: Ya existe una receta con el nombre "{nueva_receta_nombre}" o tiene extension.')
        nueva_receta_nombre = input(f"Proporciona el nombre de la nueva receta sin extension (i.e. '.txt') "
                                    f"para la categoria {categoria.stem.capitalize()} por favor:\n").title()
    else:
        nueva_receta_nombre = nueva_receta_nombre + '.txt'
    nueva_receta = open(categoria / nueva_receta_nombre, 'w')
    nueva_receta.write(input(f"Por favor escribe la receta de {nueva_receta_nombre}\n"
                             f" - Para finalizar, solo presiona la tecla 'enter':\n").capitalize())
    nueva_receta.close()
    print(f'\nSe guardo tu receta "{nueva_receta_nombre}" '
          f'en la categoria "{categoria.stem.capitalize()}" correctamente.')


# [3] Crear categoria
def create_categoria():
    categorias_rutas = get_categoria()
    categorias = [categoria.stem.title() for categoria in categorias_rutas['categorias']]
    nueva_categoria = input(f"\nProporciona el nombre de la nueva categoria por favor:\n").title()
    while nueva_categoria in categorias:
        # system('clear')
        system('cls')
        print('Categorias:', *categorias, sep='\n- ')
        nueva_categoria = input(
            f'Error: "{nueva_categoria}" ya existe, proporciona un nombre diferente por favor:\n').title()
    else:
        os.chdir(categorias_rutas['raiz'])
        os.makedirs(nueva_categoria)
        print(f'\nSe guardo tu nueva categoria "{nueva_categoria}" correctamente\n')


# [4] Eliminar receta
def delete_receta():
    receta = which_receta()
    os.remove(receta)
    print(f'Se ha eliminado la receta "{receta.name}" correctamente')


# [5] Eliminar categoria
def delete_categoria():
    categoria = which_categoria()
    os.rmdir(categoria)
    print(f'Se ha eleimando la categoria "{categoria.name}" correctamente')


def end_game():
    return print(f"Gracias por haber consultado el Recetario {nombre}, adios!")


def display_menu():
    return print(f"""\n [1] Leer receta
 [2] Crear Receta
 [3] Crear categoria
 [4] Eliminar receta
 [5] Eliminar categoria
 [6] Finalizar codigo
""")


def validar_opc(opc):
    while not opc.isdigit() or int(opc) not in range(1, 7):
        # system('clear')
        system('cls')
        display_menu()
        opc = input(f"Error: Opcion '{opc}' invalida, por favor elige una opcion valida:  ")
    else:
        return opc


def volver():
    continuar = 'x'
    while continuar.lower() != 'v':
        continuar = input("\nPresiona 'V' para regresar al menu principal:\n")


def menu():
    opc = '1'
    while int(opc) != 6:
        display_menu()
        opc = (input(f"{nombre} por favor elige la opcion deseada:  "))
        opc = validar_opc(opc)
        # system('clear')
        system('cls')
        match int(opc):
            case opc if opc == 1:
                read_receta()
            case opc if opc == 2:
                create_receta()
            case opc if opc == 3:
                create_categoria()
            case opc if opc == 4:
                delete_receta()
            case opc if opc == 5:
                delete_categoria()
        volver()
        # system('clear')
        system('cls')
    else:
        end_game()


# raiz = pathlib.Path('/home/cntrs/DevOps/Python/Projects/Recetas')
raiz = pathlib.Path('/Programacion-Cursos-Desarrollador/Python/Python-proyecto1/Dia6/recetario')
print(f"----    RECETARIO   ------\n")
nombre = input(f"Cual es tu nombre?: ").capitalize()
print(f"Bienvenido {nombre}, informo lo siguiente.\n"
      f"Ruta de acceso al recetario: {raiz}\n"
      f"Cantidad total de recetas: {count_recetas()} recetas.")
menu()