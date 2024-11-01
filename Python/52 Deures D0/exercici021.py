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
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 21')

# Definim les variables globals
mouse_pos = { "x": -1, "y": -1 }
mouse_down = False
taulell = []
cell_size = 25
rows = 10
cols = 15
num_selected = -1
start_position = (50, 50)

font = pygame.font.SysFont("Arial", 16)

# Bucle de l'aplicació
def main():
    is_looping = True

    init_board()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global mouse_pos, mouse_down
    
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    return True

# Fer càlculs
def app_run():
    global mouse_pos, mouse_down, taulell, num_selected

    cell = cell_from_point()

    if cell[0] != -1 and taulell[cell[1]][cell[0]] != None:
        if not mouse_down:
            num_selected = taulell[cell[1]][cell[0]]
        else:
            num_selected = taulell[cell[1]][cell[0]]
            for row in range(rows):
                for column in range(cols):
                    if taulell[row][column] == num_selected:
                        taulell[row][column] = None
            num_selected = -1
    else:
        num_selected = -1

# Dibuixar
def app_draw():
    global taulell, cell_size

    screen.fill(WHITE)

    # Dibuixem el taullel
    draw_board(taulell, cell_size)

    pygame.display.update()

# Inicialitzem el taullel
def init_board():
    global taulell, rows, cols

    for _ in range(rows):
        row_board = []
        for _ in range(cols):
            row_board.append(random.randint(0, 9))
        taulell.append(row_board)

# Dibuixem el taullel:
def draw_board(taulell, cell_size):
    global font, start_position, num_selected

    pos_x, pos_y = start_position

    for row in range(len(taulell)):
        for column in range(len(taulell[row])):
            pygame.draw.rect(screen, BLACK, (pos_x, pos_y, cell_size, cell_size), 2)

            if taulell[row][column] == num_selected:
                pygame.draw.rect(screen, ORANGE, (pos_x, pos_y, cell_size, cell_size))

            if taulell[row][column] != None:
                text = font.render(f"{taulell[row][column]}", True, BLACK)
                text_position = [pos_x + (cell_size / 3), pos_y + (cell_size / 8)]
                screen.blit(text, text_position)
            pos_x += cell_size
        pos_x = start_position[0]
        pos_y += cell_size

# Identifiquem si el Mouse es troba sobre una cel·la
def cell_from_point():
    global mouse_pos, cell_size, rows, cols

    posicio = (mouse_pos["x"] - 50, mouse_pos["y"] - 50)
    cell_x = int(posicio[0] / cell_size)
    cell_y = int(posicio[1] / cell_size)

    if cell_x >= cols or cell_y >= rows or cell_x < 0 or cell_y < 0:
        cell_x = -1
        cell_y = -1

    return (cell_x, cell_y)

if __name__ == "__main__":
    main()
