#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 70)

BUTTON_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici Sliders')

# Variables globals
font = pygame.font.SysFont("Arial", 24)

mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}

sliders = [
    { "value": 128, "x": 100, "y": 200, "width": 200, "height": 5, "dragging": False, "radius": 10 },
    { "value": 128, "x": 100, "y": 250, "width": 200, "height": 5, "dragging": False, "radius": 10 },
    { "value": 128, "x": 100, "y": 300, "width": 200, "height": 5, "dragging": False, "radius": 10 }
]

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
    global mouse

    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse["x"], mouse["y"] = event.pos
            else:
                mouse["x"] = -1
                mouse["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["pressed"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False

    return True

# Fer càlculs
def app_run():
    global mouse, sliders

    for slider in sliders:
        radi = slider["radius"]
        center_x = slider["x"] + (slider["value"] * slider["width"] / 255)
        center = { "x": center_x, "y": slider["y"] + int(slider["height"] / 2) }

        if mouse["pressed"]:
            # Només iniciar el dragging si cap altre slider està arrossegant-se
            if not any(s["dragging"] for s in sliders):  
                slider["dragging"] = utils.is_point_in_circle(mouse, center, radi)
        else:
            slider["dragging"] = False

        # Actualitzar el valor del slider mentre està en "dragging"
        if slider["dragging"]:
            relative_x = max(slider["x"], min(mouse["x"], slider["x"] + slider["width"]))
            slider["value"] = int((relative_x - slider["x"]) / slider["width"] * 255)
        

# Dibuixar
def app_draw():
    global sliders

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Pintem els sliders
    draw_sliders(sliders)

    # Pintrm el cuadre del color resultant
    draw_color()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_sliders(sliders):
    global screen, font

    for slider in sliders:
        rect = (slider["x"], slider["y"], slider["width"], slider["height"])

        radi = slider["radius"]
        center_x = slider["x"] + (slider["value"] * slider["width"] / 255)
        center = (center_x, slider["y"])

        padding = 10
        string_tuple_x = slider["x"] + slider["width"] + padding
        string_tuple_y = slider["y"] - slider["height"] - padding / 2
        string_tuple = (string_tuple_x, string_tuple_y)
        string_surface = font.render(str(slider["value"]), True, BLACK)
        
        pygame.draw.rect(screen, GRAY, rect)
        pygame.draw.circle(screen, BLACK, center, radi)
        screen.blit(string_surface, string_tuple)

def draw_color():
    global screen, sliders

    rect_tuple = (400, 200, 200, 100)
    color = [sliders[0]["value"], sliders[1]["value"], sliders[2]["value"]]

    pygame.draw.rect(screen, color, rect_tuple)

if __name__ == "__main__":
    main()