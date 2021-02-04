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
#clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    color = (r, g, b)
            
    mainWindow.fill(white)
    
    pygame.draw.rect(mainWindow, color, rect1)
    rect1.x += 5
    rect1.y += 5
    if rect1.x > 400:
        rect1.x = -100
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        #print(r, g, b, sep = ' ')
    if rect1.y > 300:
        rect1.y = -100
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        #print(r, g, b, sep = ' ')

    pygame.time.Clock().tick(30)
    pygame.display.update()
