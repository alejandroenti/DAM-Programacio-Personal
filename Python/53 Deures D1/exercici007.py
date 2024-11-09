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
pygame.display.set_caption('Alejandro López - Exercici 7')


# Variables globals
font14 = pygame.font.SysFont("Arial", 14)
font22 = pygame.font.SysFont("Arial", 22)
font50 = pygame.font.SysFont("Arial", 50)

mouse_data = { "x": -1, "y": -1, "pressed": False, "released": False }
buttons = [
    { "text": "-", "value": "sub", "x": 25, "y": 25, "width": 50, "height": 25, "pressed": False },
    { "text": "+", "value": "add", "x": 75, "y": 25, "width": 50, "height": 25, "pressed": False },
]

counter = 0

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
    global buttons, counter, mouse_data

    if mouse_data["pressed"]:
        for button in buttons:
            if utils.is_point_in_rect(mouse_data, button):
                button["pressed"] = True
    
    elif mouse_data["released"]:
        for button in buttons:
            if button["pressed"]:
                if button["value"] == "add":
                    counter += 1
                elif button["value"] == "sub":
                    counter -= 1
                button["pressed"] = False
   
# Dibuixar
def app_draw():
    global pos_x, pos_y, counter, font50, font14, mouse_data

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Draw buttons
    for button in buttons:
        draw_button(button)

    # Draw 'mouse pressed' text
    if mouse_data["pressed"]:
        position_x = 135
        position_y = 38

        string_surface = font14.render(f"Mouse Pressed", False, BLACK)
        string_rect = string_surface.get_rect()
        string_rect.left = position_x
        string_rect.centery = position_y

        screen.blit(string_surface, string_rect)

    # Dibuixa el comptador
    position_x = screen.get_width() / 2
    position_y = screen.get_height() / 2

    string_surface = font50.render(f"{counter}", False, BLACK)
    string_rect = string_surface.get_rect()
    string_rect.centerx = position_x
    string_rect.centery = position_y

    screen.blit(string_surface, string_rect)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_button(button):
    global font22, screen

    rect = (button["x"], button["y"], button["width"], button["height"])

    string_surface = font22.render(str(button["text"]), False, BLACK)
    string_rect = string_surface.get_rect()
    string_rect.centerx = button["x"] + button["width"] / 2
    string_rect.centery = button["y"] + button["height"] / 2

    if button["pressed"]:
        pygame.draw.rect(screen, ORANGE, rect)

    pygame.draw.rect(screen, BLACK, rect, 3)
    screen.blit(string_surface, string_rect)

if __name__ == "__main__":
    main()