import pygame

LIFEPOINTS = 8
CONDITIONPOINTS = 9
resources = [LIFEPOINTS,CONDITIONPOINTS]


PLAYERRED = pygame.image.load('Tiles/PlayerRed.gif')
#the position of the player [x,y]
playerRedPos = [10,0]
inventoryRed = {
                LIFEPOINTS          : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERBLUE = pygame.image.load('Tiles/PlayerRed.gif')
playerBluePos = [0,0]
inventoryBlue = {
                LIFEPOINTS          : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERYELLOW = pygame.image.load('Tiles/PlayerRed.gif')
playerYellowPos = [0,10]
inventoryYellow = {
                LIFEPOINTS          : 100,
                CONDITIONPOINTS     : 15
                }

PLAYERGREEN = pygame.image.load('Tiles/PlayerRed.gif')
playerGreenPos = [10,10]
inventoryGreen = {
                LIFEPOINTS          : 100,
                CONDITIONPOINTS     : 15
                }


