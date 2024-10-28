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
def app_run():
    pass

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    #Pentágono
    pygame.draw.polygon(screen, GREEN, [(150, 100), (100, 150), (125, 200), (175, 200), (200, 150)], 5)

    #Hexágono
    pygame.draw.polygon(screen, RED, [(300, 100), (250, 150), (300, 200), (350, 200), (400, 150), (350, 100)])
    pygame.draw.polygon(screen, GREEN, [(300, 100), (250, 150), (300, 200), (350, 200), 
    (400, 150), (350, 100)], 5)

    # Octágono
    pygame.draw.polygon(screen, PURPLE, [(150, 300), (100, 350), (100, 400), (150, 450), (200, 450), (250, 400), (250, 350), (200, 300)])

    # Arco
    pygame.draw.arc(screen, ORANGE, pygame.Rect(400, 250, 200, 100), math.radians(45), math.radians(180), 5)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()