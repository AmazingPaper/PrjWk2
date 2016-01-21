import pygame


LIFEPOINTSRED = 8
LIFEPOINTSBLUE = 9
LIFEPOINTSGREEN = 10
LIFEPOINTSYELLOW = 11
CONDITIONPOINTS = 12


resourcesRed = [LIFEPOINTSRED, CONDITIONPOINTS]
resourcesBlue = [LIFEPOINTSBLUE, CONDITIONPOINTS]
resourcesGreen = [LIFEPOINTSGREEN, CONDITIONPOINTS]
resourcesYellow = [LIFEPOINTSYELLOW, CONDITIONPOINTS]

HPRED = 100
HPBLUE = 100
HPYELLOW = 100
HPGREEN = 100

CPRED = 15
CPBLUE = 15
CPYELLOW = 15
CPGREEN = 15

DIRECTION = 0

PLAYERRED = pygame.image.load('Tiles/PlayerRed.gif')
#the position of the player [x,y]
playerRedPos = [10,0]
inventoryRed = {
                LIFEPOINTSRED          : HPRED,
                CONDITIONPOINTS     : CPRED
                }

PLAYERBLUE = pygame.image.load('Tiles/PlayerBlue.gif')
playerBluePos = [0,0]
inventoryBlue = {
                LIFEPOINTSBLUE         : HPBLUE,
                CONDITIONPOINTS     : CPBLUE
                }

PLAYERYELLOW = pygame.image.load('Tiles/PlayerYellow.gif')
playerYellowPos = [0,10]
inventoryYellow = {
                LIFEPOINTSYELLOW          : HPYELLOW,
                CONDITIONPOINTS     : CPYELLOW
                }

PLAYERGREEN = pygame.image.load('Tiles/PlayerGreen.gif')
playerGreenPos = [10,10]
inventoryGreen = {
                LIFEPOINTSGREEN          : HPGREEN,
                CONDITIONPOINTS     : CPGREEN
                }


