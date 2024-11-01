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
pygame.display.set_caption('Alejandro Lopez - Exercici 9')

# Definim les variables globals
font_arial_gran = pygame.font.SysFont("Arial", 18)
font_arial_petita = pygame.font.SysFont("Arial", 16)

dades = [
  {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
  {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
  {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
  {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} 
]

text_desplacament = [5, 2]
fila_alcada = 25
linia_amplada = 3

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
    global font_arial_gran, font_arial_petita, dades, text_desplacament, fila_alcada, linia_amplada
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem el fons blanc segons el nombre d'entrades a la llista dades
    ultima_fila = len(dades) * fila_alcada
    pygame.draw.rect(screen, WHITE, (150, 100, 200, ultima_fila))

    # Dibuixem primera línia
    pygame.draw.line(screen, BLACK, (150, 100), (350, 100), linia_amplada)

    pos_x = [150 + text_desplacament[0], 250 + text_desplacament[0], 300 + text_desplacament[0]]
    pos_y = 100 + text_desplacament[1]

    pos_y_linia = 125

    for dada in dades:
        string = font_arial_gran.render(f"{dada["nom"]}", True, BLACK)
        screen.blit(string, (pos_x[0], pos_y))
        string = font_arial_petita.render(f"{dada["any"]}", True, BLUE)
        screen.blit(string, (pos_x[1], pos_y))
        string = font_arial_petita.render(f"{dada["especie"]}", True, BLUE)
        screen.blit(string, (pos_x[2], pos_y))
        pygame.draw.line(screen, BLACK, (150, pos_y_linia), (350, pos_y_linia), linia_amplada)
        pos_y += fila_alcada
        pos_y_linia += fila_alcada
        

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()