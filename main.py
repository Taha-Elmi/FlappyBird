import pygame
import sys
import random

pygame.init()

mainWindow = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Flappy Bird')

black = (0, 0, 0)
white = (255, 255, 255)

upper_wall = pygame.Rect(400, 0, 40, 120)
lower_wall = pygame.Rect(400, 280, 40, 120)
bird = pygame.Rect(130, 150, 50, 50)

background_image = pygame.image.load('photos\\background.png')
background_image = pygame.transform.scale(background_image, (500, 400))
bird1_image = pygame.image.load('photos\\bird1.png')
bird1_image = pygame.transform.scale(bird1_image, (50, 50))
bird2_image = pygame.image.load('photos\\bird2.png')
bird2_image = pygame.transform.scale(bird2_image, (50, 50))
bird3_image = pygame.image.load('photos\\bird3.png')
bird3_image = pygame.transform.scale(bird3_image, (50, 50))
bird4_image = pygame.image.load('photos\\bird4.png')
bird4_image = pygame.transform.scale(bird4_image, (50, 50))
upper_wall_image = pygame.image.load('photos\\wall.png')
upper_wall_image = pygame.transform.scale(upper_wall_image, (40, 120))
lower_wall_image = pygame.image.load('photos\\wall.png')
lower_wall_image = pygame.transform.scale(lower_wall_image, (40, 120))

bird_images = [bird1_image, bird2_image, bird3_image, bird4_image]

score_file = open("best_score.txt","r")
best_score = int(score_file.read())
score_file.close()
score = 0

clock = pygame.time.Clock()
v_wall = 5
v_bird = 0
a_bird = 1
bird_images_index = 0
bird_images_ratio = 5

my_font = pygame.font.SysFont("Jokerman Regular", 50)
gameover_text = my_font.render("Game Over", True, (255, 0, 0))

my_font = pygame.font.SysFont("Jokerman Regular", 35)
score_text = my_font.render("Your Score: " + str(score), True, (255, 0, 0))
best_score_text = my_font.render("Best Score: " + str(best_score), True, (255, 0, 0))
score_renderer = my_font.render("0", True, (255, 0, 0))



state = "beginning"

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    mainWindow.blit(background_image, (0,0))
    mainWindow.blit(upper_wall_image, (upper_wall.x, upper_wall.y))
    mainWindow.blit(lower_wall_image, (lower_wall.x, lower_wall.y))
    mainWindow.blit(bird_images[bird_images_index // bird_images_ratio], (bird.x, bird.y))
    mainWindow.blit(score_renderer, (30, 30))


    if state == "beginning":
        mainWindow.blit(best_score_text, (160, 100))

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            state = "playing"
            
    if state == "playing":
        bird_images_index += 1
        if bird_images_index >= (bird_images_ratio * len(bird_images)):
            bird_images_index = 0

        upper_wall.x -= v_wall
        lower_wall.x -= v_wall

        v_bird += a_bird
        bird.y += v_bird

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            v_bird = -7
        
        if upper_wall.x <= -40:
            upper_wall.x = 500
            lower_wall.x = 500

            upper_wall.h = random.randint(40, 200)
            upper_wall_image = pygame.transform.scale(upper_wall_image, (40, upper_wall.h))
            lower_wall.h = 240 - upper_wall.h
            lower_wall.y = 400 - lower_wall.h
            lower_wall_image = pygame.transform.scale(lower_wall_image, (40, lower_wall.h))

        if bird.colliderect(upper_wall) or bird.colliderect(lower_wall):
            state = "game over"

        if bird.x == lower_wall.x + lower_wall.w :
            score += 1
            score_renderer = my_font.render(str(score), True, (255, 0, 0))

    if state == "game over":

        if score > best_score:
            best_score = score
            best_score_file = open("best_score.txt", "w")
            best_score_file.write(str(best_score))
            best_score_file.close()
            
        
        mainWindow.blit(gameover_text, (160, 100))

        score_text = my_font.render("Your Score: " + str(score), True, (255, 0, 0))
        mainWindow.blit(score_text, (180, 160))

        best_score_text = my_font.render("Best Score: " + str(best_score), True, (255, 0, 0))
        mainWindow.blit(best_score_text, (180, 200))

    clock.tick(30)
    pygame.display.update()
