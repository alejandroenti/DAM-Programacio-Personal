import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 6')

# Definim les variables globals
cela_amplada = 50
cela_alcada = 50
cela_x_inici = 50
cela_y_inici = 50

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
    global cela_x_inici, cela_y_inici, cela_amplada, cela_alcada
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    for row in range(8):
        for column in range(8):
            # Escollim el color segons la fila i la columna
            color = GRAY if (row % 2 == 0 and column % 2 == 0) or (row % 2 != 0 and column % 2 != 0) else BLACK
            pygame.draw.rect(screen, color, (cela_x_inici, cela_y_inici, cela_amplada, cela_alcada))
            cela_x_inici += cela_amplada
        
        cela_x_inici = cela_amplada
        cela_y_inici += cela_alcada
    cela_y_inici = cela_alcada

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()