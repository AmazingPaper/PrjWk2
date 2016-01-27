import pygame

from Board.Enumerations import PlayerType

PlayerTextures = {
	PlayerType.Red: pygame.image.load('Tiles/PlayerRed.gif'),
	PlayerType.Blue: pygame.image.load('Tiles/PlayerBlue.gif'),
	PlayerType.Green: pygame.image.load('Tiles/PlayerGreen.gif'),
	PlayerType.Yellow: pygame.image.load('Tiles/PlayerYellow.gif'),
}
