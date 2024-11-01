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
pygame.display.set_caption('Alejandro Lopez - Exercici 18')

# Definim les variables globals
saturarion = 1
lightness = 0.5

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
    global saturarion, lightness
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem la roda de colors
    for angle in range(0, 361, 15):
        start = utils.point_on_circle((300, 250), 25, angle)
        end = utils.point_on_circle((300, 250), 150, angle)

        start_last = utils.point_on_circle((300, 250), 25, angle - 15)
        end_last = utils.point_on_circle((300, 250), 150, angle - 15)

        color = utils.hsl_to_rgb(angle, saturarion, lightness)

        pygame.draw.line(screen, color, start, end, 5)
        pygame.draw.polygon(screen, color, [start, start_last, end_last, end])

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()