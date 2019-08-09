import pygame
from cube import Cube

RIGHT = "right"
LEFT = "left"
DOWN = "down"
UP = "up"
GREEN = (0,255,255)
class Snake:
    body = []
    turns = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = Cube(x,y, RIGHT)
        self.body.append(self.head)

    def add(self)
    def move(self, win):
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT] and self.head.direction != RIGHT:
                self.head.direction = LEFT
                self.turns.append(Cube(self.head.x, self.head.y, self.head.direction))
            if keys[pygame.K_RIGHT] and self.head.direction != LEFT:
                self.head.direction = RIGHT
                self.turns.append(Cube(self.head.x, self.head.y, self.head.direction))
            if keys[pygame.K_UP] and self.head.direction != DOWN:
                self.head.direction = UP
                self.turns.append(Cube(self.head.x, self.head.y, self.head.direction))
            if keys[pygame.K_DOWN] and self.head.direction != UP:
                self.head.direction = DOWN
                self.turns.append(Cube(self.head.x, self.head.y, self.head.direction))
        if self.head.direction == LEFT:
            self.head.x -= 50
        if self.head.direction == RIGHT:
            self.head.x += 50
        if self.head.direction == UP:
            self.head.y -= 50
        if self.head.direction == DOWN:
            self.head.y += 50

        pygame.draw.rect(win, GREEN, (self.head.x, self.head.y, 50, 50))
            