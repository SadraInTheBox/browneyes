import pygame as pg

class ImageHandler:
    nexts = {
        "rip": "alive",
        "alive": "rip"
    }
    def __init__(self, window:pg.Surface) -> None:
        self.window = window
        self.images = {
            "rip": pg.image.load("./images/rip.png"),
            "alive": pg.image.load("./images/alive.png")
        }
        self.images["rip"] = pg.transform.scale(
            self.images["rip"],
            (window.get_width(), window.get_height())
        )
        self.images["alive"] = pg.transform.scale(
            self.images["alive"],
            (window.get_width(), window.get_height())
        )
        self.select = "alive"
    
    def show(self):
        self.window.blit(
            self.images[self.select],
            (0, 0)
        )
    
    def selectNext(self):
        self.select = self.nexts[self.select]