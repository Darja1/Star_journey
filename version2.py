import pygame
pygame.init()

#library of game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (120, 120, 120)

WIDTH = 564
HEIGHT = 846
background = pygame.image.load('pygirls.jpg')

icon = pygame.image.load('background4357j.png')
pygame.display.set_icon(icon)

starIMG = pygame.transform.scale(pygame.image.load('star.png'), (400, 400))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game variables
star_x = 170
star_y = 450
platformIMG = pygame.transform.scale(pygame.image.load('cloudforgame-removebg-preview.png'), (200, 200))
platform_x = 270
platform_y = 650


#create screen 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Star Journey')

running = True
while running == True:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    screen.blit(background,(0, 0))
    screen.blit(starIMG, (star_x, star_y))
    screen.blit(platformIMG, (platform_x, platform_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()