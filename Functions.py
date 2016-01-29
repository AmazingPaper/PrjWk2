import random

from pygame.locals import *

from Board.BoardGraphics import BoardGraphics
from Board.Board import Board
from Board.Player import Player
from Board.Enumerations import PlayerType
from Board.GraphicsConstants import *
from Classes import *
from Tile import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MapWidth * TileSize, MapHeight * TileSize + 200))
img2 = pygame.image.load('images/boximg.png')
pygame.display.set_caption('Survivor')  # Title of project

clock = pygame.time.Clock()  # Add clock

board = Board()
boardGraphics = BoardGraphics(DISPLAYSURF, board)

players = {
    PlayerType.Red : Player(PlayerType.Red),
    PlayerType.Blue : Player(PlayerType.Blue),
    PlayerType.Green : Player(PlayerType.Green),
    PlayerType.Yellow : Player(PlayerType.Yellow)
}

keyPlayerMapping = {
    K_1 : PlayerType.Red,
    K_2 : PlayerType.Blue,
    K_3 : PlayerType.Green,
    K_4 : PlayerType.Yellow
}

board.placePlayer(players[PlayerType.Red], 0, 0)
board.placePlayer(players[PlayerType.Blue], 0, 10)
board.placePlayer(players[PlayerType.Green], 10, 10)
board.placePlayer(players[PlayerType.Yellow], 10, 0)

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
                if event.key in keyPlayerMapping.keys():
                    number = dieRoll()
                    playerType = keyPlayerMapping[event.key]
                    player = players[playerType].moveTimes(number)
        GameBoard()

        pygame.display.flip()  # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)  # Set FPS, PC MASTER RACE

    pygame.quit()  # Quit?
    quit()  # Okay. Doei.


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
    pygame.mixer.music.load("Sounds/SelSound.wav")
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
        TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
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
        TextRect.center = (((MapWidth*TileSize)/1.95),((MapHeight*TileSize)/5))
        DISPLAYSURF.blit(TextSurf, TextRect)

        smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
        TextSurf, TextRect = text_objects2("MENU", smallText)
        TextRect.center = (((MapWidth*TileSize)/2),((MapHeight*TileSize)/12))
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

    boardGraphics.draw()

    INVFONT = pygame.font.Font('Minecraft.ttf', 18)

    placePosition = 10

    for item in resourcesBlue:
        DISPLAYSURF.blit(textures[item], (placePosition, MapHeight * TileSize + 20))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryBlue[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 20))
        placePosition += 50

    placePosition = 450

    for item in resourcesRed:
        DISPLAYSURF.blit(textures[item], (placePosition, MapHeight * TileSize + 20))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryRed[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 20))
        placePosition += 50

    placePosition = 10

    for item in resourcesYellow:
        DISPLAYSURF.blit(textures[item], (placePosition, MapHeight * TileSize + 110))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryYellow[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 110))
        placePosition += 50

    placePosition = 450

    for item in resourcesGreen:
        DISPLAYSURF.blit(textures[item], (placePosition, MapHeight * TileSize + 110))
        placePosition += 30
        # add the text showing the amount in the inventory
        textObj = INVFONT.render(str(inventoryGreen[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 110))
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
                if event.key in keyPlayerMapping.keys():
                    number = dieRoll()
                    playerType = keyPlayerMapping[event.key]
                    players[playerType].moveTimes(number)


        pygame.display.flip()  # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)  # Set FPS, PC MASTER RACE
        GameBoard()

    pygame.quit()  # Quit?
    quit()  # Okay. Doei.