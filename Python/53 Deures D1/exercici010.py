#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import random
import utils

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Define window size
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption('Window Title')

# Variables globals
font14 = pygame.font.SysFont("Arial", 14)
font12 = pygame.font.SysFont("Arial", 12)

window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}

mouse_pos = {'x': 300, 'y': 250 }

level = 1  # Level
snake = {
    "queue": [],
    "speed": 50,
    "radius": 7,
    "status": "follow_mouse", # "follow_mouse" or "orbit_mouse"
    "direction_angle": 0
}

piece = { # (food)
    "x": -1, 
    "y": -1, 
    "value": 0,
    "radius": 7
}  

# Bucle de l'aplicació
def main():
    is_looping = True

    init_game()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global mouse_pos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window button
            return False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos['x'], mouse_pos['y'] = event.pos
    return True

# Fer càlculs
def app_run():
    set_window_size()
    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    move_snake(delta_time)

# Dibuixar
def app_draw():
    screen.fill(WHITE)

    draw_board()
    draw_piece()
    draw_snake()
    pygame.display.update()

# Estableix les mides de la finestra
def set_window_size():
    global window_size

    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

# Iniciar la serp
def init_game():
    global snake

    # Genera la primera peça 
    # (necessita tenir les mides de la finestra)
    set_window_size()
    pass

def generate_piece():
    pass

def extend_snake():
    pass

def move_snake(delta_time):
    pass

def get_next_snake_pos(delta_time):
    pass

def draw_board():
    pass

def draw_snake():
    pass

def draw_piece():
    pass

if __name__ == "__main__":
    main()
