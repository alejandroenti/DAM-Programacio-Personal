#!/usr/bin/env python3

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
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici 1')

# Variables globals
window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}

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
    global window_size

    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

# Dibuixar
def app_draw():
    global window_size

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    for q in range(20, 0, -1):
        perspective = (q / 20)

        q_ample = q * 25 * perspective
        q_alt = q * 20 * perspective

        x = window_size["center"]["x"] - int(q_ample / 2)
        y = window_size["center"]["y"] - int(q_alt / 2)

        color = (0, 0, q * 10) if q % 2 == 0 else (0, q * 10, 0)
        rect = (x, y, q_ample, q_alt)

        pygame.draw.rect(screen, color, rect)
        
    pygame.display.update()

if __name__ == "__main__":
    main()