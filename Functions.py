import random

from pygame.locals import *

from Classes import *
from Tile import *

pygame.init()
TILESIZE = 55
MAPWIDTH = 11
MAPHEIGHT = 11
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 200))
img2 = pygame.image.load('images/boximg.png')
pygame.display.set_caption('Survivor')  # Title of project

clock = pygame.time.Clock()  # Add clock

# _____________________________________________________________________________________________________________________________________

LIFEPOINTSRED = 8
LIFEPOINTSBLUE = 9
LIFEPOINTSGREEN = 10
LIFEPOINTSYELLOW = 11
CONDITIONPOINTSRED = 12
CONDITIONPOINTSYELLOW = 12
CONDITIONPOINTSBLUE = 12
CONDITIONPOINTSGREEN = 12

ROLL1 = pygame.image.load('Tiles/Roll1.png')
ROLL2 = pygame.image.load('Tiles/Roll2.png')
ROLL3 = pygame.image.load('Tiles/Roll3.png')
ROLL4 = pygame.image.load('Tiles/Roll4.png')
ROLL5 = pygame.image.load('Tiles/Roll5.png')
ROLL6 = pygame.image.load('Tiles/Roll6.png')

# Lifepoints and ConditionPoints
resourcesRed = [LIFEPOINTSRED, CONDITIONPOINTSRED]
resourcesBlue = [LIFEPOINTSBLUE, CONDITIONPOINTSBLUE]
resourcesGreen = [LIFEPOINTSGREEN, CONDITIONPOINTSGREEN]
resourcesYellow = [LIFEPOINTSYELLOW, CONDITIONPOINTSYELLOW]

DIRECTION = 0

#Player Red Information
PR = pygame.image.load('Tiles/PlayerRed.gif')
#the position of the player [x,y]
playerRedPos = PlayerRed.position
inventoryRed = {LIFEPOINTSRED: PlayerBlue.Lifepoints,
                CONDITIONPOINTSRED: PlayerBlue.Conditionpoints}

#Player Blue Information
PB = pygame.image.load('Tiles/PlayerBlue.gif')
playerBluePos = PlayerBlue.position
inventoryBlue = {LIFEPOINTSBLUE: PlayerBlue.Lifepoints,
                 CONDITIONPOINTSBLUE: PlayerBlue.Conditionpoints}

#Player Yellow Information
PY = pygame.image.load('Tiles/PlayerYellow.gif')
playerYellowPos = PlayerYellow.position
inventoryYellow = {LIFEPOINTSYELLOW: PlayerYellow.Lifepoints,
                   CONDITIONPOINTSYELLOW: PlayerYellow.Conditionpoints}

#Player Green Information.
PG = pygame.image.load('Tiles/PlayerGreen.gif')
playerGreenPos = PlayerGreen.position
inventoryGreen = {LIFEPOINTSGREEN: PlayerGreen.Lifepoints,
                  CONDITIONPOINTSGREEN: PlayerGreen.Conditionpoints}


# Ability to roll die.
def dieRoll():
    number = random.randint(1, 6)
    print(number)
    return number


# TODO: Make one text_objects function.
def text_objects(text, font):
    textSurface = font.render(text, True, SURV_BLUE)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def text_objects3(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def button(text, x, y, w, h, ac, ic, action=None):
    mouseLocation = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()

    img2 = pygame.image.load('images/boximg.png')

    pygame.draw.ellipse(DISPLAYSURF, ic, (x, y, w, h))
    smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
    TextSurf, TextRect = text_objects3(text, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))

    if x + w > mouseLocation[0] > x and y + h > mouseLocation[1] > y:
        pygame.draw.ellipse(DISPLAYSURF, ac, (x, y, w, h))
        DISPLAYSURF.blit(img2, ((x - 50), y))
        if mouseClick[0] == 1 and action != None:
            pygame.mixer.music.stop()
            action()
        else:
            pygame.draw.ellipse(DISPLAYSURF, ic, (x, y, w, h))

    DISPLAYSURF.blit(TextSurf, TextRect)


# TODO: make one movement function for every player.
#Movement on the board Player Blue
def PlayerPosBlue():
    if playerBluePos[0] == 0 and playerBluePos[1] == 0 or playerBluePos[0] >= 1 and playerBluePos[0] <= 9 and playerBluePos[1] ==0:
        DIRECTION = playerBluePos
        DIRECTION[0] += 1
    elif playerBluePos[0] == 10 and playerBluePos[1] == 0 or playerBluePos[1] >= 1 and playerBluePos[1] <= 9 and playerBluePos[0] ==10:
        DIRECTION = playerBluePos
        DIRECTION[1] += 1
    elif playerBluePos[0] == 10 and playerBluePos[1] == 10 or playerBluePos[0] >= 1 and playerBluePos[0] <= 9 and playerBluePos[1] ==10:
        DIRECTION = playerBluePos
        DIRECTION[0] -= 1
    elif playerBluePos[0] == 0 and playerBluePos[1] == 10 or playerBluePos[1] >= 1 and playerBluePos[1] <= 9 and playerBluePos[0] ==0:
        DIRECTION = playerBluePos
        DIRECTION[1] -= 1

#Movement on the board Player Red
def PlayerPosRed():
    if playerRedPos[0] == 0 and playerRedPos[1] == 0 or playerRedPos[0] >= 1 and playerRedPos[0] <= 9 and playerRedPos[1] ==0:
        DIRECTION = playerRedPos
        DIRECTION[0] += 1
    elif playerRedPos[0] == 10 and playerRedPos[1] == 0 or playerRedPos[1] >= 1 and playerRedPos[1] <= 9 and playerRedPos[0] ==10:
        DIRECTION = playerRedPos
        DIRECTION[1] += 1
    elif playerRedPos[0] == 10 and playerRedPos[1] == 10 or playerRedPos[0] >= 1 and playerRedPos[0] <= 9 and playerRedPos[1] ==10:
        DIRECTION = playerRedPos
        DIRECTION[0] -= 1
    elif playerRedPos[0] == 0 and playerRedPos[1] == 10 or playerRedPos[1] >= 1 and playerRedPos[1] <= 9 and playerRedPos[0] ==0:
        DIRECTION = playerRedPos
        DIRECTION[1] -= 1

#Movement on the board Player Yellow
def PlayerPosYellow():
    if playerYellowPos[0] == 0 and playerYellowPos[1] == 0 or playerYellowPos[0] >= 1 and playerYellowPos[0] <= 9 and playerYellowPos[1] ==0:
        DIRECTION = playerYellowPos
        DIRECTION[0] += 1
    elif playerYellowPos[0] == 10 and playerYellowPos[1] == 0 or playerYellowPos[1] >= 1 and playerYellowPos[1] <= 9 and playerYellowPos[0] ==10:
        DIRECTION = playerYellowPos
        DIRECTION[1] += 1
    elif playerYellowPos[0] == 10 and playerYellowPos[1] == 10 or playerYellowPos[0] >= 1 and playerYellowPos[0] <= 9 and playerYellowPos[1] ==10:
        DIRECTION = playerYellowPos
        DIRECTION[0] -= 1
    elif playerYellowPos[0] == 0 and playerYellowPos[1] == 10 or playerYellowPos[1] >= 1 and playerYellowPos[1] <= 9 and playerYellowPos[0] ==0:
        DIRECTION = playerYellowPos
        DIRECTION[1] -= 1

#Movement on the board Player Green
def PlayerPosGreen():
    if playerGreenPos[0] == 0 and playerGreenPos[1] == 0 or playerGreenPos[0] >= 1 and playerGreenPos[0] <= 9 and playerGreenPos[1] ==0:
        DIRECTION = playerGreenPos
        DIRECTION[0] += 1
    elif playerGreenPos[0] == 10 and playerGreenPos[1] == 0 or playerGreenPos[1] >= 1 and playerGreenPos[1] <= 9 and playerGreenPos[0] ==10:
        DIRECTION = playerGreenPos
        DIRECTION[1] += 1
    elif playerGreenPos[0] == 10 and playerGreenPos[1] == 10 or playerGreenPos[0] >= 1 and playerGreenPos[0] <= 9 and playerGreenPos[1] ==10:
        DIRECTION = playerGreenPos
        DIRECTION[0] -= 1
    elif playerGreenPos[0] == 0 and playerGreenPos[1] == 10 or playerGreenPos[1] >= 1 and playerGreenPos[1] <= 9 and playerGreenPos[0] ==0:
        DIRECTION = playerGreenPos
        DIRECTION[1] -= 1


def quitGame():
    pygame.quit()
    quit()


# _____________________________________________________________________________________________________________________________________________________________

def gameLoop():
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == KEYDOWN:
                if (event.key == K_1):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosBlue()
                    FightTile()
                if (event.key == K_2):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosRed()
                    FightTile()
                if (event.key == K_3):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosYellow()
                    FightTile()
                if (event.key == K_4):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosGreen()
                    FightTile()

        GameBoard()

        DISPLAYSURF.blit(PR, (playerRedPos[0] * TILESIZE, playerRedPos[1] * TILESIZE))
        DISPLAYSURF.blit(PB, (playerBluePos[0] * TILESIZE, playerBluePos[1] * TILESIZE))
        DISPLAYSURF.blit(PY, (playerYellowPos[0] * TILESIZE, playerYellowPos[1] * TILESIZE))
        DISPLAYSURF.blit(PG, (playerGreenPos[0] * TILESIZE, playerGreenPos[1] * TILESIZE))

        # DISPLAYSURF.blit(background, (0, 0))                   # Shows us the background
        pygame.display.flip()  # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)  # Set FPS, PC MASTER RACE

    pygame.quit()  # Quit?
    quit()  # Okay. Doei.


def FightTile():
    if playerBluePos[0] == 5 and playerBluePos[1] == 0:
        inventoryBlue[LIFEPOINTSBLUE] -= 10
        print(PlayerBlue.Lifepoints)


FightTile()


# __________________________________________________________________________________________________________________________________________


# TODO: Make one text_objects function.
def text_objects(text, font):
    textSurface = font.render(text, True, SURV_BLUE)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def text_objects3(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# TODO: make one movement function for every player.



# TODO: change format to .ogg for Mac OS X compatibility
# Adds game music
def intro_music():
    pygame.mixer.music.load("Sounds/Sandstorm.ogg")
    pygame.mixer.music.play()


#TODO: CREATE RULES MENU
def rules_menu():

    #Kopie van Menu objecten
    mouseLocation = pygame.mouse.get_pos()
    mouseClick    = pygame.mouse.get_pressed()
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAYSURF.fill(SURV_BLUE)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects2("RULES", smallText)
        TextRect.center = (((MAPWIDTH * TILESIZE) / 2), ((MAPHEIGHT * TILESIZE) / 12))
        DISPLAYSURF.blit(TextSurf, TextRect)

        img3 = pygame.image.load('images/regels.png')
        DISPLAYSURF.blit(img3, (30, 80))

        button("MENU", 50, 740, 100, 50, YELLOW, WHITE, intro_menu)
        button("FIGHT", 450, 740, 100, 50, RED, DIM_RED, gameLoop)

        pygame.display.update()
        clock.tick(30)

def intro_menu():
    intro = True

    intro_music()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAYSURF.fill(SURV_BLUE)

        #TOP TEXT
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

        #interactive button
        #als muis tussen x vh object (250+100) en begin (250) zit en
        #muis zit tussen y vh object (400+50) en begin vh object (400)


        # button(text,x,y,w,h,ac,ic,action=None)

        button("FIGHT", 250, 600, 100, 50, RED, DIM_RED, gameLoop)
        button("EXIT", 50, 700, 100, 50, GREY, DIM_GREY, quitGame)
        button("OPTIONS", 450, 700, 100, 50, BLUE, DIM_BLUE, )
        button("RULES", 250, 700, 100, 50, YELLOW, DIM_YELLOW, rules_menu)


        pygame.display.update()
        clock.tick(30)


def GameBoard():
    mouseLocation = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()

    DISPLAYSURF.fill(SURV_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond
    for row in range(MAPHEIGHT):
        # loop through each column in the row
        for column in range(MAPWIDTH):
            # Row = Y-Axis and Column = the X-Axis
            # draw the resource at that position in the tilemap, using the correct colour
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE - 2))
            # Blit image on the certain Row and Column and -2 is because of the centering on the tile
    INVFONT = pygame.font.Font('Minecraft.ttf', 18)

    placePosition = 10

    for item in resourcesBlue:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryBlue[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    placePosition = 450

    for item in resourcesRed:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryRed[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    placePosition = 10

    for item in resourcesYellow:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 110))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryYellow[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 110))
        placePosition += 50

    placePosition = 450

    for item in resourcesGreen:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 110))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryGreen[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 110))
        placePosition += 50

    if PlayerBlue.Lifepoints <= 0:
        SkullBlue = pygame.image.load('Tiles/SkullBlue.jpg')
        placePosition = 10
        DISPLAYSURF.blit(SkullBlue, (placePosition, MAPHEIGHT * TILESIZE + 20))

    #menu knop in game
    button("MENU", 250, 675, 100, 50, YELLOW, WHITE, intro_menu)
    button("RULES", 250, 730, 100, 50, YELLOW, DIM_YELLOW, rules_menu)


def fighting():
    hello


def corner():
    hello1

def gameLoop():
    crashed = False


    while not crashed:
        GameBoard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == KEYDOWN:
                if (event.key == K_1):
                    number = dieRoll()
                    inventoryBlue[LIFEPOINTSBLUE] -=10
                    for x in range(number):
                        PlayerPosBlue()
<<<<<<< HEAD
                        if playerBluePos[0] == 2 and playerBluePos[1] == 0:
                            inventoryBlue[CONDITIONPOINTSBLUE] = 15
                    if playerBluePos[0] == 0 and playerBluePos[1] == 0 or playerBluePos[0] == 1 and playerBluePos[1] == 0 or playerBluePos[0] == 0 and playerBluePos[1] == 1:
=======
                    if playerBluePos[0] == 0 and playerBluePos[1] == 0 or playerBluePos[0] == 1 and playerBluePos[
                        1] == 0 or playerBluePos[0] == 0 and playerBluePos[1] == 1:
>>>>>>> origin/master
                        inventoryBlue[LIFEPOINTSBLUE] += 10
                if (event.key == K_2):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosRed()
<<<<<<< HEAD
                        if playerRedPos[0] == 10 and playerRedPos[1] == 2:
                            inventoryRed[CONDITIONPOINTSRED] = 15
                    if playerRedPos[0] == 9 and playerRedPos[1] == 0 or playerRedPos[0] == 10 and playerRedPos[1] == 0 or playerRedPos[0] == 10 and playerRedPos[1] == 1:
=======
                    if playerRedPos[0] == 9 and playerRedPos[1] == 0 or playerRedPos[0] == 10 and playerRedPos[
                        1] == 0 or playerRedPos[0] == 10 and playerRedPos[1] == 1:
>>>>>>> origin/master
                        inventoryRed[LIFEPOINTSRED] += 10
                if (event.key == K_3):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosYellow()
<<<<<<< HEAD
                        if playerYellowPos[0] == 0 and playerYellowPos[1] == 8:
                            inventoryYellow[CONDITIONPOINTSYELLOW] = 15
                    if playerYellowPos[0] == 1 and playerYellowPos[1] == 10 or playerYellowPos[0] == 0 and playerYellowPos[1] == 10 or playerYellowPos[0] == 0 and playerYellowPos[1] == 9:
=======
                    if playerYellowPos[0] == 1 and playerYellowPos[1] == 10 or playerYellowPos[0] == 0 and \
                                    playerYellowPos[1] == 10 or playerYellowPos[0] == 0 and playerYellowPos[1] == 9:
>>>>>>> origin/master
                        inventoryYellow[LIFEPOINTSYELLOW] += 10
                if (event.key == K_4):
                    number = dieRoll()
                    for x in range(number):
                        PlayerPosGreen()
<<<<<<< HEAD
                        if playerGreenPos[0] == 8 and playerGreenPos[1] == 10:
                            inventoryGreen[CONDITIONPOINTSGREEN] = 15
                    if playerGreenPos[0] == 10 and playerGreenPos[1] == 9 or playerGreenPos[0] == 10 and playerGreenPos[1] == 10 or playerGreenPos[0] == 9 and playerGreenPos[1] == 10:
=======

                    if playerGreenPos[0] == 10 and playerGreenPos[1] == 9 or playerGreenPos[0] == 10 and playerGreenPos[
                        1] == 10 or playerGreenPos[0] == 9 and playerGreenPos[1] == 10:
>>>>>>> origin/master
                        inventoryGreen[LIFEPOINTSGREEN] += 10

        if PlayerRed.Lifepoints >= 1:
            DISPLAYSURF.blit(PR, (playerRedPos[0] * TILESIZE, playerRedPos[1] * TILESIZE))
        if inventoryBlue[LIFEPOINTSBLUE] >= 1:
            DISPLAYSURF.blit(PB, (playerBluePos[0] * TILESIZE, playerBluePos[1] * TILESIZE))
        if PlayerYellow.Lifepoints >= 1:
            DISPLAYSURF.blit(PY, (playerYellowPos[0] * TILESIZE, playerYellowPos[1] * TILESIZE))
        if PlayerGreen.Lifepoints >= 1:
            DISPLAYSURF.blit(PG, (playerGreenPos[0] * TILESIZE, playerGreenPos[1] * TILESIZE))

<<<<<<< HEAD






=======
>>>>>>> origin/master
        # DISPLAYSURF.blit(background, (0, 0))                   # Shows us the background
        pygame.display.flip()  # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)  # Set FPS, PC MASTER RACE
        GameBoard()


    pygame.quit()  # Quit?
    quit()  # Okay. Doei.
