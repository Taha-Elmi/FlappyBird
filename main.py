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

background_image = pygame.image.load('photos\\background.png')
background_image = pygame.transform.scale(background_image, (500, 400))
bird1_image = pygame.image.load('photos\\bird1.png')
bird1_image = pygame.transform.scale(bird1_image, (50, 50))
upper_wall_image = pygame.image.load('photos\\wall.png')
upper_wall_image = pygame.transform.scale(upper_wall_image, (40, 120))
lower_wall_image = pygame.image.load('photos\\wall.png')
lower_wall_image = pygame.transform.scale(lower_wall_image, (40, 120))

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

    mainWindow.blit(background_image, (0,0))
    pygame.draw.rect(mainWindow, black, upper_wall)
    pygame.draw.rect(mainWindow, black, lower_wall)
    mainWindow.blit(upper_wall_image, (upper_wall.x, upper_wall.y))
    mainWindow.blit(lower_wall_image, (lower_wall.x, lower_wall.y))
    mainWindow.blit(bird1_image, (bird.x, bird.y))


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
        upper_wall_image = pygame.transform.scale(upper_wall_image, (40, upper_wall.h))
        lower_wall.h = 240 - upper_wall_height
        lower_wall.y = 400 - lower_wall.h
        lower_wall_image = pygame.transform.scale(lower_wall_image, (40, lower_wall.h))


    clock.tick(30)
    pygame.display.update()
