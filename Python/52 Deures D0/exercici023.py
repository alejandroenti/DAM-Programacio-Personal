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
GRAY = (169, 169, 169) 
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
RED = (255, 69, 0) 

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 23')

# Definim les variables globals
sun = {
    "pos": (0, 0),
    "radius": 20
}
planets = {
    "Mercury": { "distance": 58,  "speed": 47.87, "radius": 3.80, "color": GRAY, "angle": 0, "pos": (0, 0) },
    "Venus":   { "distance": 108, "speed": 35.02, "radius": 9.50, "color": GOLD, "angle": 0, "pos": (0, 0) },
    "Earth":   { "distance": 150, "speed": 29.78, "radius": 10.0, "color": BLUE, "angle": 0, "pos": (0, 0) },
    "Mars":    { "distance": 228, "speed": 24.07, "radius": 5.30, "color": RED,  "angle": 0, "pos": (0, 0) },
}

font = pygame.font.SysFont("Arial", 12)

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
    global sun, planets

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    # La posició del sol al centre de la finestra
    sun["pos"] = (int(screen.get_width() / 2), int(screen.get_height() / 2)) 

    # Per cada planeta, calcula:
    # -El seu 'angle' a partir de "velocitat*delta_time"
    # (cada planeta té la seva pròpia velocitat "speed")

    # - La seva posició 'x,y' al perímetre de la òrbita,
    #   amb la funció 'utils.point_on_circle'
    #   * El radi és la seva distància fins al sol 
    #   * L'angle l'has calculat al pas anterior

    for values in planets.values():
        values["angle"] += (values["speed"] * delta_time) % 360
        values["pos"] = utils.point_on_circle(sun["pos"], values["distance"], values["angle"])


# Dibuixar
def app_draw():
    global sun, planets, font
    
    screen.fill(BLACK)
    utils.draw_grid(pygame, screen, 50)

    # El cercle de la òrbita de color "GRAY = (169, 169, 169)" 
    # Cada planeta a la seva posició

    # Dibuixem el Sol
    pygame.draw.circle(screen, YELLOW, sun["pos"], sun["radius"])

    for name, values in planets.items():
        # Dibuixem òrbita
        pygame.draw.circle(screen, GRAY, sun["pos"], values["distance"], 1)

        # El nom del planeta
        label = font.render(name, True, GRAY)
        label_rect = label.get_rect()
        label_rect.midleft = (values["pos"][0] + values["radius"] + 5, values["pos"][1]) 
        screen.blit(label, label_rect)

        # Dibuixem cercle per representar el planeta
        pygame.draw.circle(screen, values["color"], values["pos"], values["radius"])

    pygame.display.update()

if __name__ == "__main__":
    main()