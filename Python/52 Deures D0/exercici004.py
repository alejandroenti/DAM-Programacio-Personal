import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 4')

# Definim les variables globals
window_width, window_height = screen.get_size()
punts = []

# Bucle de l'aplicació
def main():
    global list

    is_looping = True

    for i in range(10):
        point_x = random.randint(0, window_width)
        point_y = random.randint(0, window_height)
        punts.append((point_x, point_y))

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
    global punts

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem el polígon
    pygame.draw.polygon(screen, BLACK, punts, 5)

    pygame.display.update()

if __name__ == "__main__":
    main()