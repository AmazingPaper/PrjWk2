from Board.Enumerations import *


# player class
# keeps information about player type (red, green, blue, yellow)
# which tile this is player currently at
class Player():
	def __init__(self, playerType, name="", ):
		self.playerType = playerType
		self.tile = None
		self.name = name
		self.health = 100
		self.stamina = 15

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
