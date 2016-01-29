import pygame

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


def button(text, x, y, w, h, ac, ic, scene):
	mouseLocation = pygame.mouse.get_pos()

	boxingHandImage = pygame.image.load('images/boximg.png')

	ellipseRectangle = pygame.draw.ellipse(scene, ac, (x, y, w, h))

	smallTextFont = pygame.font.Font('8-BIT WONDER.TTF', 15)
	textSurface, textRectangle = text_objects3(text, smallTextFont)
	textRectangle.center = ((x + (w / 2)), (y + (h / 2)))

	if ellipseRectangle.collidepoint(mouseLocation):
		scene.blit(boxingHandImage, ((x - 50), y))
		pygame.draw.ellipse(scene, ic, (x, y, w, h))

	scene.blit(textSurface, textRectangle)

	return ellipseRectangle

