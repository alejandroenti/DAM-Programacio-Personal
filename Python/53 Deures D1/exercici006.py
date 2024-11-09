#!/usr/bin/env python3

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
BLUE  = (100, 200, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption('Alejandro López - Exercici 6')


# Variables globals
window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}

BOARD_SIZE = (12, 8)
CELL_SIZE = 50
mouse_pos = { "x": -1, "y": -1 }

img_ship = get_emoji(pygame, "🚢", size=CELL_SIZE)
img_drop = get_emoji(pygame, "🌊", size=CELL_SIZE)
img_bomb = get_emoji(pygame, "💥", size=CELL_SIZE)

board_pos = { "x": -1, "y": -1 }
board = []

cell_size = 50

# Bucle de l'aplicació
def main():
    is_looping = True

    init_board()

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
    global mouse_pos, board, board_pos

    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for row in range(len(board)):
                for column in range(len(board[row])):
                    cell_x = board_pos["x"] + column * CELL_SIZE
                    cell_y = board_pos["y"] + row * CELL_SIZE

                    rect = { "x": cell_x, "y": cell_y, "width": cell_size, "height": cell_size }

                    if utils.is_point_in_rect(mouse_pos, rect):
                        board[row][column] = "B" if board[row][column] == "S" else "W"
                        break
    return True

# Fer càlculs
def app_run():
    global window_size
    
    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

    board_pos["x"] = window_size["center"]["x"] - int(len(board[0]) * CELL_SIZE / 2)
    board_pos["y"] = window_size["center"]["y"] - int(len(board) * CELL_SIZE / 2)

# Dibuixar
def app_draw():
    global pos_x, pos_y

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Draw board
    draw_board()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def place_ship(x, y, length, direction):
    global board

    for i in range(length):
        if direction == "Vertical":
            board[y + i][x] = "S"
        else:
            board[y][x + i] = "S"

def is_valid_position(x, y, length, direction):
    global board

    if direction == "Vertical":
        for i in range(length):
            if x == len(board[y]) - 1:
                if board[y + i][x - 1] != "" or board[y + i][x] != "":
                    return False
            elif x == 0:
                if board[y + i][x + 1] != "" or board[y + i][x] != "":
                    return False
            else:
                if board[y + i][x - 1] != "" or board[y + i][x] != "" or board[y + i][x + 1] != "":
                    return False
    else:
         for i in range(length):
            if y == len(board) - 1:
                if board[y - 1][x + i] != "" or board[y][x + i] != "":
                    return False
            elif y == 0:
                if board[y + 1][x + i] != "" or board[y][x + i] != "":
                    return False
            else:
                if board[y - 1][x + i] != "" or board[y][x + i] != "" or board[y + 1][x + i] != "":
                    return False

    return True

def init_board():
    global board

    board = [["" for _ in range(12)] for _ in range(8)]

    # 3 Vaixells verticals
    pos_x = random.randint(0, 11)
    pos_y = random.randint(0, 5)
    if is_valid_position(pos_x, pos_y, 3, "Vertical"):
        place_ship(pos_x, pos_y, 3, "Vertical")
    
    # 3 Veixells horizontals
    posicio_valida = False

    while not posicio_valida:
        pos_x = random.randint(0, 9)
        pos_y = random.randint(0, 7)

        if is_valid_position(pos_x, pos_y, 3, "Horizontal"):
            place_ship(pos_x, pos_y, 3, "Horizontal")
            posicio_valida = True
    
    # 4 vaixells horizontals
    posicio_valida = False

    while not posicio_valida:
        pos_x = random.randint(0, 9)
        pos_y = random.randint(0, 7)

        if is_valid_position(pos_x, pos_y, 4, "Horizontal"):
            place_ship(pos_x, pos_y, 4, "Horizontal")
            posicio_valida = True

def draw_board():    
    global board, board_pos, cell_size, screen, img_ship, img_drop, img_bomb

    for row in range(len(board)):
        for column in range(len(board[row])):
            cell_x = board_pos["x"] + column * CELL_SIZE
            cell_y = board_pos["y"] + row * CELL_SIZE

            rect = (cell_x, cell_y, cell_size, cell_size)

            pygame.draw.rect(screen, BLUE, rect)

            if board[row][column] == "S":
                screen.blit(img_ship, (cell_x, cell_y))
            elif board[row][column] == "W":
                screen.blit(img_drop, (cell_x, cell_y))
            elif board[row][column] == "B":
                screen.blit(img_ship, (cell_x, cell_y))
                screen.blit(img_bomb, (cell_x, cell_y))


if __name__ == "__main__":
    main()