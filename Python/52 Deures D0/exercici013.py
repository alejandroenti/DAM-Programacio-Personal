import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import math
from assets.svgmoji.emojis import get_emoji

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Alejandro Lopez - Exercici 13')

# Funció per escalar les imatges
def scale_image(image, target_width=None, target_height=None):

    original_width, original_height = image.get_size()
    aspect_ratio = original_height / original_width

    if target_width and not target_height:  # Escalar per ample mantenint la proporció
        new_width = target_width
        new_height = int(target_width * aspect_ratio)
    elif target_height and not target_width:  # Escalar per altura mantenint la proporció
        new_height = target_height
        new_width = int(target_height / aspect_ratio)
    elif target_width and target_height:  # Escalar deformant la imatge
        new_width = target_width
        new_height = target_height
    else:
        raise ValueError("Especifica almenys un dels dos paràmetres: target_width o target_height.")

    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    return scaled_image

# Definim les variables globals
img_car = pygame.image.load('./python/52 Deures D0/assets/exercici013/car.png')
img_car = scale_image(img_car, target_width=15)
img_circuit = pygame.image.load('./python/52 Deures D0/assets/exercici013/circuit.png')
img_circuit = scale_image(img_circuit, target_height=480)

car = {
    "x": 245,
    "y": 430,
    "angle": 90,
    "speed": 100,
    "img": img_car,
    "direction_x": "none",
    "direction_y": "none",
}

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global car

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:  # Tecla premuda
            if event.key == pygame.K_UP:
               car["direction_y"] = 'up'
            elif event.key == pygame.K_DOWN:
                car["direction_y"] = 'down'
            elif event.key == pygame.K_LEFT:
                car["direction_x"] = 'left'
            elif event.key == pygame.K_RIGHT:
                car["direction_x"] = 'right'
        elif event.type == pygame.KEYUP:  # Tecla alliberada
            if event.key == pygame.K_UP:
                if car["direction_y"] == 'up':
                    car["direction_y"] = 'none'
            elif event.key == pygame.K_DOWN:
                if car["direction_y"] == 'down':
                    car["direction_y"] = 'none'
            elif event.key == pygame.K_LEFT:
                if car["direction_x"] == 'left':
                    car["direction_x"] = 'none'
            elif event.key == pygame.K_RIGHT:
                if car["direction_x"] == 'right':
                    car["direction_x"] = 'none'
    return True

# Fer càlculs
def app_run():
    global car

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    displacement = car["speed"] * delta_time

    if car["direction_x"] == "left":
        car["x"] = car["x"] - displacement
        car["angle"] = 90
    elif car["direction_x"] == "right":
        car["x"] = car["x"] + displacement
        car["angle"] = 270

    if car["direction_y"] == "up":
        car["y"] = car["y"] - displacement
        if car["direction_x"] == "none":
            car["angle"] = 0
        elif car["direction_x"] == "right":
            car["angle"] = 315
        elif car["direction_x"] == "left":
            car["angle"] = 45
    elif car["direction_y"] == "down":
        car["y"] = car["y"] + displacement
        if car["direction_x"] == "none":
            car["angle"] = 180
        elif car["direction_x"] == "right":
            car["angle"] = 225
        elif car["direction_x"] == "left":
            car["angle"] = 135

# Dibuixar
def app_draw():
    global car, img_circuit

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibuixem el circuit al centre de la pantalla
    screen.blit(img_circuit, (0,0))

    # Dibuixem el cotxe amb la rotació
    rotated_img = pygame.transform.rotate(car["img"], car["angle"])
    rect = rotated_img.get_rect(center=(car["x"], car["y"]))
    screen.blit(rotated_img, rect)

    pygame.display.update()

if __name__ == "__main__":
    main()
