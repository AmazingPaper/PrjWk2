import pygame

pygame.init()

setHeight = 600                                                 # Set resolution
setWidth = 800                                                  # Also resolution

gameDisplay = pygame.display.set_mode((setHeight, setWidth))    # Apply resolution to game window
pygame.display.set_caption('Survivor')                          # Title of project

clock = pygame.Clock()                                          # Add clock

crashed = False                                                 # Crash handler

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        pygame.display.update()                                 # Can also be changed to 'pygame.display.flip()'
        clock.tick(60)                                          # Set FPS, PC MASTER RACE

pygame.quit()                                                   #Quit?
quit()                                                          #Okay. Doei.