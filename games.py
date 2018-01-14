import pygame
from TheGame import *
pygame.init()

display_width = 1400
display_height = 950

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('King Arthur')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)

clock = pygame.time.Clock()

knopImg = pygame.image.load('knop.png').convert()
geldzakImg = pygame.image.load('geldzak.png').convert()
lichtImg = pygame.image.load('licht.png')
rolletjeImg = pygame.image.load('rolletje.png').convert()
shadowImg = pygame.image.load('shadow.png')
steenachtergrondImg = pygame.image.load('steenachtergrond.png')
steenvoorgrondImg = pygame.image.load('steenvoorgrond.png')
swordImg = pygame.image.load('sword.png')

def knop(x, y):
    gameDisplay.blit(knopImg, (x, y))
def geldzak(x, y):
    gameDisplay.blit(pygame.transform.scale(geldzakImg, (350, 350)), (x, y))
def licht(x, y):
    gameDisplay.blit(lichtImg, (x, y))
def rolletje(x, y):
    gameDisplay.blit(pygame.transform.scale(rolletjeImg, (300, 350)), (x, y))
def shadow(x, y):
    gameDisplay.blit(pygame.transform.scale(shadowImg, (390, 70)), (x, y))
def steenachtergrond(x, y):
    gameDisplay.blit(steenachtergrondImg, (x, y))
def steenvoorgrond(x, y):
    gameDisplay.blit(steenvoorgrondImg, (x, y))
def sword(x, y):
    gameDisplay.blit(swordImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

gameDisplay.fill(white)
#knop(display_width * 0.45, display_height * 0.8)
geldzak(display_width * 0.05, display_height * 0.3)
licht(display_width * 0.2, display_height * -0.1429)
rolletje(display_width * 0.78, display_height * 0.03)
shadow(display_width * 0.485, display_height * 0.44)
steenachtergrond(display_width * 0.53, display_height * 0.214)
sword(display_width * 0.567, display_height * 0.226)
steenvoorgrond(display_width * 0.53, display_height * 0.214)
pygame.display.flip()

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + w > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1:
            return print(lottery(20, 300))

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Pull The Sword!", 650, 750, 500, 100, green, bright_green)

        pygame.display.update()
        clock.tick(10)

game_loop()
