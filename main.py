import pygame
import sys
import random

pygame.init()

mainWindow = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Flappy Bird')

black = (0, 0, 0)
white = (255, 255, 255)

upper_wall = pygame.Rect(100, 0, 40, 120)
lower_wall = pygame.Rect(100, 280, 40, 120)
bird = pygame.Rect(130, 50, 50, 50)

clock = pygame.time.Clock()
dif = 5
v_bird = 0
a_bird = 1
upper_wall_height = 120

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    mainWindow.fill(white)

    pygame.draw.rect(mainWindow, black, upper_wall)
    pygame.draw.rect(mainWindow, black, lower_wall)
    pygame.draw.rect(mainWindow, black, bird)

    upper_wall.x -= dif
    lower_wall.x -= dif

    v_bird += a_bird
    bird.y += v_bird

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_SPACE]:
        v_bird = -7
    
    if upper_wall.x <= -40:
        upper_wall.x = 500
        lower_wall.x = 500

        upper_wall_height = random.randint(40, 200)
        upper_wall.h = upper_wall_height
        lower_wall.h = 240 - upper_wall_height
        lower_wall.y = 400 - lower_wall.h


    clock.tick(30)
    pygame.display.update()
