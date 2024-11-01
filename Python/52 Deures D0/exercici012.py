import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from assets.svgmoji.emojis import get_emoji

# DEFINIM CONSTANTS
CELL_SIZE = 50
BOARD_ROWS = 8
BOARD_COLS = 10

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  
LIGHT_BLUE = (173, 216, 230)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejnadro Lopez - Exercici 12')

# Definim les variables globals
tauler = []

img_tree = get_emoji(pygame, "🌲", size=CELL_SIZE)
img_sman = get_emoji(pygame, "☃️", size=CELL_SIZE)
img_snow = get_emoji(pygame, "❄️", size=CELL_SIZE)
img_skater = get_emoji(pygame, "🏂", size=CELL_SIZE)

pos_skater = { "row": 0, "column": 0}

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
    global pos_skater

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYUP:  # Tecla alliberada
            new_row = pos_skater["row"]
            new_col = pos_skater["column"]
            if event.key == pygame.K_UP:
                new_row -= 1
            elif event.key == pygame.K_DOWN:
                new_row += 1
            elif event.key == pygame.K_LEFT:
                new_col -= 1
            elif event.key == pygame.K_RIGHT:
                new_col += 1

            if is_skiable_cell(new_row, new_col):
                pos_skater["row"] = new_row
                pos_skater["column"] = new_col

    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global tauler, img_skater, img_tree, img_sman, img_snow

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem el fons del tauler
    pygame.draw.rect(screen, LIGHT_BLUE, (50, 50, CELL_SIZE * BOARD_COLS, CELL_SIZE * BOARD_ROWS))

    # Dibuixem l'escenari
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLS):
            if tauler[row][column] != "":
                pos = (column * CELL_SIZE + CELL_SIZE, row * CELL_SIZE + CELL_SIZE)
                if tauler[row][column] == "T":
                    img = img_tree
                elif tauler[row][column] == "M":
                    img = img_sman
                else:
                    img = img_snow
                screen.blit(img, pos)
    
    # Dibuixem l'skater
    pos = (pos_skater["column"] * CELL_SIZE + CELL_SIZE, pos_skater["row"] * CELL_SIZE + CELL_SIZE)
    screen.blit(img_skater, pos)

    pygame.display.update()

# Inicialitzem el tauller
def init_board():
    global tauler

    tauler = [["" for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    place_random_letters("T", 9)
    place_random_letters("S", 3)
    place_random_letters("M", 3)

def place_random_letters(letter, count):
    global tauler

    posades = 0

    while posades < count:
        fila = random.randint(0, BOARD_ROWS - 1)
        columna = random.randint(0, BOARD_COLS - 1)

        if fila == 0 and columna == 0:
            continue
        if tauler[fila][columna] != "":
            continue

        tauler[fila][columna] = letter
        posades += 1

def is_skiable_cell(row, col):
    global tauler

    if row < 0 or col < 0 or row >= BOARD_ROWS or col >= BOARD_COLS:
        return False

    return tauler[row][col] == "" or tauler[row][col] == "S"

if __name__ == "__main__":
    main()
