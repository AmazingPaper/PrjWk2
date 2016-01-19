import pygame, sys
import os

from cl import *
from Tile import *
from Player import *

from pygame.locals import *

pygame.init()
TILESIZE  = 55
MAPWIDTH  = 11
MAPHEIGHT = 11
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('Survivor')                          # Title of project



clock = pygame.time.Clock()                                     # Add clock
crashed = False                                                 # Crash handler



for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
        #Row = Y-Axis and Column = the X-Axis
        #draw the resource at that position in the tilemap, using the correct colour
        DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE-2))
        # Blit image on the certain Row and Column and -2 is because of the centering on the tile


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        DISPLAYSURF.blit(PLAYERRED,(playerRedPos[0]*TILESIZE,playerRedPos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERBLUE,(playerBluePos[0]*TILESIZE,playerBluePos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERYELLOW,(playerYellowPos[0]*TILESIZE,playerYellowPos[1]*TILESIZE))
        DISPLAYSURF.blit(PLAYERGREEN,(playerGreenPos[0]*TILESIZE,playerGreenPos[1]*TILESIZE))


        #DISPLAYSURF.blit(background, (0, 0))                   # Shows us the background
        pygame.display.flip()                                 # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)                                          # Set FPS, PC MASTER RACE

pygame.quit()                                                   #Quit?
quit()                                                          #Okay. Doei.