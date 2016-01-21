import pygame, sys
import os
import random
from cl import *
from Tile import *
from Player import *
from pygame.locals import *

#box glove image
img2 = pygame.image.load('images/boximg.png')

def dieRoll():
    thrown = random.randint(1, 6)
    print(thrown)

pygame.init()
TILESIZE  = 55
MAPWIDTH  = 11
MAPHEIGHT = 11
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 200))
pygame.display.set_caption('Survivor')                          # Title of project

clock = pygame.time.Clock()                                     # Add clock

def GameBoard():
    mouseLocation = pygame.mouse.get_pos()
    mouseClick    = pygame.mouse.get_pressed()

    DISPLAYSURF.fill(SURV_BLUE)    #maakt achtergrond weer blauw ipv menu achtergrond
    for row in range(MAPHEIGHT):
        #loop through each column in the row
        for column in range(MAPWIDTH):
            #Row = Y-Axis and Column = the X-Axis
            #draw the resource at that position in the tilemap, using the correct colour
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE-2))
            # Blit image on the certain Row and Column and -2 is because of the centering on the tile
    INVFONT = pygame.font.Font('Minecraft.ttf',18)

    placePosition = 10

    for item in resourcesRed:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryRed[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    placePosition = 450

    for item in resourcesGreen:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryGreen[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 50

    placePosition = 10

    for item in resourcesBlue:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT *TILESIZE+110))
        placePosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryBlue[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT *TILESIZE+110))
        placePosition += 50

    placePosition = 450

    for item in resourcesYellow:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT *TILESIZE+110))
        placePosition += 30
        #add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryYellow[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT *TILESIZE+110))
        placePosition += 50

    #menu knop in game
    if 250+100 > mouseLocation[0] > 250 and 675 + 50 > mouseLocation[1] > 675:
        pygame.draw.rect(DISPLAYSURF,YELLOW,(250,675,100,50))
        DISPLAYSURF.blit(img2,(200,675))
        if mouseClick[0] == 1:
            intro_menu()
    else:
        pygame.draw.rect(DISPLAYSURF,DIM_YELLOW,(250,675,100,50))

    smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
    TextSurf, TextRect = text_objects3("Menu", smallText)
    TextRect.center = (((MAPWIDTH*TILESIZE)/2),((MAPHEIGHT*TILESIZE)/0.867))
    DISPLAYSURF.blit(TextSurf, TextRect)

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
                pygame.mixer.music.stop()
                gameLoop()

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

        #text_of_buttons
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


def gameLoop():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        GameBoard()

        DISPLAYSURF.blit(PLAYERRED,(playerRedPos[0]*TILESIZE,playerRedPos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERBLUE,(playerBluePos[0]*TILESIZE,playerBluePos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERYELLOW,(playerYellowPos[0]*TILESIZE,playerYellowPos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERGREEN,(playerGreenPos[0]*TILESIZE,playerGreenPos[1]*TILESIZE))


        #DISPLAYSURF.blit(background, (0, 0))                   # Shows us the background
        pygame.display.flip()                                 # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)                                          # Set FPS, PC MASTER RACE

    pygame.quit()                                                   #Quit?
    quit()                                                          #Okay. Doei.

intro_menu()

