import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 14')

# Definim les variables globals
cell_size = 50

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

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global cell_size
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    start_position = [50, 150]
    # Dibuixem la línia del color Vermell
    for counter in range(0, 11):
        light = counter * (255 / 10)
        pygame.draw.rect(screen, (light, 0, 0), (start_position[0], start_position[1], cell_size, cell_size))
        start_position[0] += cell_size
    
    start_position[0] = cell_size
    start_position[1] += cell_size

    # Dibuixem la línia del color Verd
    for counter in range(0, 11):
        light = counter * (255 / 10)
        pygame.draw.rect(screen, (0, light, 0), (start_position[0], start_position[1], cell_size, cell_size))
        start_position[0] += cell_size
    
    start_position[0] = cell_size
    start_position[1] += cell_size

    # Dibuixem la línia del color Blau
    for counter in range(0, 11):
        light = counter * (255 / 10)
        pygame.draw.rect(screen, (0, 0, light), (start_position[0], start_position[1], cell_size, cell_size))
        start_position[0] += cell_size
    
    start_position[0] = cell_size
    start_position[1] += cell_size

    # Dibuixem la línia monocromàtica
    for counter in range(0, 11):
        light = counter * (255 / 10)
        pygame.draw.rect(screen, (light, light, light), (start_position[0], start_position[1], cell_size, cell_size))
        start_position[0] += cell_size

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()