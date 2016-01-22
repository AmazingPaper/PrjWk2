import pygame
from FighterClasses import *

LIFEPOINTSRED = 8
LIFEPOINTSBLUE = 9
LIFEPOINTSGREEN = 10
LIFEPOINTSYELLOW = 11
CONDITIONPOINTS = 12

# Lifepoints and ConditionPoints
resourcesRed = [LIFEPOINTSRED, CONDITIONPOINTS]
resourcesBlue = [LIFEPOINTSBLUE, CONDITIONPOINTS]
resourcesGreen = [LIFEPOINTSGREEN, CONDITIONPOINTS]
resourcesYellow = [LIFEPOINTSYELLOW, CONDITIONPOINTS]

DIRECTION = 0

#Player Red Information
PR = pygame.image.load('Tiles/PlayerRed.gif')
#the position of the player [x,y]
playerRedPos = PlayerRed.position
inventoryRed = {LIFEPOINTSRED: PlayerBlue.Lifepoints,
                CONDITIONPOINTS: PlayerBlue.Conditionpoints}

#Player Blue Information
PB = pygame.image.load('Tiles/PlayerBlue.gif')
playerBluePos = PlayerBlue.position
inventoryBlue = {LIFEPOINTSBLUE: PlayerBlue.Lifepoints,
                 CONDITIONPOINTS: PlayerBlue.Conditionpoints}

#Player Yellow Information
PY = pygame.image.load('Tiles/PlayerYellow.gif')
playerYellowPos = PlayerYellow.position
inventoryYellow = {LIFEPOINTSYELLOW: PlayerYellow.Lifepoints,
                    CONDITIONPOINTS: PlayerYellow.Conditionpoints}

#Player Green Information.
PG = pygame.image.load('Tiles/PlayerGreen.gif')
playerGreenPos = PlayerGreen.position
inventoryGreen = {LIFEPOINTSGREEN: PlayerGreen.Lifepoints,
                  CONDITIONPOINTS: PlayerGreen.Conditionpoints}


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