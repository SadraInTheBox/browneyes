import pygame as pg
import random
import noise

class SnowFlock:
    targetRect:pg.Rect = None
    def __init__(self, window:pg.Surface):
        self.window = window
        self.pos = [
            random.randint(0, window.get_width()),
            random.randint(0, window.get_height())
        ]
        self.now = random.choice(range(0, 20000, 100))
        self.size = random.randint(2, 10)

    def setNewX(self):
        self.targetRect = pg.Rect(
            random.randint(0, self.window.get_width()),
            0,
            10, 10
        )

    def _getNewX(self):
        if self.targetRect == None:
            return

        self.targetRect.y = self.pos[1]

        if self.targetRect.x > self.pos[0]:
            self.pos[0] += 1
        if self.targetRect.x < self.pos[0]:
            self.pos[1] -= 1
        
        if self.targetRect.collidepoint(self.pos[0],self.pos[1]):
            self.setNewX()

    def getNewX(self):
        self.pos[0] += noise.pnoise1(self.now)*10
        self.now += 0.001
        if self.pos[0] < 0:
            self.pos[0] * -1

    def draw(self):
        self.pos[1] += 1
        if self.pos[1] > self.window.get_width():
            self.pos[1] = 0

        pg.draw.circle(
            self.window,
            (255,255,255),
            self.pos, self.size
        )

        if self.targetRect == None:
            self.setNewX()

        self.getNewX()