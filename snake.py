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

    def add(self, win):
        d = self.body[-1]
        if d.direction == RIGHT:
            temp = Cube(d.x - 50, d.y, d.direction)
        if d.direction == LEFT:
            temp = Cube(d.x + 50, d.y, d.direction) 
        if d.direction == UP:
            temp = Cube(d.x, d.y + 50, d.direction) 
        if d.direction == DOWN:
            temp = Cube(d.x, d.y - 50, d.direction)
        self.body.append(temp)
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
        for c in self.body:
            for t in self.turns:
                if t.x == c.x and t.y == c.y:
                    c.direction = t.direction 

        

        for c in self.body:
            if c.direction == LEFT:
                c.x -= 50
            if c.direction == RIGHT:
                c.x += 50
            if c.direction == UP:
                c.y -= 50
            if c.direction == DOWN:
                c.y += 50
            pygame.draw.rect(win, GREEN, (c.x, c.y, 50, 50))
            