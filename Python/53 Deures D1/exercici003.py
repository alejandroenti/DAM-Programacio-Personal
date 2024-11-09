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
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (50, 150, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption('Alejandro López - Exercici 3')
# Variables globals
window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}
mouse_pos = { "x": -1, "y": -1 }

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
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
    global mouse_pos

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    # Definir mida rectangle exterior
    ext_rect = (
        50, 50,  window_size["width"] - 100, window_size["height"] - 100
    )


    # Dibuixar limits
    pygame.draw.rect(screen, BLACK, ext_rect, 4)

    # Linia vertical
    start_pos = (window_size["width"] / 2, 0)
    end_pos = (window_size["width"] / 2, window_size["height"])

    pygame.draw.line(screen, BLACK, start_pos, end_pos, 4)

    # Linia horitzontal
    start_pos = (0, window_size["height"] / 2)
    end_pos = (window_size["width"], window_size["height"] / 2)

    pygame.draw.line(screen, BLACK, start_pos, end_pos, 4)

    # Dibuixar quadre
    size = 40
    rect = (mouse_pos["x"] - size / 2, mouse_pos["y"] - size / 2, size, size)
    color = get_color()

    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 3)

    pygame.display.update()

def get_color():
    global mouse_pos

    rect = {"x": 50, "y": 50,  "width": window_size["width"] - 100, "height": window_size["height"] - 100}
    if utils.is_point_in_rect(mouse_pos, rect):
        if mouse_pos["x"] < window_size["width"] / 2:
            return RED if mouse_pos["y"] < window_size["height"] / 2 else GREEN
        else:
            return BLUE if mouse_pos["y"] < window_size["height"] / 2 else YELLOW
    else:
        return BLACK

if __name__ == "__main__":
    main()