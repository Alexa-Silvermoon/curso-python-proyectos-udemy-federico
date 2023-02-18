import pygame
import random
import math
from pygame import mixer  # libreria python para trabajar con sonidos

# inicializar pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Invasion Espacial - By: Alexander Martinez")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

# musica
mixer.music.load('MusicaFondo.mp3')
# mixer.music.set_volume(0.3)  # controlar el volumen del juego
mixer.music.play(-1)  # la musica se repite cada vez que termina

# jugador y sus variables posiciones
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368  # posicion en pantalla en pixeles 368 porque es el resultado de 400 - la mitad del jugador 32
jugador_y = 500  # 600 - 64 = 536
jugador_x_cambio = 0

# multiples enemigos y sus variables posiciones
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10

# el enemigo se genera 10 veces
for e in range(cantidad_enemigos):

    # enemigo y sus variables posiciones, cada cosa se genera 8 veces
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))  # enemigo aparece al azar en eje x entre ese rango de px
    enemigo_y.append(random.randint(50, 200))  # enemigo aparece al azar en eje y entre ese rango de px
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

"""# enemigo y sus variables posiciones
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0, 736)  # enemigo aparece al azar en eje x entre ese rango de px
enemigo_y = random.randint(50, 200)  # enemigo aparece al azar en eje y entre ese rango de px
enemigo_x_cambio = 0.3
enemigo_y_cambio = 50"""

# bala y sus variables
img_bala = pygame.image.load("bala.png")
bala_x = 0  # bala eje x solo cambia dependiendo de donde este la nave
#  bala_y = 500  # la bala inicia a la misma altura de la nave
bala_y = 525  # correccion, la bala debe iniciar mas abajo porque si invasor toca nave, suma puntaje lo cual es un error
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False  # solo sera visible cuando se dispare

# puntaje
puntaje = 0
# fuente = pygame.font.Font('freesansbold.ttf', 32)  # estilo de letra y tamaño
fuente = pygame.font.Font('28 Days Later.ttf', 32)  # estilo de letra y tamaño
texto_x = 10  # el texto del puntaje estara al lado izquierdo de la pantalla pero no pegado al borde
texto_y = 10  # el texto del puntaje estara al lado superior de la pantalla pero no pegado al borde

# texto final de juego
fuente_final = pygame.font.Font('Game Over.otf', 100)  # tipo de letra y tamaño


def texto_final():
    mi_fuente_final = fuente_final.render('FIN DEL JUEGO', True, (255, 255, 255,))  # letra fin del juego, color blanco
    pantalla.blit(mi_fuente_final, (60, 200))  # fin del juego aparece al centro de la pantalla


# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))  # puntaje, antialias, color texto blanco
    pantalla.blit(texto, (x, y))  # poner yrxto en pantalla y con cordenadas


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))  # blit es para poner imagenes en pantalla


# funcion enemigo
def enemigo(x, y, ene):  # ene = enemigo, ene contiene un indice
    pantalla.blit(img_enemigo[ene], (x, y))


# funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    #  pantalla.blit(img_bala, (x + 16, y + 10))  # bala aparecera en el centro de la nave
    pantalla.blit(img_bala, (x + 16, y + 10))  # bala aparecera en el centro de la nave


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):

    # calcular distancia entr objetos d = √((x2 - x1)2 + (y2 - y1)2
    #  sqrt() hallar raiz, pow() hallar potencia al cuadrado
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))

    if distancia < 27:
        return True
    else:
        return False


# loop del juego
se_ejecuta = True
while se_ejecuta:

    # poner imagen de fondo:
    pantalla.blit(fondo, (0, 0))  # ubicacion 0px 0px

    # rellenar colores de la pantalla
    # pantalla.fill((205, 144, 228))
    # jugador_x += 0.1 # desplazamiento eje x del jugador

    # iterear eventos
    for evento in pygame.event.get():  # recorrera por todos los eventos del pygame

        # evento cerrar
        if evento.type == pygame.QUIT:  # evento que ocurre cuando se presiona la X de cerrar el juego
            se_ejecuta = False  # si se encuentra el evento QUIT (presionar la X) el ciclo se interrumpe y el juego se cierra

        # evento presionar flechas y tecla disparar
        if evento.type == pygame.KEYDOWN:  # se fija si se pulsa una tecla
            # print("una Tecla Fue Presionada")

            if evento.key == pygame.K_LEFT:  # se fija si la tecla pulsada flecha izquierda
                # print("Flecha izquierda presionada")
                jugador_x_cambio = -0.5  # moverse a la izquierda
            if evento.key == pygame.K_RIGHT:  # se fija si la tecla pulsada flecha derecha
                # print("Flecha derecha presionada")
                jugador_x_cambio = 0.5  # moverse a la derecha
            if evento.key == pygame.K_SPACE:  # se fija si la tecla espacio fue pulsada para disparar la bala
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()

                if not bala_visible:  # si la bala no es invisible, no se interrumpe el trayecto de la bala
                    bala_x = jugador_x  # la bala sigue verticalmente sin imitar la posicion ejex de la nave
                    disparar_bala(bala_x, bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:  # se fija si se suelta una tecla

            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  # se fija si se suelta la tecla flecha izquierda o flecha derecha
                # print("Tecla Flecha Soltada")
                jugador_x_cambio = 0  # deja de producirse movimiento

    # modificar posicion de jugador
    jugador_x += jugador_x_cambio  # pasara los valores del movimiento a la posicion jugador_x

    # mantener jugador dentro de bordes de pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:  # 800px - 64px de la nave
        jugador_x = 736

    # modificar posicion de enemigo
    for e in range(cantidad_enemigos):

        # fin del juego
        # if enemigo_y[e] > 500:  # si un enemigo alcanza a nave del jugador
        if enemigo_y[e] > 490:  # si un enemigo alcanza a nave del jugador
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000  # enemigos quedan fuera del rango de vision

            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]  # pasara los valores del movimiento a la posicion enemigo_x

        # mantener cada enemigo dentro de bordes de pantalla
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3  # empieza a moverse a la derecha
            enemigo_y[e] += enemigo_y_cambio[e]  # baja 50px cuando toca el borde izquierdo
        elif enemigo_x[e] >= 736:  # 800px - 64px de la nave
            enemigo_x_cambio[e] = -0.3  # empieza a moverse a la izquierda
            enemigo_y[e] += enemigo_y_cambio[e]  # baja 50px cuando toca el borde derecho

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            #  bala_y = 500  # si hay colision bala vuelve a estar a la altura de la nave pero invisible
            bala_y = 525  # si hay colision bala vuelve a estar a la altura de la nave pero invisible
            bala_visible = False
            puntaje += 1  # por cada enemigo muerto, suma 1 punto
            # print("Puntaje Colision: ", puntaje)

            # si hay una colision, nuevo enemigo se genera aleatoriamente
            enemigo_x[e] = random.randint(0, 736)  # enemigo aparece al azar en eje x entre ese rango de px
            enemigo_y[e] = random.randint(50, 200)  # enemigo aparece al azar en eje y entre ese rango de px

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:  # cuando bala haya desaparecido totalmente, volvera a la altura de la nave
        # bala_y = 500
        bala_y = 525
        bala_visible = False

    if bala_visible:  # es True
        disparar_bala(bala_x, bala_y)  # la bala sigue verticalmente sin imitar la posicion ejex de la nave
        bala_y -= bala_y_cambio  # bala ira subiendo en pantalla, restando 1px en cada iteracio

    jugador(jugador_x, jugador_y)
    # enemigo(enemigo_x, enemigo_y)

    mostrar_puntaje(texto_x, texto_y)

    # actualizar casa cosa en pantalla
    pygame.display.update()  # actualizar los colores

# CHRISTIAN ALEXANDER MARTINEZ MILLAN
# https://www.flaticon.com/
# https://www.1001freefonts.com/
# https://www.youtube.com/watch?v=s_vVq1aajr0
# https://pypi.org/project/auto-py-to-exe/

# convert code to exe
# pip install auto-py-to-exe
# auto-py-to-exe

# crear pantalla del juego: https://www.udemy.com/course/python-total/learn/lecture/29133948#questions
# cambiar titulo, icono y color: https://www.udemy.com/course/python-total/learn/lecture/29134606?start=30#questions
# agrgar protagonista y ubicacion: https://www.udemy.com/course/python-total/learn/lecture/29135116?start=75#questions
# mover al personaje: https://www.udemy.com/course/python-total/learn/lecture/29136584#questions
# controlar el movimiento de la nave y posicion: https://www.udemy.com/course/python-total/learn/lecture/29142438#questions
# limitar movimiento cohete, paredes a los lados: https://www.udemy.com/course/python-total/learn/lecture/29143852#questions
# crear enemigos y su posicion: https://www.udemy.com/course/python-total/learn/lecture/29154778#questions
# generar movimiento del enemigo: https://www.udemy.com/course/python-total/learn/lecture/29155740?start=30#questions
# agregar imagen de fondo: https://www.udemy.com/course/python-total/learn/lecture/29156718#questions
# disoarar balas: https://www.udemy.com/course/python-total/learn/lecture/29173912#questions
# movimiento de las balas: https://www.udemy.com/course/python-total/learn/lecture/29174752#questions
# hallar distancia entre dos objetos: https://es.wikihow.com/hallar-la-distancia
# detectar colisiones: https://www.udemy.com/course/python-total/learn/lecture/29178282?start=15#questions
# agregar enemigos: https://www.udemy.com/course/python-total/learn/lecture/29180822#questions
# mostrar puntaje: https://www.udemy.com/course/python-total/learn/lecture/29181546?start=15#questions
# agregar musica y sonidos: https://www.udemy.com/course/python-total/learn/lecture/29200170#questions
# terminar el juego: https://www.udemy.com/course/python-total/learn/lecture/29200196#questions
