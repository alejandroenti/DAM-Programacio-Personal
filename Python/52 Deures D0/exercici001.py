import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 150, 100)
RED = (200, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro López - Exercici 1')

# Definim variables globals
font_arial_gran = pygame.font.SysFont("Arial", 60)
font_arial_petita = pygame.font.SysFont("Arial", 28)
font_courier = pygame.font.SysFont("Courier New", 40, True)

string_titol = font_arial_gran.render("HEADLINES NEWS", True, WHITE)
string_subtitol = font_courier.render("World goes Wrong!", True, BLACK)
string_verda = font_courier.render("YEP#", True, GREEN)
string_cos_0 = font_arial_petita.render("Lorem ipsum dolor sit amet, consectetur", True, BLACK)
string_cos_1 = font_arial_petita.render("adipiscing elit, sed do eiusmod tempor", True, BLACK)
string_cos_2 = font_arial_petita.render("incididunt ut labore et dolore magna aliqua.", True, BLACK)

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
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    # Dibujamos el rectángulo del título
    pygame.draw.rect(screen, RED, (50, 50, 550, 100))
    screen.blit(string_titol, (60, 70))
    screen.blit(string_subtitol, (50, 160))
    screen.blit(string_verda, (520, 155))
    screen.blit(string_cos_0, (50, 250))
    screen.blit(string_cos_1, (50, 280))
    screen.blit(string_cos_2, (50, 310))

    pygame.display.update()

if __name__ == "__main__":
    main()