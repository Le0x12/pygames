import pygame
import constantes

class Personaje():
    #Inicializa el personaje posicion en ventana y tamaño
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
       
        #Imagen de la animacion mostrada
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0  
        self.image = animaciones[self.frame_index]
        #------------------------------------------
        self.image = animaciones[0]
        self.forma = self.image.get_rect()
        self.forma.center = (x, y)

    #Dibuja al personaje forma y color
    def dibujar(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(image_flip, self.forma)
        #pygame.draw.rect(interfaz, (constantes.COLOR_PERSONAJE), self.forma)

    #Define el movimiento del personaje 
    def movimiento(self,  delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    
    def update(self):
        cooldown_animacion = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index > len(self.animaciones) - 1 :
            self.frame_index = 0