import pygame

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
	def __init__(self, surface, board):
		self.DISPLAYSURF = surface
		self.board = board

	def draw(self):
		# draw each tile
		self.board.Iter(self.drawTile)

	def drawTile(self, tile):
		texture = getTileTexture(tile)
		position = (tile.posY * TileSize, tile.posX * TileSize - 2)

		self.DISPLAYSURF.blit(texture, position)
		playerGraphics = PlayerGraphics(self.DISPLAYSURF)

		for player in tile.players:
			playerGraphics.draw(player)
