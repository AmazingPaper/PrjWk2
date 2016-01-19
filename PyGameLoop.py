import pygame, sys
import os

from cl import *
from Tile import *

from pygame.locals import *

pygame.init()
TILESIZE  = 55
MAPWIDTH  = 11
MAPHEIGHT = 11
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('Survivor')                          # Title of project



clock = pygame.time.Clock()                                     # Add clock
crashed = False                                                 # Crash handler

background = pygame.Surface(DISPLAYSURF.get_size())             # Gets the size of the screen
background = background.convert()
background.fill((GREY))                                  # Fills the screen with the given color in the cl

# Display some text
# font = pygame.font.Font(None, 36)
# text = font.render("Player 1's turn", 1, (10, 10, 10))
# textpos = text.get_rect()
# textpos.centerx = background.get_rect().centerx
# background.blit(text, textpos)

for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
        #Row = Y-Axis and Column = the X-Axis
        #draw the resource at that position in the tilemap, using the correct colour
        DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))# Blit image on the certain Row and Column


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


        #DISPLAYSURF.blit(background, (0, 0))                   # Shows us the background
        pygame.display.update()                                 # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)                                          # Set FPS, PC MASTER RACE

pygame.quit()                                                   #Quit?
quit()                                                          #Okay. Doei.