from Board.GraphicsConstants import *

from Board.PlayerTextures import PlayerTextures


class PlayerGraphics():
	def __init__(self, surface):
		self.surface = surface

	def draw(self, player):
		playerTexture = PlayerTextures[player.playerType]
		position = (player.tile.posY * TileSize, player.tile.posX * TileSize)

		self.surface.blit(playerTexture, position)
