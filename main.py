import pygame
import constantes
from personaje import Personaje

#Inicilaizamos pygame 
pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer Juego")   

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#Imagen del Jugador 
#player_image = pygame.image.load("assets//images//characters//player1.png")
#player_image = escalar_img(player_image, constantes.ESCALA_PERSONAJE)

#Guardar las imagenes en un arreglo 
animaciones = []
for i in range (3):
    img = pygame.image.load(f"assets//images//characters//player{i}.png")
    img = escalar_img(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

jugador  = Personaje(50, 50, animaciones)

#Definir movimeinto del jugador 
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#Metodo de control de Frame Rate 
relog = pygame.time.Clock()

run = True
while run:

    #Definieindo en la ejecucion el FPS
    relog.tick(constantes.FPS)
  
    #Borrando los pasos del juagdor 
    ventana.fill(constantes.COLOR_BG)

    #Movimiento del Jugador cantidad de frames
    delta_x = 0
    delta_y = 0

    #Definicion para mover al jugado sumando valores de x y y
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #Invoca la funcion de movimiento 
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    #Pintar el jugador en ventana
    jugador.dibujar(ventana)

   

    #For de update y persistencia de venytana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        
        #If para activar el movimiento del personaje 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        #If para frenar el movimiento del personaje 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
                
    pygame.display.update()

pygame.quit