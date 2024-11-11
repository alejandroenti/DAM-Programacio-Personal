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

BUTTON_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici Paint')

# Variables globals
mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}
points = []
line_width = 1
buttons_width = [
    { "width": 1, "x": 25, "y": 390 },
    { "width": 2, "x": 50, "y": 390 },
    { "width": 3, "x": 25, "y": 415 },
    { "width": 4, "x": 50, "y": 415 },
    { "width": 5, "x": 25, "y": 440 },
    { "width": 6, "x": 50, "y": 440 },
]
selected_color = BLACK
buttons_color = []

padding = 20

surface = pygame.Surface((640, 480))

# Bucle de l'aplicació
def main():
    is_looping = True

    surface.fill(WHITE)
    init_color_buttons()

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
    global mouse, points, surface, buttons_width, line_width

    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

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
            # Pintem punts al la surface
            draw_points(points, surface)
            mouse["pressed"] = False

            # Revisem si ha clicat sobre algun del botons de canvi de gruix
            check_buttons_width_clicked()

            # Revisem si ha clicat sobre algun dels colors
            check_buttons_color_clicked()

    return True

# Fer càlculs
def app_run():
    global mouse, points

    if mouse["pressed"]:
        point = (mouse["x"], mouse["y"])
        points.append(point)
    else:
        points.clear()


# Dibuixar
def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Pintem la surface
    screen.blit(surface, (0,0))

    # Pintem els botons
    for button_width in buttons_width:
        draw_button_width(button_width)
    
    for button_color in buttons_color:
        draw_button_color(button_color)

    # Dibuixem quadre on es veu el color actual que hem seleccionat
    rect = (350, 390, padding * 2 + 10, padding * 3 + 10)
    pygame.draw.rect(screen, selected_color, rect)

    # Pintem punts al la pantalla
    draw_points(points, screen)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_points(points, surface):
    global line_width, selected_color

    if len(points) > 2:
        pygame.draw.lines(surface, selected_color, False, points, line_width)

def draw_button_width(button):
    global screen, padding

    color = YELLOW if line_width == button["width"] else GRAY

    rect = (button["x"], button["y"], padding, padding)

    start_pos = (button["x"] - 1, button["y"] + padding + 1)
    end_pos = (button["x"] + padding + 1, button["y"] - 1)

    pygame.draw.rect(screen, color, rect)
    pygame.draw.line(screen, BLACK, start_pos, end_pos, button["width"])

def draw_button_color(button):
    global screen, selected_color, padding

    color = button["color"]

    rect = (button["x"], button["y"], padding, padding)

    pygame.draw.rect(screen, color, rect)
    if button["color"] == WHITE:
        pygame.draw.rect(screen, BLACK, rect, 2)
    
    if button["color"] == selected_color:
        pygame.draw.rect(screen, WHITE, rect, 2)

def check_buttons_width_clicked():
    global mouse, buttons_width, line_width, padding

    for button_width in buttons_width:
        rect = {"x": button_width["x"], "y": button_width["y"], "width": padding, "height": padding}
        if utils.is_point_in_rect(mouse, rect):
            line_width = button_width["width"]
            break

def check_buttons_color_clicked():
    global mouse, buttons_color, selected_color, padding

    for button_color in buttons_color:
        rect = {"x": button_color["x"], "y": button_color["y"], "width": padding, "height": padding}
        if utils.is_point_in_rect(mouse, rect):
            selected_color = button_color["color"]
            break

def init_color_buttons():
    global buttons_color

    rows = 3
    columns = 10

    init_pos_x = 75
    init_pos_y = 390
    increment = 25

    pos_x = init_pos_x
    pos_y = init_pos_y
    
    lightness = [0.25, 0.5, 0.85]

    for index in range(rows):
        light = lightness[index]
        for hue in range(0, 360, int(360 / columns)):
            buttons_color.append({
                "color": utils.hsl_to_rgb(hue, 1.0, light),
                "x": pos_x,
                "y": pos_y
            })
            pos_x += increment
        
        pos_x = init_pos_x
        pos_y += increment
    
    buttons_color.append({ "color": BLACK, "x": 325, "y": 390 })
    buttons_color.append({ "color": (128, 128, 128), "x": 325, "y": 415 })
    buttons_color.append({ "color": WHITE, "x": 325, "y": 440 })


if __name__ == "__main__":
    main()