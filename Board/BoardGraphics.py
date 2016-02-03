from Board.BoardTextures import *
from Board.Enumerations import TileType
from Board.GraphicsConstants import *
from Board.PlayerGraphics import PlayerGraphics


def getTileTexture(tile):
	if tile.tileType == TileType.PlayerCorner:
		return boardTextures[CornerTextures][tile.cornerOfPlayer]
	elif tile.tileType == TileType.Fight:
		return boardTextures[FightTexture]
	elif tile.tileType == TileType.IdleBlack or tile.tileType == TileType.IdleWhite:
		return boardTextures[tile.tileType]

	return ""


class BoardGraphics():
	def __init__(self, images, surface, board):
		self.images = images
		self.screen = surface
		self.board = board

	def draw(self):
		# draw each tile
		self.board.Iter(self.drawTile)

	def drawTile(self, tile):
		texture = getTileTexture(tile)
		position = (tile.posY * TileSize, tile.posX * TileSize - 2)

		self.screen.blit(texture, position)
		playerGraphics = PlayerGraphics(self.screen)

		for player in tile.players:
			playerGraphics.draw(player)

		self.screen.blit(self.images['background'], (55, 55))


