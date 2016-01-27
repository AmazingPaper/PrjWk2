import pygame

from Board.Enumerations import PlayerType, TileType

FightTexture = 0
CornerTextures = 1

boardTextures = {
	FightTexture: pygame.image.load('Tiles/FightTile.png'),
	CornerTextures: {
		PlayerType.Yellow: pygame.image.load('Tiles/YellowTile.png'),
		PlayerType.Blue: pygame.image.load('Tiles/BlueTile.png'),
		PlayerType.Red: pygame.image.load('Tiles/RedTile.png'),
		PlayerType.Green: pygame.image.load('Tiles/GreenTile.png'),
	},
	TileType.IdleBlack: pygame.image.load('Tiles/GreyTile.png'),
	TileType.IdleWhite: pygame.image.load('Tiles/WhiteTile.png')
}
