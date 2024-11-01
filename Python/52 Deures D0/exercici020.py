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

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 20')

# Definim les variables globals
board = {
    "position": { 
        "x": 50, 
        "y": 50 
    },
    "size": { 
        "rows": 15, 
        "cols": 10 
    },
    "cell_size": 25
}

mouse_pos = {"x": -1, "y": -1}

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

    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global board, mouse_pos
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixem el taulell
    draw_board(board)
    cell = cell_from_point(mouse_pos, board)
    print(mouse_pos, cell)

    if cell[0] != -1:
        pos = point_from_cell(cell, board)
        pygame.draw.rect(screen, BLUE, (pos[0], pos[1], board["cell_size"], board["cell_size"]))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

# Inicialitzem un taulell
def draw_board(board):
    global screen 

    pos_x = board["position"]["x"]
    pos_y = board["position"]["y"]

    for row in range(board["size"]["rows"]):
        for column in range(board["size"]["cols"]):
            pygame.draw.rect(screen, BLACK, (pos_x, pos_y, board["cell_size"], board["cell_size"]), 1)
            pos_x += board["cell_size"]
        pos_x = board["position"]["x"]
        pos_y += board["cell_size"]

# Identifiquem si el Mouse es troba sobre una cel·la
def cell_from_point(point, board):
    posicio = (point["x"] - board["position"]["x"], point["y"] - board["position"]["y"])
    cell_x = int(posicio[0] / board["cell_size"])
    cell_y = int(posicio[1] / board["cell_size"])

    if cell_x >= board["size"]["cols"] or cell_y >= board["size"]["rows"] or cell_x < 0 or cell_y < 0:
        cell_x = -1
        cell_y = -1

    return (cell_x, cell_y)

# Retornem la posició d'una cel·la en pantalla
def point_from_cell(cell, board):
    pos_x = cell[0] * board["cell_size"] + board["position"]["x"]
    pos_y = cell[1] * board["cell_size"] + board["position"]["y"]

    return (pos_x, pos_y)

if __name__ == "__main__":
    main()
