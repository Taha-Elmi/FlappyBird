import pygame
import sys
import random

pygame.init()

mainWindow = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Flappy Bird')

r = 0
g = 0
b = 0
color = (r, g, b)
white = (255, 255, 255)

upper_wall = pygame.Rect(100, 0, 40, 120)
lower_wall = pygame.Rect(100, 280, 40, 120)

clock = pygame.time.Clock()
dif = 5
upper_wall_height = 120

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    mainWindow.fill(white)

    color = (r, g, b)
    pygame.draw.rect(mainWindow, color, upper_wall)
    pygame.draw.rect(mainWindow, color, lower_wall)

    upper_wall.x -= dif
    lower_wall.x -= dif
    if upper_wall.x <= -40:
        upper_wall.x = 400
        lower_wall.x = 400

        upper_wall_height = random.randint(40, 200)
        upper_wall.h = upper_wall_height
        lower_wall.h = 240 - upper_wall_height
        lower_wall.y = 400 - lower_wall.h
        #r = random.randint(0, 255)
        #g = random.randint(0, 255)
        #b = random.randint(0, 255)


    clock.tick(30)
    pygame.display.update()
