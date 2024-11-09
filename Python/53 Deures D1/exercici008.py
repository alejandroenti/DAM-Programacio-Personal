#!/usr/bin/env python3

import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from assets.svgmoji.emojis import get_emoji

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (100, 200, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici 8')


# Variables globals
font = pygame.font.SysFont("Arial", 14)

mouse_data = { "x": -1, "y": -1, "pressed": False, "released": False }
buttons = [
    { "value": "up",   "x": 25, "y": 25, "width": 25, "height": 25, "pressed": False },
    { "value": "down", "x": 25, "y": 50, "width": 25, "height": 25, "pressed": False },
]

circle = {
    "x": 525,
    "y": 250,
    "radius": 25,
    "color": BLUE
}

direction = "up"

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
    global mouse_data
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_data["x"] = event.pos[0]
                mouse_data["y"] = event.pos[1]
            else:
                mouse_data["x"] = -1
                mouse_data["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_data["pressed"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_data["pressed"] = False
            mouse_data["released"] = True

    return True

# Fer càlculs
def app_run():
    global buttons, direction, circle

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    speed = 100

    if mouse_data["pressed"]:
        for button in buttons:
            if utils.is_point_in_rect(mouse_data, button):
                button["pressed"] = True
    
    elif mouse_data["released"]:
        for button in buttons:
            if button["pressed"]:
                direction = button["value"]
                button["pressed"] = False
    
    if direction == "up":
        displacement = max(circle["radius"], circle["y"] - (speed * delta_time))
    elif direction == "down":
        displacement = min(screen.get_height() - circle["radius"], circle["y"] + (speed * delta_time))

    circle["y"] = displacement

# Dibuixar
def app_draw():
    global mouse_data, buttons, font

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Draw buttons
    for button in buttons:
        draw_button(button)

    # Draw circle
    center = (circle["x"], circle["y"])
    pygame.draw.circle(screen, circle["color"], center, circle["radius"])

    # Draw 'mouse pressed' text
    if mouse_data["pressed"]:
        position_x = 55
        position_y = 38

        string_surface = font.render(f"Mouse Pressed", False, BLACK)
        string_rect = string_surface.get_rect()
        string_rect.left = position_x
        string_rect.centery = position_y

        screen.blit(string_surface, string_rect)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_button(button):
    global direction

    rect = (button["x"], button["y"], button["width"], button["height"])

    if button["pressed"] and direction != button["value"]:
        pygame.draw.rect(screen, ORANGE, rect)
    elif direction == button["value"]:
        pygame.draw.rect(screen, BLUE, rect)

    pygame.draw.rect(screen, BLACK, rect, 3)

if __name__ == "__main__":
    main()