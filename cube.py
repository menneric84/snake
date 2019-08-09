import pygame
class Cube:

    def __init__(self, x, y, direction):
        self.height = 50
        self.width = 50
        self.x = x
        self.y = y
        self.direction = direction

    def draw(self,win, color):
        pygame.draw.rect(win, color, (self.x, self.y, self.width, self.height))
