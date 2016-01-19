import pygame, sys
from pygame.locals import *
from cl import *

# The colors are imported from the Colorlist

#constants representing the different Tiles
FIGHT  = 0
CORNERYELLOW = 1
CORNERBLUE = 2
CORNERRED = 3
CORNERGREEN = 4
IDLETILE = 5
IDLETILE2 = 6
BLANK = 7


#a dictionary tiles to the colors
textures =   {
                FIGHT  : pygame.image.load('FightTile.png'),
                CORNERYELLOW : pygame.image.load('YellowTile.png'),
                CORNERBLUE : pygame.image.load('BlueTile.png'),
                CORNERRED  : pygame.image.load('RedTile.png'),
                CORNERGREEN : pygame.image.load('GreenTile.png'),
                IDLETILE   : pygame.image.load('WhiteTile.png'),
                IDLETILE2  : pygame.image.load('GreyTile.png'),
                BLANK       : pygame.image.load('BlackTile.png')
            } #Image for the tile

#a list representing our tilemap
tilemap = [
            [CORNERBLUE, CORNERBLUE, IDLETILE2, IDLETILE, IDLETILE2, FIGHT, IDLETILE2, IDLETILE, IDLETILE2, CORNERRED, CORNERRED],
            [CORNERBLUE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, CORNERRED],
            [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
            [IDLETILE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE],
            [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
            [FIGHT, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, FIGHT],
            [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
            [IDLETILE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE],
            [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
            [CORNERYELLOW, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, CORNERGREEN],
            [CORNERYELLOW, CORNERYELLOW, IDLETILE2, IDLETILE, IDLETILE2, FIGHT, IDLETILE2, IDLETILE, IDLETILE2, CORNERGREEN, CORNERGREEN]
          ] # This is the 11x11 format for the map





