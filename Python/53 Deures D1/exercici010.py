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
pygame.display.set_caption('Alejandro López - Exercici 10')

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
    
    generate_piece()

    for _ in range(5):
        extend_snake()

def generate_piece():
    global piece, window_size

    padding = 100

    piece["x"] = random.randint(padding, window_size["width"] - padding)
    piece["y"] = random.randint(padding, window_size["height"] - padding)
    piece["value"] = random.randint(1, 5)

def extend_snake():
    global snake, window_size

    if len(snake["queue"]) == 0:
        snake["queue"].append({ "x": window_size["width"] / 2, "y": window_size["height"] / 2 })
        return
    
    last_pos = len(snake["queue"]) - 1

    snake["queue"].append({
        "x": snake["queue"][last_pos]['x'], 
        "y": snake["queue"][last_pos]['y']
    })

def move_snake(delta_time):
    global snake, level

    hit = utils.is_point_in_circle(snake["queue"][0], piece, piece["radius"])
    if hit:
        level += 1
        snake["speed"] = min(200, snake["speed"] * 1.05)
        for _ in range(piece['value']):
            extend_snake()             
        generate_piece()

    next_pos = get_next_snake_pos(delta_time)
    snake["queue"].insert(0, next_pos)

    snake["queue"].pop()

def get_next_snake_pos(delta_time):
    global snake

    # Calcula la diferència en les coordenades entre el cap de la serp i el ratolí
    delta_x = mouse_pos['x'] - snake["queue"][0]['x']
    delta_y = mouse_pos['y'] - snake["queue"][0]['y']
   
    # Calcula la distància entre el cap de la serp i la posició del ratolí
    distancia = math.hypot(delta_x, delta_y)

    # Determina l'estat de la serp segons la distància al ratolí
    if distancia < 5:
        snake["status"] = 'orbit_mouse'  # Estat per orbitar prop del ratolí
    if distancia > 50:
        snake["status"] = 'follow_mouse'  # Estat per seguir el ratolí

    # Si la serp està en estat d'òrbita, 
    # augmenta l'angle de direcció per fer-la girar
    if snake["status"] == 'orbit_mouse':
        snake["direction_angle"] += distancia * math.pi / 1000
    else:
        # Calcula el pendent per obtenir l'angle; 
        # si delta_x és 0, s'estableix a infinit per evitar divisió per zero
        if delta_x != 0:
            pendent = delta_y / delta_x
        else:
            pendent = float('inf')

        # Calcula l'angle de direcció de la serp per seguir el ratolí
        if delta_x == 0 and mouse_pos['y'] < snake["queue"][0]['y']:
            # Angle per anar amunt (270 graus)
            snake["direction_angle"] = (3 * math.pi) / 2
        elif delta_x == 0 and mouse_pos['y'] >= snake["queue"][0]['y']:
            # Angle per anar avall (90 graus)
            snake["direction_angle"] = math.pi / 2
        elif mouse_pos['x'] > snake["queue"][0]['x']:
            # Angle per anar cap a la dreta 
            snake["direction_angle"] = math.atan(pendent)
        else:
            # Angle per anar cap a l'esquerra (180 graus)
            snake["direction_angle"] = math.atan(pendent) + math.pi

    return {
        "x": snake["queue"][0]['x'] + snake["speed"] * delta_time * math.cos(snake["direction_angle"]), 
        "y": snake["queue"][0]['y'] + snake["speed"] * delta_time * math.sin(snake["direction_angle"])
    }

def draw_board():
    global screen, snake, level, font14

    level_surface = font14.render(f"Level: {level}", True, BLACK)
    length_surface = font14.render(f"Length: {len(snake['queue'])}", True, BLACK)
    speed_surface = font14.render(f"Speed: {snake['speed']:.2f}", True, BLACK)

    level_rect = level_surface.get_rect()
    length_rect = length_surface.get_rect()
    speed_rect = speed_surface.get_rect()

    level_rect.left = 15
    length_rect.left = 15
    speed_rect.left = 15

    level_rect.centery = 25
    length_rect.centery = 50
    speed_rect.centery = 75

    screen.blit(level_surface, level_rect)
    screen.blit(length_surface, length_rect)
    screen.blit(speed_surface, speed_rect)

def draw_snake():
    global screen, snake

    for index in reversed(range(len(snake["queue"]))):
        cercle = snake["queue"][index]
        if len(snake["queue"]) > 1:
            lightness = int((index * 225) / (len(snake["queue"]) - 1))
        else:
            lightness = 0
        color = (lightness, lightness, lightness)
        pygame.draw.circle(screen, color, (int(cercle['x']), int(cercle['y'])), snake["radius"])

def draw_piece():
    global screen, piece, font12

    position = (piece["x"], piece["y"])
    pygame.draw.circle(screen, RED, position, piece["radius"])

    value_surface = font12.render(str(piece["value"]), True, BLACK)
    value_rect = value_surface.get_rect()

    value_rect.centerx = piece["x"]
    value_rect.centery = piece["y"]

    screen.blit(value_surface, value_rect)

if __name__ == "__main__":
    main()
