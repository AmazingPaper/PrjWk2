import pygame

from Board.Board import Corners
from Board.Enumerations import *


# player class
# keeps information about player type (red, green, blue, yellow)
# which tile this is player currently at


class Player():
	def __init__(self, playerType, name, corner, damages):
		self.playerType = playerType
		self.name = name
		self.corner = corner
		self.damages = damages


		self.tile = None
		self.health = 100
		self.stamina = 15

		imageName = name.replace(' ', '')

		self.image = pygame.image.load("images/Players/{}.png".format(imageName))

	# is this user currently at his/her corner?
	def isAtOwnCorner(self):
		# if user is not placed on board then return False
		if self.tile is None:
			return False

		# return if is at own corner
		return self.tile.tileType == TileType.PlayerCorner and self.tile.cornerOfPlayer == self.playerType

	# is this user currently at anther player's corner?
	def isAtOtherPlayersCorner(self):
		# if user is not placed on board then return False
		if self.tile is None:
			return False

		# return if is at another user's corner
		return self.tile.tileType == TileType.PlayerCorner and self.tile.cornerOfPlayer != self.playerType

	# are there other players in current tile?
	def isWithOtherPlayers(self):
		players = self.otherPlayers()
		return len(players) > 0

	# returns list of ther players in tile that this player is in
	# but not player himself/herself
	def otherPlayers(self):
		return [player for player in self.tile.players if player != self]

	# return string representation of player
	# player type and  location if is placed on board
	def __str__(self):
		if self.tile is None:
			return str(self.playerType)

		return "{} @ {}:{}".format(self.playerType, self.tile.posX, self.tile.posY)

	def lostGame(self):
		return self.health <= 0

class Players:
	MikeTysen = Player(PlayerType.Blue, "Mike Tysen", Corners.TopLeft, [[(3, -1),(9, -2),(19, -3)],[(5, -2),(11, -3),(15,-5)],[(7, -3),(12,-3),(16,-4)],
      [(2, -1),(4,-2),(6, -3)],[(10, -2),(20, -5),(30,-8)],[(8,-3),(13,-4),(17,-5)]])
	RockyBelboa = Player(PlayerType.Red, "Rocky Belboa", Corners.TopRight, [[(10, -2),(20, -5),(30, -8)],[(8, -3),(13, -4),(17,-5)],[(3, -1),(9,-2),(19,-3)],
      [(5, -2),(11,-3),(15, -5)],[(7, -2),(12, -3),(16,-4)],[(2,-1),(4,-2),(6,-3)]])
	BadrHerl = Player(PlayerType.Green, "Badr Herl", Corners.BottomRight, [[(5, -2),(11, -3),(15, -5)],[(3, -1),(9, -2),(19,-3)],[(2, -1),(4,-2),(6,-3)],
      [(7, -2),(12,-3),(16, -4)],[(8, -3),(13, -4),(17,-5)],[(10,-2),(20,-5),(30,-8)]])
	MannyPecquiao = Player(PlayerType.Yellow, "Manny Pecquiao", Corners.BottomLeft, [[(8, -3),(13, -4),(17, -5)],[(10, -2),(20, -5),(30,-8)],[(5, -2),(11,-3),(15,-5)],
      [(3, -1),(9,-2),(19, -3)],[(2, -1),(4, -2),(6,-3)],[(7,-2),(12,-3),(16,-4)]])
