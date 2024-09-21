import pygame
from pygame import display

pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

dis = display.set_mode((800, 600))
pygame.display.set_caption('Zmeyka')

game_over = False #status of a game

clock = pygame.time.Clock()

# start position for zmeyka
x1 = 200
y1 = 200

x1_change = 0 # change of horizontal
y1_change = 0 # change of vertical

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # movement
        if event.type == pygame.KEYDOWN:
            # down
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            #up
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            #right
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            #left
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    #update coordinats
    x1 += x1_change
    y1 += y1_change

    dis.fill(white)

    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()
    #new step
    clock.tick(30)

pygame.quit()

quit()