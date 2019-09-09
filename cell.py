import pygame, consts


class Cell:
    def __init__(self, surface, sx, sy, color=consts.back_color):
        self.sx = sx
        self.sy = sy
        self.size = consts.cell_size
        self.surface = surface
        self.color = color
        pygame.draw.rect(surface, (0, 0, 0), (sx, sy, consts.cell_size, consts.cell_size), 1)
        self.set_color(color)

    def set_color(self, color):
        self.color = color
        pygame.draw.rect(self.surface, color, (self.sx + 1, self.sy + 1, self.size - 2, self.size - 2))
        pygame.display.update()

    def is_empty(self):
        return self.color == consts.back_color

    def is_fruit(self):
        return self.color == consts.fruit_color
