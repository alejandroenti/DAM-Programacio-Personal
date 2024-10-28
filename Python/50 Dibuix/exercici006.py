import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((720, 560))
pygame.display.set_caption('Window Title')

# Variables de l'estat del ratolí
mouse_pos = { "x": -1, "y": -1 }
mouse_down = False

# Matriz de números aleatorios
matrix_size = 10
matrix = []

width_box = 50
height_box = 50

position_selected = []

start_position = [width_box, height_box]

font = pygame.font.SysFont("Arial", 36)

# Bucle de l'aplicació
def main():
    is_looping = True

    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(random.randint(1, 9))
        
        matrix.append(row)

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
    global mouse_pos, mouse_down
    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"], mouse_pos["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
    return True

# Fer càlculs
def app_run():
    global position_selected

    if mouse_pos["x"] > width_box * matrix_size + width_box or mouse_pos["y"] > height_box * matrix_size + height_box:
        return

    pos_x = int(mouse_pos["x"] / width_box) - 1
    pos_y = int(mouse_pos["y"] / height_box) - 1

    position_selected = [pos_x, pos_y]

    if mouse_down:
        current_number = matrix[pos_y][pos_x]
        if pos_y > 0:
            up_number = matrix[pos_y - 1][pos_x]
            if up_number == current_number:
                matrix[pos_y - 1][pos_x] = None
        if pos_y < matrix_size - 1:
            down_number = matrix[pos_y - 1][pos_x]
            if down_number == current_number:
                matrix[pos_y + 1][pos_x] = None
        if pos_x > 0:
            left_number = matrix[pos_y][pos_x - 1]
            if left_number == current_number:
                matrix[pos_y][pos_x - 1] = None
        if pos_x < matrix_size - 1:
            right_number = matrix[pos_y][pos_x + 1]
            if right_number == current_number:
                matrix[pos_y][pos_x + 1] = None
        matrix[pos_y][pos_x] = None

# Dibuixar
def app_draw():
    global font, start_position

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibujamos los números con las tablas

    for row in range(matrix_size):
        for column in range(matrix_size):
            if position_selected == [column, row]:
                color = BLUE if mouse_down else GREEN
                pygame.draw.rect(screen, color, (start_position[0], start_position[1], width_box, height_box))
            else:
                pygame.draw.rect(screen, BLACK, (start_position[0], start_position[1], width_box, height_box), 5)

            if matrix[row][column] != None:
                text = font.render(f"{matrix[row][column]}", True, BLACK)
                text_position = [start_position[0] + (width_box / 4), start_position[1] + (height_box / 4)]
                screen.blit(text, text_position)

            start_position[0] += width_box
        
        start_position[0] = width_box
        start_position[1] += height_box
    
    start_position = [width_box, height_box]

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
