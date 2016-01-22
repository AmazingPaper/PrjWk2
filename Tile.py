import pygame

# Colorlist
#            R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
SURV_BLUE = (16, 66, 111)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DIM_RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DIM_BLUE = (0, 0, 180)
YELLOW = (255, 255, 0)
DIM_YELLOW = (200, 200, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
GREY = (130, 130, 130)
DIM_GREY = (100, 100, 100)
BLACK = (0, 0, 0)

# constants representing the different Tiles
FIGHT = 0
CORNERYELLOW = 1
CORNERBLUE = 2
CORNERRED = 3
CORNERGREEN = 4
IDLETILE = 5
IDLETILE2 = 6
BLANK = 7
LIFEPOINTSRED = 8
LIFEPOINTSBLUE = 9
LIFEPOINTSGREEN = 10
LIFEPOINTSYELLOW = 11
CONDITIONPOINTS = 12

# a dictionary tiles to the colors
textures = {
    FIGHT: pygame.image.load('Tiles/FightTile.png'),
    CORNERYELLOW: pygame.image.load('Tiles/YellowTile.png'),
    CORNERBLUE: pygame.image.load('Tiles/BlueTile.png'),
    CORNERRED: pygame.image.load('Tiles/RedTile.png'),
    CORNERGREEN: pygame.image.load('Tiles/GreenTile.png'),
    IDLETILE: pygame.image.load('Tiles/WhiteTile.png'),
    IDLETILE2: pygame.image.load('Tiles/GreyTile.png'),
    BLANK: pygame.image.load('Tiles/BlackTile.png'),
    LIFEPOINTSRED: pygame.image.load('Tiles/Lifepoints.png'),
    LIFEPOINTSBLUE: pygame.image.load('Tiles/LifepointsBlue.png'),
    LIFEPOINTSGREEN: pygame.image.load('Tiles/LifepointsGreen.png'),
    LIFEPOINTSYELLOW: pygame.image.load('Tiles/LifepointsYellow.png'),
    CONDITIONPOINTS: pygame.image.load('Tiles/Conditionpoints.png')
}  # Image for the tile

# a list representing our tilemap
tilemap = [
    [CORNERBLUE, CORNERBLUE, IDLETILE2, IDLETILE, IDLETILE2, FIGHT, IDLETILE2, IDLETILE, IDLETILE2, CORNERRED,
     CORNERRED],
    [CORNERBLUE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, CORNERRED],
    [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
    [IDLETILE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE],
    [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
    [FIGHT, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, FIGHT],
    [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
    [IDLETILE, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE],
    [IDLETILE2, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, IDLETILE2],
    [CORNERYELLOW, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, CORNERGREEN],
    [CORNERYELLOW, CORNERYELLOW, IDLETILE2, IDLETILE, IDLETILE2, FIGHT, IDLETILE2, IDLETILE, IDLETILE2, CORNERGREEN,
     CORNERGREEN]
]  # This is the 11x11 format for the map
