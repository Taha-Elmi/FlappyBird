import pygame
import sys
import random

pygame.init()

mainWindow = pygame.display.set_mode((400, 300))
pygame.display.set_caption('The First Game with Python')

r = 0
g = 0
b = 0
color = (r, g, b)

white = (255, 255, 255)
rect1 = pygame.Rect(100, 100, 100, 100)
clock = pygame.time.Clock()

dif = 5

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    mainWindow.fill(white)

    color = (r, g, b)
    pygame.draw.rect(mainWindow, color, rect1)

    rect1.x += dif
    if rect1.x >= 300 or rect1.x <= 0:
        dif *= -1
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)


    clock.tick(30)
    pygame.display.update()
