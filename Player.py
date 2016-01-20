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


PLAYERRED = pygame.image.load('Tiles/PlayerRed.gif')
#the position of the player [x,y]
playerRedPos = [10,0]
inventoryRed = {
                LIFEPOINTSRED          : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERBLUE = pygame.image.load('Tiles/PlayerBlue.gif')
playerBluePos = [0,0]
inventoryBlue = {
                LIFEPOINTSBLUE         : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERYELLOW = pygame.image.load('Tiles/PlayerYellow.gif')
playerYellowPos = [0,10]
inventoryYellow = {
                LIFEPOINTSYELLOW          : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERGREEN = pygame.image.load('Tiles/PlayerGreen.gif')
playerGreenPos = [10,10]
inventoryGreen = {
                LIFEPOINTSGREEN          : 100,
                CONDITIONPOINTS     : 15
                }


