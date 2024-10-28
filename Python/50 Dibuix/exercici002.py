import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

angle = 0
centre = (200, 250)
radi = 100

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs (resol aquí l'exercici)
def posicio_perimetre_cercle(center, radi, angle_graus):
    angle_radians = math.radians(angle_graus)  # Convertir l'angle a radians
    x = center[0] + radi * math.cos(angle_radians)    # Coordenada X
    y = center[1] + radi * math.sin(angle_radians)    # Coordenada Y
    return x, y

def app_run():
    global pos, angle

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    
    speed = 50  # píxels per segon
    displacement = speed * delta_time

    pos = posicio_perimetre_cercle(centre, radi, angle)
    angle = (angle + displacement) % 360

# Dibuixar
def app_draw():
    global pos

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    pygame.draw.circle(screen, ORANGE, centre, radi, 5)
    pygame.draw.line(screen, BLACK, centre, pos, 5)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()