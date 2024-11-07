#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BUTTON_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici Scroll')

# Variables globals
font = pygame.font.SysFont("Arial", 24)

mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}

scroll = {
    "percentage": 0,
    "dragging": False,
    "x": 400,
    "y": 100,
    "width": 5,
    "height": 200,
    "radius": 10,
    "surface_offset": 0,
    "visible_height": 200
}

# TODO: Superficie de 320x500
surface = pygame.Surface((320, 540))  
surface.fill(GRAY) # Fons gris

# Bucle de l'aplicació
def main():
    is_looping = True

    # TODO: Fer un dibuix a la surface 
    # (fons gris dues linies en forma de creucreu)

    # Dibuixem les línies
    start_pos_red = (0, 0)
    start_pos_green = (320, 0)
    end_pos_red = (320, 540)
    end_pos_green = (0, 540)

    pygame.draw.line(surface, RED, start_pos_red, end_pos_red, 5)
    pygame.draw.line(surface, GREEN, start_pos_green, end_pos_green, 5)

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
    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse["x"], mouse["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["pressed"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
    return True

# Fer càlculs
def app_run():
    global scroll, mouse

    radi = scroll["radius"]
    center = {
        "x": int(scroll["x"] + scroll["width"] / 2),
        "y": int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"])
    }

    # TODO: Comprovar si el mouse ha fet click dins del cercle i iniciar l'arrossegament
    # definir scroll["dragging"]
    # si s'està arrossegant, atualitzar la posició del cercle
    # aturar l'arrosegament quan s'aixeca el botó del mouse
    if mouse["pressed"] and not scroll["dragging"] and utils.is_point_in_circle(mouse, center, radi):
        scroll["dragging"] = True

    if not mouse["pressed"]:
        scroll["dragging"] = False

    if scroll["dragging"]:
        relative_y = max(min(mouse["y"], scroll["y"] + scroll["height"]), scroll["y"])
        scroll["percentage"] = ((relative_y - scroll["y"]) / scroll["height"]) * 100

    # TODO: Calcular la posició "y" de dibuix de la superfície
    # scroll["surface_offset"] = int((scroll["percentage"] / 100) * (surface.get_height() - scroll["visible_height"]))
    scroll["surface_offset"] = int((scroll["percentage"] / 100) * (surface.get_height() - scroll["visible_height"]))

# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem la surface
    #surface_tuple = (50, 100)
    #screen.blit(surface, surface_tuple)

    # TODO: Dibuixar la subimatge desplaçada de la surface    
    # sub_surface = surface.subsurface((0, scroll["surface_offset"], surface.get_width(), scroll["visible_height"]))
    # screen.blit(sub_surface, (50, 100))

    # Dibuixar la subimatge desplaçada de la surface    
    sub_surface = surface.subsurface((0, scroll["surface_offset"], surface.get_width(), scroll["visible_height"]))
    screen.blit(sub_surface, (50, 100))

    # Dibuixar l'scroll
    draw_scroll()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()


def draw_scroll():
    global screen, scroll

    rect = (scroll["x"], scroll["y"], scroll["width"], scroll["height"])

    center = (scroll["x"] + scroll["width"] / 2, int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"]))
    radius = scroll["radius"]

    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.circle(screen, BLACK, center, radius)

if __name__ == "__main__":
    main()

