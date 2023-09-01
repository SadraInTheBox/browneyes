from pygame.constants import *
import pygame as pg
from .image import ImageHandler
from .snow import SnowFlock

pg.init()

def run():
    window = pg.display.set_mode((700, 700))
    imageHandler = ImageHandler(window)
    snows:list[SnowFlock] = []
    for i in range(100):
        snows.append(
            SnowFlock(window)
        )
    
    running = True
    clock = pg.time.Clock()

    while running:
        window.fill((51, 51, 51))

        for event in pg.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_RIGHT, K_LEFT]:
                    imageHandler.selectNext()
        
        imageHandler.show()

        for snow in snows:
            snow.draw()

        pg.display.update()
        pg.display.flip()
        clock.tick(clock.get_fps())