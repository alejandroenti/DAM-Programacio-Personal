import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
BROWN = (165, 42, 42)  
YELLOW = (255, 255, 0)  
GREEN = (0, 255, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 19')

# Definim les variables globals
moves_house = [{"direction": "right", "distance": 250}, {"direction": "up", "distance": 200}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 200}]
moves_sun = [{"direction": "right", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "left", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 25}, {"direction": "left", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "left", "distance": 25} ]
moves_car = [{"direction": "up", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 50} ]
moves_grass = [{"direction": "right", "distance": 650}, {"direction": "down", "distance": 100}, {"direction": "left", "distance": 650}]

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
    pass

# Dibuixar
def app_draw():
    global moves_house, moves_sun, moves_grass, moves_car

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem les figures segons les instruccions
    draw_moves(BROWN, (350, 400), moves_house)
    draw_moves(YELLOW, (50, 100), moves_sun)
    draw_moves(BLUE, (100, 400), moves_car)
    draw_moves(GREEN, (0, 400), moves_grass)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_moves(color, start_pos, moves):
    # Dibuixa un poligon segons les instruccions rebudes a la llista 'moves'
    # Les instruccions són una direcció (up, down, left, right) i una distància
    global screen

    posicions = [start_pos]
    pos_x, pos_y = start_pos

    for move in moves:
        if move["direction"] == "up":
            pos_y -= move["distance"]
        elif move["direction"] == "down":
            pos_y += move["distance"]
        elif move["direction"] == "left":
            pos_x -= move["distance"]
        elif move["direction"] == "right":
            pos_x += move["distance"]
        
        posicions.append((pos_x, pos_y))
    
    pygame.draw.polygon(screen, color, posicions)

if __name__ == "__main__":
    main()