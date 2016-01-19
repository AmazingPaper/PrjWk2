import pygame, sys
import os
import cl

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600,600))
pygame.display.set_caption('Survivor')                          # Title of project



clock = pygame.time.Clock()                                     # Add clock
crashed = False                                                 # Crash handler

background = pygame.Surface(DISPLAYSURF.get_size())             # Gets the size of the screen
background = background.convert()
background.fill((cl.NAVYBLUE))                                  # Fills the screen with the given color in the cl

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        DISPLAYSURF.blit(background, (0, 0))                    # Shows us the background
        pygame.display.update()                                 # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)                                          # Set FPS, PC MASTER RACE

pygame.quit()                                                   #Quit?
quit()                                                          #Okay. Doei.