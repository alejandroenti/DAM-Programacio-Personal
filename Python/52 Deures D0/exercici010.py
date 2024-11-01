import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
GOLD = (255, 215, 0)
NAVY = (0, 0, 128)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 10')

# Definim les variables globals
rectangles = [
    { "rect": pygame.Rect(50, 100, 250, 50), "color": RED, "mouse_over": False },
    { "rect": pygame.Rect(50, 200, 100, 200), "color": GOLD, "mouse_over": False },
    { "rect": pygame.Rect(200, 200, 100, 100), "color": BLUE, "mouse_over": False },
    { "rect": pygame.Rect(200, 350, 400, 50), "color": PURPLE, "mouse_over": False },
    { "rect": pygame.Rect(350, 100, 50, 200), "color": ORANGE, "mouse_over": False },
    { "rect": pygame.Rect(450, 100, 150, 100), "color": GREEN, "mouse_over": False },
    { "rect": pygame.Rect(450, 250, 150, 50), "color": NAVY, "mouse_over": False }
]

mouse_pos = { "x": -1, "y": -1 }

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"], mouse_pos["y"] = event.pos
    return True

# Fer càlculs
def app_run():
    global mouse_pos, rectangles

    # Recorrem els rectangles y revisem si el Mouse es troba en algun d'ells.
    # Canviem flag mouse_over a True

    for rectangle in rectangles:
        if rectangle["rect"].collidepoint(mouse_pos["x"], mouse_pos["y"]):
            rectangle["mouse_over"] = True
        else:
            rectangle["mouse_over"] = False

# Dibuixar
def app_draw():
    global rectangles

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Recorrem els rectangles y si tenen la flag mouse_over a True, fem un altre rectangle amb el color corresponent
    for rectangle in rectangles:
        if rectangle["mouse_over"]:
            pygame.draw.rect(screen, rectangle["color"], rectangle["rect"])
        
        pygame.draw.rect(screen, BLACK, rectangle["rect"], 5)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()