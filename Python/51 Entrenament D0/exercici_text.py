#!/usr/bin/env python3

import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici Text')

font = pygame.font.SysFont("Arial", 22)
mouse = { "x": -1, "y": -1, "pressed": False }

# Definir el quadre d'entrada
input_box = {
    "x": 100,
    "y": 200,
    "width": 200,
    "height": 32,
    "text": "",
    "focused": False
}

cursor = {
    "visible": True,
    "timer": 0,
    "position": 0,
    "blink_speed": 0.5
}

def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global mouse, input_box

    rect_input_box = (input_box["x"], input_box["y"], input_box["width"], input_box["height"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # TODO: Recuperar la posició del mouse i si fem clic canviar atribut 'focused'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["x"], mouse["y"] = event.pos
            if utils.is_point_in_rect(mouse, input_box):
                input_box["focused"] = True
            else:
                input_box["focused"] = False
        # TODO: Detectar input del teclat i afegir a la variable 'text'
        elif event.type == pygame.KEYDOWN and input_box["focused"]:
            if event.key == pygame.K_BACKSPACE:
                input_box["text"] = input_box["text"][0:-1]
                cursor["position"] = max(0, cursor["position"] - 1)
            elif event.unicode.isprintable() and event.unicode not in "`´^¨~":
                input_box["text"] += event.unicode
                cursor["position"] += 1
    return True

def app_run():
    global cursor

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    # TODO: Controlar el blink del cursor
    if input_box["focused"]:
        cursor["timer"] = cursor["timer"] + delta_time
        if cursor["timer"] >= cursor["blink_speed"]:
            cursor["visible"] = not cursor["visible"]
            cursor["timer"] = 0
    else:
        cursor["timer"] = 0
        cursor["visible"] = False

def app_draw():
    global input_box, font

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # TODO: Dibuix del quadre de text
    rect_tuple = (input_box["x"], input_box["y"], input_box["width"], input_box["height"])
    color = BLUE if input_box["focused"] else GRAY

    pygame.draw.rect(screen, WHITE, rect_tuple)
    pygame.draw.rect(screen, color, rect_tuple, 2)
    
    # TODO: Dibuix del text dins del quadre de text
    string_tuple = (input_box["x"] + 5, input_box["y"] + 5)
    string_surface = font.render(input_box["text"], True, BLACK)
    screen.blit(string_surface, string_tuple)
    
    # TODO: Dibuix del cursor (intermitent)
    text_width = font.size(input_box["text"])[0]
    padding = 5
    cursor_x = input_box["x"] + text_width + padding
    start_pos = (cursor_x, input_box["y"] + padding)
    end_pos = (cursor_x, input_box["y"] + input_box["height"] - padding)
    if cursor["visible"]:
        pygame.draw.line(screen, BLACK, start_pos, end_pos, 2)

    pygame.display.update()

if __name__ == "__main__":
    main()
