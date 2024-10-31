import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)
colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 7')

# Definim les variables globals
colors = [(127, 184, 68), (240, 187, 64), (226, 137, 50), (202, 73, 65), (135, 65, 152), (75, 154, 217)]
mida_cuadrat = 50
radi = 25
inici_cuadrat_y = 50
inici_cercle_y = 175
posicio_triangle = [75, 275]
posicio_pentagon = [75, 375]

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
    global colors, inici_cuadrat_y, inici_cercle_y, mida_cuadrat, radi, posicio_triangle, posicio_pentagon
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem la primera fila de rectangles
    for index, pos_x in enumerate(range(50, 551, 100)):
        pygame.draw.rect(screen, colors[index], (pos_x, inici_cuadrat_y, mida_cuadrat, mida_cuadrat))
    
    # Dibuixem la línia de cercles
    for index, pos_x in enumerate(range(75, 576, 100)):
        pygame.draw.circle(screen, colors[index], (pos_x, inici_cercle_y), radi, 2)
    
    # Dibuixem la línia de triangles
    for color in range(0, 126, 25):
        draw_polygon(screen, (color, color, color), posicio_triangle, radi, 3)
        posicio_triangle[0] += 100
    posicio_triangle = [75, 275]

    # Dibuixem la línia de pentàgons
    for color in range(0, 126, 25):
        draw_polygon(screen, (color, color, color), posicio_pentagon, radi, 5)
        posicio_pentagon[0] += 100
    posicio_pentagon = [75, 375]

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
    points = [
        (
            center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
            center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
        )
        for i in range(num_vertices)
    ]
    pygame.draw.polygon(screen, color, points)

if __name__ == "__main__":
    main()