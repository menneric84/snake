import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from cube import Cube
from snake import Snake

ROWS = 20
COLUMNS = 20
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)
SIZE = 50
def getNewFood():
    global food, snake, win
    if food == None or (snake.head.x == food.x and snake.head.y == food.y):
        food = Cube(random.randint(1,9) * SIZE, random.randint(1,9) * SIZE, "NONE")
        if food != None:
            snake.add(win)
def drawGrid():
    global win
    x = 50
    y = 0
    while x < 500:
        pygame.draw.line(win, WHITE, (x,0), (x,500))
        x += 50
    while y < 500:
        pygame.draw.line(win, WHITE, (0,y), (500,y))
        y += 50

def redraw():
    global win
    win.fill((0,0,0))  # Fills the screen with black
    getNewFood()
    food.draw(win,RED)
    drawGrid()  # Will draw our grid lines
    snake.move(win)
    pygame.display.update()  # Updates the screen

def main():
    global snake, food, win
    bodyFlag = False
    snake = Snake(0,0)
    food = Cube(random.randint(1,10) * SIZE, random.randint(1,10) * SIZE, "NONE")
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock() # creating a clock object
    redraw()
    run = True
    while run:
        pygame.time.delay(100)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        redraw()

    


if __name__ == '__main__':
    main()