import pygame
from PyGameLoop import *
from cl.py      import *

def text_objects(text, font):
    textSurface = font.render(text, True, SURV_BLUE)
    return textSurface, textSurface.get_rect()

def text_objects2 (text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def text_objects3 (text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#sounds
def intro_music():
    pygame.mixer.music.load("Sounds/Sandstorm.mp3")
    pygame.mixer.music.play()

def intro_menu():
    intro = True
    if intro == True:
        intro_music()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #text objects
        DISPLAYSURF.fill(SURV_BLUE)
        pygame.draw.rect(DISPLAYSURF,YELLOW,(20,70,570,100)) #title box
        largeText = pygame.font.Font('8-BIT WONDER.TTF',75)
        TextSurf, TextRect = text_objects("SURVIVOR", largeText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/1.95),((MAPHEIGHT*TILESIZE)/5))
        DISPLAYSURF.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects2("MENU", smallText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/2),((MAPHEIGHT*TILESIZE)/12))
        DISPLAYSURF.blit(TextSurf, TextRect)

        #images
        img = pygame.image.load('images/survivorstockimage.png')
        DISPLAYSURF.blit(img,(20,180))

        img2 = pygame.image.load('images/boximg.png')

        #button objects
        #play
        pygame.draw.rect(DISPLAYSURF,DIM_RED,(250,400,100,50))
        #quit
        pygame.draw.rect(DISPLAYSURF,DIM_GREY,(50,500,100,50))
        #settings
        pygame.draw.rect(DISPLAYSURF,DIM_BLUE,(450,500,100,50))
        #rules
        pygame.draw.rect(DISPLAYSURF,DIM_YELLOW,(250,500,100,50))

        #interactive button
        #als muis tussen x vh object (250+100) en begin (250) zit en
        #muis zit tussen y vh object (400+50) en begin vh object (400)
        mouseLocation = pygame.mouse.get_pos()
        mouseClick    = pygame.mouse.get_pressed()

        if 250+100 > mouseLocation[0] > 250 and 400 + 50 > mouseLocation[1] > 400:
            pygame.draw.rect(DISPLAYSURF,RED,(250,400,100,50))
            DISPLAYSURF.blit(img2,(200,400))
            if mouseClick[0] == 1:
                None        #SHOULD run Gameloop function

        else:
            pygame.draw.rect(DISPLAYSURF,DIM_RED,(250,400,100,50))

        if 50+100 > mouseLocation[0] > 50 and 500 + 50 > mouseLocation[1] > 500:
            pygame.draw.rect(DISPLAYSURF,GREY,(50,500,100,50))
            DISPLAYSURF.blit(img2,(0,500))
            if mouseClick[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(DISPLAYSURF,DIM_GREY,(50,500,100,50))

        if 450+100 > mouseLocation[0] > 450 and 500 + 50 > mouseLocation[1] > 500:
            pygame.draw.rect(DISPLAYSURF,BLUE,(450,500,100,50))
            DISPLAYSURF.blit(img2,(400,500))
        else:
            pygame.draw.rect(DISPLAYSURF, DIM_BLUE, (450,500,100,50))

        if 250+100 > mouseLocation[0] > 250 and 500 + 50 > mouseLocation[1] > 500:
            pygame.draw.rect(DISPLAYSURF,YELLOW,(250,500,100,50))
            DISPLAYSURF.blit(img2,(200,500))
        else:
            pygame.draw.rect(DISPLAYSURF,DIM_YELLOW,(250,500,100,50))

        #text_of_buttons (250,400,100,50))

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects3("EXIT", smallText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/6),((MAPHEIGHT*TILESIZE)/1.15))
        DISPLAYSURF.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects3("FIGHT", smallText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/2.01),((MAPHEIGHT*TILESIZE)/1.43))
        DISPLAYSURF.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects3("OPTIONS", smallText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/1.21),((MAPHEIGHT*TILESIZE)/1.15))
        DISPLAYSURF.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects3("RULES", smallText)
        TextRect.center = (((MAPWIDTH*TILESIZE)/2),((MAPHEIGHT*TILESIZE)/1.15))
        DISPLAYSURF.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(30)

intro_menu()